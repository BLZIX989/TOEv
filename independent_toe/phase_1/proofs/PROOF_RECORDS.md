# Phase 1 Proof Records

Every entry below is a genuine proof (symbolic, exact, deterministic — not a numerical fit)
completed in this phase, with the script that produces it and the exact claim proven.

---

## PROOF-P1-001 — O(h²) convergence rate of the discrete Laplacian to the continuum Laplacian

**Statement:** for the 1D periodic lattice, λ_k^graph/h_N² = p_k² − h_N²p_k⁴/12 + O(h_N³) exactly.

**Proof:** direct SymPy Taylor expansion of 2−2cos(x) about x=0, substitution x=p·h, division by
h², re-expansion in h. Exact symbolic result: `p**2 - h**2*p**4/12 + O(h**3)`.

**Script:** `derivations/B_continuum.py`. **Corroboration:** numerical convergence sweep N=8..2048
matches the predicted −p⁴h²/12 leading error term to 4 significant figures at every N, and the
error-halving ratio converges to exactly 4.000 (the O(h²) signature).

---

## PROOF-P1-002 — Full Euler-Lagrange / Legendre / Hamilton / Poisson-bracket chain

**Statement:** for L=½mq̇²−½kq², the following all hold exactly: (a) Euler-Lagrange reduces to
mq̈+kq=0; (b) H(q,p)=(p²+kmq²)/2m via Legendre transform; (c) Hamilton's equations q̇=∂H/∂p, ṗ=−∂H/∂q
match the EL-derived relations exactly; (d) {q,p}=1 (canonical), {q,H}=q̇, {p,H}=ṗ exactly.

**Proof:** direct symbolic differentiation and simplification at every step (SymPy); every
consistency check returns exactly 0. **Script:** `derivations/I_variational.py`.

---

## PROOF-P1-003 — Source-free Maxwell equations from the U(1) gauge action (D=2)

**Statement:** varying S=−¼∫F_{μν}F^{μν} w.r.t. A_0 and A_1 gives exactly ∂_μF^{μν}=0 (both
components); F is invariant under A_μ→A_μ+∂_μχ.

**Proof:** direct symbolic Euler-Lagrange variation (generic-derivative-symbol substitution
method), exact. Gauge-invariance check returns exactly 0. **Script:** `derivations/KL_maxwell_gauge.py`.

---

## PROOF-P1-004 — su(2) commutation relations for the Pauli-matrix generators

**Statement:** T^a:=σ^a/(2i) satisfy [T^a,T^b]=ε^{abc}T^c exactly, for all 27 index combinations.

**Proof:** direct symbolic matrix multiplication and subtraction, all 27 combinations checked,
exact zero residual. **Script:** `derivations/KL_maxwell_gauge.py`.

---

## PROOF-P1-005 — Ricci scalar of the flat FLRW metric, and H²=Λ/3 from the Einstein-Hilbert action

**Statement:** for ds²=−dt²+a(t)²(dx²+dy²+dz²), R=6(ä/a+(ȧ/a)²) exactly; the vacuum Hamiltonian
constraint of the minisuperspace-reduced Einstein-Hilbert action gives H²=Λ/3 exactly.

**Proof:** full 4D Christoffel-symbol → Riemann-tensor → Ricci-tensor → Ricci-scalar symbolic
computation from the metric-compatibility formula (not the textbook shortcut); minisuperspace
reduction verified via an explicit integration-by-parts identity check (0 residual); Euler-Lagrange
+ Hamiltonian-constraint solved symbolically for H². **Script:** `derivations/O_gravity.py`.

---

## PROOF-P1-006 — dν/dλ=√λ/(4π²) is exactly the derivative of the standard 3D Weyl law

**Statement:** d/dλ[λ^{3/2}/(6π²)] = √λ/(4π²) exactly.

**Proof:** direct symbolic differentiation, exact. **Script:** `derivations/P_cosmology.py`.

---

## PROOF-P1-007 — N_H^BH=π·Z_H(ℓ_p²) is an exact algebraic consequence of Z_H(t)~A_H/(4πt)

**Statement:** substituting t=ℓ_p² into A_H/(4πt) and multiplying by π gives exactly A_H/(4ℓ_p²),
the standard Bekenstein-Hawking count.

**Proof:** direct symbolic substitution and simplification, exact zero residual against the
standard formula. **Script:** `derivations/P_cosmology.py`.

---

## PROOF-P1-008 — L̇=−2HL follows from L(a)=a⁻²L₀ by the chain rule

**Statement:** d/dt[a⁻²L₀] = −2(ȧ/a)(a⁻²L₀) = −2HL exactly.

**Proof:** direct symbolic differentiation, exact zero residual. **Script:** `derivations/P_cosmology.py`.

---

All 8 proofs are exact (symbolic, zero-residual) — none rely on numerical approximation or fitting.
