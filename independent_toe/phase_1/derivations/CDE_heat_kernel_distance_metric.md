# Nodes C/D/E — Heat Kernel, Spectral Distance, Metric Recovery

## Node C — Heat Kernel trace asymptotics

**Claim tested:** Tr(K_t) ~ Len/√(4πt) (1D) and Tr(K_t) ~ Area/(4πt) (2D) as t→0 — the standard
external Minakshisundaram–Pleijel short-time heat-trace expansion.

**Independent reconstruction:** computed numerically on a 4096-vertex ring (circumference 2π) and a
48×48 torus (physical area (2π)²), **using the rescaled generator L/h_N²** established in Node B
(a genuine methodological finding recorded here: the *bare* graph Laplacian gives ratios 70×–300×
off from the continuum prediction; only the h²-rescaled generator matches — the same lesson
PRF-PRIM found for τ vs. exp(−tL), now shown to apply to the heat-trace normalization too).
With rescaling: 1D ratios 1.0000–1.0001 across 5 t-values; 2D ratios 1.004–1.049, converging to 1
as t→0. **Directly verifies the functional form used in the Special Rule for the cosmological
horizon (Z_H(t)~A_H/(4πt))** — see Node P.

Output: `../C_heat_kernel/heat_trace_results.json`.

## Node D — Spectral/diffusion distance

**Construction:** d(i,j)² = K_t(i,i)+K_t(j,j)−2K_t(i,j) (standard diffusion-map distance, t=1.0).

**Independent reconstruction:** computed on all 9 PRF-PRIM benchmark graphs; verified symmetry
(error <10⁻¹⁵), non-negativity, and the triangle inequality on **every** triple of vertices in
**every** graph — 0 violations found on all 9 families. This is a genuine metric, not merely
asserted.

Output: `../D_distance/spectral_distance_metric_check.json`.

## Node E — Metric recovery (qualitative)

**Test:** on a 64-vertex ring, is diffusion distance from vertex 0 monotonic in graph-geodesic
distance up to half the circumference (the weakest non-trivial Euclidean-recovery check)?

**Result:** YES, monotonic (verified numerically, 0 violations).

Output: `../E_metric/metric_recovery_ring_check.json`.

## Status separation

| Node | SOURCE_STATUS | INDEPENDENT_STATUS | CLOSURE_STATUS | VERIFICATION_STATUS |
|---|---|---|---|---|
| C | ADMITTED (source never states the rescaling requirement explicitly) | CALCULATED (this repo, both 1D/2D, rescaled generator) | CALCULATED, scoped (2 lattice families) | VERIFIED |
| D | ADMITTED (d(i,j) named "diffusion distance" in DER-GEO-001, formula not spelled out) | CALCULATED (this repo, 9/9 families, exact metric-axiom check) | CALCULATED-UNIVERSAL for the metric-axiom part (spectral-theorem guarantee); scoped for the specific numeric values | VERIFIED |
| E | ADMITTED | CALCULATED (qualitative monotonicity, 1 family) | CONDITIONAL (lattice-only, not tested on general graphs) | VERIFIED |

## Comparison classification
**B. Equivalent representation** for C and D (source's bare claims made explicit and quantitative,
not contradicted). **G (unresolved)** is NOT triggered — no contradiction found in any of C/D/E.
