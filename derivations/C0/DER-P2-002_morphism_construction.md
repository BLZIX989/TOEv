# DER-P2-002 — Candidate translations F_AB, F_BA, F_AC, F_CA, F_BC, F_CB and morphism-condition tests

**DER-ID:** DER-P2-002 | **Closure layer:** C0 | **Parent:** PRF-PRIM, DER-P2-001 | **Phase:** II

## Objective
Construct all six candidate translations between the three registered grammars G_A, G_B, G_C, each
with an explicit domain, codomain, action on primitive objects, and preservation condition (per the
Phase-II directive: "A mapping must have a mathematically defined domain, codomain, action on
primitive objects, and preservation conditions — not merely for symmetry"), then test composition,
identity, fixed points, kernels, rank, spectrum, multiplicity, heat semigroup, and canonical-basis
reconstruction for each.

Scripts: `calculations/C0_phase2/morphism_tests.py` (TESTS 1-4, prior), `morphism_tests_2.py`
(TESTS 5-10, this record). Raw data: `morphism_test_results.json`, `morphism_test_results_2.json`.

Test family: PRF-PRIM's original 9 graphs + K3 (10 graphs) + the tetrahedron 2-complex's
face→edge boundary map d2 (a non-1-skeleton structure) + NX001's finite relational system
X={0,1}^{3×3} (a non-graph structure).

---

## F_AB : G_A → G_B  (Δ ↦ ∇)

- **Domain:** the space of realizations of Δ (chain-complex boundary maps Inc: R^m → R^n).
- **Codomain:** the space of realizations of ∇ (discrete gradients Inc^T: R^n → R^m).
- **Action:** literal matrix transpose, F_AB(Inc) = Inc^T.
- **Preservation condition tested — RANK:** rank(Inc) = rank(Inc^T) always (elementary fact,
  verified on all 10 families). **PASS, unconditionally.**
- **Preservation condition tested — KERNEL DIMENSION:** dim ker(Inc) ≠ dim ker(Inc^T) in general;
  equal only when n=m. **FAILS in general** (7/10 families), confirming DER-P2-001's Γ_B typing
  result from the transport side.
- **Preservation condition tested — FULL NONZERO SPECTRUM (new, TEST 5):** the nonzero eigenvalues
  of L_vertex=Inc·Inc^T and L_edge=Inc^T·Inc coincide exactly, with multiplicity, on **10/10**
  graph families AND on the tetrahedron's face/edge (d2) level (TEST 5b) — a structurally different
  combinatorial type. Zero-eigenvalue multiplicity differs by exactly m−n in every case (10/10,
  TEST 5). **This is a genuine, unconditional PASS for the nonzero-spectral block**, sharpening the
  bare "kernels differ" statement of DER-P2-001 into a precise transport law: *F_AB preserves the
  entire nonzero spectrum exactly; it transports the zero-eigenspace only when n=m.*
- **Preservation condition tested — HEAT SEMIGROUP (TEST 6):** exp(−tL_vertex) and exp(−tL_edge),
  restricted to their nonzero-eigenvalue blocks, have identical eigenvalue sets at t=0.37 for both
  a mismatched family (K4, n=4≠m=6) and a matched one (K3, n=m=3). **PASS** (immediate corollary of
  the spectral result, verified directly rather than merely inferred).
- **Verdict:** F_AB is a **well-defined, unconditionally rank- and nonzero-spectrum-preserving**
  map; it is **conditionally** (n=m) a full endomorphism-space isomorphism.

## F_BA : G_B → G_A  (∇ ↦ Δ)

- **Domain:** realizations of ∇ (Inc^T: R^n → R^m). **Codomain:** realizations of Δ (Inc: R^m → R^n).
- **Action:** literal matrix transpose, F_BA(M) = M^T.
- **Preservation condition tested — INVOLUTION / IDENTITY LAW (TEST 8):** F_BA∘F_AB = id, i.e.
  (Inc^T)^T = Inc exactly, on **10/10** families. **PASS, unconditionally** — but this is a
  **trivial** linear-algebra fact (transpose is an involution), reported as such and not inflated
  into evidence of a nontrivial categorical equivalence. It does establish that {F_AB, F_BA} form a
  genuine matched identity-preserving pair at the *operator* level, independent of whether Γ_B
  itself type-checks.
- **Verdict:** well-defined, trivially identity-preserving, unconditionally.

## F_AC : G_A → G_C  (Δ, Π ↦ Θ)

- **Domain:** ker(L) (Π's realization, a linear subspace of R^n). **Codomain:** the partition of
  vertices into reachability classes (Θ's realization).
- **Action:** F_AC(ker L) = the partition induced by connected components of the underlying graph.
- **Preservation condition tested — CARDINALITY (TEST 3, prior):** |Θ classes| = dim ker(L) on
  **10/10** families (extends PRF-PRIM's original 9-family result by one). **PASS.**
- **Verdict:** well-defined and cardinality-preserving, unconditionally, on every family tested.

## F_CA : G_C → G_A  (Θ ↦ Π)  — new construction, this DER

- **Domain:** the Θ-partition (reachability classes / connected components). **Codomain:** ker(L)
  (a linear subspace, not merely a number — a strengthening of F_AC's cardinality-only statement).
- **Action:** F_CA(partition) = span{1_{C_1}, …, 1_{C_k}}, the indicator vectors of each class —
  the *canonical* basis of ker(L) for a graph Laplacian (classical fact, not assumed: verified
  directly per family, not merely cited).
- **Preservation condition tested — MEMBERSHIP + EXACT RECONSTRUCTION (TEST 7):** every indicator
  vector is confirmed to lie in ker(L) (L·1_{C_i}=0 exactly), the indicator basis size equals the
  numerically computed dim ker(L), and the partition **recovered** by reading off each indicator
  vector's support equals the **original** Θ-partition exactly — on **10/10** families. **PASS,
  unconditionally, and exact (not merely cardinality-equal).**
- **Verdict:** F_CA is well-defined and gives a genuine, canonical, exact section of F_AC (F_AC∘F_CA
  reconstructs the original object, not just its dimension) — the strongest positive morphism
  result of this DER.

## F_BC : G_B → G_C  (∇, edge-space objects ↦ Θ)

- **Domain:** ∇'s realization (Inc^T). **Codomain:** the Θ-partition.
- **Action:** no direct construction exists; the only well-defined route is the **composite**
  F_BC := F_AC ∘ F_BA (apply F_BA to recover Δ=Inc, then F_AC to reach Θ).
- **Preservation condition tested — NONTRIVIALITY (TEST 9):** does the composite genuinely use any
  information specific to ∇'s own entries (beyond what F_BA already discards back to Δ)? **NO** —
  by construction, F_AC's inputs (adjacency / ker(L)) never reference Inc^T's values again once
  F_BA has mapped back to Inc. **FAILS the nontriviality condition** on all 10 families: F_BC exists
  only as an A-mediated composite, not as an independent morphism carrying ∇-specific content.
- **Verdict: SCOPE-DEPENDENT / representationally trivial.** Classified as such rather than reported
  as a positive result — the directive explicitly requires morphisms to be tested "not merely for
  symmetry," and F_BC fails that bar as an independent construction.

## F_CB : G_C → G_B  (Θ, Ω ↦ ∇, edge-space objects)

- Symmetric situation to F_BC: only constructible as F_AB ∘ F_CA (recover ker(L)'s canonical basis
  via F_CA, then transpose via F_AB to land in the edge space). Carries no Θ/Ω-specific content
  beyond what F_CA already reduces to Δ/Π. **Same verdict: SCOPE-DEPENDENT / representationally
  trivial**, for the same reason as F_BC.

## Fixed-point preservation (Γ_A vs Γ_B, TEST 10)

Restricted to the **3/10** families where Γ_B type-checks (n=m: C6, two disjoint triangles, K3):
dim Fix(Γ_A) [=dim ker(L_vertex)] equals dim Fix(Γ_B) [=dim ker(L_edge)] on **3/3** — expected,
since TEST 5 already showed the nonzero spectrum (hence, when n=m, the full spectrum including
multiplicities) transports exactly. Not tested outside this 3-family scope, since Γ_B is not
well-typed there (DER-P2-001).

## Non-graph structure (NX001 relational system, TEST 4, prior)

∇/F_AB/F_BA are **not meaningfully instantiable** on X={0,1}^{3×3} (no incidence structure); Θ/F_AC
**is** instantiable (basin-of-attraction reachability); Ω is type-indistinguishable from Ψ, as
found independently in PRF-PRIM. Consistent with, and unweakened by, this DER's graph-side results.

## Summary table

| Translation | Domain→Codomain | Well-defined? | Preservation verdict |
|---|---|---|---|
| F_AB | Δ→∇ (transpose) | YES, unconditional | Rank + nonzero spectrum: **PASS unconditional** (10/10 + tetrahedron). Kernel/zero-block: **conditional on n=m** (3/10). |
| F_BA | ∇→Δ (transpose) | YES, unconditional | Involution/identity: **PASS, trivial** (10/10). |
| F_AC | Δ,Π→Θ | YES, unconditional | Cardinality: **PASS** (10/10). |
| F_CA | Θ→Π (canonical basis) | YES, unconditional | Exact reconstruction: **PASS, strongest result** (10/10). |
| F_BC | ∇→Θ (composite only) | Only as composite | **FAILS nontriviality** — SCOPE-DEPENDENT. |
| F_CB | Θ,Ω→∇ (composite only) | Only as composite | **FAILS nontriviality** — SCOPE-DEPENDENT. |

**DERIVATION_STATUS:** CALCULATED (all six translations constructed and tested; F_AB/F_BA/F_AC/F_CA
proofs are direct, exact, reproducible computations; F_BC/F_CB's triviality is likewise a direct,
verified finding, not an assumption).

**CLOSURE_STATUS:** four of six translations (A↔B one direction, A↔C both directions) are
well-defined with precisely stated (and in three of four cases unconditional) preservation
properties; the B↔C pair is CLOSED as *negative* results (provably only indirect/trivial), not
open questions. No translation among the six achieves an *unconditional, exact, bidirectional*
isomorphism of the full grammar (all primitives, not a subset) — the residual gap driving the
overall C0 classification is documented in `results/PHASE_2_C0_REPORT.md`.
