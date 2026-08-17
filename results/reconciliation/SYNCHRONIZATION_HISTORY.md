# Synchronization Master History — v1.0 → v2.0 → v3.0 → DAG Closure → Bridge Closure Execution

**Method:** every worksheet of every file was exported to CSV and SHA-256-hashed per sheet. Two
sheets are "identical" only if their hash matches exactly (verbatim cell-for-cell). No sheet was
read for meaning-based comparison where a hash comparison was possible — this avoids any risk of
silently smoothing over a real difference.

## Result: the entire chain is strictly additive

```
Sync_v1.0 (50 sheets)
   |  +13 new sheets (40_DER_CANONICAL_SOURCE .. 52_V2_SYNCHRONIZATION_DELTA)
   |  0 sheets removed, 0 shared sheets content-changed (except 00_DASHBOARD)
   v
Sync_v2.0 (63 sheets)
   |  +10 new sheets (53_SOURCE_CORPUS_REGISTRY .. 62_V3_SYNC_CHECKSUMS)
   |  0 sheets removed, 0 shared sheets content-changed (except 00_DASHBOARD)
   v
Sync_v3.0 (73 sheets)  ============ 0 diffs on all 73 shared sheets ============
   |  +29 new sheets (DAG_00_DASHBOARD .. DAG_28_AUDIT_CORRECTIONS)
   v
Master_Dependency_DAG_Closure_v1.0 (102 sheets)  === 101/102 shared sheets identical ===
   |  +8 new sheets (BRIDGE_00_MASTER_REGISTRY .. BRIDGE_07_SOURCE_EVIDENCE)
   |  1 sheet changed: DAG_00_DASHBOARD (+2 additive summary rows for the Bridge extension)
   v
UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0 (110 sheets)  [= SOURCE-004, already in repo]
```

At every step: **zero sheets removed, zero renamed, zero reclassified, zero existing row content
modified**, except the rolling `00_DASHBOARD` / `DAG_00_DASHBOARD` summary sheets, which are
expected to change (they report live counts). This is a clean, monotonic, purely additive
synchronization history. No corrective, superseding, or exploratory-and-abandoned change was found
anywhere in this chain — every version is a strict superset of its predecessor.

## Sheet-level diffs

### v1.0 → v2.0

**New sheets (13):** `40_DER_CANONICAL_SOURCE`, `41_EQUATIONS_SOURCE_EXACT`,
`42_EQUATION_RECONCILIATION`, `43_TOE_GAP_MATRIX_164`, `44_CANONICAL_NODE_REGISTRY`,
`45_DEPENDENCY_EDGES_DER`, `46_RECOVERY_BRANCHES`, `47_C0_C10_CANONICAL_MATRIX`,
`48_EQUATION_LINEAGE`, `49_VARIABLE_REGISTRY`, `50_EQUATION_DER_LINKS`, `51_SYNC_SOURCE_HASHES`,
`52_V2_SYNCHRONIZATION_DELTA`.

**Nature of the change (per v2's own `52_V2_SYNCHRONIZATION_DELTA` sheet, preserved verbatim in
`registries/MASTER_DER_VERSION_RECONCILIATION.csv`'s sibling context):** ADDITIVE. v2 restored the
exact source DER registry and Master Equation Matrix (v1's sheets were compact extractions), added
a normalized Gap Matrix table, a unified canonical node registry, an executable dependency-edge
registry, a recovery-branch registry, a C0–C10 canonical matrix, equation lineage, a variable
registry, and a source-hash registry. Classified by this reconciliation as: **ADDITIVE**, not
corrective (no v1 row was overwritten; v1's sheets are still present, byte-identical, inside v2).

**Removed:** none. **Renamed:** none. **Reclassified:** none.

### v2.0 → v3.0

**New sheets (10):** `53_SOURCE_CORPUS_REGISTRY`, `54_SOURCE_TEXT_CORPUS`,
`55_SOURCE_XLSX_SNAPSHOTS`, `56_DER_VERSION_RECONCILIATION`, `57_STATUS_SEMANTICS_CANONICAL`,
`58_CURRENT_CHAT_CANONICAL_RULES`, `59_COSMO_DYN_EXECUTED_AND_OPEN`, `60_BRIDGE_REGISTRY_ENRICHED`,
`61_V3_WORKBOOK_INVENTORY`, `62_V3_SYNC_CHECKSUMS`.

**Nature of the change:** ADDITIVE. v3 added the full upstream source-corpus registry (17 SRC-*
entries), the raw extracted source text corpus (3,017 rows) and xlsx snapshots (605 rows), an
explicit DER v1-vs-v2 version reconciliation table (102 rows), canonical status semantics, current-
chat governance rules, a COSMO-DYN executed/open split, an enriched bridge registry, a full
workbook inventory, and file-level sync checksums. Classified: **ADDITIVE**.

**Removed:** none. **Renamed:** none. **Reclassified:** none. **Content-changed on shared
sheets: NONE (0/73)** — this is the cleanest transition in the whole chain.

### v3.0 → Master_Dependency_DAG_Closure_v1.0

**New sheets (29):** the full `DAG_00_DASHBOARD` .. `DAG_28_AUDIT_CORRECTIONS` family — nodes,
edges, equation/bridge/theorem/proof/prediction sub-DAGs, cycle audit, topological order, closure
obligations, critical frontier, impact map, source provenance, synchronization audit, phase
execution plan, audit corrections.

**Nature of the change:** ADDITIVE — this is exactly the "make the dependency graph executable"
step. **Content-changed on shared sheets: 0/73.**

### DAG Closure v1.0 → Bridge Closure Execution v2.0 (= SOURCE-004, already in repo)

**New sheets (8):** `BRIDGE_00_MASTER_REGISTRY` .. `BRIDGE_07_SOURCE_EVIDENCE`.

**Nature of the change:** ADDITIVE — adds BR-001–BR-029 execution plans, equation triples,
canonical chains, status audit, remaining frontier, dashboard, source evidence, on top of the
already-existing bridge registry (`22_BRIDGES`, unchanged).

**Content-changed: 1/102 sheets** — `DAG_00_DASHBOARD` gained exactly 2 additive rows ("Bridge
closure extension", "Bridge records") reporting the new BR- coverage. No existing row altered.

## Dashboard evolution (the one sheet that changes at every step)

| Version | Timestamp | Equations | DER unique | Gap Qs | Nodes | Edges | Notable new metric |
|---|---|---|---|---|---|---|---|
| v1.0 | 2026-08-16T19:00:55 | 174 | ~60 (compact) | — | — | — | "Observational-input firewall" rule stated |
| v2.0 | 2026-08-16T19:03:48 | 174 | 55 | 164 | 518 | 70 | Canonical node registry introduced |
| v3.0 | 2026-08-16T19:08:34 | 174 | 55 | 164 | 518 | 70 | Source corpus (17 records), source text (3,017 rows) |
| DAG Closure v1.0 (`DAG_00_DASHBOARD`) | 2026-08-16T19:12:52Z | 174 | 59 | — | 779 | 320 (106 internal) | Cycle audit: 0 cycles |
| Bridge Closure Execution v2.0 (SOURCE-004) | (same, +2 rows) | 174 | 59 | — | 779 | 320 | +BR-001..029 registry |

Note the DER-unique-entry count moves 60(compact)→55→55→59 — not a contradiction: v1's "60" was an
explicitly compact/abbreviated extraction (per v1's own dashboard wording, "60 registry rows
including primitives, axioms, recovery, validation and theorem entries" — a broader count than
"DER entries" alone), while v2/v3's "55" and the DAG layer's "59" are the same DER-ID namespace
counted more precisely as the registry matured. This is discussed further in
`registries/MASTER_DER_VERSION_RECONCILIATION.csv` (already ingested in Phase 1) and is NOT a new
conflict — it is the same v1→v2 delta Phase 1 already had access to via SOURCE-004's embedded copy.

## Canonical synchronization decision

**No selection was necessary.** Because the chain is verified byte-identical wherever content is
shared, there is no case in this chain where v1, v2, or v3 disagrees with SOURCE-004 on any row
that survived. **SOURCE-004 (`UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0.xlsx`) remains the
canonical, most-complete synthesis** — this newly-ingested chain does not change that conclusion,
it independently *proves* it by hash, closing a provenance gap Phase 1 could not close (Phase 1
had to treat the v1/v2/v3/DAG-Closure files as "referenced but not independently present";
they are now present and verified).

**The one file that changes this picture is `UOC_ToE_Open_Closure_Master_v1.0.xlsx` (SOURCE-010)**,
which is NOT part of this chain at all (zero sheet-name overlap, not referenced in SOURCE-004's own
provenance tables) — see `NEWLY_DISCOVERED_CALCULATIONS.md` and `CONFLICTS_AND_VERSION_RESOLUTION.md`.

## Historical snapshots preserved

Per governance rule 5 (preserve earlier synchronization states), the differing dashboard sheets
from all 3 sync versions and the pre-Bridge DAG dashboard are preserved verbatim at:
- `source_records/spreadsheets/UOC_ToE_Canonical_Synchronization_Master_v1.0/00_DASHBOARD.csv`
- `source_records/spreadsheets/UOC_ToE_Canonical_Synchronization_Master_v2.0/00_DASHBOARD.csv`
- `source_records/spreadsheets/UOC_ToE_Canonical_Synchronization_Master_v3.0/00_DASHBOARD.csv`
- `source_records/spreadsheets/UOC_ToE_Master_Dependency_DAG_Closure_v1.0/DAG_00_DASHBOARD.csv`

The other ~250 sheets across these 4 files were NOT re-copied into the repository a second time
(they are verified byte-identical to files already present from Phase 1) — this avoids duplicating
several hundred redundant CSV files while still fully documenting and hash-verifying their content.
