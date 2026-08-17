"""
Phase 1, Node O (folder O_gravity).

Independently derives the vacuum Friedmann equation H^2 = Lambda/3 from the Einstein-Hilbert
action, by:

  1. Computing the Ricci scalar R for the flat FLRW metric ds^2 = -dt^2 + a(t)^2(dx^2+dy^2+dz^2)
     via EXPLICIT symbolic Christoffel-symbol / Riemann-tensor computation (full 4D tensor
     algebra, SymPy) -- NOT quoting the textbook formula, actually computing it.
  2. Reducing the Einstein-Hilbert action S = integral sqrt(-g) (R - 2*Lambda) d^4x to a 1D
     "minisuperspace" Lagrangian L(a, adot) via the standard integration-by-parts trick
     (eliminates the second time derivative of a, standard GR technique, external not
     UOC-original) -- verified symbolically that the boundary term removed is a total derivative.
  3. Varying the minisuperspace action w.r.t. a(t): the Euler-Lagrange equation gives the second
     Friedmann equation; the vanishing-Hamiltonian constraint (from reparametrization invariance
     of the original 4D action) gives the FIRST Friedmann equation, independently reproduced and
     compared against the corpus's own COSMO-DYN claim H^2 = Lambda/3 (registries/
     MASTER_COSMO_DYN_RESULTS.csv).

BLOCKER carried forward from Nodes F/G/H: this derives standard GR structure (external, not
UOC-original) FROM AN ASSUMED SMOOTH FLRW METRIC -- it does NOT independently establish that this
metric is what the graph-spectral substrate converges to (that full construction remains BLOCKER-001).
"""
import json, os
import sympy as sp

REPO = '/home/user/TOEv/independent_toe/'
OUT = REPO + 'phase_1/O_gravity/'
os.makedirs(OUT, exist_ok=True)

def compute_ricci_scalar_flat_FLRW():
    t, x, y, z = sp.symbols('t x y z', real=True)
    coords = [t, x, y, z]
    a = sp.Function('a')(t)
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    n = 4

    # Christoffel symbols Gamma^k_{ij} = 1/2 g^{kl}(d_i g_{jl} + d_j g_{il} - d_l g_{ij})
    Gamma = [[[sp.Rational(0)]*n for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                s = 0
                for l in range(n):
                    s += ginv[k, l] * (sp.diff(g[j, l], coords[i]) + sp.diff(g[i, l], coords[j]) - sp.diff(g[i, j], coords[l]))
                Gamma[k][i][j] = sp.simplify(s / 2)

    # Riemann tensor R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma}
    #                                     + Gamma^rho_{mu lam} Gamma^lam_{nu sigma} - Gamma^rho_{nu lam} Gamma^lam_{mu sigma}
    def Riemann(rho, sigma, mu, nu):
        term1 = sp.diff(Gamma[rho][nu][sigma], coords[mu])
        term2 = sp.diff(Gamma[rho][mu][sigma], coords[nu])
        term3 = sum(Gamma[rho][mu][lam] * Gamma[lam][nu][sigma] for lam in range(n))
        term4 = sum(Gamma[rho][nu][lam] * Gamma[lam][mu][sigma] for lam in range(n))
        return sp.simplify(term1 - term2 + term3 - term4)

    # Ricci tensor R_{sigma nu} = R^rho_{sigma rho nu} (contract first and third indices)
    Ricci = sp.zeros(n, n)
    for sigma in range(n):
        for nu in range(n):
            Ricci[sigma, nu] = sp.simplify(sum(Riemann(rho, sigma, rho, nu) for rho in range(n)))

    # Ricci scalar R = g^{sigma nu} R_{sigma nu}
    R_scalar = sp.simplify(sum(ginv[s, n_] * Ricci[s, n_] for s in range(n) for n_ in range(n)))
    return R_scalar, Ricci, g, ginv, a, t

def main():
    R_scalar, Ricci, g, ginv, a, t = compute_ricci_scalar_flat_FLRW()
    adot = sp.diff(a, t)
    addot = sp.diff(a, t, 2)

    # Standard textbook result to compare against (external, well-known): R = 6(addot/a + (adot/a)^2)
    textbook_R = 6 * (addot / a + (adot / a)**2)
    match = sp.simplify(R_scalar - textbook_R)

    # --- reduce to minisuperspace Lagrangian ---
    # sqrt(-g) = a^3 (for this metric, det(g) = -a^6, sqrt(-det g) = a^3)
    sqrtg = a**3
    Lambda = sp.symbols('Lambda', positive=True)
    G = sp.symbols('G', positive=True)
    # Full integrand (before integration by parts): a^3 * (R - 2*Lambda) / (16*pi*G)
    integrand_before_ibp = sqrtg * (R_scalar - 2*Lambda) / (16*sp.pi*G)

    # Standard IBP identity (external, verified symbolically): a^3 * 6*addot/a = 6*a^2*addot
    #   = d/dt(6*a^2*adot) - 12*a*adot^2   (product rule check)
    lhs_ibp = 6*a**2*addot
    rhs_ibp = sp.diff(6*a**2*adot, t) - 12*a*adot**2
    ibp_check = sp.simplify(lhs_ibp - rhs_ibp)

    # minisuperspace Lagrangian after dropping the total-derivative (boundary) term:
    # a^3 R = 6a^2*addot + 6*a*adot^2  ->  (after IBP, dropping total-deriv) ->  -6*a*adot^2
    L_mini = (-6*a*adot**2 - 2*Lambda*a**3) / (16*sp.pi*G)

    # Euler-Lagrange for L_mini(a,adot): d/dt(dL/dadot) - dL/da = 0
    a_s, adot_s = sp.symbols('a_s adot_s')
    L_mini_generic = (-6*a_s*adot_s**2 - 2*Lambda*a_s**3) / (16*sp.pi*G)
    dL_dadot = sp.diff(L_mini_generic, adot_s).subs({a_s: a, adot_s: adot})
    dL_da = sp.diff(L_mini_generic, a_s).subs({a_s: a, adot_s: adot})
    second_friedmann_lhs = sp.simplify(sp.diff(dL_dadot, t) - dL_da)
    second_friedmann_eq = sp.Eq(second_friedmann_lhs, 0)

    # Hamiltonian constraint (first Friedmann eq): for a Lagrangian L=K(a)*adot^2 - V(a) with no
    # explicit t-dependence, the conserved "energy" E = adot*(dL/dadot) - L = 0 is the constraint
    # (standard minisuperspace/ADM result: total Hamiltonian vanishes identically for a
    # reparametrization-invariant action -- external GR fact, applied here)
    E_constraint = sp.simplify(adot * dL_dadot - L_mini)
    first_friedmann_eq = sp.Eq(sp.simplify(E_constraint * (16*sp.pi*G) / (-6*a)), 0)  # normalize

    # solve first_friedmann_eq for adot^2/a^2 = H^2
    H = sp.symbols('H', real=True)
    first_friedmann_normalized = sp.simplify(E_constraint)
    # E_constraint should reduce to a linear combination of a*adot^2 and a^3*Lambda; solve for adot^2/a^2
    sol = sp.solve(sp.Eq(E_constraint, 0), adot**2)
    H_squared_result = sp.simplify(sol[0] / a**2) if sol else None

    results = {
        "Ricci_scalar_R_computed_from_full_4D_Christoffel/Riemann_tensor_algebra": str(sp.simplify(R_scalar)),
        "textbook_comparison_R=6(addot/a+(adot/a)^2)": str(textbook_R),
        "match_check_(0=exact_match)": str(match),
        "IBP_identity_check_(0=verified)": str(ibp_check),
        "minisuperspace_Lagrangian_L(a,adot)": str(L_mini_generic),
        "second_Friedmann_equation_(Euler-Lagrange)_lhs=0": str(second_friedmann_lhs),
        "Hamiltonian_constraint_(first_Friedmann_eq)_E=0": str(sp.simplify(E_constraint)),
        "H^2_solved_from_constraint": str(H_squared_result),
        "corpus_claim_(registries/MASTER_COSMO_DYN_RESULTS.csv)": "H^2 = Lambda/3",
        "comparison": f"H^2 = {H_squared_result} (independently derived) vs corpus's H^2=Lambda/3 claim -- "
                      f"see whether these match exactly (up to convention/normalization of Lambda and G).",
    }
    with open(OUT + 'friedmann_derivation_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print("=== Node O: Gravity (Friedmann equation from Einstein-Hilbert action, flat FLRW) ===")
    for k, v in results.items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    main()
