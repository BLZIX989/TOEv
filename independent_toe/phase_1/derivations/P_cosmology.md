# Node P — Cosmology

**Governance compliance:** no observed H, Λ, Ξ, horizon area, or information count was used as an
input anywhere in this node — every symbol is free/symbolic; only internal algebraic/dimensional
self-consistency of the corpus's own given formulas was tested (per the Special Rule: Cosmology).

## 1. Weyl-law recognition (dν/dλ=√λ/(4π²))

Independently differentiated the **standard external** 3D Weyl eigenvalue-counting law
ν(λ)~λ^{3/2}/(6π²) (unit volume) — the result is **exactly** √λ/(4π²), matching the corpus's claim
with zero symbolic discrepancy. This recognizes the corpus's formula as a correct citation of
well-known spectral geometry (Weyl, 1911), not a UOC-original derivation.

## 2. Dimensional/scaling consistency

ρ_vac=(ħc)/(16π²)Λ*⁴, Λ_cosm=(ℓ_p²)/(2π)Λ*⁴, Ξ=Λ*ℓ_p checked for dimensional consistency given
[ℓ_p]=length, [Λ*]=1/length: ρ_vac ~ energy/length³ ✓ (correct for energy density), Λ_cosm ~
1/length² ✓ (correct for a cosmological constant), Ξ ~ dimensionless ✓ (matches the corpus's own
numeric claim Ξ≈6.5×10⁻³¹ being a pure number). The scaling law L(a)=a⁻²L₀ ⇒ L̇=−2HL was verified
**by direct differentiation** (chain rule, H:=ȧ/a) — exact match, 0 discrepancy.

## 3. Horizon heat-trace normalization — reproduces the corpus's "discrepancy" finding

Using **Node C's independently-verified** short-time asymptotic Z_H(t)~A_H/(4πt) (this repository,
2D torus, ratios 1.004–1.049), substituted t=ℓ_p² and multiplied by π: **π·Z_H(ℓ_p²) =
A_H/(4ℓ_p²) exactly** — algebraically identical to the standard external Bekenstein-Hawking count
N_H^BH=A_H/(4ℓ_p²). **This is a genuine positive finding**: the corpus's own claimed relation
N_H^BH=π·Z_H(ℓ_p²) is not an independent postulate — it is an **exact algebraic consequence** of
the (independently verified) heat-trace asymptotic evaluated at the Planck scale. This confirms
internal consistency; it does **not** establish that A_H or a genuine "horizon selector P_H" are
themselves derivable from Γ (that remains OPEN — see below).

## 4. Unresolved upstream generators (explicitly preserved as OPEN)

Γ→ℓ*, Γ→P_H, Γ→N_H^UOC all remain **OPEN** — no independent construction was found or attempted;
the source's own governance rules mark these OPEN (SEL-008: "Unique horizon selector... OPEN";
C4-002: absolute scale anchor OPEN). The physical (not merely formal) justification for *why* L
should rescale as a⁻² under cosmic expansion was not independently established — flagged OPEN.

Output: `../P_cosmology/cosmology_consistency_results.json`. Script: `P_cosmology.py`.

## Status separation

| Sub-result | SOURCE_STATUS | INDEPENDENT_STATUS | CLOSURE_STATUS | VERIFICATION_STATUS |
|---|---|---|---|---|
| Weyl-law formula | ADMITTED (stated without derivation) | CALCULATED (exact symbolic match to external Weyl law) | CALCULATED-UNIVERSAL (standard math) | VERIFIED |
| Dimensional consistency of ρ_vac/Λ_cosm/Ξ | ADMITTED | CALCULATED (dimensional analysis) | CALCULATED | VERIFIED |
| L̇=−2HL scaling | ADMITTED | CALCULATED (exact derivative match) | CALCULATED | VERIFIED |
| N_H^BH=π·Z_H(ℓ_p²) normalization | CALCULATED (source states this as a "normalization discrepancy" to resolve) | **CALCULATED** (confirmed to be an exact algebraic consequence of Node C's result — this is a genuine, positive, independently-derived confirmation, not a resolution of the underlying physical question) | OPEN (the underlying question — whether N_H^BH IS the physically correct information count, or the corpus's alternative normalization is — remains unresolved) | VERIFIED (algebra) |
| Γ→ℓ*, Γ→P_H, Γ→N_H^UOC | OPEN (source's own governance rules) | **OPEN** — not touched, not silently closed | OPEN | NOT VERIFIED |

## Comparison classification
**A. Notation only** for items 1–3 (independent confirmation, no discrepancy). **G. Unresolved**
for item 4 (both source and this branch leave these open — not a contradiction, a shared gap).
