# Node N — Thermodynamics / Statistical Mechanics

## Independent reconstruction

Canonical-ensemble partition function Z(β)=Tr(exp(−βH)) built from the SAME toy H:=L (graph
Laplacian spectrum, Node M) for all 9 benchmark graphs. Verified, by direct calculation (not
assumption), that standard thermodynamic identities hold exactly:

- U(β)=−∂(lnZ)/∂β, computed **two independent ways** (central finite difference, and the direct
  Boltzmann-weighted average U=Σλ_ne^{−βλn}/Z) — agree to 10⁻¹⁰–10⁻¹¹ on all 9 graphs (the tiny
  residual is finite-difference truncation error, not a real discrepancy).
- F(β)=−(1/β)lnZ, S=(U−F)β (k_B=1) — computed for all 9 graphs.
- **Entropy non-negativity** (S≥0) verified on all 9 graphs (range 0.26–1.51).

This independently reconstructs the *formalism* of statistical mechanics using the corpus's own
spectral data as input — it does **not** claim the graph Laplacian eigenvalues are physical
energies (see Node M's explicit non-identification).

Output: `../N_thermodynamics/thermodynamics_results.json`. Script: `N_thermodynamics.py`.

## Status separation

| Field | Value |
|---|---|
| SOURCE_STATUS | ADMITTED (DER-TRC-001..005, "CERTIFIED" for first law, entropy, entropy flux, Clausius-Duhem, Fourier flux — standard thermodynamics, mechanism connecting to L not shown) |
| INDEPENDENT_DERIVATION_STATUS | CALCULATED (partition-function machinery, 9/9 families, U/F/S all internally consistent) |
| CLOSURE_STATUS | CALCULATED-UNIVERSAL for the U=−∂lnZ/∂β identity (a general calculus fact, not family-limited) |
| VERIFICATION_STATUS | VERIFIED (two independent computation methods agree to ~10⁻¹⁰) |
| PROVENANCE | phase_1/N_thermodynamics/thermodynamics_results.json |

## Comparison classification
**A. Notation only** — standard statistical mechanics, independently reconstructed exactly as
expected; no discrepancy with the source (which cites the same standard formulas without deriving
them from the spectral substrate specifically).
