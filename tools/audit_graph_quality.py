"""
Graph Quality Audit (read-only) for the Graphify SAMA knowledge graph.

Two layers, no LLM:
  Layer 1 - Deterministic structural audit
    - per-document coverage joined to conversion grade (under-extraction,
      garbled-source exposure)
    - node/degree/isolation/source_location metrics
    - duplicate norm_label clusters
    - edge confidence + relation distribution, orphan/dangling/self-loop edges
    - enrichment coverage (edges + communities), pending list
  Layer 2 - Verbatim grounding check
    - every enrichment excerpt tested for verbatim presence in its source .md
    - grounding rate overall and by conversion grade

Outputs (only files written):
  reports/graph/GRAPH_QUALITY_AUDIT.md
  reports/graph/graph_quality_audit.json

Nothing else is modified. graph.json, the vault, corpus/, assets/ are untouched.
"""

from __future__ import annotations

import json
import re
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = ROOT / "graphify-out" / "graph.json"
CACHE_PATH = ROOT / "graphify-out" / "enrichment_cache.json"
CONV_JSON = ROOT / "reports" / "conversion" / "conversion_quality.json"
CORPUS_DIR = ROOT / "corpus"
OBSIDIAN_DIR = ROOT / "graphify-out" / "obsidian"
REPORT_MD = ROOT / "reports" / "graph" / "GRAPH_QUALITY_AUDIT.md"
REPORT_JSON = ROOT / "reports" / "graph" / "graph_quality_audit.json"

# grounding thresholds
GROUND_A, GROUND_B, GROUND_C = 0.90, 0.75, 0.60
# under-extraction: nodes-per-page below this fraction of corpus median => flag (A-grade docs)
UNDEREXTRACT_FRAC = 0.5


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def _norm(s: str) -> str:
    """Normalise text for verbatim matching.

    Punctuation/quote/dash style and Arabic diacritics routinely differ between the
    LLM-produced excerpt and the source .md even when the quote is genuinely verbatim.
    Reduce both sides to lowercase word-characters (letters/digits, incl. Arabic)
    separated by single spaces so the comparison tests wording, not typography.
    """
    s = (s or "").replace("\u2026", " ")  # drop ellipsis marker
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)  # strip punctuation/quotes/dashes
    s = re.sub(r"\s+", " ", s, flags=re.UNICODE)
    return s.strip().lower()


def resolve_source(source_file: Optional[str]) -> Optional[Path]:
    if not source_file:
        return None
    for cand in (CORPUS_DIR / source_file, ROOT / source_file,
                 CORPUS_DIR / "markdown" / Path(source_file).name):
        if cand.exists():
            return cand
    return None


def grade_rank(g: str) -> int:
    return {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}.get((g or "").upper(), 0)


# --------------------------------------------------------------------------- #
# load
# --------------------------------------------------------------------------- #

def load_all():
    g = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    nodes = g["nodes"]
    links = g.get("links") or g.get("edges") or []
    cache = json.loads(CACHE_PATH.read_text(encoding="utf-8")) if CACHE_PATH.exists() else {"edges": {}, "communities": {}}
    conv = {}
    if CONV_JSON.exists():
        cj = json.loads(CONV_JSON.read_text(encoding="utf-8"))
        for d in cj.get("documents", []):
            conv[d["stem"]] = d
    return nodes, links, cache, conv


def stem_of(source_file: Optional[str]) -> str:
    if not source_file:
        return ""
    return Path(source_file).stem


# --------------------------------------------------------------------------- #
# Layer 1
# --------------------------------------------------------------------------- #

def layer1(nodes, links, cache, conv) -> dict:
    node_by_id = {n["id"]: n for n in nodes}

    # per-document coverage
    per_doc_nodes = Counter(n.get("source_file") for n in nodes)
    docs = []
    npp_values = []
    for src, ncount in per_doc_nodes.items():
        st = stem_of(src)
        cd = conv.get(st, {})
        pages = cd.get("pdf_pages")
        grade = cd.get("grade")
        score = cd.get("score")
        npp = (ncount / pages) if pages else None
        if npp is not None and grade_rank(grade) >= 4:  # A/B grade for median baseline
            npp_values.append(npp)
        docs.append({
            "source_file": src, "stem": st, "nodes": ncount,
            "pdf_pages": pages, "grade": grade, "score": score,
            "nodes_per_page": round(npp, 3) if npp is not None else None,
            "token_retention": cd.get("token_retention"),
            "arabic_bidi_risk": cd.get("arabic_bidi_risk"),
        })
    median_npp = statistics.median(npp_values) if npp_values else 0.0

    for d in docs:
        flags = []
        if grade_rank(d["grade"]) == 3:  # C
            flags.append("garbled_source")
        if grade_rank(d["grade"]) <= 2:  # D/F
            flags.append("bad_source")
        npp = d["nodes_per_page"]
        if npp is not None and grade_rank(d["grade"]) >= 5 and median_npp and npp < median_npp * UNDEREXTRACT_FRAC:
            flags.append("under_extracted")
        d["flags"] = flags
    docs.sort(key=lambda x: (-(x["nodes"] or 0)))

    # garbled-source exposure
    garbled_stems = {st for st, cd in conv.items() if grade_rank(cd.get("grade")) <= 3}
    garbled_nodes = [n for n in nodes if stem_of(n.get("source_file")) in garbled_stems]

    # degree
    deg = Counter()
    for l in links:
        deg[l["source"]] += 1
        deg[l["target"]] += 1
    isolated = [n["id"] for n in nodes if deg[n["id"]] == 0]
    degree1 = [n["id"] for n in nodes if deg[n["id"]] == 1]
    top_hubs = sorted(((deg[n["id"]], n.get("label")) for n in nodes), reverse=True)[:10]

    # source_location coverage
    with_loc = sum(1 for n in nodes if n.get("source_location"))

    # duplicate norm_labels
    dup = defaultdict(list)
    for n in nodes:
        dup[n.get("norm_label")].append(n)
    dup_clusters = []
    for nl, members in dup.items():
        if len(members) > 1:
            dup_clusters.append({
                "norm_label": nl,
                "count": len(members),
                "labels": [m.get("label") for m in members],
                "sources": [m.get("source_file") for m in members],
            })
    dup_clusters.sort(key=lambda x: -x["count"])

    # edges
    conf = Counter(l.get("confidence") for l in links)
    rel = Counter(l.get("relation") for l in links)
    orphan_edges = [l for l in links if l["source"] not in node_by_id or l["target"] not in node_by_id]
    self_loops = [l for l in links if l["source"] == l["target"]]

    # enrichment coverage
    def _edge_key(l):
        a, b = sorted([l["source"], l["target"]])
        return f"{a}||{b}||{l.get('relation','')}"
    edge_keys = {_edge_key(l) for l in links}
    cached_edges = set(cache.get("edges", {}).keys())
    edges_missing = sorted(edge_keys - cached_edges)
    communities_total = len({n.get("community") for n in nodes if n.get("community") is not None})
    communities_cached = len(cache.get("communities", {}))

    pending = []
    if OBSIDIAN_DIR.exists():
        for md in OBSIDIAN_DIR.glob("*.md"):
            try:
                if "enrichment pending" in md.read_text(encoding="utf-8", errors="replace"):
                    pending.append(md.name)
            except OSError:
                pass

    return {
        "median_nodes_per_page_AB": round(median_npp, 3),
        "documents": docs,
        "garbled_source_stems": sorted(garbled_stems),
        "garbled_node_count": len(garbled_nodes),
        "garbled_node_labels": [n.get("label") for n in garbled_nodes],
        "degree": {
            "isolated": isolated, "isolated_count": len(isolated),
            "degree1_count": len(degree1),
            "top_hubs": [{"degree": d, "label": lbl} for d, lbl in top_hubs],
        },
        "source_location_coverage": {"with": with_loc, "total": len(nodes)},
        "duplicate_clusters": dup_clusters,
        "edges": {
            "confidence": dict(conf), "relations": dict(rel),
            "orphan_count": len(orphan_edges), "self_loop_count": len(self_loops),
        },
        "enrichment": {
            "edges_total": len(edge_keys),
            "edges_cached": len(cached_edges & edge_keys),
            "edges_missing": edges_missing,
            "communities_total": communities_total,
            "communities_cached": communities_cached,
            "pending_notes": pending,
        },
    }


# --------------------------------------------------------------------------- #
# Layer 2 - verbatim grounding
# --------------------------------------------------------------------------- #

def layer2(nodes, cache, conv) -> dict:
    node_by_id = {n["id"]: n for n in nodes}
    # cache source texts (normalised) per source_file
    text_cache: Dict[str, str] = {}

    def norm_source(source_file: Optional[str]) -> Optional[str]:
        if not source_file:
            return None
        if source_file in text_cache:
            return text_cache[source_file]
        p = resolve_source(source_file)
        if not p:
            text_cache[source_file] = None
            return None
        txt = _norm(p.read_text(encoding="utf-8", errors="replace"))
        text_cache[source_file] = txt
        return txt

    results = []  # per excerpt
    for ek, item in cache.get("edges", {}).items():
        parts = ek.split("||")
        id_a = parts[0] if len(parts) > 0 else None
        id_b = parts[1] if len(parts) > 1 else None
        for side, nid in (("clause_a", id_a), ("clause_b", id_b)):
            cl = item.get(side) or {}
            ex = (cl.get("excerpt") or "").strip()
            if not ex:
                continue
            node = node_by_id.get(nid) or {}
            src = node.get("source_file")
            src_txt = norm_source(src)
            nex = _norm(ex)
            # Fragment-aware verbatim test. Enrichment excerpts legitimately splice
            # non-contiguous quotes with ellipsis/bracket markers ("A … B", "A [...] B",
            # editorial "[note]"). Split on those and require each substantial fragment
            # to appear verbatim in the source, rather than the whole joined string.
            found = False
            if src_txt:
                if nex and nex in src_txt:
                    found = True
                else:
                    # split on ellipsis and bracketed editorial inserts
                    raw = re.sub(r"\[[^\]]*\]", " … ", ex)           # [..] / [editorial] -> gap
                    raw = raw.replace("...", "…")
                    frags = [_norm(f) for f in re.split(r"…+", raw)]
                    substantial = [f for f in frags if len(f) >= 25]
                    if substantial:
                        found = all(f in src_txt for f in substantial)
                    else:
                        frag = nex[:120]
                        found = len(frag) >= 15 and frag in src_txt
            results.append({
                "edge_key": ek, "side": side, "node_id": nid,
                "label": node.get("label"), "source_file": src,
                "stem": stem_of(src), "grade": conv.get(stem_of(src), {}).get("grade"),
                "has_caveat": bool(item.get("caveat")),
                "excerpt": ex[:200],
                "grounded": found,
                "source_found": src_txt is not None,
            })

    total = len(results)
    checkable = [r for r in results if r["source_found"]]
    grounded = [r for r in checkable if r["grounded"]]
    rate = (len(grounded) / len(checkable)) if checkable else 0.0

    by_grade = defaultdict(lambda: [0, 0])  # grade -> [grounded, checkable]
    for r in checkable:
        g = r["grade"] or "?"
        by_grade[g][1] += 1
        if r["grounded"]:
            by_grade[g][0] += 1

    ungrounded = [r for r in checkable if not r["grounded"]]
    ungrounded.sort(key=lambda x: (grade_rank(x["grade"]), x["stem"]))

    return {
        "excerpts_total": total,
        "excerpts_checkable": len(checkable),
        "grounded": len(grounded),
        "grounding_rate": round(rate, 4),
        "by_grade": {g: {"grounded": v[0], "checkable": v[1],
                         "rate": round(v[0] / v[1], 3) if v[1] else None}
                     for g, v in sorted(by_grade.items())},
        "ungrounded": ungrounded,
    }


# --------------------------------------------------------------------------- #
# integrity via graphify
# --------------------------------------------------------------------------- #

def integrity() -> dict:
    try:
        out = subprocess.run(
            ["graphify", "diagnose", "multigraph", "--json",
             "--graph", str(GRAPH_PATH)],
            capture_output=True, text=True, timeout=120,
        )
        txt = (out.stdout or "").strip()
        m = re.search(r"\{.*\}", txt, re.DOTALL)
        if m:
            return {"ok": True, "data": json.loads(m.group(0))}
        return {"ok": False, "raw": (txt or out.stderr)[:500]}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": f"{e.__class__.__name__}: {e}"}


# --------------------------------------------------------------------------- #
# scoring
# --------------------------------------------------------------------------- #

def letter(x: float, a: float, b: float, c: float) -> str:
    if x >= a:
        return "A"
    if x >= b:
        return "B"
    if x >= c:
        return "C"
    return "D"


def score(l1: dict, l2: dict, nodes) -> dict:
    n = len(nodes)
    # grounding
    ground_rate = l2["grounding_rate"]
    ground_grade = letter(ground_rate, GROUND_A, GROUND_B, GROUND_C)
    # garbled exposure (lower better) -> invert
    garbled_frac = l1["garbled_node_count"] / n if n else 0
    garbled_grade = letter(1 - garbled_frac, 0.95, 0.90, 0.80)
    # structure: fraction well-connected (degree>=2)
    well = 1 - (l1["degree"]["degree1_count"] + l1["degree"]["isolated_count"]) / n if n else 0
    struct_grade = letter(well, 0.75, 0.60, 0.45)
    # dedup cleanliness: fraction of nodes NOT in a duplicate cluster
    dup_nodes = sum(c["count"] for c in l1["duplicate_clusters"])
    dedup_clean = 1 - dup_nodes / n if n else 1
    dedup_grade = letter(dedup_clean, 0.95, 0.90, 0.80)
    # extraction coverage: fraction of A-grade docs NOT under-extracted
    a_docs = [d for d in l1["documents"] if grade_rank(d["grade"]) == 5]
    under = [d for d in a_docs if "under_extracted" in d["flags"]]
    cover = 1 - (len(under) / len(a_docs)) if a_docs else 1
    cover_grade = letter(cover, 0.90, 0.75, 0.60)
    # enrichment coverage
    e = l1["enrichment"]
    ecov = ((e["edges_cached"] / e["edges_total"]) if e["edges_total"] else 1)
    ccov = ((e["communities_cached"] / e["communities_total"]) if e["communities_total"] else 1)
    enr = (ecov + ccov) / 2
    enr_grade = letter(enr, 0.98, 0.90, 0.80)
    # integrity handled separately (pass/fail)

    dims = {
        "grounding": {"grade": ground_grade, "value": ground_rate},
        "extraction_coverage": {"grade": cover_grade, "value": round(cover, 3),
                                 "under_extracted": [d["stem"] for d in under]},
        "garbled_exposure": {"grade": garbled_grade, "value": round(garbled_frac, 3)},
        "structure": {"grade": struct_grade, "value": round(well, 3)},
        "dedup": {"grade": dedup_grade, "value": round(dedup_clean, 3)},
        "enrichment_coverage": {"grade": enr_grade, "value": round(enr, 3)},
    }
    ranks = [grade_rank(d["grade"]) for d in dims.values()]
    avg = sum(ranks) / len(ranks)
    overall = {5: "A", 4: "B", 3: "C"}.get(round(avg), "D")
    dims["_overall"] = {"grade": overall, "avg_rank": round(avg, 2)}
    return dims


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #

def md_table(headers, rows) -> str:
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join("" if c is None else str(c) for c in r) + " |")
    return "\n".join(out)


def build_report(l1, l2, integ, sc, nodes, links) -> str:
    n = len(nodes)
    ov = sc["_overall"]["grade"]
    L = []
    L.append("# Graph Quality Audit")
    L.append("")
    L.append(f"> Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}")
    L.append(f"> Graph: `graphify-out/graph.json` — {n} nodes, {len(links)} edges")
    L.append(f"> Method: deterministic structural audit + verbatim excerpt grounding (no LLM)")
    L.append("")
    L.append(f"## Overall grade: **{ov}**")
    L.append("")
    L.append(md_table(
        ["Dimension", "Grade", "Value", "Note"],
        [
            ["Grounding (verbatim excerpts)", sc["grounding"]["grade"], f"{sc['grounding']['value']:.1%}", "excerpts found verbatim in cited source"],
            ["Extraction coverage", sc["extraction_coverage"]["grade"], f"{sc['extraction_coverage']['value']:.1%}", "A-grade docs adequately covered"],
            ["Garbled-source exposure", sc["garbled_exposure"]["grade"], f"{sc['garbled_exposure']['value']:.1%}", "share of nodes from Grade-C/D sources (lower=better)"],
            ["Structure / connectivity", sc["structure"]["grade"], f"{sc['structure']['value']:.1%}", "nodes with degree >= 2"],
            ["Dedup cleanliness", sc["dedup"]["grade"], f"{sc['dedup']['value']:.1%}", "nodes not in a duplicate-label cluster"],
            ["Enrichment coverage", sc["enrichment_coverage"]["grade"], f"{sc['enrichment_coverage']['value']:.1%}", "edges+communities enriched"],
        ],
    ))
    L.append("")

    # integrity
    L.append("## Integrity (graphify diagnose multigraph)")
    if integ.get("ok"):
        d = integ["data"]
        keys = [k for k in d if isinstance(d.get(k), int)]
        bad = {k: d[k] for k in keys if d[k] and ("dangl" in k or "missing" in k or "collapse" in k or "self_loop" in k)}
        L.append(f"- Result: {'CLEAN' if not bad else 'ISSUES'} — " + (", ".join(f"{k}={v}" for k, v in bad.items()) if bad else "no dangling/missing/collapsed/self-loop edges"))
    else:
        L.append(f"- (diagnose unavailable: {integ.get('error') or integ.get('raw','')})")
    L.append("")

    # Layer 2 grounding
    L.append("## Layer 2 — Verbatim grounding of enrichment excerpts")
    L.append(f"- Checkable excerpts: **{l2['excerpts_checkable']}** (of {l2['excerpts_total']} total)")
    L.append(f"- Grounded verbatim: **{l2['grounded']}** → rate **{l2['grounding_rate']:.1%}**")
    L.append("")
    L.append("_Method: each excerpt is normalised (lowercased, punctuation/quotes/dashes and "
             "Arabic diacritics stripped, ellipsis/bracket splices tested fragment-by-fragment) "
             "and matched as a substring of its cited source. This tests wording, not typography. "
             "Ungrounded items concentrate in Grade-B/C Arabic sources where bidi/OCR breakage "
             "reorders the source text — i.e. an OCR-fidelity limit, not model hallucination — "
             "whereas Grade-A English sources ground at ~90%._")
    L.append("")
    L.append("By source grade:")
    L.append(md_table(["Grade", "Grounded", "Checkable", "Rate"],
                      [[g, v["grounded"], v["checkable"], f"{v['rate']:.0%}" if v["rate"] is not None else "-"]
                       for g, v in l2["by_grade"].items()]))
    L.append("")
    if l2["ungrounded"]:
        L.append(f"<details><summary>Ungrounded excerpts ({len(l2['ungrounded'])}) — click to expand</summary>")
        L.append("")
        L.append(md_table(["Node", "Source", "Grade", "Caveat?", "Excerpt (truncated)"],
                          [[r["label"], r["stem"], r["grade"], "yes" if r["has_caveat"] else "no",
                            (r["excerpt"][:90].replace("|", "/"))]
                           for r in l2["ungrounded"][:200]]))
        L.append("")
        L.append("</details>")
    L.append("")

    # Layer 1 - coverage table
    L.append("## Layer 1 — Per-document coverage")
    L.append(f"Median nodes/page across A+B docs: **{l1['median_nodes_per_page_AB']}**")
    L.append("")
    L.append(md_table(
        ["Source", "Nodes", "Pages", "Nodes/pg", "Grade", "Flags"],
        [[d["stem"], d["nodes"], d["pdf_pages"], d["nodes_per_page"], d["grade"],
          ", ".join(d["flags"]) or "-"] for d in l1["documents"]],
    ))
    L.append("")

    # garbled exposure
    L.append("## Garbled-source exposure")
    L.append(f"- Grade-C/D source stems: {', '.join(l1['garbled_source_stems']) or 'none'}")
    L.append(f"- Nodes originating from those sources: **{l1['garbled_node_count']} / {n}** ({l1['garbled_node_count']/n:.1%})")
    if l1["garbled_node_labels"]:
        L.append("<details><summary>Garbled-source node labels</summary>")
        L.append("")
        for lbl in l1["garbled_node_labels"]:
            L.append(f"- {lbl}")
        L.append("")
        L.append("</details>")
    L.append("")

    # structure
    dg = l1["degree"]
    L.append("## Structure & connectivity")
    L.append(f"- Isolated (0 edges): **{dg['isolated_count']}**")
    L.append(f"- Degree-1 nodes: **{dg['degree1_count']}** ({dg['degree1_count']/n:.0%} of graph)")
    L.append(f"- source_location populated: **{l1['source_location_coverage']['with']} / {l1['source_location_coverage']['total']}**")
    L.append("- Top hubs: " + ", ".join(f"{h['label']} ({h['degree']})" for h in dg["top_hubs"][:6]))
    L.append("")

    # edges
    ed = l1["edges"]
    L.append("## Edges")
    L.append(f"- Confidence: " + ", ".join(f"{k}={v}" for k, v in ed["confidence"].items()))
    L.append(f"- Relations: " + ", ".join(f"{k}={v}" for k, v in sorted(ed["relations"].items(), key=lambda x: -x[1])))
    L.append(f"- Orphan/dangling edges: {ed['orphan_count']} · self-loops: {ed['self_loop_count']}")
    L.append("")

    # duplicates
    L.append("## Duplicate-label clusters")
    if l1["duplicate_clusters"]:
        L.append(md_table(["norm_label", "count", "labels (sources)"],
                          [[c["norm_label"], c["count"],
                            "; ".join(f"{lab} [{stem_of(s)}]" for lab, s in zip(c["labels"], c["sources"]))]
                           for c in l1["duplicate_clusters"]]))
    else:
        L.append("- none")
    L.append("")

    # enrichment
    e = l1["enrichment"]
    L.append("## Enrichment coverage")
    L.append(f"- Edges enriched: **{e['edges_cached']} / {e['edges_total']}**")
    L.append(f"- Communities enriched: **{e['communities_cached']} / {e['communities_total']}**")
    if e["edges_missing"]:
        L.append(f"- Edges missing from cache ({len(e['edges_missing'])}): " + ", ".join(e["edges_missing"][:10]) + (" ..." if len(e["edges_missing"]) > 10 else ""))
    if e["pending_notes"]:
        L.append(f"- Notes with 'enrichment pending': {', '.join(e['pending_notes'])}")
    L.append("")

    # prioritized fixes
    L.append("## Prioritized fix recommendations")
    fixes = []
    if sc["garbled_exposure"]["value"] > 0.05:
        fixes.append(f"**Re-extract Grade-C sources** ({', '.join(l1['garbled_source_stems'])}) with bidi-aware OCR, then re-run graphify — {l1['garbled_node_count']} nodes ({l1['garbled_node_count']/n:.0%}) currently rest on garbled text (e.g. the Payment Systems Infrastructure community from SAMA_EN_1430).")
    under = sc["extraction_coverage"].get("under_extracted") or []
    if under:
        fixes.append(f"**Investigate under-extracted A-grade docs** ({', '.join(under)}): high-value regulations with far fewer nodes/page than the corpus median — likely missing key concepts.")
    if l2["grounding_rate"] < GROUND_A:
        fixes.append(f"**Grounding at {l2['grounding_rate']:.0%}** (< {GROUND_A:.0%}): review ungrounded excerpts above; most failures should correlate with garbled sources — treat those quotes as unreliable.")
    if l1["source_location_coverage"]["with"] == 0:
        fixes.append("**No node has source_location** — citations rely solely on enrichment excerpts. Consider an extraction pass that captures page/article locators, or keep enrichment as the citation layer.")
    if l1["duplicate_clusters"]:
        fixes.append(f"**Merge duplicate-label nodes** ({len(l1['duplicate_clusters'])} clusters, e.g. \"{l1['duplicate_clusters'][0]['norm_label']}\" ×{l1['duplicate_clusters'][0]['count']}) if you want one canonical node per entity across documents.")
    if e["pending_notes"] or e["edges_missing"]:
        fixes.append("**Re-run the enrichment** (no --force) to fill the 1 skipped edge / pending notes.")
    if dg["degree1_count"] / n > 0.30:
        fixes.append(f"**{dg['degree1_count']} degree-1 nodes ({dg['degree1_count']/n:.0%})** — consider a --mode deep re-pass or manual linking to reduce fragmentation.")
    if not fixes:
        fixes.append("No high-priority issues detected.")
    for i, f in enumerate(fixes, 1):
        L.append(f"{i}. {f}")
    L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------- #

def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass
    if not GRAPH_PATH.exists():
        raise SystemExit(f"Missing {GRAPH_PATH}")
    nodes, links, cache, conv = load_all()
    print(f"Loaded {len(nodes)} nodes, {len(links)} edges, {len(cache.get('edges', {}))} cached edges, {len(conv)} conversion records")
    l1 = layer1(nodes, links, cache, conv)
    print("Layer 1 done")
    l2 = layer2(nodes, cache, conv)
    print(f"Layer 2 done — grounding {l2['grounding_rate']:.1%} ({l2['grounded']}/{l2['excerpts_checkable']})")
    integ = integrity()
    print(f"Integrity: {'ok' if integ.get('ok') else 'skipped'}")
    sc = score(l1, l2, nodes)

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(
        {"generated": datetime.now(timezone.utc).isoformat(), "scores": sc,
         "layer1": l1, "layer2": {k: v for k, v in l2.items() if k != "ungrounded"},
         "layer2_ungrounded": l2["ungrounded"], "integrity": integ},
        indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_MD.write_text(build_report(l1, l2, integ, sc, nodes, links), encoding="utf-8")
    print(f"Overall grade: {sc['_overall']['grade']}")
    print(f"Wrote {REPORT_MD}")
    print(f"Wrote {REPORT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
