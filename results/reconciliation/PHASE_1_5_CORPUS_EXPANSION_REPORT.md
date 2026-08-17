# PHASE 1.5 — Corpus Expansion + Reconciliation Report

**Scope: reconciliation only.** No new theorem was proven, no new DER was executed, no new
hypothesis was numerically explored. Per the Execution Firewall (directive Section 8A), the only
computations performed were: (1) SHA-256 verification of 5 new files and 318 extracted worksheets,
and (2) one trivial arithmetic reproduction (Ξ_UOC⁴) to check a claim already implied by an existing
registered value.

## 1. What was ingested

Five new files:

| File | SOURCE-ID | Bytes | Relationship to existing corpus |
|---|---|---|---|
| UOC_ToE_Canonical_Synchronization_Master_v1.0.xlsx | SOURCE-006 | 358,987 | Ancestor of SOURCE-004, 49/50 sheets already present |
| UOC_ToE_Canonical_Synchronization_Master_v2.0.xlsx | SOURCE-007 | 468,963 | Ancestor of SOURCE-004, 62/63 sheets already present |
| UOC_ToE_Canonical_Synchronization_Master_v3.0.xlsx | SOURCE-008 | 809,889 | Ancestor of SOURCE-004, 73/73 sheets already present (0 diffs) |
| UOC_ToE_Master_Dependency_DAG_Closure_v1.0.xlsx | SOURCE-009 | 1,044,948 | Direct ancestor of SOURCE-004, 101/102 sheets already present |
| UOC_ToE_Open_Closure_Master_v1.0.xlsx | SOURCE-010 | 134,233 | **Genuinely new — 0 sheet overlap with anything else in the corpus** |

Full detail: `results/reconciliation/SYNCHRONIZATION_HISTORY.md`, `registries/source_registry_vNEXT.csv`.

## 2. Headline finding: the provenance chain closes cleanly

Every sheet of every new file was extracted and SHA-256-hashed. The result: **SOURCE-006 → 007 →
008 → 009 → SOURCE-004 is a single, strictly additive lineage** — 0 sheets removed at any step, 0
existing rows modified anywhere except the expected rolling dashboard summaries. This independently
*proves*, rather than merely asserts, what Phase 1 could only treat as a narrative claim (Phase 1
had these files only as "referenced but not independently present"). **SOURCE-004 remains the
canonical, most-complete synthesis** — this phase does not change that conclusion; it closes the
provenance gap behind it.

The one exception is **SOURCE-010 (`Open_Closure_v1.0`)**, which is not part of this chain at all.

## 3. What is genuinely new: SOURCE-010

`UOC_ToE_Open_Closure_Master_v1.0.xlsx` is a standalone, 30-sheet "open closure program" —
external ToE-completeness benchmarks, successful-theory and external-QG-program comparisons, an
internal open-problem/theorem/proof/equation/variable/simulation-target registry, per-domain
closure sheets, a per-question closure-flag audit of all 164 gap-matrix questions, a past-attempts
log, a theorem-target dependency graph, a priority execution plan, and a candidate scorecard.

**No previously-executed-but-unregistered calculation was found in it.** It is, by its own stated
purpose, a planning and gap-analysis document, not a calculation record. Full search record:
`results/reconciliation/NEWLY_DISCOVERED_CALCULATIONS.md`.

**Two material findings did come out of it:**

1. **TDIC ("Typed Dependency Incidence Complex")** — a proposed replacement canonical substrate for
   ARBS. No formal mathematical definition was found anywhere in the corpus; registered as
   **PROPOSED, NOT EXECUTED**, not tested.
2. **ARBS canonicity dispute** — SOURCE-010 states ARBS is *"LEGACY ONLY... not canonical,"*
   directly conflicting with SOURCE-004's characterization of ARBS as *"the most formally rigorous
   component of the compiler architecture"* and 8 CERTIFIED ARBS theorems in
   `registries/MASTER_THEOREM_REGISTRY.csv`. **Not resolved; not applied to any registry.** Full
   record: `results/reconciliation/CONFLICTS_AND_VERSION_RESOLUTION.md`, CONFLICT-001.

A third finding: SOURCE-010 references closure layers **C11–C14 and C16**, beyond the canonical
C0–C10 architecture, with no formal definitions — registered as a **PROPOSED EXTENSION, NOT
ADOPTED** (CONFLICT-002).

## 4. C0 / PRF-PRIM reassessment

**PRF-PRIM is preserved exactly as executed. It was NOT rerun.**

`TH-001` (SOURCE-010, `06_OPEN_THEOREMS`) gives the formal theorem target PRF-PRIM approximates:
reconcile **DTC/UDP/gradient/MDCL/NCG** realizations. PRF-PRIM tested 4 systems (DTC, gradient/
Physical, Computational B=(U,V,E), Extended MDCL) but did not independently test **UDP** or **NCG**
as their own primitive-grammar realizations. This **broadens the known scope of the parent target**
without invalidating, strengthening, weakening, or contradicting anything PRF-PRIM computed. `INT-001`
and `SEL-001` (SOURCE-010) independently confirm PRF-PRIM targeted the correct, still-open problem.
Full detail: `results/reconciliation/NEWLY_DISCOVERED_CALCULATIONS.md` Section 7,
`results/workbooks/PHASE_1_5_CORPUS_RECONCILIATION.xlsx` sheet `C0_Impact`.

## 5. C0–C9 closure frontier (5-axis reassessment)

Full table: `results/workbooks/PHASE_1_5_CORPUS_RECONCILIATION.xlsx` sheet `C1_C9_Frontier`.
Summary: C0 (PARTIALLY ADVANCED, OPEN), C1 (OPEN), C2 (CALCULATED/PARTIAL, scoped), C3 (OPEN), C4
(PARTIAL), C5 (PARTIAL), C6 (CALCULATED/PARTIAL, scoped), C7 (OPEN), **C8 (PARTIAL/DISPUTED — ARBS
canonicity conflict)**, C9 (OPEN/PARTIAL). No layer's status was changed by this phase; C8 gained an
explicit dispute flag.

## 6. Master DAG update

`compiler/dag/MASTER_DAG_vNEXT_nodes.csv` / `MASTER_DAG_vNEXT_edges.csv`: all 783 existing nodes /
326 existing edges preserved verbatim (verified 0 modified), plus **229 new nodes** and **30 new
edges**, all sourced from SOURCE-010 and tagged `SOURCE-REGISTERED`, none promoted past its source
status. Cycle audit: **PASS** (0 cycles, both the new 30-edge sub-graph and the full 353-edge merged
graph independently checked). No speculative edge was added — the 30 new edges are exactly
SOURCE-010's own `21_MASTER_CLOSURE_DAG` parent→child records, not inferred. `master_nodes.csv` /
`master_edges.csv` themselves are unchanged (Phase-1/PRF-PRIM state preserved).

## 7. Governance compliance

- No result was rewritten, downgraded, or reinterpreted. PRF-PRIM's conclusion (OPEN, 3-slot
  reduction within A/D only, 4 falsifications, 2 new lemmas) stands exactly as reported.
- No candidate (TDIC) was promoted to a theorem.
- No conflict (ARBS canonicity, closure-layer numbering, PRF-* namespace) was silently resolved —
  all three are recorded in `CONFLICTS_AND_VERSION_RESOLUTION.md` with explicit UNRESOLVED status.
- All registry updates are append-only (verified: existing rows byte-identical before/after in
  every touched file) or new `_vNEXT` files that never overwrite their Phase-1 predecessors.
- No observational value was used as an ancestor of any internally-generated quantity.

---

## NEXT EXECUTABLE DER

**Ranked priority list (per directive Section 9):**

1. **DER-ORG-006** — Fixed-point equivalence theorem (C1)
2. **PRF-PRIM-DELTA-TYPE** — resolve Δ's boundary-operator-vs-endomorphism type inconsistency (C0)
3. Test UDP and NCG as independent primitive-grammar realizations against TH-001's full scope (C0)

**DER ID:** DER-ORG-006

**TITLE:** Fixed-point equivalence theorem

**DEPENDENCIES:** DER-ORG-003 (persistence fixed point, CERTIFIED), DER-SPC-005 (persistence
operator R=exp(-βL), CERTIFIED); conceptually downstream of PRF-PRIM (C0), which remains open but
was independently confirmed by this phase to not block C1 computationally (no downstream branch,
including the fixed-point machinery, was found in either PRF-PRIM or this reconciliation to require
a specific C0 resolution first).

**WHY IT IS NEXT:** Unchanged from the prior recommendation. SOURCE-010's own, independently
authored priority plan (`22_PRIORITY_EXECUTION_PLAN`, task P0-02: "Close Γ fixed-point
implementation... CRITICAL") ranks this same obligation immediately after "freeze canonical
substrate" (P0-01) — an independent confirmation from the newly-ingested corpus that this is the
correct next target, not merely a holdover recommendation. No newly-discovered calculation in
SOURCE-010 substitutes for or completes it; `TH-002`/`TH-003`/`TH-004` (SOURCE-010's own C1 theorem
targets) confirm it is still OPEN with the identical statement PRF-PRIM's execution left it in.

**PREREQUISITES CONFIRMED:** DER-ORG-003 and DER-SPC-005 are both CERTIFIED in
`registries/MASTER_DER_REGISTRY.csv` (unchanged this phase). PRF-PRIM's falsification of
`Γ_graph` conjugate to `exp(-hL)` (FALS-003) is directly relevant prior evidence: DER-ORG-006 must
NOT assume `Fix(Γ)=Fix(e^{-βL})` (matches the corpus's own governance rule C7-001, independently
reinforced by PRF-PRIM's computation).

**EXPECTED OUTPUTS:** A DER-ORG-006 workbook and report characterizing the relationship between
Fix(Γ) (organizational fixed points), Fix(R) (spectral persistence fixed points, R=exp(-βL)), least
fixed points, and organizational closure — either an explicit morphism φ with stated hypotheses, or
a documented obstruction/counterexample, per PRF-PRIM's own template
(`results/workbooks/TOEV_DERIVATION_TEMPLATE.xlsx`).

**FALSIFICATION CRITERIA:** An explicit counterexample where Fix(Γ) and Fix(R) disagree under the
realization tested; a proof obligation that fails under stated hypotheses; or a dependency
contradiction with PRF-PRIM's established results (e.g. if a claimed Fix(Γ)=Fix(R) identity turns
out to require the same Liouville-violating `τ=exp(-tL)` identification PRF-PRIM already falsified).

**This DER is a recommendation only. It has not been executed in this phase.**
