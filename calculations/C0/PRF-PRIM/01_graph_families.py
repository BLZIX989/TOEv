"""
PRF-PRIM Phase 9 (benchmark family) / Phase 3 substrate -- construct the graph family used for
every subsequent computational test in this DER.

Includes the corpus's own existing benchmark graphs (K4, K3,3 -- see registries/
MASTER_COSMO_DYN_RESULTS.csv, COSMO-BRIDGE-003/004/005) plus additional families required by
directive Phase 9 (falsification): a cycle, a tree/path (no cycles), a disconnected union
(to stress-test rank(L)=N-c), a graph with a provably degenerate (repeated) nonzero eigenvalue,
and a periodic lattice/torus family.

Run: python3 01_graph_families.py
Output: graphs/C0/PRF-PRIM/graph_families.json  (adjacency + basic invariants per graph)
"""
import json, os
import numpy as np
import networkx as nx

HERE = os.path.dirname(__file__)
GRAPH_OUT = os.path.join(HERE, '..', '..', '..', 'graphs', 'C0', 'PRF-PRIM')
GRAPH_OUT = os.path.normpath(GRAPH_OUT)
os.makedirs(GRAPH_OUT, exist_ok=True)

def build_families():
    fams = {}
    fams['K4'] = nx.complete_graph(4)
    fams['K33'] = nx.complete_bipartite_graph(3, 3)
    fams['C6'] = nx.cycle_graph(6)
    fams['P5'] = nx.path_graph(5)                      # tree, zero cycles
    fams['disjoint_K4_K33'] = nx.disjoint_union(nx.complete_graph(4), nx.complete_bipartite_graph(3, 3))
    fams['two_triangles_disjoint'] = nx.disjoint_union(nx.complete_graph(3), nx.complete_graph(3))  # degenerate spectrum by construction (two copies -> repeated eigenvalues)
    fams['torus_4x4'] = nx.grid_2d_graph(4, 4, periodic=True)
    fams['petersen'] = nx.petersen_graph()              # strongly regular -> highly degenerate spectrum
    fams['star_K1_5'] = nx.star_graph(5)                # extreme non-regular tree
    return fams

def main():
    fams = build_families()
    out = {}
    for name, G in fams.items():
        G = nx.convert_node_labels_to_integers(G)
        A = nx.to_numpy_array(G, dtype=float)
        n = G.number_of_nodes()
        m = G.number_of_edges()
        comps = nx.number_connected_components(G)
        out[name] = {
            "n_nodes": n,
            "n_edges": m,
            "n_connected_components": comps,
            "adjacency": A.tolist(),
            "edge_list": [list(e) for e in G.edges()],
            "is_regular": bool(len(set(dict(G.degree()).values())) == 1),
            "degree_sequence": [d for _, d in sorted(G.degree())],
        }
        print(f"{name}: n={n}, m={m}, components={comps}, regular={out[name]['is_regular']}")
    with open(os.path.join(GRAPH_OUT, 'graph_families.json'), 'w') as f:
        json.dump(out, f, indent=2)
    print("Wrote", os.path.join(GRAPH_OUT, 'graph_families.json'))

if __name__ == '__main__':
    main()
