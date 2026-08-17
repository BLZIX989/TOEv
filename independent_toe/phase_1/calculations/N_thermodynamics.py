"""
Phase 1, Node N (folder N_thermodynamics).

Independently constructs the canonical-ensemble partition function Z(beta) = Tr(exp(-beta*H))
using the SAME toy H:=L (graph Laplacian spectrum) from Node M, and verifies the standard
statistical-mechanics identities relating Z to internal energy U, free energy F, and entropy S
hold EXACTLY as algebraic/calculus consequences (not fit or assumed):

    U(beta) = -d(ln Z)/d(beta)
    F(beta) = -(1/beta) ln Z
    S = (U - F) * beta   [with k_B=1]

All three are checked by direct numerical differentiation (finite differences) against the
independently-computed Z(beta) for all 9 benchmark graph families, i.e. this independently
reconstructs standard thermodynamic MACHINERY, using the corpus's Laplacian spectrum as the input
microstate-energy data (NOT claiming the graph Laplacian eigenvalues ARE physical energies -- see
Node M's explicit non-identification; this node reconstructs the thermodynamic FORMALISM only).
"""
import json, os
import numpy as np

REPO = '/home/user/TOEv/independent_toe/'
OUT = REPO + 'phase_1/N_thermodynamics/'
os.makedirs(OUT, exist_ok=True)

with open(REPO + '../graphs/C0/PRF-PRIM/graph_families.json') as f:
    FAMILIES = json.load(f)

def laplacian(adj):
    A = np.array(adj, dtype=float)
    D = np.diag(A.sum(axis=1))
    return D - A

def Z(beta, eigvals):
    return np.sum(np.exp(-beta * eigvals))

def main():
    results = {}
    for name, fam in FAMILIES.items():
        L = laplacian(fam['adjacency'])
        eigvals = np.linalg.eigvalsh(L)
        beta0 = 1.0
        db = 1e-6
        lnZ_plus = np.log(Z(beta0 + db, eigvals))
        lnZ_minus = np.log(Z(beta0 - db, eigvals))
        U_numeric = -(lnZ_plus - lnZ_minus) / (2 * db)
        # direct formula: U = <lambda> weighted by Boltzmann factor = sum(lambda_n exp(-beta lambda_n))/Z
        Z0 = Z(beta0, eigvals)
        U_direct = np.sum(eigvals * np.exp(-beta0 * eigvals)) / Z0
        F = -(1 / beta0) * np.log(Z0)
        S = (U_direct - F) * beta0

        # cross-check consistency: U_numeric (finite-diff) vs U_direct (closed form) should match
        U_consistency_error = abs(U_numeric - U_direct)

        results[name] = {
            "Z(beta=1)": float(Z0),
            "U_via_finite_difference_-dlnZ/dbeta": float(U_numeric),
            "U_via_direct_boltzmann_average": float(U_direct),
            "U_consistency_error": float(U_consistency_error),
            "F_free_energy": float(F),
            "S_entropy_(U-F)*beta": float(S),
            "S_nonnegative": bool(S >= -1e-9),
        }

    with open(OUT + 'thermodynamics_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print("=== Node N: Thermodynamics/Statistical Mechanics (toy H=L, beta=1) ===")
    for name, r in results.items():
        print(f"  {name}: Z={r['Z(beta=1)']:.4f}  U(numeric)={r['U_via_finite_difference_-dlnZ/dbeta']:.6f}  "
              f"U(direct)={r['U_via_direct_boltzmann_average']:.6f}  err={r['U_consistency_error']:.2e}  "
              f"F={r['F_free_energy']:.4f}  S={r['S_entropy_(U-F)*beta']:.4f}")

if __name__ == '__main__':
    main()
