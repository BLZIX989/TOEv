# C0 — PRF-PRIM: Primitive/Grammar Reconciliation — Execution Report

**DER-ID:** PRF-PRIM &nbsp;|&nbsp; **Closure layer:** C0 &nbsp;|&nbsp; **Date:** 2026-08-17 &nbsp;|&nbsp;
**Session:** session_01UBKp9Jq2qXFgravroyUp32

## Objective

Determine, by explicit calculation (not narrative), whether the primitive/grammar systems
registered in the TOEv corpus are equivalent, hierarchically related, mutually embeddable,
reducible to a common minimal representation, or genuinely inequivalent — without assuming the
DTC/UOC grammar is uniquely canonical, and without forcing an answer either way.

## Source records used

- `registries/MASTER_PRIMITIVE_REGISTRY.csv`, `MASTER_PROOF_REGISTRY.csv` (PRF-PRIM entry)
- `source_records/spreadsheets/UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0/03_RAW_DOC_TABLES.csv`
  and `04_RAW_DOC_PARAGRAPHS.csv` — the embedded raw-text extraction of *UCG Specification v5.docx*
  (Sections 3.1–3.4, 15) and *Combined Compiler Theories Whitepaper* (Part IV §7.2, paragraphs
  460–553), which supplied the exact primitive definitions and the corpus's own narrative
  acknowledgment of the unreconciled disagreement.
- `compiler/dag/master_nodes.csv`, `master_edges.csv` (pre-existing canonical DAG, cross-checked)
- `registries/MASTER_COSMO_DYN_RESULTS.csv` (COSMO-BRIDGE-003/004/005, reproduced exactly)

## Exact definitions recovered (Phase 1)

Four primitive systems were investigated, per the execution directive:

| System | Source ID | Primitives | Source document |
|---|---|---|---|
| A — DTC/Organizational | PRIM-G-001..004 | Δ, τ, κ, Π | UCG Spec §3.1 |
| B — Physical | PRIM-P-001..002 | E, ∇Φ | UCG Spec §3.2 |
| C — Computational | PRIM-C-001 | B=(U,V,E) | UCG Spec §3.3 |
| D — Extended MDCL v2.0 | PRIM-X-001..006 | Δ,τ,κ,Θ,Π,Ω | UCG Spec §3.4 |

**Scope note:** PRF-PRIM's own text names only 3 grammars ({Δ,τ,κ,Π}; {Δ,τ,κ}+gradient;
{Δ,τ,κ,Θ,Π,Ω}) — PRIM-C is a 4th registered set not named inside PRF-PRIM's own obligation text,
investigated here because the execution directive explicitly required it. Both facts are preserved,
not silently merged (see `derivations/C0/PRF-PRIM/01_primitive_systems_recovery.py`).

**Key corpus admission recovered verbatim** (Combined Compiler Theories Whitepaper, para. 549):
*"All three sets agree on Distinction, Transformation, and Constraint as core primitives. They
disagree on whether Persistence is primitive or derived, and v2.0 alone adds Accessibility and
Organizational State. This paper does not adjudicate between the three versions... and records the
disagreement rather than silently standardizing on one."*

## Calculations performed

All scripts are in `derivations/C0/PRF-PRIM/` (symbolic/structural) and `calculations/C0/PRF-PRIM/`
(numerical), fully reproducible (deterministic, no randomization, no observational data). Full
detail in `results/workbooks/C0_PRF_PRIM_Primitive_Reconciliation.xlsx` (21 sheets).

1. **Type-theoretic reconciliation** — every primitive assigned a type (operator, relation,
   scalar, vector, graph object, persistence operator, state transition). First-pass 4×4
   compatibility matrix built (no "equivalent" claims without a tested mapping).
2. **Benchmark family** — 9 graphs: K4, K3,3, C6, P5, K4⊔K3,3 (disconnected), two disjoint
   triangles (degenerate spectrum), 4×4 periodic torus, Petersen graph, star K1,5.
3. **Laplacian/persistence recovery** — Spec(L), ker(L), rank(L), P_ker(L), lim exp(-tL) computed
   for all 9 families. **Exactly reproduced** the corpus's own COSMO-BRIDGE-003 (K4: Spec={0,4,4,4},
   rank=3) and COSMO-BRIDGE-004/005 (K3,3: rank=5) results via independent sympy exact arithmetic.
   `rank(L)=N−c` held on 9/9 families.
4. **Incidence/gradient identity** — proved and verified exactly (sympy) that L=Inc·Inc^T on 9/9
   families, giving an exact structural bridge for grad(Φ) [grammar B] toward Δ's downstream chain.
5. **Liouville/volume-preservation test** — the central falsification of this DER (see below).
6. **Reachability/Θ test** — Θ's reachability-class partition exactly equals the connected-
   component partition on 9/9 families, i.e. equals dim ker(L).
7. **Elimination audit** — tested whether κ, Π are independently necessary in the graph-spectral
   realization.
8. **Composition type-check** — built an actual simplicial complex (K4 tetrahedron) and tested
   Δ's own formula d(dΩ)=0 against its required usage in Ψ_{t+1}=κ(τ(Δ(Ψ_t))).
9. **Grammar-recursion conjugacy test** — tested whether Γ_graph=κ∘τ∘Δ_alt is conjugate to the
   heat semigroup exp(−hL), for 2 candidate readings of Δ, on 9/9 families.
10. **Minimality/Γ_min search** — synthesized all of the above into a minimality table and searched
    for a common minimal grammar across all 4 systems.

## Proofs

Two lemmas proven and saved as standalone proof records in `proofs/C0/PRF-PRIM/`:

- **LEMMA-AUT-PROJ-001**: graph automorphisms commute with every spectral projector of L
  (general proof, 4 steps; verified 9/9 families, max error 3.9×10⁻¹⁶).
- **LEMMA-INC-001** (external, admitted EXT-001): L = Inc·Inc^T (standard algebraic graph theory,
  Godsil & Royle Ch. 13; verified exactly 9/9).

## Falsifications (full records: `falsification/C0/PRF-PRIM/FALSIFICATION_RECORDS.md`)

| ID | Claim tested | Families | Result |
|---|---|---|---|
| FALS-001 | τ = exp(−tL) satisfies the Liouville (volume-preserving) condition that PRIM-G-002 itself requires | 9/9 | **FALSIFIED, all 9.** det(exp(−tL)) = exp(−t·2\|E\|) → 0 as t→∞ for any graph with an edge. |
| FALS-002 | Δ = I−P_ker(L), composed as κ∘τ∘Δ | 9/9 | **FALSIFIED.** Composition is identically the zero map (Δ and κ are exactly complementary commuting projectors). |
| FALS-003 | Γ_graph conjugate (orthogonal Procrustes) to exp(−hL) | 9/9 | **FALSIFIED.** Residuals 0.88–0.97 on every family; no near-conjugacy found. |
| FALS-004 | Δ reconstructible from τ(automorphisms)+κ(spectrum) alone | external, admitted | **FALSIFIED.** Cospectral non-isomorphic graphs are a standard counterexample (EXT-002). |

This directly and independently confirms, by computation rather than assertion, the corpus's own
governance caution (`MASTER_CURRENT_CHAT_CANONICAL_RULES.csv`, C7-001): *"Do not assume
Fix(Γ)=Fix(e^{-βL})."* This DER extends that caution one level further down, to τ itself.

## Surviving correspondences (not falsified, multi-family verified)

- **κ ~ P_ker(L)**: idempotent to machine precision on 9/9 families; commutes exactly (proven) with
  τ realized as a graph automorphism.
- **Π ~ ker(L)**: derivable as im(κ) once κ=P_ker(L); consistent with the corpus's own naming of
  `R=exp(−βL)` as the "Persistence operator" (DER-SPC-005) and `Ω` as "Master attractor... Fixed
  point of R^n" (USR-027) — those names already anticipated this correspondence; this execution is
  the first point where it was actually tested rather than assumed.
- **Θ ~ reachability-classes ~ connected components ~ dim ker(L)**: exact three-way coincidence on
  9/9 families — the strongest cross-grammar (D↔A) correspondence found in this DER.
- **grad(Φ) [B] structurally parallels Δ [A/D]**: via the exact identity L=Inc·Inc^T, though this is
  NOT the same as proving grad(Φ)=Δ — the map Inc^T is neither globally injective nor surjective.

## Unresolved relationships

- Which realization of τ is actually intended (automorphism vs. diffusion vs. neither) — **OPEN**.
- Whether grad(Φ) *is* Δ or merely structurally parallel to it — **OPEN**.
- How PRIM-C-001 (B=(U,V,E)) relates to any of A, B, or D — **zero tested or source-documented
  connection found**. The corpus's own downstream pipeline (DER-SPC-001) is sourced from
  DER-ORG-001, not from PRIM-C-001, suggesting PRIM-C may not actually be used downstream at all
  despite being registered — flagged, not resolved.
- Whether Ω (PRIM-X-006) is the same object as Ψ (grammar A's state variable) — no computation or
  recovered source text distinguishes them; not merged by assumption.
- **Δ's own formal definition is internally type-inconsistent**: PRIM-G-001's literal formula
  (boundary operator, d(dΩ)=0, mapping between *different* graded spaces) was demonstrated (on an
  actual tetrahedron simplicial complex, d1∘d2=0 verified exactly) to be type-incompatible with
  DER-ORG-002's required usage (Δ as an endomorphism of the state space X, needed for
  Ψ_{t+1}=κ(τ(Δ(Ψ_t))) to even be iterable). This is a genuine internal inconsistency in the source
  corpus's own primitive definitions, not an artifact of this DER's modeling choices.

## Dependency impact

No downstream CERTIFIED result in the corpus (COSMO-DYN chain, geometry/gravity recovery, gauge
recovery, quantum recovery) was found to computationally *require* a specific resolution of C0 —
every one of those chains is fully computable from a bare graph G=(V,E) onward, independent of how
Δ/τ/κ/Π are labeled or philosophically justified. This matches, and computationally substantiates,
the corpus's own status-preservation rule (governance rule C2-001: "preserve executed results;
derive persistence functional/threshold" independent of C0 closure).

## Final status

Per the directive's required multi-axis classification (full table:
`results/workbooks/C0_PRF_PRIM_Primitive_Reconciliation.xlsx`, sheet `Status`):

- **A embeds in D** (textual, direct source identification): **ADMITTED**, scoped to 4 shared primitives.
- **κ idempotent, commutes with τ(automorphism)**: **CALCULATED/DERIVED**, universal (proof is general).
- **τ=exp(−tL) satisfies Liouville**: **FALSIFIED**, general (NO-GO).
- **τ=automorphism satisfies Liouville**: **DERIVED**, universal.
- **Π derivable from κ**: **CALCULATED**, conditional on κ=P_ker(L) realization.
- **Θ-classes = ker(L)-dim**: **CALCULATED**, universal for undirected graphs (general fact, not merely observed).
- **L=Inc·Inc^T**: **DERIVED/PROVEN**, universal (external theorem).
- **Δ reconstructible from τ+κ**: **FALSIFIED**, general (NO-GO).
- **Γ_graph conjugate to exp(−hL)**: **FALSIFIED (conditional NO-GO)** — tested only for the specific realizations and criterion used.
- **Common minimal grammar Γ_min across all 4 systems**: **OPEN / NOT ESTABLISHED.**
- **PRF-PRIM overall**: **PARTIALLY ADVANCED — remains OPEN.** C0's status in
  `registries/MASTER_CLOSURE_LAYERS_C0_C10.csv` is unchanged (still OPEN THEOREM); this execution
  adds computed sub-results, 2 new CERTIFIED lemmas, 4 new sub-obligations, and 5 new NO-GO/OPEN
  entries underneath it (`registries/MASTER_OPEN_PROPOSED_NO_GO.csv`).

**Answering the 10 required questions directly:**

- **A.** Mathematically equivalent? **No** — no exact equivalence established between any two of the 4 grammars.
- **B.** Hierarchically related? **Partially** — A embeds injectively in D (by direct textual identification); B and C are not shown hierarchically related to A/D or each other.
- **C.** Embeddable in a common grammar? **Partially** — see B; B structurally parallels A via an exact external identity but is not shown embedded; C is not shown embeddable in anything.
- **D.** Minimal common representation? **Not established across all 4.** Within A/D alone, {Δ,τ,κ,Π} reduces to 3 independently-necessary slots {Δ, τ-slot, κ}, with Π derivable and Θ redundant, *given* the graph-spectral realization tested here.
- **E.** Genuinely irreducible primitive(s)? **Δ** (cannot be reconstructed from τ+κ — external theorem). The **τ-slot** is irreducible; its filler is underdetermined.
- **F.** Merely representational differences? **Π vs. Θ** — shown to coincide under the graph realization; likely representational there.
- **G.** Physically/structurally meaningful differences? **Δ's own dual formulation** (boundary operator vs. endomorphism) — a substantive type inconsistency, not mere notation.
- **H.** Downstream branches depending on the reconciliation? **None found to computationally require it** — COSMO-DYN and all tested downstream chains are self-contained given a bare graph.
- **I.** Does PRF-PRIM close C0? **No.**
- **J.** Exact unresolved dependencies remaining? τ's intended realization; grad(Φ)=Δ or not; PRIM-C's link to everything else (currently zero); Ω vs. Ψ identity; Δ's internal type inconsistency.

## Next executable calculation

Per the newly-calculated dependency graph (`compiler/dag/master_edges.csv`, new edges
EDGE-PRF-PRIM-001..005) and the corpus's own phase-execution plan
(`compiler/dag/supplementary_DAG_27_PHASE_EXECUTION_PLAN.csv`, P2: "Fixed points / attractors /
compiler closure"), the highest-leverage next step is:

> **DER-ORG-006 — Fixed-point equivalence theorem (C1).** This DER found that Γ's operational
> content depends on resolving exactly what this next obligation is about: the relationship between
> Fix(Γ) (the organizational fixed-point set) and spectral fixed points (P_ker(L)-type objects).
> This execution already falsified the naive route (Γ_graph conjugate to exp(−hL)) and showed κ/Π's
> spectral realizations behave well in isolation — DER-ORG-006 is the natural next target because it
> asks the DAG-adjacent question this DER could not fully answer: whether *any* realization of Γ has
> a fixed-point set related to Fix(exp(−βL))=ker(L), not merely the two specific realizations tested
> here. A secondary candidate, equally well-motivated by this execution's PRF-PRIM-DELTA-TYPE finding,
> is resolving Δ's type inconsistency directly (construct an explicit reconciled definition of Δ that
> satisfies both PRIM-G-001's boundary-operator formula and DER-ORG-002's endomorphism requirement,
> or formally prove no such reconciliation exists).
