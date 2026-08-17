"""
PRF-PRIM Phase 3/8 -- Operationalize kappa (constraint = idempotent projector) and Pi
(persistence = kernel of an invariant operator surviving repeated tau under kappa) as concrete
graph-spectral objects, and cross-check against the corpus's OWN already-calculated COSMO-DYN
results (registries/MASTER_COSMO_DYN_RESULTS.csv, entries COSMO-BRIDGE-003/004/005) for K4 and
K3,3 specifically, before extending the same computation to the full benchmark family built in
01_graph_families.py.

Candidate mapping under test (CANDIDATE, not yet certified):
    kappa  ~  P_ker(L)   (the spectral projector onto ker(L); idempotent by the spectral theorem)
    Pi     ~  ker(L)     (the persistence subspace itself; DER-SPC-005 already names R=exp(-beta L)
                           the "Persistence operator" in the source corpus, and USR-027 names
                           Omega = "Master attractor... Fixed point of R^n" -- so the corpus's own
                           naming already anticipates this correspondence; this script is the first
                           point where it is actually tested rather than assumed)

For every graph in the family this script computes, exactly (numpy eigh, float64) or symbolically
(sympy, exact rational/integer arithmetic) where the graph is small enough:
    - L = D - A
    - Spec(L), multiplicities
    - ker(L) (eigenspace at eigenvalue 0), dim ker(L)
    - rank(L)
    - P_ker(L) via spectral projector: sum of outer products of an orthonormal basis of ker(L)
    - idempotency check: || P_ker(L)^2 - P_ker(L) || (must be ~0 to machine precision)
    - lim_{t->inf} exp(-tL) via direct computation at large t, compared against P_ker(L)
    - cross-check: rank(L) == N - (#connected components)

Run: python3 02_laplacian_spectrum_and_persistence.py
Output: calculations/C0/PRF-PRIM/output/laplacian_results.json  (numeric, all families)
        calculations/C0/PRF-PRIM/output/K4_K33_exact_symbolic.txt (exact sympy cross-check vs corpus)
"""
import json, os
import numpy as np
import networkx as nx
import sympy as sp

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, 'output')
os.makedirs(OUT, exist_ok=True)
GRAPH_IN = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'graphs', 'C0', 'PRF-PRIM', 'graph_families.json'))

with open(GRAPH_IN) as f:
    FAMILIES = json.load(f)

def laplacian_from_adjacency(A):
    A = np.array(A, dtype=float)
    D = np.diag(A.sum(axis=1))
    return D - A

def spectral_projector_kernel(L, tol=1e-8):
    """P_ker(L) via eigendecomposition of symmetric L; returns (P, ker_dim, eigvals)."""
    eigvals, eigvecs = np.linalg.eigh(L)
    ker_mask = np.abs(eigvals) < tol
    ker_dim = int(ker_mask.sum())
    V0 = eigvecs[:, ker_mask]
    P = V0 @ V0.T
    return P, ker_dim, eigvals

def main():
    results = {}
    for name, fam in FAMILIES.items():
        A = fam['adjacency']
        n = fam['n_nodes']
        L = laplacian_from_adjacency(A)
        P_ker, ker_dim, eigvals = spectral_projector_kernel(L)
        rank_L = n - ker_dim
        n_components = fam['n_connected_components']

        # idempotency test: P^2 = P
        idempotency_error = float(np.max(np.abs(P_ker @ P_ker - P_ker)))
        # symmetry test (P should be symmetric since L symmetric)
        symmetry_error = float(np.max(np.abs(P_ker - P_ker.T)))

        # lim_{t->inf} exp(-tL) via scipy-free matrix exponential (eigendecomposition based, exact for symmetric L)
        eigvals_full, eigvecs_full = np.linalg.eigh(L)
        t_large = 500.0
        exp_tL = eigvecs_full @ np.diag(np.exp(-t_large * eigvals_full)) @ eigvecs_full.T
        limit_error = float(np.max(np.abs(exp_tL - P_ker)))

        # cross-check rank(L) = N - components
        rank_matches_components = (rank_L == n - n_components)

        # kappa-tau commutation prerequisite check deferred to script 04 (automorphisms)

        results[name] = {
            "n_nodes": n,
            "eigenvalues_sorted": sorted([round(float(x), 8) for x in eigvals]),
            "ker_dim": ker_dim,
            "rank_L": rank_L,
            "n_connected_components": n_components,
            "rank_L_equals_N_minus_components": rank_matches_components,
            "P_ker_idempotency_error": idempotency_error,
            "P_ker_symmetry_error": symmetry_error,
            "lim_exp(-tL)_minus_P_ker_error_at_t=500": limit_error,
            "degenerate_spectrum": len(set(round(float(x), 6) for x in eigvals)) < len(eigvals),
        }
        print(f"{name}: Spec(L)={results[name]['eigenvalues_sorted']}")
        print(f"   ker_dim={ker_dim}  rank(L)={rank_L}  components={n_components}  "
              f"rank=N-c: {rank_matches_components}  idempotency_err={idempotency_error:.2e}  "
              f"limit_err={limit_error:.2e}")

    with open(os.path.join(OUT, 'laplacian_results.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # ---- Exact symbolic cross-check against corpus's own COSMO-BRIDGE-003/004/005 claims (K4, K3,3) ----
    lines = []
    lines.append("EXACT SYMBOLIC CROSS-CHECK against registries/MASTER_COSMO_DYN_RESULTS.csv\n")

    # K4 -- cast adjacency to exact integers (sympy) before computing, so eigenvalues come out
    # as exact rationals/integers rather than floating-point residues near zero.
    A_K4 = sp.Matrix([[int(round(x)) for x in row] for row in FAMILIES['K4']['adjacency']])
    D_K4 = sp.diag(*[sum(A_K4.row(i)) for i in range(A_K4.rows)])
    L_K4 = D_K4 - A_K4
    ev_K4 = L_K4.eigenvals()  # {eigval: multiplicity}, exact integers
    lines.append(f"K4: L eigenvalues (exact) = {ev_K4}")
    lines.append(f"    Corpus claim (COSMO-BRIDGE-003): Spec={{0,4,4,4}}, rank(L)=3")
    rank_K4 = L_K4.rank()
    lines.append(f"    Computed rank(L) = {rank_K4}  -->  {'MATCHES' if rank_K4 == 3 and ev_K4 == {0: 1, 4: 3} else 'MISMATCH'} corpus claim\n")

    # K3,3
    A_K33 = sp.Matrix([[int(round(x)) for x in row] for row in FAMILIES['K33']['adjacency']])
    D_K33 = sp.diag(*[sum(A_K33.row(i)) for i in range(A_K33.rows)])
    L_K33 = D_K33 - A_K33
    ev_K33 = L_K33.eigenvals()
    rank_K33 = L_K33.rank()
    lines.append(f"K3,3: L eigenvalues (exact) = {ev_K33}")
    lines.append(f"    Corpus claim (COSMO-BRIDGE-004/005): N_bulk = rank(L) = 5, d_spectral = 5")
    lines.append(f"    Computed rank(L) = {rank_K33}  -->  {'MATCHES' if rank_K33 == 5 and ev_K33 == {0: 1, 6: 1, 3: 4} else 'MISMATCH'} corpus claim\n")

    with open(os.path.join(OUT, 'K4_K33_exact_symbolic.txt'), 'w') as f:
        f.write('\n'.join(lines))
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
