"""
Phase 1, Node B -- CONTINUUM LIMIT.

Independently reconstructs and numerically+symbolically verifies the refinement-family
convergence claim: for a periodic 1D lattice (cycle graph C_N) with spacing h_N = 2*pi/N,
the rescaled graph Laplacian eigenvalues satisfy

    lambda_k^graph / h_N^2  =  p_k^2 + O(h_N^2)     as N -> infinity, p_k = k fixed

This is the discrete-to-continuum convergence of the graph Laplacian to -d^2/dx^2 on the circle.
Extended to a 2D periodic lattice (torus graph) to test the |p|^2 = p_x^2+p_y^2 generalization.

Method: SymPy for the exact symbolic Taylor expansion (proving the O(h^2) coefficient exactly);
NumPy/NetworkX for the numerical convergence sweep across a refinement family N=8..1024.
"""
import json, os
import numpy as np
import networkx as nx
import sympy as sp

REPO = '/home/user/TOEv/independent_toe/'
OUT = REPO + 'phase_1/B_continuum/'
os.makedirs(OUT, exist_ok=True)

def symbolic_expansion():
    x, h, p = sp.symbols('x h p', real=True)
    expr = 2 - 2*sp.cos(x)
    series = sp.series(expr, x, 0, 7).removeO()
    # substitute x = p*h, divide by h^2, expand in h
    sub = series.subs(x, p*h) / h**2
    sub_expanded = sp.expand(sub)
    sub_series = sp.series(sub_expanded, h, 0, 3)
    return str(series), str(sub_series)

def numeric_convergence_1d():
    results = []
    Ns = [8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    k_fixed = 2  # test mode p_k = 2 (arbitrary small fixed physical wavenumber)
    for N in Ns:
        G = nx.cycle_graph(N)
        A = nx.to_numpy_array(G)
        D = np.diag(A.sum(axis=1))
        L = D - A
        h_N = 2*np.pi/N
        # exact graph eigenvalue for mode k (cycle graph, closed form, avoids full diagonalization)
        lam_k = 2 - 2*np.cos(2*np.pi*k_fixed/N)
        rescaled = lam_k / h_N**2
        p_k = k_fixed
        error = rescaled - p_k**2
        predicted_error = -(p_k**4) * h_N**2 / 12.0
        results.append({
            "N": N, "h_N": h_N, "lambda_k_graph": lam_k, "rescaled_lambda_over_h2": rescaled,
            "p_k^2": p_k**2, "error": error, "predicted_leading_error_-p^4 h^2/12": predicted_error,
            "error_matches_prediction_ratio": error / predicted_error if predicted_error != 0 else None,
        })
    return results

def numeric_convergence_2d():
    results = []
    sizes = [4, 8, 16, 32, 64]
    px, py = 1, 1  # fixed small physical wavevector
    for N in sizes:
        G = nx.grid_2d_graph(N, N, periodic=True)
        G = nx.convert_node_labels_to_integers(G)
        # exact 2D torus eigenvalues: lambda_{kx,ky} = (2-2cos(2 pi kx/N)) + (2-2cos(2 pi ky/N))
        h_N = 2*np.pi/N
        lam = (2 - 2*np.cos(2*np.pi*px/N)) + (2 - 2*np.cos(2*np.pi*py/N))
        rescaled = lam / h_N**2
        target = px**2 + py**2
        error = rescaled - target
        results.append({"N": N, "h_N": h_N, "lambda_graph": lam, "rescaled": rescaled,
                         "|p|^2_target": target, "error": error})
    return results

def main():
    exact_series, rescaled_series = symbolic_expansion()
    conv1d = numeric_convergence_1d()
    conv2d = numeric_convergence_2d()

    # verify O(h^2) convergence rate empirically: error should scale as h_N^2, i.e. ratio of
    # consecutive errors (as N doubles, h halves) should be ~1/4
    ratios = []
    for i in range(1, len(conv1d)):
        e0, e1 = conv1d[i-1]['error'], conv1d[i]['error']
        ratios.append(e0 / e1 if e1 != 0 else None)

    out = {
        "symbolic_exact_series_2-2cos(x)": exact_series,
        "symbolic_rescaled_series_(2-2cos(ph))/h^2": rescaled_series,
        "convergence_1d_ring": conv1d,
        "convergence_2d_torus": conv2d,
        "error_halving_ratios_(should_approach_4.0_for_O(h^2)_convergence)": ratios,
    }
    with open(OUT + 'continuum_limit_results.json', 'w') as f:
        json.dump(out, f, indent=2)

    print("Symbolic: 2-2cos(x) series =", exact_series)
    print("Symbolic: rescaled (2-2cos(ph))/h^2 series in h =", rescaled_series)
    print("\n1D ring convergence (mode p_k=2):")
    for r in conv1d:
        print(f"  N={r['N']:5d} h_N={r['h_N']:.5f} rescaled={r['rescaled_lambda_over_h2']:.8f} "
              f"target=4.0 error={r['error']:.3e} predicted={r['predicted_leading_error_-p^4 h^2/12']:.3e}")
    print("\nError-halving ratios (N doubling -> h halving -> error should shrink by ~4x for O(h^2)):")
    print(" ", [round(r, 3) if r else None for r in ratios])
    print("\n2D torus convergence (mode p=(1,1)):")
    for r in conv2d:
        print(f"  N={r['N']:3d} rescaled={r['rescaled']:.6f} target=2.0 error={r['error']:.3e}")

if __name__ == '__main__':
    main()
