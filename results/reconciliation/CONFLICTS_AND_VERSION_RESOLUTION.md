# Conflicts and Version Resolution — Phase 1.5

Per directive Section 4/12: every disagreement is recorded with SOURCE A, SOURCE B, OBJECT,
CONFLICT TYPE, VERSION, PROVENANCE, CURRENT STATUS, RECOMMENDED RESOLUTION, CONFIDENCE. **No
conflict below has been silently resolved** — where a recommendation is given, it is a
recommendation only; no registry status was changed as a result of this document.

---

## CONFLICT-001 — ARBS canonicity

| Field | Value |
|---|---|
| SOURCE A | SOURCE-004 (`UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0.xlsx`), embedded UCG Specification text, Section 16: *"The ARBS Specification (Phases XXIII through XXV) is **the most formally rigorous component of the compiler architecture**."* Also `registries/MASTER_THEOREM_REGISTRY.csv`: 8 ARBS-derived theorems (RF-001..005, RK-001..003), all status **CERTIFIED**. |
| SOURCE B | SOURCE-010 (`UOC_ToE_Open_Closure_Master_v1.0.xlsx`), `00_README`: *"ARBS governance: ARBS is **LEGACY ONLY. It is not canonical.** Preserve non-ARBS results; re-derive ARBS-dependent results in TDIC/UOC/MDCL."* Repeated in `19_PAST_ATTEMPTS_RECOMMENDATIONS` (ATT-004: "Retire as canonical; preserve transferable results; re-derive ARBS-dependent claims in TDIC") and `22_PRIORITY_EXECUTION_PLAN` (P0-01: "ARBS legacy only"). |
| OBJECT | Canonical status of the ARBS (Automated Recovery / Bridge / Spectral?) framework and its 8 certified theorems. |
| CONFLICT TYPE | Direct status contradiction — SOURCE A treats ARBS as the most rigorous, canonical, certified component; SOURCE B treats it as legacy/non-canonical, to be retired and re-derived elsewhere. |
| VERSION | SOURCE-004 has no internal date beyond its synchronization timestamp (2026-08-16T19:08–19:12). SOURCE-010 has no internal date at all — no dashboard, no timestamp field found anywhere in its 30 sheets. **Chronological ordering between the two documents cannot be established from internal evidence.** |
| PROVENANCE | SOURCE-004: 90→110-sheet synthesis with an explicit, auditable synchronization chain (Sync v1→v2→v3→DAG Closure→Bridge Closure, all hash-verified this phase). SOURCE-010: a standalone document with zero sheet-name overlap with any other file in the corpus and zero reference to it in SOURCE-004's own 17-row source-corpus registry — it is not part of the verified synchronization chain at all. |
| CURRENT STATUS | UNRESOLVED. Both positions are preserved. `registries/MASTER_THEOREM_REGISTRY.csv`'s ARBS entries remain CERTIFIED (unchanged). |
| RECOMMENDED RESOLUTION | Do not downgrade the 8 ARBS theorems. They were CERTIFIED under an explicit proof basis (Mosco convergence, Gromov-Hausdorff, Trotter-Kato, Mac Lane coherence — see `registries/MASTER_THEOREM_REGISTRY.csv`), and a later document *asserting* non-canonicity is not itself a falsification or a superseding proof — it is a governance recommendation with no accompanying counter-proof. The recommended treatment is to flag ARBS as **"CERTIFIED, CANONICITY DISPUTED"** pending either (a) an explicit proof obligation showing an ARBS-dependent result fails, or (b) a dated, sourced governance decision that supersedes SOURCE-004's Section 16 characterization. This is a *recommendation*, not applied to the registries by this phase. |
| CONFIDENCE | MEDIUM. High confidence the conflict is real and textually explicit; medium confidence on resolution because chronology cannot be established, so it is not possible to determine whether SOURCE-010 is a later correction or an independent/earlier exploratory branch. |

---

## CONFLICT-002 — Closure-layer numbering (C0–C10 vs. C0–C16)

| Field | Value |
|---|---|
| SOURCE A | `registries/MASTER_CLOSURE_LAYERS_C0_C10.csv` (from SOURCE-004): exactly 11 layers, C0 through C10, each with a named core target, closure criterion, and explicit obligations. This is the scheme used throughout Phase 1 and the PRF-PRIM execution. |
| SOURCE B | SOURCE-010: references layers **C11** (UV completion — `01_TOE_BENCHMARK` TOE-005, `19_PAST_ATTEMPTS_RECOMMENDATIONS` ATT-013/016/017/018), **C12/C13** (known-limit hierarchy / renormalization — TOE-009, TOE-016), **C14** (black-hole information — TOE-018, ATT-019), and **C16** (selection/uniqueness — `15_SELECTION_UNIQUENESS`, TOE-013, D-029). No formal definition sheet for any of C11–C16 exists anywhere in SOURCE-010 (no `11_...` / `12_...` / `13_...` closure-layer-definition sheet analogous to SOURCE-004's `24_C0_C10_CLOSURE_LAYERS`) — they appear only as scattered cell references. C15 is never referenced. |
| OBJECT | The total number and identity of closure layers in the UOC architecture. |
| CONFLICT TYPE | Scope extension without formal specification — not a direct contradiction (C0–C10's own definitions are not disputed), but SOURCE B presupposes additional layers that SOURCE A's canonical registry does not contain. |
| VERSION | Same as CONFLICT-001 — no internal dating available for SOURCE-010. |
| PROVENANCE | Same as CONFLICT-001. |
| CURRENT STATUS | UNRESOLVED / UNADOPTED. `registries/MASTER_CLOSURE_LAYERS_C0_C10.csv` is unchanged; C11–C16 are NOT added to it. |
| RECOMMENDED RESOLUTION | Register C11 ("UV completion"), C12/C13 ("known-limit hierarchy / renormalization"), C14 ("black-hole information — note: distinct from and narrower than C7's existing horizon/information scope"), and C16 ("selection/uniqueness") as a **PROPOSED EXTENSION** to the closure architecture, pending a formal definition sheet with the same rigor as `24_C0_C10_CLOSURE_LAYERS`. Do not renumber or merge into C0–C10 without that. |
| CONFIDENCE | HIGH that the scope-extension is real and intentional (used consistently across 6+ sheets); LOW confidence on exact boundaries since no formal definitions exist to check against. |

---

## CONFLICT-003 — PRF-* ID namespace ambiguity

| Field | Value |
|---|---|
| SOURCE A | `registries/MASTER_PROOF_REGISTRY.csv`: named IDs (`PRF-ROG-3`, `PRF-PiO`, `PRF-ATU`, `PRF-SFP`, `PRF-UGNT`, `PRF-BORN`, `PRF-LOR`, `PRF-GEN`, `PRF-CONST`, `PRF-BNAT`, `PRF-PRIM`, plus this phase's 4 new `PRF-PRIM-*` sub-obligations). |
| SOURCE B | SOURCE-010, `07_OPEN_PROOFS`: numeric IDs `PRF-001` through approximately `PRF-018`, e.g. `PRF-001,Primitive reconciliation,"Formal equivalence/reduction among DTC, UDP, gradient, MDCL, NCG grammar routes",C0,OPEN,...` — note `PRF-001`'s CONTENT is the same obligation as `PRF-PRIM`, but under a DIFFERENT ID. |
| OBJECT | The proof-obligation ID namespace. |
| CONFLICT TYPE | Namespace collision risk — `PRF-001..018` (numeric) and `PRF-PRIM`/`PRF-BORN`/etc. (named) are different ID schemes referring to overlapping content, not literally colliding today, but liable to collide if either scheme is extended numerically or if `PRF-PRIM` is ever renamed `PRF-001`-style. |
| VERSION | Same dating limitation as above. |
| PROVENANCE | Same as CONFLICT-001. |
| CURRENT STATUS | No collision has occurred (verified: no existing registry ID matches any SOURCE-010 numeric PRF-* ID exactly). Not merged. |
| RECOMMENDED RESOLUTION | Treat SOURCE-010's `PRF-001..018` as an independent, PARALLEL enumeration (register with a source-qualified prefix, e.g. `OPEN-PRF-001`, if ever merged) rather than assuming `PRF-001` = `PRF-PRIM`. Content mapping (which numeric ID corresponds to which named obligation) was NOT performed in this phase — flagged as future reconciliation work, not resolved here. |
| CONFIDENCE | HIGH the risk is real; MEDIUM on the specific content-mapping since it was not exhaustively cross-checked row by row. |

---

## Non-conflicts (checked, confirmed clean — recorded to show the check was actually performed)

| Item | Check performed | Result |
|---|---|---|
| Sync v1.0/v2.0/v3.0 vs. SOURCE-004 content | Full per-sheet SHA-256 diff, all 4 files, 318 sheets | 0 unexpected diffs — see `SYNCHRONIZATION_HISTORY.md` |
| DER-entry count 60→55→59 across sync versions | Cross-checked against `registries/MASTER_DER_VERSION_RECONCILIATION.csv` (already ingested Phase 1) | Already explained (v1 used a broader "registry rows" count including primitives/axioms; v2/v3/DAG-layer count DER-IDs specifically) — not a new conflict, not re-litigated |
| BR-* IDs in SOURCE-010's `05_OPEN_BRIDGES` (17 rows) | Compared against `registries/MASTER_BRIDGE_REGISTRY.csv` BR-001..029 | All 17 IDs are pre-existing; content of the one spot-checked (BR-001) is consistent, not contradictory — this is a re-listing in an "open closure status" framing, not a new or conflicting bridge |
| Q_ID values in `25_NOT_YET_ADDRESSED` (164 rows) | Compared against `registries/MASTER_TOE_GAP_MATRIX_164.csv` | Same 164-question numbering; this sheet is a valuable NEW per-question closure-flag layer, not a conflicting renumbering — see `NEWLY_DISCOVERED_CALCULATIONS.md` |
| Ξ_UOC⁴ arithmetic (`24_AUDIT_DASHBOARD`) | Independently recomputed: (6.50×10⁻³¹)⁴ | Exact match (1.7850625×10⁻¹²¹) — reproducible, not a conflict |
