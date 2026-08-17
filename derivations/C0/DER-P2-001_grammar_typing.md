# DER-P2-001 — Formal typing of G_A, G_B, G_C and well-typedness of Γ

**DER-ID:** DER-P2-001 | **Closure layer:** C0 | **Parent:** PRF-PRIM | **Phase:** II

## Objective
Represent each registered grammar as a typed mathematical structure and determine whether
Γ=κ∘τ∘Δ is well-typed in every proposed realization, per the Phase-II directive.

## G_A = {Δ, τ, κ, Π} — DTC/organizational

| Primitive | Type (this repository's realizations, tested) | Domain | Codomain |
|---|---|---|---|
| Δ (literal, PRIM-G-001) | Boundary/chain-complex operator, d with d²=0 | C₁ (edge space, dim m) | C₀ (vertex space, dim n) |
| Δ (NX001 realization) | Elementwise threshold, endomorphism | X={0,1}^{k×k} | X |
| τ (automorphism reading) | Orthogonal group element (permutation matrix) | R^n | R^n |
| τ (semigroup reading) | Contraction semigroup generator's exponential, exp(−tL) | R^n | R^n |
| τ (NX001 realization) | Boolean relational composition + join | X | X |
| κ | Idempotent projector / reflexive-symmetric closure | R^n or X | Same (endomorphism) |
| Π | Kernel/fixed-point subspace (a SET, not an operator) | — | subspace of R^n, or subset of X |

**Γ_A = κ∘τ∘Δ well-typed?**
- **Literal Δ (boundary op) reading: NO** (PRF-PRIM, `derivations/C0/PRF-PRIM/05_composition_type_check.py`
  — Δ:C₁→C₀ cannot compose with κ,τ:R^n→R^n unless n=m, and even then the *chain-complex* semantics
  differ from the *endomorphism* semantics).
- **NX001 finite-relation reading: YES** (Δ,τ,κ:X→X all endomorphisms by explicit construction,
  proven well-typed and composition-closed; `NX001_01_DERIVATION`, step 5). **This does not resolve
  the literal-Δ type mismatch — it sidesteps it by choosing a different Δ definition.** Both facts
  preserved, not merged.

## G_B = {Δ, τ, κ} + gradient (∇)

∇ realized as the discrete gradient Inc^T: R^n (vertex space) → R^m (edge space) — the **exact
transpose/adjoint** of Δ's literal boundary-map realization Inc (PRF-PRIM: L=Inc·Inc^T, proven).

**Γ_B=κ∘τ∘∇ well-typed?** **NO, in general.** τ,κ (as PRF-PRIM realized them) act on the **vertex**
space (dim n); ∇'s codomain is the **edge** space (dim m). Type-checks **only when n=m**.

**Tested on 10 graph families** (PRF-PRIM's original 9 + K3, newly added): only **3/10** satisfy
n=m (C6, two disjoint triangles, K3) — the rest (K4, K3,3, P5, disjoint K4⊔K3,3, torus_4x4,
Petersen, star) **fail this type-check**. This is a *new*, concrete, counterexample-supported type
mismatch, structurally analogous to (but distinct from) PRF-PRIM's Δ mismatch.

Script: `calculations/C0_phase2/morphism_tests.py`, TEST 2.

## G_C = {Δ, τ, κ, Θ, Π, Ω} — Extended MDCL

Δ, τ, κ, Π: **directly identified** with G_A's own (source text: "same as PRIM-G-00X", PRF-PRIM
finding). Θ realized as reachability-closure / basin structure (graph case: connected components;
NX001 non-graph case: basins of attraction under Γ-iteration — both well-typed). Ω realized as an
element of the state space (Ω=Ψ_t)  — **type-indistinguishable from G_A's own Ψ** in every domain
tested (graph and non-graph alike).

**Γ_C well-typed?** **UNDEFINED** — no single composed formula for Γ_C exists anywhere in the
corpus (PRF-PRIM's own finding, unchanged this phase); nothing to type-check.

## Status separation

| Claim | SOURCE_STATUS | INDEPENDENT_DERIVATION_STATUS | CLOSURE_STATUS |
|---|---|---|---|
| Γ_A well-typed (literal Δ) | SOURCE-REGISTERED (BR-001, "CERTIFIED SPINE") | **FALSIFIED** (PRF-PRIM, unchanged) | NO-GO for this reading |
| Γ_A well-typed (NX001 finite-relation Δ) | PROPOSED CALCULATION (NX001) | **CALCULATED / DERIVED** for this realization | CALCULATED, scoped to X={0,1}^{k×k} |
| Γ_B well-typed | Not addressed in source | **CALCULATED — CONDITIONAL** (holds iff n=m, 3/10 tested families) | CONDITIONAL, test-family scoped |
| Γ_C well-typed | Not addressed in source (no formula given) | **OPEN** (nothing to test) | OPEN |

Full data: `calculations/C0_phase2/morphism_test_results.json` (TEST 1, TEST 2).
