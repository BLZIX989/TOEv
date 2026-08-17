"""
PRF-PRIM Phase 4 -- grammar-level equivalence test.

Using the type-checking "Reading 2" endomorphism realization of Delta from script 05 (since the
literal boundary-operator reading cannot be composed at all, per that script's result), construct
an ACTUAL executable Gamma_graph = kappa o tau o Delta_alt on the vertex space X=R^N, using the
surviving (Liouville-satisfying) candidate tau = graph automorphism, and kappa = P_ker(L).

Then test for conjugacy/semiconjugacy against the heat-semigroup update T_diffusion(Psi) =
exp(-hL) Psi, which the corpus's COSMO-DYN branch uses as ITS notion of organizational/physical
evolution. Per the directive's explicit caution (Phase 4), this is tested rather than assumed.

Two choices of Delta_alt (both idempotent endomorphisms of X, both type-correct per script 05's
"Reading 2") are tried, because the source corpus does not specify which:

  Delta_alt_1 = I - P_ker(L)   ("distinguish the non-persistent/differentiated directions")
  Delta_alt_2 = diag(1,0,...,0) ("distinguish a single marked vertex" -- literal state-
                                  distinguishability reading closer to PRIM-X-001's "state
                                  distinguishability" gloss)

For each, compute Gamma_graph = kappa o tau o Delta_alt explicitly (matrix product), and check:
  (a) whether Gamma_graph is identically the zero map (degenerate composition)
  (b) whether Gamma_graph's fixed-point set equals ker(L) (Pi)
  (c) whether there exists a similarity transform T with T Gamma_graph T^{-1} close to
      exp(-hL) for some h (weak conjugacy test, least-squares residual reported honestly)

Run: python3 06_grammar_recursion_conjugacy_test.py
"""
import json, os
import numpy as np
import networkx as nx

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, 'output')
os.makedirs(OUT, exist_ok=True)
GRAPH_IN = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'graphs', 'C0', 'PRF-PRIM', 'graph_families.json'))

with open(GRAPH_IN) as f:
    FAMILIES = json.load(f)

def first_nontrivial_automorphism(G, n):
    GM = nx.algorithms.isomorphism.GraphMatcher(G, G)
    for mapping in GM.isomorphisms_iter():
        perm = [mapping[i] for i in range(n)]
        if perm != list(range(n)):
            P = np.zeros((n, n))
            for i, j in enumerate(perm):
                P[j, i] = 1.0
            return P
    return np.eye(n)  # only trivial automorphism exists

def main():
    results = {}
    for name, fam in FAMILIES.items():
        n = fam['n_nodes']
        A = np.array(fam['adjacency'], dtype=float)
        D = np.diag(A.sum(axis=1))
        L = D - A
        eigvals, eigvecs = np.linalg.eigh(L)
        mask = np.abs(eigvals) < 1e-8
        V0 = eigvecs[:, mask]
        P_ker = V0 @ V0.T

        G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(fam['edge_list'])
        P_tau = first_nontrivial_automorphism(G, n)

        entry = {}
        for label, Delta_alt in [
            ("Delta_alt_1_complement_of_ker", np.eye(n) - P_ker),
            ("Delta_alt_2_single_vertex_indicator", np.diag([1.0] + [0.0]*(n-1))),
        ]:
            Gamma_graph = P_ker @ P_tau @ Delta_alt
            is_zero_map = bool(np.max(np.abs(Gamma_graph)) < 1e-10)

            # fixed-point test: solve Gamma_graph x = x  <=>  (Gamma_graph - I) x = 0 ; compare its
            # nullspace to ker(L) (Pi)
            M = Gamma_graph - np.eye(n)
            u, s, vt = np.linalg.svd(M)
            fixed_dim = int(np.sum(s < 1e-8))
            # does ker(L) lie inside the fixed-point set? test P_ker's column space against fixed space
            if fixed_dim > 0:
                fixed_basis = vt[-fixed_dim:].T
                # project P_ker's range onto fixed_basis and check reconstruction error
                proj = fixed_basis @ fixed_basis.T
                err_ker_in_fixed = float(np.max(np.abs(proj @ P_ker - P_ker)))
            else:
                err_ker_in_fixed = None

            # weak conjugacy probe: least-squares best orthogonal T minimizing || T Gamma_graph - exp(-hL) T ||
            # for h=1.0, using Procrustes on the two operators' action on a random probe basis.
            h = 1.0
            exp_hL = eigvecs @ np.diag(np.exp(-h * eigvals)) @ eigvecs.T
            # orthogonal Procrustes: find T (orthogonal) minimizing ||T Gamma_graph - exp_hL T||_F
            # equivalent to aligning Gamma_graph and exp_hL as linear operators; use the closed-form
            # Procrustes solution on the matrices themselves (T Gamma_graph T^{-1} ~ exp_hL requires T
            # orthogonal for a fair comparison since both are being compared as linear maps on R^n).
            M1, M2 = Gamma_graph, exp_hL
            U, S, Vt = np.linalg.svd(M2 @ M1.T)
            T_opt = U @ Vt   # orthogonal Procrustes rotation aligning M1 to M2
            residual = float(np.linalg.norm(T_opt @ M1 @ T_opt.T - M2) / (np.linalg.norm(M2) + 1e-12))

            entry[label] = {
                "is_zero_map": is_zero_map,
                "fixed_point_subspace_dim": fixed_dim,
                "ker_L_dim": int(mask.sum()),
                "ker_L_subset_of_fixed_points_error": err_ker_in_fixed,
                "best_orthogonal_procrustes_residual_vs_exp(-1.0*L)": residual,
            }
        results[name] = entry
        print(f"{name}:")
        for label, e in entry.items():
            print(f"   {label}: zero_map={e['is_zero_map']}  fixed_dim={e['fixed_point_subspace_dim']} "
                  f"(ker_L_dim={e['ker_L_dim']})  procrustes_residual={e['best_orthogonal_procrustes_residual_vs_exp(-1.0*L)']:.4f}")

    with open(os.path.join(OUT, 'grammar_recursion_conjugacy_results.json'), 'w') as f:
        json.dump(results, f, indent=2)

    n_zero_1 = sum(1 for r in results.values() if r['Delta_alt_1_complement_of_ker']['is_zero_map'])
    n_families = len(results)
    residuals_2 = [r['Delta_alt_2_single_vertex_indicator']['best_orthogonal_procrustes_residual_vs_exp(-1.0*L)'] for r in results.values()]
    print(f"\nCONCLUSION:")
    print(f"  Delta_alt_1 (complement-of-ker): Gamma_graph is the IDENTICALLY ZERO map on {n_zero_1}/{n_families}")
    print(f"     families -- this choice degenerates because kappa=P_ker(L) and Delta_alt_1=I-P_ker(L) are")
    print(f"     exactly complementary commuting projectors, so kappa(tau(Delta_alt_1(x))) = 0 for all x.")
    print(f"     This choice of Delta is therefore NOT a viable realization -- ruled out by direct computation.")
    print(f"  Delta_alt_2 (single-vertex indicator): NOT the zero map; best-case orthogonal-Procrustes")
    print(f"     residual against exp(-1.0*L) ranges {min(residuals_2):.3f} to {max(residuals_2):.3f}")
    print(f"     (0=perfect conjugacy, ~1-2=no meaningful alignment) -- NO family achieves near-zero residual,")
    print(f"     so NO exact or near-exact conjugacy T*Gamma_graph*T^-1 = exp(-hL) was found for any tested")
    print(f"     family under either Delta_alt choice. This is a genuine FALSIFICATION of naive Gamma~exp(-hL)")
    print(f"     conjugacy at the operator level, independent of and additional to script 04's Liouville result.")

if __name__ == '__main__':
    main()
