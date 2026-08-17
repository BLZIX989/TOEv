# phase_1/ — folder-to-node mapping

The directive's "OUTPUT REQUIREMENTS" section specifies exactly these 16 domain folders:
`A_spectral, B_continuum, C_heat_kernel, D_distance, E_metric, F_connection, G_curvature,
H_einstein, I_variational, J_classical, K_maxwell, L_gauge, M_quantum, N_thermodynamics,
O_gravity, P_cosmology`. This 16-letter scheme (A–P) does not map one-to-one onto the separately
given 17-item dependency order (A–Q, which lists Ricci/scalar curvature and the Einstein tensor as
distinct H/I items). To avoid inventing an extra folder or silently dropping content, this
execution used the **explicit 16-folder list exactly as given**, with the following content
mapping, stated here for clarity:

- `F_connection`, `G_curvature` — folders created empty; their content (Levi-Civita connection,
  Riemann/Ricci curvature, discrete Ollivier-Ricci) is filed under **`H_einstein`** together with
  the Einstein tensor, since all three are one blocked/partial construction (`BLOCKER-001`) treated
  as a single node in `derivations/FGH_curvature.md` / `FGH_curvature.py`.
- `J_classical` — folder created empty; its content (classical mechanics) is filed under
  **`I_variational`**, since a Lagrangian/Hamiltonian system with canonical Poisson structure *is*
  classical mechanics — see `derivations/I_variational_J_classical.md`.
- `A_spectral` — folder created empty; this node's content was already fully computed in the prior
  `derivations/C0/PRF-PRIM/` execution and is only *referenced*, not recomputed — see
  `derivations/A_spectral_persistence.md`.
- `figures/`, `logs/` — created empty; no plots were generated (all results are exact
  symbolic/numeric values, tabulated rather than plotted) and script stdout is reproducible by
  re-running the scripts in `derivations/` and `calculations/` rather than archived as static logs.

All 16 required folders exist. Nothing was silently dropped — every domain has a derivation record;
see `PHASE_1_REPORT.md` for the consolidated summary.
