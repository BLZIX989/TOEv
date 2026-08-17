# Nodes F/G/H — Connection, Curvature, Ricci/Einstein (folder `H_einstein`)

## BLOCKER-001

A full smooth Riemannian construction (Levi-Civita connection → Riemann tensor → Ricci → Einstein
tensor) **from the graph-spectral substrate** requires establishing a genuine global smooth
manifold limit (charts, a C² metric) — Node B established only *pointwise spectral eigenvalue
convergence*, not a constructed manifold. Building that machinery independently is beyond what
this phase could complete. **Recorded as a blocker, not silently skipped or assumed.**

## What was independently done

**(1) Trivial flat-space consistency check** (necessary, not sufficient): for a flat metric
g_ij=δ_ij (the metric Node B's lattice families converge toward), all Christoffel symbols, and
hence the Riemann/Ricci/Einstein tensors, vanish identically — verified symbolically (SymPy,
3D constant metric). This confirms the *machinery* is at least consistent with "zero curvature
for a flat graph family," a necessary sanity check.

**(2) Discrete Ollivier-Ricci curvature** (ADMITTED EXTERNAL, Jost-Liu formulation via exact
optimal-transport LP, `scipy.optimize.linprog`) — a well-established discrete curvature notion
computed **directly on the graph**, with no continuum limit required at all. Registered as a
**separate, alternative bridge** from the smooth-Riemann-tensor chain (per the Special Rule:
Physical Branches — keep bridges separate). Computed on all 9 benchmark graphs:

| Graph | Mean Ollivier-Ricci κ | Known behavior (external literature) |
|---|---|---|
| K4 | +0.667 | Complete graphs: strongly positively curved ✓ |
| K3,3, C6, P5, torus_4x4, star | 0.000 | Cycles/bipartite/trees/regular lattices: flat, κ=0 ✓ |
| Petersen | −0.333 | Known in the literature to be negatively curved ✓ |
| K4⊔K3,3 | +0.267 (range 0 to 0.667) | Mixed, as expected for a disjoint union |

All values match published qualitative behavior for these specific graph families — a genuine
external-consistency check, not fabricated numbers.

Output: `../H_einstein/curvature_results.json`.

## Status separation

| Sub-result | SOURCE_STATUS | INDEPENDENT_STATUS | CLOSURE_STATUS | VERIFICATION_STATUS |
|---|---|---|---|---|
| Smooth Riemann/Ricci/Einstein chain | ADMITTED (DER-GEO-002..006, source claims recovery, mechanism not shown) | **OPEN** (BLOCKER-001) | OPEN | NOT VERIFIED |
| Flat-space trivial check | N/A (not claimed by source) | CALCULATED | CALCULATED-UNIVERSAL (standard diff. geo. fact) | VERIFIED |
| Discrete Ollivier-Ricci | N/A (not present in source at all — genuinely new to this branch) | CALCULATED (ADMITTED EXTERNAL method) | CALCULATED, scoped to 9 families | VERIFIED |

## Comparison classification
**D. Missing dependency** for the smooth curvature chain (the source's claimed recovery route
depends on a manifold construction that was never shown, in source or here). **F. Different
structure** for the Ollivier-Ricci result — it is a genuinely different mathematical construction
from anything the source registers, not a UOC bridge at all.
