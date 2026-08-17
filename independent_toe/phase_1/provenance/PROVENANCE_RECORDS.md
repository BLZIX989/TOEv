# Phase 1 Provenance Records

## Session / reproducibility

- Session: `session_01UBKp9Jq2qXFgravroyUp32`. Date: 2026-08-17.
- Software: Python 3, SymPy 1.14.0, NumPy 2.4.6, NetworkX 3.6.1, SciPy (Ollivier-Ricci LP solver).
- Determinism: all results are either exact symbolic computations (deterministic by construction)
  or numerical computations on fixed inputs with fixed random seeds where randomness appears
  (`rng = np.random.default_rng(0)` in Node M). No result depends on network access, external
  APIs, or observational data.
- Every script is self-contained and re-runnable: `phase_1/derivations/*.py`,
  `phase_1/calculations/*.py` — each writes its own JSON output to its node subfolder.

## Inputs used (all internal to this repository, per governance)

- 9-graph benchmark family: `graphs/C0/PRF-PRIM/graph_families.json` (built in the C0/PRF-PRIM
  execution, reused here unmodified).
- Corpus registries read (never modified): `registries/MASTER_DER_REGISTRY.csv`,
  `registries/MASTER_COSMO_DYN_RESULTS.csv`, `registries/MASTER_CURRENT_CHAT_CANONICAL_RULES.csv`,
  `registries/MASTER_PROOF_REGISTRY.csv`.
- Phase 0 object registry: `independent_toe/source_extract/ontology_neutral_objects.csv`.

## External (ADMITTED) mathematics used, registered per governance rule 7 ("every new result must
have provenance")

| EXT-ID | Fact used | Where |
|---|---|---|
| EXT-005 (new) | Minakshisundaram-Pleijel short-time heat-trace expansion (1D: Len/√(4πt); 2D: Area/(4πt)) | Node C |
| EXT-006 (new) | Weyl's law (1911), 3D eigenvalue counting function ~λ^{3/2}/(6π²) | Node P |
| EXT-007 (new) | Ollivier-Ricci discrete graph curvature (Jost-Liu 2014 combinatorial formulation) | Node F/G/H |
| EXT-008 (new) | Standard calculus of variations (Euler-Lagrange, Legendre transform) | Node I |
| EXT-009 (new) | Standard classical field theory (Maxwell action, Yang-Mills, su(2) Lie algebra) | Node K/L |
| EXT-010 (new) | Standard GR (Christoffel/Riemann/Ricci construction, ADM minisuperspace, ADM Hamiltonian constraint) | Node O |
| EXT-011 (new) | Bekenstein-Hawking horizon entropy/information count (external, standard) | Node P |
| EXT-001..004 | Carried forward from PRF-PRIM (`registries/source_registry_vNEXT.csv` / earlier EXT registrations) | Node A |

None of these are UOC-original results; all are well-established external mathematics/physics,
applied here to independently test the corpus's claims — consistent with the governing rule that
external information "must never silently become project fact."

## What was NOT independently verified (explicit, not hidden)

- The smooth manifold construction from the graph-spectral substrate (BLOCKER-001).
- Full non-Abelian gauge-curvature covariance (Node L, admitted rather than re-proven).
- The correspondence between graph-Laplacian eigenvalues and physical energies (Node M, kept CANDIDATE).
- All 4 cosmological "generator" bridges (Γ→ℓ*, Γ→P_H, Γ→N_H^UOC, and the physical justification for
  the a⁻² rescaling rule) — all remain OPEN.
