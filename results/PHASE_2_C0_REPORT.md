# PHASE II — C0/PRF-PRIM Reconciliation — Execution Report

**Closure layer:** C0 &nbsp;|&nbsp; **Parent DER:** PRF-PRIM &nbsp;|&nbsp; **New DERs:** DER-P2-001, DER-P2-002
**Date:** 2026-08-17

## 1. Objective

Resolve PRF-PRIM as far as mathematically possible for the three registered grammar families
G_A={Δ,τ,κ,Π}, G_B={Δ,τ,κ}+gradient, G_C={Δ,τ,κ,Θ,Π,Ω}, using the five newly-uploaded NX001-family
calculation packages as mandatory prior evidence, without repeating Phase-I domain calculations and
without advancing to C1 until C0 is formally classified. This phase does **not** attempt to prove a
Theory of Everything, and does not force convergence between grammars where the evidence does not
support it.

## 2. Governance / Execution Firewall

- No Phase-I domain calculation (A_spectral…P_cosmology) was repeated; PRF-PRIM's own 9-family
  benchmark, LEMMA-AUT-PROJ-001, LEMMA-INC-001, and all four FALS-00x records are **cited**, not
  rederived.
- Every new claim below is backed by an explicit mapping + composition/preservation test, not
  assertion (directive requirement).
- CALCULATED ≠ UNIVERSALLY DERIVED, and DOWNSTREAM RECOVERY ≠ C0 CLOSURE are maintained throughout
  (see §11 status matrix — no row collapses these distinctions).
- No convergence was forced: two of the six candidate translations (F_BC, F_CB) are reported as
  **failing** their nontriviality test, not quietly omitted or reframed as partial successes.

## 3. Mandatory prior-calculation recovery (NX001 family)

Full crosswalk: `results/reconciliation/C0_PRIOR_CALCULATION_CROSSWALK.csv/.xlsx` (8 rows, schema
per directive). Source lineage verified by SHA-256 (`source_records/spreadsheets/NX001_family/README.md`):
NX001 ⊂ NX001B ⊂ NX001E ⊂ NX001F (additive superset, 0 diffs on shared sheets); NX001G is a separate
standalone document.

| Finding | Classification |
|---|---|
| NX001 core (Δ,τ,κ endomorphisms on X={0,1}^(3×3), Fix(Γ)=5=Bell(3)) | EXTENDED |
| NX001 τ/κ ↔ PRF-PRIM correspondence | CONFIRMED |
| NX001B (Γ_A vs Γ_B one-step 48/512 mismatch, terminal 512/512 agreement) | narrower than registered C0 scope, but extends it |
| NX001C (4×4 extension, 15=Bell(4) fixed points, 0/65536 terminal mismatch) | CONFIRMED |
| NX001E (general closure-operator theorem, Γ_A*=Γ_B*=Eq for all finite V) | CONFIRMED — independently logically re-verified sound this phase |
| NX001F (spectral descent T1-T7, block-Laplacian spectrum formula) | CONFIRMED |
| NX001F's own F7 spectral-invariance conjecture | SUPERSEDED |
| NX001G (falsifies F7: clique-graph vs incidence-graph functors give different spectra) | CONTRADICTED (contradicts NX001F's own conjecture, not this phase's work) |

No new calculation in this phase duplicates any NX001-family result; all are cited as evidence and
attached to the C0 proof graph via the DAG edges in §15.

## 4. Grammar formalization (typed structures)

Full typed tables: `derivations/C0/DER-P2-001_grammar_typing.md`. Summary:

- **G_A**: Δ has two incompatible realizations in the corpus — the literal boundary-operator
  reading (type-mismatched against κ,τ, per PRF-PRIM) and NX001's finite-relation endomorphism
  reading (well-typed, but a *different* Δ definition — this does not resolve the original
  mismatch, both are preserved as distinct facts).
- **G_B**: ∇ realized as Inc^T, the exact adjoint of Δ=Inc. Γ_B=κ∘τ∘∇ well-typed **only when n=m**
  (vertex count = edge count) — a new, counterexample-supported, precisely stated conditional.
- **G_C**: Δ,τ,κ,Π directly identified with G_A's own (source text: "same as PRIM-G-00X"). Θ
  well-typed on both graph and non-graph domains. Ω type-indistinguishable from Ψ everywhere
  tested. Γ_C has **no composed formula anywhere in the corpus** — UNDEFINED, nothing to type-check.

## 5. Candidate translations constructed

Full domain/codomain/action/preservation specification for all six: `derivations/C0/
DER-P2-002_morphism_construction.md`. Summary table:

| Translation | Well-defined? | Preservation verdict |
|---|---|---|
| F_AB (Δ→∇, transpose) | YES, unconditional | Rank + nonzero spectrum: **PASS unconditional** (10/10 + tetrahedron d2). Kernel/zero-block: conditional on n=m. |
| F_BA (∇→Δ, transpose) | YES, unconditional | Involution/identity: **PASS**, trivial (10/10). |
| F_AC (Δ,Π→Θ) | YES, unconditional | Cardinality: **PASS** (10/10). |
| F_CA (Θ→Π, canonical basis) | YES, unconditional | Exact reconstruction: **PASS, strongest result** (10/10). |
| F_BC (composite only) | Only as composite | **FAILS** nontriviality — SCOPE-DEPENDENT. |
| F_CB (composite only) | Only as composite | **FAILS** nontriviality — SCOPE-DEPENDENT. |

## 6. Morphism condition test results

Scripts: `calculations/C0_phase2/morphism_tests.py` (TESTS 1-4), `morphism_tests_2.py` (TESTS 5-10).
Composition, identity, fixed points, kernels, rank, spectrum, multiplicity, heat semigroup, and
canonical-basis reconstruction were all tested (not merely rank/kernel, per directive requirement):

- **Rank** (TEST 1): always equal for Δ/∇ (transpose pair) — trivial, confirmed 10/10.
- **Kernel dimension** (TEST 1, TEST 2): equal only when n=m — 3/10 families.
- **Full nonzero spectrum + multiplicity** (TEST 5, TEST 5b): preserved exactly, **unconditionally**,
  10/10 graphs + tetrahedron d2 level.
- **Heat semigroup** (TEST 6): nonzero-block eigenvalues of exp(−tL) match exactly, verified
  directly on K4 (n≠m) and K3 (n=m).
- **Fixed points** (TEST 10): dim Fix(Γ_A)=dim Fix(Γ_B) on all 3/3 families where Γ_B type-checks.
- **Canonical-basis / exact reconstruction** (TEST 7): F_CA recovers the *original* Θ-partition
  exactly (not just its cardinality) on 10/10 families — the phase's strongest positive result.
- **Composition nontriviality** (TEST 9): F_BC, F_CB tested explicitly for whether they carry any
  information beyond what the A-mediated composite trivially provides — **both fail**, 10/10.
- **Non-graph instantiation** (TEST 4): ∇ not meaningfully instantiable on NX001's relational
  system X={0,1}^(3×3); Θ and Ω are (as basin-reachability and state-identity respectively).

## 7. Counterexample sweep

10 graph families (PRF-PRIM's original 9 + K3), the tetrahedron 2-complex (non-1-skeleton
structure, face↔edge boundary d2), and NX001's finite relational system (non-graph structure) —
full table `results/workbooks/C0_PRF_PRIM_RECONCILIATION_PHASE2.xlsx` sheet `12_COUNTEREXAMPLES`.
Periodic lattice (torus 4×4), complete/complete-bipartite (K4, K3,3), and disconnected graphs are
all represented. Every claim of "unconditional" above was tested against every member of this set,
not a favorable subset.

## 8. Proofs

- **THM-P2-FCA-001**: F_CA exact canonical reconstruction (Theta→Pi) — connected-component
  indicator vectors are a canonical ker(L) basis; recovering the original partition from them is
  exact, not merely cardinality-matching. Verified 10/10.
- **THM-P2-FAB-SPECTRAL-001**: F_AB nonzero-spectrum transport law — classical fact (M·Mᵀ and Mᵀ·M
  share nonzero spectrum with multiplicity), independently re-verified numerically on 10 graphs +
  tetrahedron d2 level, not merely cited.
- NX001E's general closure-operator theorem (cited, independently logically re-verified sound this
  phase — standard extensivity+monotonicity+finite-chain-termination technique).

Full records: `results/workbooks/C0_PRF_PRIM_RECONCILIATION_PHASE2.xlsx` sheet `13_PROOFS`.

## 9. Falsifications

| Claim | Result |
|---|---|
| Γ_B=κ∘τ∘∇ well-typed in general | **FALSIFIED** — 7/10 test families have n≠m |
| F_BC, F_CB are independent (non-composite) morphisms | **FALSIFIED** — no construction found that does not factor through A, 10/10 |
| NX001F's own F7 broader spectral-invariance conjecture (cited) | **FALSIFIED by NX001G**, prior to this phase |
| (Baseline, cited) Γ_A=κ∘τ∘Δ well-typed (literal Δ) | **FALSIFIED** (PRF-PRIM, unchanged) |

## 10. Obstructions (minimal, formal)

1. **Γ_B typing**: kappa,τ act on the vertex space (dim n); ∇'s codomain is the edge space (dim m).
   Composition type-checks **iff n=m**. Formal, precise, counterexample-backed (7/10 fail).
2. **No direct B↔C translation**: every attempted F_BC/F_CB construction factors through A and
   discards all ∇/Θ/Ω-specific content in the process (TEST 9, 10/10).
3. **Γ_C undefined**: no composed formula for any well-typed subset of {Δ,τ,κ,Θ,Π,Ω} appears
   anywhere in the corpus.
4. **Ω vs Ψ type-identity**: unresolved in every domain tested (graph and NX001 relational alike) —
   extends, does not close, PRF-PRIM's original PRF-PRIM-OMEGA-PSI finding.

These are registered as new OPEN rows in `registries/MASTER_OPEN_PROPOSED_NO_GO.csv` (C0 layer),
not left implicit.

## 11. Status matrix (DERIVATION_STATUS × CLOSURE_STATUS)

| Claim | DERIVATION_STATUS | CLOSURE_STATUS |
|---|---|---|
| Γ_A well-typed (literal Δ) | FALSIFIED | NO-GO |
| Γ_A well-typed (NX001 Δ) | CALCULATED/DERIVED | CALCULATED, scoped to X={0,1}^(k×k) |
| Γ_B well-typed | CALCULATED-CONDITIONAL | CONDITIONAL, iff n=m |
| Γ_C well-typed | OPEN | OPEN |
| F_AB (rank, nonzero spectrum) | CALCULATED | CLOSED, unconditional |
| F_AB (kernel/zero-block) | CALCULATED | CONDITIONAL, iff n=m |
| F_BA | CALCULATED | CLOSED, unconditional (trivial) |
| F_AC | CALCULATED | CLOSED, unconditional |
| F_CA | CALCULATED | CLOSED, unconditional (exact, strongest result) |
| F_BC, F_CB | CALCULATED (negative) | OPEN — SCOPE-DEPENDENT / trivial only |
| G_A ↔ G_C (as a pair) | CALCULATED | **HIERARCHICALLY CLOSED** |
| G_A ↔ G_B (as a pair) | CALCULATED-CONDITIONAL | **CONDITIONALLY CLOSED**, iff n=m |
| G_B ↔ G_C (as a pair) | CALCULATED (negative) | **OPEN** |
| Ω vs Ψ | OPEN | OPEN |

## 12. C0 decision logic — final classification

Per the directive's seven-way relationship taxonomy and six-letter (A–F) decision logic, this
phase's evidence does not support a single uniform relationship across all three grammars
simultaneously — and reporting one would misrepresent genuinely heterogeneous results. The honest
classification is a **primary label with two explicit qualifiers**:

> **Overall C0/PRF-PRIM classification: C — HIERARCHICAL**, primary evidence the G_A↔G_C pair:
> G_C's Δ,τ,κ,Π are directly, textually identified with G_A's own ("same as PRIM-G-00X"), and this
> phase newly proved (not merely asserted) that this identification is backed by an **exact,
> unconditional, canonical, bidirectional** correspondence between G_A's Π and G_C's Θ (F_AC/F_CA,
> §5, §8) — the strongest and most unconditional result of the entire phase. G_C is therefore a
> genuine, rigorously verified *extension* of G_A (adding Ω, whose relationship to G_A's Ψ remains
> the one open residual), not merely a nominal relabeling and not an incompatible alternative.
>
> **Qualifier 1 (sub-classification B, CONDITIONALLY EQUIVALENT)**: the G_A↔G_B relationship is
> conditional, not hierarchical — Γ_B is well-typed, and F_AB/F_BA preserve rank, nonzero spectrum,
> and fixed points, **exactly when n=m** (3/10 test families), an explicit, stated, and
> counterexample-verified assumption, not an unstated hedge.
>
> **Qualifier 2 (sub-classification F, OPEN with minimal obstruction identified)**: the G_B↔G_C
> relationship remains open — no direct (non-A-mediated) translation exists (obstruction #2, §10),
> and this is reported as a genuine open question with its minimal obstruction formally identified,
> not as "not yet investigated" (both F_BC and F_CB were explicitly constructed and explicitly
> tested and explicitly failed their nontriviality condition).

This is not a forced convergence: the negative results (F_BC/F_CB, Γ_C undefined, Ω vs Ψ) are
reported as negative, not reframed. It is not a forced divergence either: F_AC/F_CA's exact,
unconditional bidirectionality is a real, positive, well-evidenced result that would be understated
by a blanket "OPEN" or "INCOMPATIBLE" label for all of C0.

## 13. Downstream impact / C1 readiness decision

Per the directive ("do NOT advance to C1 merely because C0 is inconvenient; do NOT begin
DER-ORG-006 or any C1 fixed-point equivalence theorem until the C0 result has been classified"):

C0 is now classified (§12), but **not uniformly closed** — only the G_A↔G_C pair is hierarchically
closed; G_A↔G_B is conditional; G_B↔G_C is open. **Decision: do not open C1 broadly.** If a future
C1 obligation depends *only* on the G_A↔G_C relationship (e.g., an obligation phrased purely in
terms of Δ,τ,κ,Π,Θ,Π-as-Θ-preimage), the G_A↔G_C closure proven here (F_AC/F_CA, exact,
unconditional) may be cited as a satisfied scoped prerequisite. Any C1 obligation that requires the
full three-grammar closure (in particular anything invoking G_B's gradient primitive together with
G_C's Θ/Ω, or anything requiring Γ_C to be well-typed) is **blocked** on the obstructions in §10 and
must not be started this phase. This decision is recorded, not merely implied, in
`results/workbooks/C0_PRF_PRIM_RECONCILIATION_PHASE2.xlsx` sheet `16_DOWNSTREAM_IMPACT`.

## 14. Comparison to Phase-I PRF-PRIM baseline

PRF-PRIM (Phase I) established: Γ_A(literal) FALSIFIED, κ~P_ker(L) idempotent/commuting,
Θ-classes=dim ker(L) (9/9), L=Inc·Inc^T (9/9), τ=exp(−tL) FALSIFIED (Liouville), Γ_graph not
conjugate to exp(−hL) (9/9), Ω vs Ψ unresolved, PRIM-C disconnected from A/B/D. This phase (II)
**preserves every one of those findings unchanged** and adds: the NX001-Δ alternate typed
realization; Γ_B's precise n=m conditionality (new); the full nonzero-spectrum transport law for
F_AB (sharpens the old bare kernel-mismatch statement); the exact F_CA reconstruction theorem (new,
strongest result); the explicit F_BC/F_CB triviality finding (new); confirmation that Ω vs Ψ remains
unresolved in a second, non-graph domain (NX001 relational system). No PRF-PRIM finding was
overwritten, only extended or cited (append-only governance maintained, `diff`-verified after each
registry append).

## 15. Registry / DAG updates

New, append-only (verified via row-count and per-row diff after each write, no existing row
modified):

- `registries/MASTER_THEOREM_REGISTRY.csv` (+2: THM-P2-FCA-001, THM-P2-FAB-SPECTRAL-001)
- `registries/MASTER_PROOF_REGISTRY.csv` (+2: PRF-P2-GAMMA-B-CONDITIONAL, PRF-P2-BC-CB-TRIVIALITY)
- `registries/MASTER_DER_REGISTRY.csv` (+2: DER-P2-001, DER-P2-002)
- `registries/MASTER_OPEN_PROPOSED_NO_GO.csv` (+3, C0 layer)
- `compiler/dag/master_nodes.csv` (+4), `master_edges.csv` (+6) — canonical corpus DAG, extended not modified
- `compiler/dag/MASTER_INDEPENDENT_TOE_DAG_PHASE2.csv` (new file, 12 edges, UPSTREAM/OPERATOR/
  DOWNSTREAM/EVIDENCE/STATUS/SCOPE/PROVENANCE schema; cycle audit
  `MASTER_INDEPENDENT_TOE_DAG_PHASE2_cycle_audit.txt` — 3 benign 2-node cycles detected and
  explicitly documented as intentional forward/reverse morphism pairs, not silently excluded)
- `registries/MASTER_INDEPENDENT_OBJECT_REGISTRY_PHASE2.csv` (new file, 18 typed objects)

## 16. Workbook & artifact index

- `results/workbooks/C0_PRF_PRIM_RECONCILIATION_PHASE2.xlsx` — 18 sheets, `00_README` through
  `17_PROVENANCE`, per directive.
- `results/reconciliation/C0_PRIOR_CALCULATION_CROSSWALK.csv/.xlsx` — mandatory first output.
- `derivations/C0/DER-P2-001_grammar_typing.md`, `DER-P2-002_morphism_construction.md`.
- `calculations/C0_phase2/morphism_tests.py`, `morphism_tests_2.py`, and their `.json` outputs.
- `source_records/spreadsheets/NX001_family/` (source copies + lineage README).
- `registries/scripts/build_phase2_dag_registry.py`, `results/reconciliation/build_phase2_workbook.py`
  (build scripts, reproducible).

## 17. Next executable calculation

The exact next executable calculation, following directly from §10's obstruction #2 (no direct
B↔C translation) and #3 (Γ_C undefined) — the two obstructions blocking full C0 closure:

> **DER-P2-003 — Construct or formally exclude a direct (non-A-mediated) B↔C translation, and
> attempt an explicit construction of Γ_C.** Concretely: (a) search for a translation from ∇'s
> edge-space structure directly to Θ/Ω that does not route through Δ/Π (e.g., testing whether edge-
> space reachability, or an edge-space analogue of basins-of-attraction, carries independent content
> not recoverable from the vertex-space F_AC/F_CA pair) — if none exists, attempt a formal
> impossibility proof rather than leaving obstruction #2 as a bare negative result; (b) attempt to
> construct an explicit composed formula for Γ_C using Θ and Ω in place of, or alongside, Δ (e.g.
> Γ_C = κ∘τ∘Θ, testing well-typedness the same way DER-P2-001 tested Γ_A/Γ_B), since no such
> construction has yet been attempted in either PRF-PRIM or this phase — only its *absence* from the
> corpus has been confirmed. This is **not** executed in this phase, per the Execution Firewall
> and the explicit directive not to advance to C1 before this residual is addressed.
