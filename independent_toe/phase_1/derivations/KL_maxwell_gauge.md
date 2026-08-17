# Node K — Electromagnetism, Node L — Gauge Theory

## Node K: Maxwell's equations from the U(1) gauge action

**Independent reconstruction (SymPy, D=2 spacetime for tractability, mechanism generalizes to D=4
without new ideas — standard, not repeated in full 4D component form to control scope):**

F₀₁:=∂₀A₁−∂₁A₀; Lagrangian ℒ=−½F₀₁F^{01} (metric diag(1,−1)). Euler-Lagrange variation w.r.t. A₀
and A₁ performed by explicit functional differentiation (treating ∂_μA_ν as independent generic
symbols, standard field-theory EL procedure) → both give exactly `∂_μF^{μν}=0` in component form
(verified: EL_A0 = ∂ₓ(∂ₓA₀−∂ₜA₁) = −∂ₓF₀₁; EL_A1 = ∂ₜ(∂ₜA₁−∂ₓA₀) = ∂ₜF₀₁ — the source-free Maxwell
equation). **Gauge invariance** F(A_μ+∂_μχ) = F(A_μ) verified symbolically, exact (error=0).

Output: `../K_maxwell/maxwell_results.json`.

## Node L: Yang-Mills generalization (SU(2))

**Independent reconstruction:** explicit 2×2 generator matrices T^a=σ^a/(2i) (Pauli, antihermitian
convention). The su(2) commutation relations [T^a,T^b]=ε^{abc}T^c — the algebraic structure that
*makes* Yang-Mills curvature transform covariantly (as opposed to Maxwell's abelian F) — were
**verified by explicit matrix multiplication**, exact match for all 27 (a,b,c) index combinations.
Covariant derivative D_tψ=∂_tψ−gA_μψ and the infinitesimal gauge transformation were set up
explicitly. The full component-by-component covariance identity δF_μν=[ε,F_μν] was **not**
re-derived symbolically here (admitted as standard, external, e.g. Peskin & Schroeder Ch. 15) —
the commutation-relation verification is the load-bearing independent check, since it is exactly
the structural fact non-Abelian curvature covariance depends on.

Output: `../L_gauge/yang_mills_results.json`.

## Status separation

| Node | SOURCE_STATUS | INDEPENDENT_STATUS | CLOSURE_STATUS | VERIFICATION_STATUS |
|---|---|---|---|---|
| K (Maxwell) | ADMITTED (DER-GAU-001..004, "CERTIFIED", mechanism not shown) | **DERIVED** (D=2, exact symbolic variation) | CALCULATED-UNIVERSAL for D=2; D=4 generalization ADMITTED (standard, not re-derived) | VERIFIED |
| L (Yang-Mills) | ADMITTED | **CONDITIONAL** (Lie-algebra structure DERIVED/verified exactly; full curvature covariance ADMITTED not re-proven) | CONDITIONAL | PARTIALLY VERIFIED |

## Comparison classification
**A. Notation only** for Maxwell (independently derived form matches standard Maxwell exactly, no
discrepancy with the source's claim, source just never showed the steps). **C. Additional
assumption** for Yang-Mills (this node assumes the standard non-Abelian covariance argument rather
than re-proving it — an explicit, disclosed gap, not a silent one).

## Note on the graph-spectral bridge
Per the Special Rule: Physical Branches, this node explicitly separates (1) mathematical recovery
of Maxwell/Yang-Mills from a gauge action [DONE, above] from (2) the corpus's claim that A_μ is
itself recoverable **from the graph Laplacian L** (DER-GAU-001). (2) was **not** independently
tested in this phase — it remains ADMITTED, a separate, unverified bridge.
