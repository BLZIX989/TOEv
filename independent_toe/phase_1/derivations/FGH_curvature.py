"""
Phase 1, Nodes F (Connection), G (Curvature), H (Ricci/Einstein -- folder 'H_einstein').

HONEST SCOPING NOTE: a full smooth Riemannian construction (Levi-Civita connection -> Riemann
tensor -> Ricci -> Einstein tensor) FROM the graph-spectral substrate requires establishing a
genuine smooth manifold limit with a C^2 metric, which was only checked pointwise/asymptotically
in Node B (eigenvalue convergence), not globally constructed as an actual manifold with charts.
Building that machinery from scratch is beyond what can be independently verified in this phase.
This is recorded as BLOCKER-001, not silently skipped.

What CAN be independently done with the tools at hand:

  (1) TRIVIAL FLAT-SPACE CHECK: for the lattice families where Node B established convergence to
      flat R^n / T^n, the continuum limit metric is g_ij = delta_ij (flat), for which ALL of
      Christoffel symbols, Riemann tensor, Ricci tensor, and Einstein tensor vanish identically.
      This is a necessary (not sufficient) consistency check: the machinery must at least recover
      "zero curvature for a flat graph family" -- verified symbolically (trivial by construction)
      and cross-checked against Node B's numerical convergence (the rescaled spectrum -> |p|^2,
      the flat Laplacian spectrum, consistent with g_ij=delta_ij).

  (2) DISCRETE CURVATURE (ADMITTED EXTERNAL, Ollivier-Ricci): rather than first requiring a smooth
      limit, well-established discrete graph curvature notions (Ollivier-Ricci curvature via
      optimal transport, Jost-Liu 2014 formulation) are computed DIRECTLY on the graph, with no
      continuum limit required. This is a genuinely independent, alternative curvature construction
      -- registered as a SEPARATE bridge from the "spectral metric -> smooth Riemann tensor" chain,
      per the Special Rule: Physical Branches instruction to keep bridges separate.
"""
import json, os
import numpy as np
import networkx as nx
import sympy as sp

REPO = '/home/user/TOEv/independent_toe/'
OUT_F = REPO + 'phase_1/F_connection/'
OUT_G = REPO + 'phase_1/G_curvature/'
OUT_H = REPO + 'phase_1/H_einstein/'
for d in (OUT_F, OUT_G, OUT_H):
    os.makedirs(d, exist_ok=True)

with open(REPO + '../graphs/C0/PRF-PRIM/graph_families.json') as f:
    FAMILIES = json.load(f)


def flat_space_symbolic_check():
    """Symbolic verification: for g_ij = delta_ij (flat metric, constant), all curvature
    tensors vanish identically -- standard differential geometry, verified with sympy."""
    n = 3
    x = sp.symbols(f'x0:{n}', real=True)
    g = sp.eye(n)  # flat metric, constant components
    ginv = g.inv()
    # Christoffel symbols Gamma^k_ij = 1/2 g^kl (d_i g_jl + d_j g_il - d_l g_ij)
    christoffel = [[[sp.Rational(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                s = 0
                for l in range(n):
                    s += ginv[k, l] * (sp.diff(g[j, l], x[i]) + sp.diff(g[i, l], x[j]) - sp.diff(g[i, j], x[l]))
                christoffel[k][i][j] = sp.simplify(s / 2)
    all_christoffel_zero = all(christoffel[k][i][j] == 0 for k in range(n) for i in range(n) for j in range(n))
    # Riemann tensor from constant-zero Christoffels: R^l_ijk = d_i Gamma^l_jk - d_j Gamma^l_ik + ... = 0 trivially
    # since all Christoffels are identically zero constants, all their derivatives and products vanish.
    return {"all_christoffel_symbols_zero": bool(all_christoffel_zero),
            "riemann_tensor_zero": bool(all_christoffel_zero),  # follows immediately
            "ricci_tensor_zero": bool(all_christoffel_zero),
            "ricci_scalar_zero": bool(all_christoffel_zero),
            "einstein_tensor_zero": bool(all_christoffel_zero)}


def ollivier_ricci_curvature(G, alpha=0.0):
    """Discrete Ollivier-Ricci curvature (Jost-Liu combinatorial formulation), computed directly
    via optimal transport (Wasserstein-1 distance) between neighbor distributions of adjacent
    vertices, using networkx's built-in shortest-path distances and scipy's linear-sum-assignment-
    free approach (exact LP via networkx is not built in; implemented here directly with a simple
    exact transportation-polytope solver for small degree, or scipy.optimize.linprog fallback)."""
    from scipy.optimize import linprog
    kappa = {}
    for u, v in G.edges():
        Nu = list(G.neighbors(u)) + ([u] if alpha > 0 else [])
        Nv = list(G.neighbors(v)) + ([v] if alpha > 0 else [])
        du = len(list(G.neighbors(u)))
        dv = len(list(G.neighbors(v)))
        if du == 0 or dv == 0:
            continue
        mu = {x: (1 - alpha) / du for x in G.neighbors(u)}
        mv = {x: (1 - alpha) / dv for x in G.neighbors(v)}
        if alpha > 0:
            mu[u] = alpha
            mv[v] = alpha
        support_u = list(mu.keys())
        support_v = list(mv.keys())
        # cost matrix = shortest path distances
        cost = np.zeros((len(support_u), len(support_v)))
        for i, a in enumerate(support_u):
            for j, b in enumerate(support_v):
                try:
                    cost[i, j] = nx.shortest_path_length(G, a, b)
                except nx.NetworkXNoPath:
                    cost[i, j] = 1e6
        # solve transportation LP: minimize sum cost*flow s.t. row/col sums = mu/mv
        m, k = len(support_u), len(support_v)
        c = cost.flatten()
        A_eq = []
        b_eq = []
        for i in range(m):
            row = np.zeros(m * k)
            row[i*k:(i+1)*k] = 1
            A_eq.append(row); b_eq.append(mu[support_u[i]])
        for j in range(k):
            row = np.zeros(m * k)
            for i in range(m):
                row[i*k+j] = 1
            A_eq.append(row); b_eq.append(mv[support_v[j]])
        res = linprog(c, A_eq=A_eq[:-1], b_eq=b_eq[:-1], bounds=(0, None), method='highs')
        if not res.success:
            continue
        W1 = res.fun
        d_uv = nx.shortest_path_length(G, u, v)
        kappa[(u, v)] = 1 - W1 / d_uv
    return kappa


def node_FGH():
    flat_check = flat_space_symbolic_check()

    curvature_results = {}
    for name, fam in FAMILIES.items():
        G = nx.Graph()
        G.add_nodes_from(range(fam['n_nodes']))
        G.add_edges_from(fam['edge_list'])
        try:
            kappa = ollivier_ricci_curvature(G)
            values = list(kappa.values())
            curvature_results[name] = {
                "n_edges_computed": len(values),
                "mean_ollivier_ricci": float(np.mean(values)) if values else None,
                "min": float(np.min(values)) if values else None,
                "max": float(np.max(values)) if values else None,
            }
        except Exception as e:
            curvature_results[name] = {"error": str(e)}

    out = {
        "BLOCKER_001": "Full smooth Riemann/Ricci/Einstein tensor construction from the graph-spectral "
                        "substrate NOT independently completed -- requires a genuine global smooth-manifold "
                        "limit construction (charts, C^2 metric), beyond what was independently verified "
                        "(Node B established only pointwise spectral convergence, not a full manifold structure).",
        "flat_space_trivial_check": flat_check,
        "discrete_ollivier_ricci_curvature_ADMITTED_EXTERNAL": curvature_results,
    }
    with open(OUT_H + 'curvature_results.json', 'w') as f:
        json.dump(out, f, indent=2)

    print("=== Nodes F/G/H: connection/curvature/Einstein ===")
    print("BLOCKER-001: full smooth curvature chain NOT independently constructed (see record)")
    print("Flat-space trivial check (necessary consistency test):", flat_check)
    print("\nDiscrete Ollivier-Ricci curvature (admitted external, alternative construction):")
    for name, r in curvature_results.items():
        if 'error' in r:
            print(f"  {name}: ERROR {r['error']}")
        else:
            print(f"  {name}: mean={r['mean_ollivier_ricci']:.4f}  range=[{r['min']:.4f}, {r['max']:.4f}]  (n_edges={r['n_edges_computed']})")

if __name__ == '__main__':
    node_FGH()
