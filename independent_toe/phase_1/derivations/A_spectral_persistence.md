# Node A — Spectral / Persistence

**Object:** G → L → Spec(L) → e^{−tL} → P_ker(L)

## Definitions, inputs, equations
Graph G=(V,E) → Laplacian L=D−A=Inc·Inc^T → spectral decomposition L=Σλ_n E_n → heat semigroup
K_t=exp(−tL) → orthogonal projector P_ker(L)=lim_{t→∞} K_t.

## Independent reconstruction
This chain was already independently computed and verified in `derivations/C0/PRF-PRIM/` (prior
session, this branch's own repository) across 9 benchmark graph families (K4, K3,3, C6, P5,
K4⊔K3,3, two disjoint triangles, 4×4 torus, Petersen, star): exact eigenvalue reproduction for K4
(Spec={0,4,4,4}) and K3,3 (Spec={0,3,3,3,3,6}), idempotency of P_ker(L) to machine precision (max
error 5.6×10⁻¹⁷), convergence lim K_t → P_ker(L) verified to ~10⁻¹⁴, and the exact identity
L=Inc·Inc^T proven and verified on all 9 families. Carried forward into Phase 1 as the established
kernel, not re-executed.

## Status separation

| Field | Value |
|---|---|
| SOURCE_STATUS | CALCULATED (registries/MASTER_COSMO_DYN_RESULTS.csv, COSMO-BRIDGE-003/004/005) |
| INDEPENDENT_DERIVATION_STATUS | CALCULATED (derivations/C0/PRF-PRIM/, this repository, 9/9 families, exact/machine-precision) |
| CLOSURE_STATUS | CALCULATED-UNIVERSAL for the linear-algebra core (spectral theorem guarantees idempotency/convergence for ANY finite graph, not just the 9 tested) |
| VERIFICATION_STATUS | VERIFIED (reproducible scripts, deterministic) |
| PROVENANCE | derivations/C0/PRF-PRIM/02_type_signatures_and_compatibility.py, 04_tau_liouville_and_kappa_commutation.py; calculations/C0/PRF-PRIM/02_laplacian_spectrum_and_persistence.py |

## Comparison classification
**A. Notation only** — this node's independent reconstruction and the canonical source use
identical mathematics; only the label ("persistence operator R" vs. "spectral projector P_ker(L)")
differs, and PRF-PRIM already established the equivalence explicitly.
