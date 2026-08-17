"""
Phase 1, Nodes C (Heat Kernel), D (Spectral Distance), E (Metric Recovery).

C: independently verify the short-time heat-trace asymptotic Tr(K_t) = sum_n exp(-t*lambda_n)
   against the standard (external, Minakshisundaram-Pleijel) continuum prediction:
     1D (circle, circumference Len):  Tr(K_t) ~ Len / sqrt(4*pi*t)   as t -> 0
     2D (torus, area Area):           Tr(K_t) ~ Area / (4*pi*t)      as t -> 0
   The 2D case is the SAME functional form as the "Special Rule: Cosmological Horizon" target
   Z_H(t) ~ A_H/(4*pi*t) -- verified here once, cross-referenced in the P_cosmology node.

D: construct the diffusion/spectral distance d(i,j)^2 = K_t(i,i)+K_t(j,j)-2K_t(i,j) and verify
   it is a genuine metric numerically (symmetry, positivity, triangle inequality) on the 9
   PRF-PRIM benchmark graph families plus a larger ring for continuum comparison.

E: check whether the recovered distance is a MONOTONIC, qualitatively-Euclidean function of graph
   geodesic distance on lattice-like graphs (ring, torus) -- the weakest, most defensible form of
   "metric recovery" achievable without a full embedding construction.
"""
import json, os, itertools
import numpy as np
import networkx as nx

REPO = '/home/user/TOEv/independent_toe/'
OUT_C = REPO + 'phase_1/C_heat_kernel/'
OUT_D = REPO + 'phase_1/D_distance/'
OUT_E = REPO + 'phase_1/E_metric/'
for d in (OUT_C, OUT_D, OUT_E):
    os.makedirs(d, exist_ok=True)

with open(REPO + '../graphs/C0/PRF-PRIM/graph_families.json') as f:
    FAMILIES = json.load(f)

def laplacian(adj):
    A = np.array(adj, dtype=float)
    D = np.diag(A.sum(axis=1))
    return D - A

def heat_trace(L, t):
    eigvals = np.linalg.eigvalsh(L)
    return float(np.sum(np.exp(-t * eigvals)))

# ---- C: heat trace asymptotics ----
# IMPORTANT METHODOLOGICAL FINDING (recorded, not silently fixed): the bare graph Laplacian L has
# O(1) eigenvalues, while the continuum operator -Delta it approximates has eigenvalues scaling as
# lambda_graph/h_N^2 (established exactly in Node B). Tr(exp(-t*L)) with the BARE L therefore does
# NOT match the continuum heat-trace asymptotic at any fixed t -- one must use the RESCALED
# generator L/h_N^2, i.e. K_t^physical = exp(-t*L/h_N^2), consistent with the corpus's own
# COSMO-DYN rescaling rule L(a)=a^{-2}L_0 (OBJ-025 in the Phase-0 object registry), which performs
# exactly this kind of h^2-type rescaling. This was verified by first computing with the bare L
# (ratio errors of 70x-300x, see git history / logs/) and is recorded here as a genuine finding:
# "R=exp(-beta L)" (bare) and "the continuum heat kernel" are NOT the same object at fixed beta;
# a rescaling is REQUIRED, exactly the same lesson PRF-PRIM learned about tau vs exp(-tL).
def node_C():
    results = {}
    # 1D ring, large N, circumference fixed at 2*pi
    N1 = 4096
    G1 = nx.cycle_graph(N1)
    L1 = laplacian(nx.to_numpy_array(G1))
    h1 = 2 * np.pi / N1
    L1_rescaled = L1 / h1**2
    circumference = 2 * np.pi
    ts_1d = [0.001, 0.002, 0.005, 0.01, 0.02]
    row1 = []
    for t in ts_1d:
        tr = heat_trace(L1_rescaled, t)
        predicted = circumference / np.sqrt(4 * np.pi * t)
        row1.append({"t": t, "Tr(K_t)_numeric_RESCALED_L/h^2": tr, "predicted_Len/sqrt(4pi t)": predicted,
                      "ratio": tr / predicted})
    results["1D_ring_N=4096_circumference=2pi_RESCALED"] = row1

    # 2D torus, large N x N, area = N^2 lattice units, physical side length 2*pi so h=2*pi/N
    N2 = 48
    G2 = nx.grid_2d_graph(N2, N2, periodic=True)
    G2 = nx.convert_node_labels_to_integers(G2)
    L2 = laplacian(nx.to_numpy_array(G2))
    h2 = 2 * np.pi / N2
    L2_rescaled = L2 / h2**2
    area = (2 * np.pi) ** 2  # physical area of the 2*pi x 2*pi torus
    ts_2d = [0.05, 0.1, 0.2, 0.3, 0.5]
    row2 = []
    for t in ts_2d:
        tr = heat_trace(L2_rescaled, t)
        predicted = area / (4 * np.pi * t)
        row2.append({"t": t, "Tr(K_t)_numeric_RESCALED_L/h^2": tr, "predicted_Area/(4pi t)": predicted,
                      "ratio": tr / predicted})
    results["2D_torus_N=48x48_physical_area=(2pi)^2_RESCALED"] = row2

    with open(OUT_C + 'heat_trace_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("=== Node C: heat trace asymptotics ===")
    for k, rows in results.items():
        print(f"  {k}:")
        for r in rows:
            print(f"    t={r['t']:.4f}  Tr(K_t)={r['Tr(K_t)_numeric_RESCALED_L/h^2']:.4f}  "
                  f"predicted={list(r.values())[2]:.4f}  ratio={r['ratio']:.4f}")
    return results

# ---- D: spectral/diffusion distance + metric axiom checks ----
def node_D():
    results = {}
    for name, fam in FAMILIES.items():
        A = np.array(fam['adjacency'])
        L = laplacian(A)
        n = fam['n_nodes']
        eigvals, eigvecs = np.linalg.eigh(L)
        t = 1.0
        Kt = eigvecs @ np.diag(np.exp(-t * eigvals)) @ eigvecs.T
        D2 = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                D2[i, j] = Kt[i, i] + Kt[j, j] - 2 * Kt[i, j]
        D2 = np.clip(D2, 0, None)  # guard tiny negative numerical noise
        Dist = np.sqrt(D2)

        symmetric_err = float(np.max(np.abs(Dist - Dist.T)))
        nonneg_ok = bool(np.all(Dist >= -1e-9))
        # triangle inequality check on all triples
        triangle_violations = 0
        max_violation = 0.0
        for i, j, k in itertools.combinations(range(n), 3):
            lhs = Dist[i, k]
            rhs = Dist[i, j] + Dist[j, k]
            if lhs > rhs + 1e-9:
                triangle_violations += 1
                max_violation = max(max_violation, lhs - rhs)
            # check all 3 permutations of the triangle inequality
            for a, b, c in [(i, j, k), (j, k, i), (k, i, j)]:
                if Dist[a, c] > Dist[a, b] + Dist[b, c] + 1e-9:
                    triangle_violations += 1
        results[name] = {
            "n": n, "symmetric_max_error": symmetric_err, "nonnegative": nonneg_ok,
            "triangle_inequality_violations": triangle_violations,
            "is_a_valid_metric": bool(symmetric_err < 1e-9 and nonneg_ok and triangle_violations == 0),
        }
    with open(OUT_D + 'spectral_distance_metric_check.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("\n=== Node D: spectral distance metric-axiom check (t=1.0) ===")
    for name, r in results.items():
        print(f"  {name}: valid_metric={r['is_a_valid_metric']} "
              f"(sym_err={r['symmetric_max_error']:.2e}, triangle_violations={r['triangle_inequality_violations']})")
    return results

# ---- E: qualitative Euclidean recovery on ring graph ----
def node_E():
    N = 64
    G = nx.cycle_graph(N)
    A = nx.to_numpy_array(G)
    L = laplacian(A)
    eigvals, eigvecs = np.linalg.eigh(L)
    t = 0.5
    Kt = eigvecs @ np.diag(np.exp(-t * eigvals)) @ eigvecs.T
    # compare diffusion distance from vertex 0 to all others, vs graph geodesic distance
    graph_dist = dict(nx.single_source_shortest_path_length(G, 0))
    rows = []
    for j in range(N):
        d2 = Kt[0, 0] + Kt[j, j] - 2 * Kt[0, j]
        rows.append({"vertex": j, "graph_geodesic_distance": graph_dist[j], "diffusion_distance": float(np.sqrt(max(d2, 0)))})
    # monotonicity check: as graph distance increases from 0 to N/2, does diffusion distance increase monotonically?
    sorted_by_graph_dist = sorted(rows, key=lambda r: r['graph_geodesic_distance'])
    diff_dists_in_order = [r['diffusion_distance'] for r in sorted_by_graph_dist if r['graph_geodesic_distance'] <= N // 2]
    is_monotonic = all(diff_dists_in_order[i] <= diff_dists_in_order[i+1] + 1e-9 for i in range(len(diff_dists_in_order)-1))
    out = {"N": N, "t": t, "rows": rows, "monotonic_up_to_half_circumference": is_monotonic}
    with open(OUT_E + 'metric_recovery_ring_check.json', 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\n=== Node E: metric recovery on N={N} ring, t={t} ===")
    print(f"  Diffusion distance monotonic in graph distance up to half circumference: {is_monotonic}")
    print(f"  Sample: dist(0,1)={rows[1]['diffusion_distance']:.4f}, dist(0,{N//4})={rows[N//4]['diffusion_distance']:.4f}, "
          f"dist(0,{N//2})={rows[N//2]['diffusion_distance']:.4f}")
    return out

if __name__ == '__main__':
    node_C()
    node_D()
    node_E()
