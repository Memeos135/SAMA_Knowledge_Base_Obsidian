"""
Enrich Graphify Obsidian notes with decision-useful link descriptions + grounding.

Persona: SAMA regulatory compliance/legal analyst (no RegTech / system-design lens).

Per edge (written into both endpoint node notes):
  - What this link tells you : integrated advisory narrative — leads with the
                               practical decision framing, folds in the regulatory
                               basis, ends with the consequence for the KB user.
                               Tone matches confidence (directive for EXTRACTED,
                               tentative "verify before relying" for INFERRED).
  - Grounding A/B            : short verbatim excerpt from each node's source (+ locator)
  - Caveat                   : only if INFERRED/AMBIGUOUS, weak support, or OCR noise

Per community note:
  - Theme                 : regime-aware cluster summary (legal, brief)
  - How members connect   : 2-4 short bullets (legal linkage only, no per-edge dump)

Usage:
  $env:ANTHROPIC_API_KEY = "<key>"
  python tools/enrich_graph_notes.py
  python tools/enrich_graph_notes.py --limit-edges 5   # smoke test
  python tools/enrich_graph_notes.py --force           # ignore cache, re-enrich
  python tools/enrich_graph_notes.py --skip-communities
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = ROOT / "graphify-out" / "graph.json"
# Vault location is configurable so the enricher can target a custom export dir
# (e.g. `graphify export obsidian --dir SAMA_Knowledge_Base_Obsidian`).
OBSIDIAN_DIR = Path(
    os.environ.get("GRAPHIFY_VAULT_DIR", str(ROOT / "SAMA_Knowledge_Base_Obsidian"))
)
CORPUS_DIR = ROOT / "corpus"
CACHE_PATH = ROOT / "graphify-out" / "enrichment_cache.json"
MODEL = os.environ.get("GRAPHIFY_ENRICH_MODEL", "claude-opus-4-8")
API_URL = "https://api.anthropic.com/v1/messages"
EDGE_BATCH = 5
COMMUNITY_BATCH = 4
MAX_CONTEXT_CHARS = 4500
MAX_EXCERPT_CHARS = 280

AGENT_PROFILE = """\
You are a SAMA regulatory compliance/legal analyst. For each pair of linked nodes
in this Saudi Central Bank (SAMA) knowledge graph, your job is to make the link
DECISION-USEFUL: explain what the relationship between the two instruments/
provisions means for someone using this knowledge base to make compliance and
legal decisions about KSA financial-sector rules.

Domain stance:
- Read obligations as enforceable requirements (who must do what, when, to whom).
- Identify the nature of each link: e.g. defines / is-defined-by, imposes an
  obligation on, cross-references, amends, is subordinate to (law -> implementing
  regulation -> circular -> guide), scopes or limits, is an exception to.
- Distinguish regimes: AML/CTF, payments/PSP, BNPL/finance companies, consumer
  protection, data/credit information, sanctions/TFS, governance/risk; flag
  cross-regime interactions when relevant (e.g. BNPL "Consumer" vs AML "Customer";
  merchant-as-customer / KYB; third-party CDD reliance vs ordinary counterparties).
- Preserve defined terms carefully; note scope limits; never invent article numbers
  or text not present in the provided context.

Do NOT provide RegTech, system-design, tooling, workflow, or implementation advice
(no "build a screening workflow", "configure a monitoring rule", "maintain an
evidence trail"). Stay at the level of legal/regulatory meaning and its consequence
for a compliance or legal decision.

Out of scope: formal legal advice to a named firm; marketing tone; generic
"important for compliance" filler; quoting text not present in provided context.
Tone: precise, neutral, practical, brief.
"""

SYSTEM_EDGES = AGENT_PROFILE + """
Task: write a decision-useful description of each knowledge-graph edge in this SAMA
regulatory corpus. Return ONLY valid JSON (no markdown fences).

For each input edge, produce:
{
  "edge_key": "<same as input>",
  "why": "The integrated 'what this link tells you' narrative (2-4 sentences). LEAD with the practical decision framing addressed to the reader (e.g. 'When scoping obligations for a finance company, compliance and internal audit shouldn't be treated separately, because...'). FOLD IN the regulatory basis that makes it true (shared parent law, defined term, cross-reference, obligation chain, hierarchy). END with the concrete consequence for the reader's decision (what they would conclude, check, or not rely on). No RegTech/system advice.",
  "clause_a": {"locator": "Page N / Art X / section if known, else null", "excerpt": "short verbatim quote from node A's source that grounds the link"},
  "clause_b": {"locator": "Page N / Art X / section if known, else null", "excerpt": "short verbatim quote from node B's source that grounds the link"},
  "caveat": null
}

Rules:
- The 'why' is the product: it must be genuinely informative for decision-making, not a restatement that the two nodes are related. A reader should finish it knowing how the link changes what they do.
- CONFIDENCE-MATCHED TONE. If confidence is EXTRACTED: write directively (the link is textually supported). If confidence is INFERRED or AMBIGUOUS, or the relation is 'conceptually_related_to' / 'semantically_similar_to': write tentatively — say the instruments *appear* to connect, frame it as a lead, and tell the reader to verify the primary text before relying on it.
- Prefer verbatim excerpts from the provided source contexts to ground the link. If no good quote exists, use a tight paraphrase and set caveat explaining that.
- ARABIC QUOTING RULE: Only quote Arabic verbatim if it is clean, correctly-joined Arabic in natural reading order. Much of this corpus is OCR/PDF extraction with broken Arabic — disjointed isolated glyphs (presentation forms), letters that do not connect, or right-to-left text stored reversed. NEVER reproduce such text in an excerpt. When a side's Arabic is garbled: (a) prefer that document's parallel ENGLISH text if present; (b) otherwise put a concise English paraphrase in the excerpt and note 'source Arabic is OCR-garbled' in the caveat. When both languages are clean, prefer the English excerpt.
- Keep each excerpt short (~20 words / under ~40 max). Do not invent article numbers, locators, or text.
- Set caveat only when confidence is INFERRED/AMBIGUOUS, evidence is thin, OCR/bidi noise is likely, or the relation is weak; otherwise null.
- Output: {"edges":[...]} matching every input edge_key exactly once.
"""

SYSTEM_COMMUNITIES = AGENT_PROFILE + """
Task: write short community blurbs for this SAMA regulatory knowledge graph.
Return ONLY valid JSON (no markdown fences).

For each community:
{
  "community_id": <int>,
  "theme": "1-2 sentences: the regulatory theme/regime that binds these members and why they cluster",
  "how_members_connect": ["2-4 short bullets on the legal linkage — shared definitions, obligation chains, cross-references, or hierarchy (law -> regulation -> circular -> guide) — not a dump of every edge"]
}

Rules:
- Frame the theme for a compliance/legal reader (what regulatory problem-space this community covers). No RegTech/system framing.
- Stay concrete and brief; no filler.
- Output: {"communities":[...]} for every input community_id exactly once.
"""


# ---------------------------------------------------------------------------
# HTTP / Claude
# ---------------------------------------------------------------------------

def require_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        raise SystemExit(
            "ANTHROPIC_API_KEY is not set. Example:\n"
            '  $env:ANTHROPIC_API_KEY = "sk-ant-..."\n'
            "  python tools/enrich_graph_notes.py"
        )
    return key


def claude_json(system: str, user: str, api_key: str, max_tokens: int = 8192) -> dict:
    body = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Anthropic HTTP {e.code}: {err[:800]}") from e

    parts = []
    for block in payload.get("content", []):
        if block.get("type") == "text":
            parts.append(block.get("text", ""))
    text = "\n".join(parts).strip()
    # strip accidental fences
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


# ---------------------------------------------------------------------------
# Graph + source helpers
# ---------------------------------------------------------------------------

def load_graph() -> Tuple[Dict[str, dict], List[dict]]:
    raw = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in raw["nodes"]}
    edges = raw["links"]
    return nodes, edges


def edge_key(e: dict) -> str:
    a, b = sorted([e["source"], e["target"]])
    return f"{a}||{b}||{e.get('relation', '')}"


def resolve_source(source_file: Optional[str]) -> Optional[Path]:
    if not source_file:
        return None
    # Graphify paths are relative to the extract root (corpus/)
    p = CORPUS_DIR / source_file
    if p.exists():
        return p
    # fallback: already under corpus/markdown
    p2 = ROOT / source_file
    if p2.exists():
        return p2
    p3 = CORPUS_DIR / "markdown" / Path(source_file).name
    return p3 if p3.exists() else None


def _keyword_chunks(label: str) -> List[str]:
    stop = {
        "the", "and", "of", "for", "to", "a", "an", "in", "on", "law", "sama",
        "saudi", "central", "bank", "rules", "guide", "article", "provisions",
    }
    words = re.findall(r"[A-Za-z\u0600-\u06FF0-9]{3,}", label.lower())
    return [w for w in words if w not in stop][:8]


def source_context(path: Optional[Path], label: str, max_chars: int = MAX_CONTEXT_CHARS) -> str:
    if not path or not path.exists():
        return "(source file not found)"
    text = path.read_text(encoding="utf-8", errors="replace")
    keys = _keyword_chunks(label)
    if not keys:
        return text[:max_chars]

    # Score pages / windows by keyword hits
    pages = re.split(r"(?=^## Page \d+)", text, flags=re.MULTILINE)
    scored: List[Tuple[int, str]] = []
    for page in pages:
        if not page.strip():
            continue
        low = page.lower()
        score = sum(low.count(k) for k in keys)
        if score:
            scored.append((score, page.strip()))
    scored.sort(key=lambda x: -x[0])

    if not scored:
        return text[:max_chars]

    out: List[str] = []
    size = 0
    for _, page in scored:
        chunk = page[:1800]
        if size + len(chunk) > max_chars:
            remain = max_chars - size
            if remain > 200:
                out.append(chunk[:remain])
            break
        out.append(chunk)
        size += len(chunk)
        if size >= max_chars:
            break
    return "\n\n----\n\n".join(out)


def safe_filename(label: str) -> str:
    # Match Graphify Obsidian naming: label as filename (export uses node_filename)
    # Obsidian notes use the label directly with Windows-forbidden chars stripped lightly
    bad = '<>:"/\\|?*'
    name = "".join("_" if c in bad else c for c in label).strip() or "node"
    # Obsidian export may truncate; we resolve by reading frontmatter/title match
    return name


def find_node_note(label: str) -> Optional[Path]:
    """Find Obsidian note file for a node label."""
    direct = OBSIDIAN_DIR / f"{safe_filename(label)}.md"
    if direct.exists():
        return direct
    # Graphify may add _1 suffixes for collisions
    candidates = list(OBSIDIAN_DIR.glob(f"{safe_filename(label)}*.md"))
    # Prefer exact title match
    for c in candidates:
        if c.name.startswith("_COMMUNITY_"):
            continue
        try:
            head = c.read_text(encoding="utf-8", errors="replace")[:800]
        except OSError:
            continue
        m = re.search(r"^# (.+)$", head, re.MULTILINE)
        if m and m.group(1).strip() == label:
            return c
    # fuzzy: startswith
    for c in candidates:
        if not c.name.startswith("_COMMUNITY_"):
            return c
    return None


def find_community_note(name: str) -> Optional[Path]:
    p = OBSIDIAN_DIR / f"_COMMUNITY_{name}.md"
    if p.exists():
        return p
    # try sanitized
    for c in OBSIDIAN_DIR.glob("_COMMUNITY_*.md"):
        head = c.read_text(encoding="utf-8", errors="replace")[:400]
        m = re.search(r"^# (.+)$", head, re.MULTILINE)
        if m and m.group(1).strip() == name:
            return c
    return None


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

def load_cache() -> dict:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {"edges": {}, "communities": {}, "meta": {}}


def save_cache(cache: dict) -> None:
    cache["meta"] = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "model": MODEL,
    }
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# Enrichment generation
# ---------------------------------------------------------------------------

def _is_presentation_form(ch: str) -> bool:
    """Arabic Presentation Forms-A (FB50-FDFF) / Forms-B (FE70-FEFF).

    Their presence is a reliable signal of garbled OCR/PDF Arabic extraction
    (isolated, non-joining glyphs, usually stored in reversed visual order).
    Clean Arabic uses the standard block U+0600-U+06FF and never appears here.
    """
    o = ord(ch)
    return 0xFB50 <= o <= 0xFDFF or 0xFE70 <= o <= 0xFEFF


def sanitize_excerpt(ex: str) -> Tuple[str, bool]:
    """Return (excerpt, garbled). If the excerpt is meaningfully composed of
    Arabic presentation-form glyphs it is garbled OCR — drop it so it never
    reaches a note. Clean text (incl. clean standard-block Arabic) is kept."""
    ex = (ex or "").strip()
    if not ex:
        return "", False
    non_space = [c for c in ex if not c.isspace()]
    if not non_space:
        return "", False
    pf = sum(1 for c in non_space if _is_presentation_form(c))
    if pf and pf / len(non_space) > 0.15:
        return "", True
    if pf:
        # Mostly-clean excerpt with a few stray OCR glyphs — strip the glyphs
        # and tidy the whitespace/orphaned separators they leave behind.
        ex = "".join(c for c in ex if not _is_presentation_form(c))
        ex = re.sub(r"\s{2,}", " ", ex).strip()
        ex = re.sub(r"\s+([,.;:])", r"\1", ex)
    return ex, False


def clean_locator(loc: Optional[str]) -> Optional[str]:
    """Strip garbled Arabic presentation-form glyphs from a locator string and
    tidy the parenthetical debris they leave behind (e.g.
    'Page 5 (ﺔﻣﺪﻘﻣ / Introduction)' -> 'Page 5 (Introduction)')."""
    if not loc:
        return loc
    if not any(_is_presentation_form(c) for c in loc):
        return loc
    loc = "".join(c for c in loc if not _is_presentation_form(c))
    loc = re.sub(r"\(\s*/\s*", "(", loc)        # "( / Introduction" -> "(Introduction"
    loc = re.sub(r"\s*/\s*\)", ")", loc)         # "list / )" -> "list)"
    loc = re.sub(r"\(\s*\)", "", loc)            # empty "()"
    loc = re.sub(r"\s{2,}", " ", loc).strip()
    loc = re.sub(r"\s+\)", ")", loc)
    return loc or None


def build_edge_payload(
    batch: List[dict],
    nodes: Dict[str, dict],
) -> str:
    items = []
    for e in batch:
        # Canonical orientation: sorted node ids (matches edge_key)
        id_a, id_b = sorted([e["source"], e["target"]])
        a = nodes[id_a]
        b = nodes[id_b]
        a_path = resolve_source(a.get("source_file"))
        b_path = resolve_source(b.get("source_file"))
        items.append(
            {
                "edge_key": edge_key(e),
                "relation": e.get("relation"),
                "confidence": e.get("confidence"),
                "node_a": {
                    "id": id_a,
                    "label": a.get("label"),
                    "type": a.get("file_type"),
                    "source_file": a.get("source_file"),
                    "context": source_context(a_path, a.get("label", "")),
                },
                "node_b": {
                    "id": id_b,
                    "label": b.get("label"),
                    "type": b.get("file_type"),
                    "source_file": b.get("source_file"),
                    "context": source_context(b_path, b.get("label", "")),
                },
            }
        )
    return json.dumps({"edges_to_enrich": items}, ensure_ascii=False)


def enrich_edges(
    edges: List[dict],
    nodes: Dict[str, dict],
    cache: dict,
    api_key: str,
    limit: Optional[int] = None,
) -> dict:
    # unique undirected edges
    unique: Dict[str, dict] = {}
    for e in edges:
        unique[edge_key(e)] = e
    keys = list(unique.keys())
    if limit is not None:
        keys = keys[:limit]

    pending = [unique[k] for k in keys if k not in cache.get("edges", {})]
    print(f"Edges: {len(keys)} selected, {len(keys) - len(pending)} cached, {len(pending)} to enrich")

    def _store(result: dict) -> None:
        for item in result.get("edges", []):
            ek = item.get("edge_key")
            if not ek:
                continue
            # sanitize + clamp excerpts; drop garbled-OCR Arabic
            garbled_any = False
            for side in ("clause_a", "clause_b"):
                cl = item.get(side) or {}
                ex, garbled = sanitize_excerpt(cl.get("excerpt") or "")
                if garbled:
                    garbled_any = True
                    cl["excerpt"] = ""  # renderer shows an OCR marker instead
                elif len(ex) > MAX_EXCERPT_CHARS:
                    cl["excerpt"] = ex[: MAX_EXCERPT_CHARS - 1].rstrip() + "…"
                else:
                    cl["excerpt"] = ex
                item[side] = cl
            if garbled_any:
                note = "Source Arabic is OCR-garbled; verbatim quote omitted — consult the original document."
                cav = (item.get("caveat") or "").strip()
                item["caveat"] = f"{cav} {note}".strip() if cav else note
            cache.setdefault("edges", {})[ek] = item

    def _repair_keys(result: dict, batch: List[dict]) -> dict:
        """The model sometimes echoes a truncated/mangled edge_key (e.g. drops the
        '||relation' suffix). Remap any unrecognized key back to the batch's real
        key by matching the two node-id parts."""
        expected = {edge_key(e) for e in batch}
        prefix_map = {}
        for k in expected:
            a, b, _rel = k.split("||", 2)
            prefix_map[a + "||" + b] = k
        for item in result.get("edges", []):
            ek = item.get("edge_key", "")
            if ek in expected:
                continue
            parts = ek.split("||")
            if len(parts) >= 2:
                pref = parts[0] + "||" + parts[1]
                if pref in prefix_map:
                    item["edge_key"] = prefix_map[pref]
        return result

    def _process(batch: List[dict]) -> None:
        """Enrich a batch; on malformed JSON, split and retry, skipping only the bad edge."""
        user = build_edge_payload(batch, nodes)
        try:
            _store(_repair_keys(claude_json(SYSTEM_EDGES, user, api_key), batch))
            return
        except Exception as ex:  # noqa: BLE001 - resilience over strictness
            if len(batch) > 1:
                mid = len(batch) // 2
                print(f"    batch of {len(batch)} failed ({ex.__class__.__name__}); splitting {mid}+{len(batch) - mid}")
                _process(batch[:mid])
                _process(batch[mid:])
                return
            # single edge: one retry, then skip
            try:
                _store(_repair_keys(claude_json(SYSTEM_EDGES, user, api_key), batch))
                return
            except Exception as ex2:  # noqa: BLE001
                print(f"    SKIP edge (bad JSON after retry): {edge_key(batch[0])} [{ex2.__class__.__name__}]")

    n_batches = (len(pending) + EDGE_BATCH - 1) // EDGE_BATCH
    for i in range(0, len(pending), EDGE_BATCH):
        batch = pending[i : i + EDGE_BATCH]
        print(f"  edge batch {i // EDGE_BATCH + 1}/{n_batches} ({len(batch)} edges)...")
        _process(batch)
        save_cache(cache)
        time.sleep(0.4)
    return cache


def enrich_communities(
    nodes: Dict[str, dict],
    edges: List[dict],
    cache: dict,
    api_key: str,
) -> dict:
    # community_id -> members
    communities: Dict[Any, List[str]] = defaultdict(list)
    labels: Dict[Any, str] = {}
    for nid, n in nodes.items():
        cid = n.get("community")
        if cid is None:
            continue
        communities[cid].append(nid)
        if n.get("community_name"):
            labels[cid] = n["community_name"]

    # relation summary inside community
    payloads = []
    for cid, members in sorted(communities.items(), key=lambda x: x[0]):
        if str(cid) in cache.get("communities", {}) or cid in cache.get("communities", {}):
            continue
        member_labels = [nodes[m].get("label", m) for m in members]
        # internal edges
        mset = set(members)
        internal = []
        for e in edges:
            if e["source"] in mset and e["target"] in mset:
                internal.append(
                    {
                        "a": nodes[e["source"]].get("label"),
                        "b": nodes[e["target"]].get("label"),
                        "relation": e.get("relation"),
                    }
                )
        payloads.append(
            {
                "community_id": cid,
                "name": labels.get(cid, f"Community {cid}"),
                "members": member_labels,
                "internal_edges_sample": internal[:20],
            }
        )

    def _store_comm(result: dict) -> None:
        for item in result.get("communities", []):
            cid = item.get("community_id")
            if cid is None:
                continue
            cache.setdefault("communities", {})[str(cid)] = item

    def _process_comm(batch: List[dict]) -> None:
        user = json.dumps({"communities_to_enrich": batch}, ensure_ascii=False)
        try:
            _store_comm(claude_json(SYSTEM_COMMUNITIES, user, api_key, max_tokens=8192))
            return
        except Exception as ex:  # noqa: BLE001
            if len(batch) > 1:
                mid = len(batch) // 2
                print(f"    community batch of {len(batch)} failed ({ex.__class__.__name__}); splitting {mid}+{len(batch) - mid}")
                _process_comm(batch[:mid])
                _process_comm(batch[mid:])
                return
            try:
                _store_comm(claude_json(SYSTEM_COMMUNITIES, user, api_key, max_tokens=8192))
                return
            except Exception as ex2:  # noqa: BLE001
                print(f"    SKIP community (bad JSON after retry): {batch[0].get('community_id')} [{ex2.__class__.__name__}]")

    print(f"Communities: {len(communities)} total, {len(payloads)} to enrich")
    for i in range(0, len(payloads), COMMUNITY_BATCH):
        batch = payloads[i : i + COMMUNITY_BATCH]
        print(f"  community batch {i // COMMUNITY_BATCH + 1} ({len(batch)})...")
        _process_comm(batch)
        save_cache(cache)
        time.sleep(0.4)
    return cache


# ---------------------------------------------------------------------------
# Write Obsidian notes
# ---------------------------------------------------------------------------

def truncate_quote(text: str) -> str:
    t = (text or "").strip().replace("\n", " ")
    # Strip any stray Arabic presentation-form (OCR) glyphs that rode along in an
    # otherwise-clean excerpt, then tidy the debris they leave behind.
    if any(_is_presentation_form(c) for c in t):
        t = "".join(c for c in t if not _is_presentation_form(c))
        t = re.sub(r"\s+([,.;:])", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) > MAX_EXCERPT_CHARS:
        t = t[: MAX_EXCERPT_CHARS - 1].rstrip() + "…"
    return t


_WIKILINK_FORBIDDEN = set('<>:"/\\|?*')


def wikilink(label: str) -> str:
    """Return an Obsidian wikilink that resolves to the exported note filename.

    Graphify strips Windows-forbidden characters from note filenames (e.g.
    "AML/CTF Guide" -> "AMLCTF Guide.md"). A raw ``[[AML/CTF Guide]]`` link would
    fail to resolve and, for '/', spawn a hollow phantom node on the graph edge.
    When the label contains such a character we emit the alias form
    ``[[AMLCTF Guide|AML/CTF Guide]]`` so the link resolves while keeping the
    readable display text.
    """
    if any(c in _WIKILINK_FORBIDDEN for c in label):
        stripped = "".join(c for c in label if c not in _WIKILINK_FORBIDDEN)
        return f"[[{stripped}|{label}]]"
    return f"[[{label}]]"


def format_connection_block(
    neighbor_label: str,
    relation: str,
    confidence: str,
    enrichment: dict,
    self_is_a: bool,
) -> str:
    why = (enrichment.get("why") or "").strip()
    caveat = enrichment.get("caveat")
    ca = enrichment.get("clause_a") or {}
    cb = enrichment.get("clause_b") or {}
    # Map: clause_a is always node_a (edge source side in enrichment payload =
    # sorted? We stored by edge endpoints as given in batch: node_a=source, node_b=target
    # When rendering from a node's perspective, need correct sides.
    # edge_key uses sorted ids, but enrichment node_a/b follow original edge source/target
    # from the batch which used unique[e]=original edge. So clause_a = original source, clause_b = target.
    # Caller passes self_is_a meaning "this note is the edge's source node".

    my_cl = ca if self_is_a else cb
    other_cl = cb if self_is_a else ca

    def fmt_clause(cl: dict, title: str) -> str:
        loc = clean_locator(cl.get("locator"))
        ex = truncate_quote(cl.get("excerpt") or "")
        loc_s = f" ({loc})" if loc else ""
        if not ex:
            return f"- **{title}{loc_s}:** _(source text unavailable / OCR-garbled — consult original)_"
        return f"- **{title}{loc_s}:** \"{ex}\""

    lines = [
        f"### {wikilink(neighbor_label)} — `{relation}` [{confidence}]",
    ]
    if why:
        lines.append(f"- **What this link tells you:** {why}")
    lines.append(fmt_clause(my_cl, "Grounding — this node"))
    lines.append(fmt_clause(other_cl, "Grounding — related node"))
    if caveat:
        lines.append(f"- **Caveat:** {caveat}")
    lines.append("")
    return "\n".join(lines)


def split_frontmatter(text: str) -> Tuple[str, str]:
    if text.startswith("---"):
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
        if m:
            return m.group(1), m.group(2)
    return "", text


def rewrite_node_note(
    path: Path,
    node_id: str,
    nodes: Dict[str, dict],
    edges: List[dict],
    cache: dict,
) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = split_frontmatter(text)

    # Gather incident edges
    incident = []
    for e in edges:
        if e["source"] == node_id or e["target"] == node_id:
            incident.append(e)
    if not incident:
        return False

    blocks = []
    for e in sorted(incident, key=lambda x: nodes[x["target"] if x["source"] == node_id else x["source"]].get("label", "")):
        other_id = e["target"] if e["source"] == node_id else e["source"]
        other = nodes[other_id]
        ek = edge_key(e)
        enr = cache.get("edges", {}).get(ek)
        if not enr:
            # fallback thin line
            blocks.append(
                f"### {wikilink(other.get('label'))} — `{e.get('relation')}` [{e.get('confidence', 'EXTRACTED')}]\n"
                f"- **What this link tells you:** _(enrichment pending)_\n"
            )
            continue
        # clause_a/b follow sorted(node ids) orientation used at enrich time
        id_a, id_b, _rel = ek.split("||", 2)
        self_is_a = node_id == id_a
        blocks.append(
            format_connection_block(
                other.get("label", other_id),
                e.get("relation", ""),
                e.get("confidence", "EXTRACTED"),
                enr,
                self_is_a=self_is_a,
            )
        )

    # Rebuild body: keep title, replace Connections, keep trailing tags
    title_m = re.search(r"^# .+$", body, re.MULTILINE)
    title = title_m.group(0) if title_m else f"# {nodes[node_id].get('label')}"

    tags_m = re.search(r"\n(#graphify/\S.*)$", body, re.MULTILINE)
    # collect all trailing tag lines
    tag_lines = []
    for line in body.strip().splitlines()[::-1]:
        if line.startswith("#graphify/") or line.startswith("#community/"):
            tag_lines.append(line)
        elif line.strip() == "":
            continue
        else:
            break
    tag_lines.reverse()
    if not any("graphify/enriched" in t for t in tag_lines):
        # append enriched marker into a tag line if present
        if tag_lines:
            tag_lines[-1] = tag_lines[-1] + " #graphify/enriched"
        else:
            tag_lines = ["#graphify/enriched"]

    new_body = (
        f"{title}\n\n"
        f"## Connections\n\n"
        + "\n".join(blocks)
        + "\n"
        + " ".join(tag_lines)
        + "\n"
    )

    # ensure enriched tag in frontmatter tags list
    if fm:
        if "graphify/enriched" not in fm:
            if "tags:" in fm:
                fm = fm.rstrip() + "\n  - graphify/enriched\n"
            else:
                fm = fm.rstrip() + "\ntags:\n  - graphify/enriched\n"
        new_text = f"---\n{fm.strip()}\n---\n\n{new_body}"
    else:
        new_text = new_body

    path.write_text(new_text, encoding="utf-8")
    return True


def rewrite_community_note(
    path: Path,
    cid: Any,
    cache: dict,
) -> bool:
    enr = cache.get("communities", {}).get(str(cid))
    if not enr:
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = split_frontmatter(text)

    theme = (enr.get("theme") or "").strip()
    bullets = enr.get("how_members_connect") or []

    insert = ["## Why this community", ""]
    if theme:
        insert.append(theme)
        insert.append("")
    insert.append("## How members connect")
    insert.append("")
    for b in bullets:
        b = str(b).lstrip("- ").strip()
        if b:
            insert.append(f"- {b}")
    insert.append("")
    block = "\n".join(insert)

    # Insert after title / cohesion header, before ## Members
    if "## Why this community" in body:
        # replace existing enrichment block through How members connect
        body = re.sub(
            r"## Why this community\n.*?(?=\n## Members|\n## Live Query|\Z)",
            block,
            body,
            count=1,
            flags=re.DOTALL,
        )
    elif "## Members" in body:
        body = body.replace("## Members", block + "## Members", 1)
    else:
        body = body.rstrip() + "\n\n" + block

    if fm:
        if "enriched: true" not in fm:
            fm = fm.rstrip() + "\nenriched: true\n"
        new_text = f"---\n{fm.strip()}\n---\n\n{body.lstrip()}"
    else:
        new_text = body
    path.write_text(new_text, encoding="utf-8")
    return True


def apply_to_vault(nodes: Dict[str, dict], edges: List[dict], cache: dict) -> Tuple[int, int]:
    node_n = 0
    for nid, n in nodes.items():
        label = n.get("label") or nid
        path = find_node_note(label)
        if not path:
            continue
        if rewrite_node_note(path, nid, nodes, edges, cache):
            node_n += 1

    comm_n = 0
    # map community id -> name
    names: Dict[Any, str] = {}
    for n in nodes.values():
        if n.get("community") is not None and n.get("community_name"):
            names[n["community"]] = n["community_name"]
    for cid, name in names.items():
        path = find_community_note(name)
        if path and rewrite_community_note(path, cid, cache):
            comm_n += 1
    return node_n, comm_n


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Enrich Graphify Obsidian notes with link context")
    ap.add_argument("--limit-edges", type=int, default=None, help="Only enrich N edges (smoke test)")
    ap.add_argument("--skip-communities", action="store_true")
    ap.add_argument("--apply-only", action="store_true", help="Skip LLM; rewrite notes from cache")
    ap.add_argument("--no-apply", action="store_true", help="Enrich cache only; do not touch vault notes (smoke test)")
    ap.add_argument("--force", action="store_true", help="Ignore cache and re-enrich")
    args = ap.parse_args()

    if not GRAPH_PATH.exists():
        raise SystemExit(f"Missing {GRAPH_PATH}")
    if not OBSIDIAN_DIR.exists():
        raise SystemExit(f"Missing {OBSIDIAN_DIR} — run graphify export obsidian first")

    nodes, edges = load_graph()
    cache = load_cache()
    if args.force:
        cache["edges"] = {}
        cache["communities"] = {}

    if not args.apply_only:
        api_key = require_api_key()
        print(f"Model: {MODEL}")
        enrich_edges(edges, nodes, cache, api_key, limit=args.limit_edges)
        if not args.skip_communities and args.limit_edges is None:
            enrich_communities(nodes, edges, cache, api_key)
        elif not args.skip_communities and args.limit_edges is not None:
            print("Skipping communities during --limit-edges smoke test")

    if args.no_apply:
        print("--no-apply: cache written, vault left untouched")
        print(f"Cache: {CACHE_PATH}")
        return 0

    node_n, comm_n = apply_to_vault(nodes, edges, cache)
    print(f"Updated {node_n} node notes, {comm_n} community notes")
    print(f"Cache: {CACHE_PATH}")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore
    except Exception:
        pass
    raise SystemExit(main())
