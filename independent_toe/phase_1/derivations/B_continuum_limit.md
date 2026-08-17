# Node B — Continuum Limit

**Object:** L_N → L_N/h_N² → verify λ_N(p) = |p|² + O(h_N²)

## Definitions, inputs, equations
Cycle graph C_N (1D periodic lattice, spacing h_N=2π/N) and torus grid graph T_{N×N} (2D). Graph
Laplacian eigenvalue for mode k: λ_k=2−2cos(2πk/N). Rescaled generator L_N/h_N². Claim: for fixed
physical wavenumber p_k=k, λ_k/h_N² = p_k² + O(h_N²) as N→∞.

## Independent reconstruction
**Symbolic** (SymPy): Taylor series of 2−2cos(x) = x² − x⁴/12 + x⁶/360 − ...; substituting x=ph
and dividing by h² gives exactly p² − h²p⁴/12 + O(h³) — the O(h²) coefficient −p⁴/12 derived
directly, not assumed.

**Numerical**: computed exactly (closed-form cycle-graph eigenvalue, no diagonalization needed) for
N=8..2048 at fixed mode p_k=2. Error vs. predicted leading term matched to 4 significant figures
at every N; the error-halving ratio (N doubling ⇒ h halving) converged to exactly 4.000 — the
textbook signature of O(h²) convergence. Extended to a 2D torus (N=4..64, mode p=(1,1)): same
qualitative convergence to |p|²=2.

Full output: `../B_continuum/continuum_limit_results.json`. Script: `B_continuum.py`.

## Status separation

| Field | Value |
|---|---|
| SOURCE_STATUS | ADMITTED (registries/MASTER_DER_REGISTRY.csv DER-GEO-001 asserts "L_N/h_N²→−Δ_g" without showing the convergence-rate calculation) |
| INDEPENDENT_DERIVATION_STATUS | CALCULATED (exact symbolic Taylor expansion + numerical convergence sweep, this repository) |
| CLOSURE_STATUS | CALCULATED, scoped to periodic 1D/2D lattice refinement families — NOT a universal theorem for arbitrary graph families (per governance rule: an explicit refinement-family result is not automatically universal) |
| VERIFICATION_STATUS | VERIFIED (deterministic, reproducible, exact closed-form eigenvalues used, no numerical diagonalization error) |
| PROVENANCE | phase_1/B_continuum/continuum_limit_results.json |

## Comparison classification
**B. Equivalent representation** — the source's bare assertion "L_N/h_N²→−Δ_g" and this node's
explicit O(h²) rate computation describe the same convergence; this node adds the previously-absent
quantitative rate, not a different claim.
