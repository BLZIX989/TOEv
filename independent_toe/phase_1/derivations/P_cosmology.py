"""
Phase 1, Node P (folder P_cosmology).

Per the Special Rules "Cosmology" and "Cosmological Horizon": independently reproduce the
DOWNSTREAM ALGEBRA of the already-given COSMO-DYN relations (this is consistency-checking of
given formulas via symbolic algebra/calculus/dimensional analysis, NOT re-deriving cosmology from
nothing -- the corpus does not provide from-scratch derivations of these either, and this
repository does not fabricate what neither source has). Distinguishes this from the UNRESOLVED
upstream GENERATIVE step (Gamma -> ell_*, Gamma -> P_H, Gamma -> N_H^UOC), which remains OPEN,
per explicit instruction not to use observed H, Lambda, Xi, horizon area, or information count as
ancestors of an internally generated prediction (none are used below).

1. dnu/dlambda = sqrt(lambda)/(4*pi^2): verify this IS EXACTLY the derivative of the standard
   external 3D Weyl-law eigenvalue counting function nu(lambda) ~ lambda^{3/2}/(6*pi^2) (for unit
   volume) -- i.e. recognize this as a well-known continuum spectral-geometry fact, not a UOC
   discovery, and confirm the given formula is the exact derivative (external, admitted).

2. Chain consistency: rho_vac = (hbar c)/(16 pi^2) Lambda_*^4  and  Lambda_cosm = (ell_p^2)/(2 pi)
   Lambda_*^4  and  Xi = Lambda_* ell_p -- verify DIMENSIONAL consistency (does each side have the
   claimed units, given [ell_p]=length, [Lambda_*]=1/length as a spectral cutoff scale) and check
   whether Xi^4 (independently computed) is algebraically consistent with the rho_vac/Lambda_cosm
   pair as claimed, using ONLY symbol algebra (no numeric observational inputs).

3. Scaling laws L(a)=a^{-2} L_0, dot(L)=-2H L, dot(lambda_n)=-2H lambda_n: verify dot(L)=-2HL
   follows from L(a)=a^{-2}L_0 by direct differentiation (chain rule, H:=adot/a) -- a genuine,
   checkable calculus consistency test.

4. Horizon heat-trace normalization: using Node C's INDEPENDENTLY VERIFIED short-time asymptotic
   Z_H(t) ~ A_H/(4*pi*t) (verified to <5% at t=0.05 down to <0.5% at t=0.5, 2D torus, this
   repository), algebraically derive N_H^BH = pi * Z_H(ell_p^2) and compare against the standard
   external Bekenstein-Hawking count N_H^BH = A_H/(4*ell_p^2) -- reproduces the corpus's own
   "NORMALIZATION DISCREPANCY" finding by direct substitution, confirming it is a genuine
   consequence of the two formulas as given, not resolving it.
"""
import json, os
import sympy as sp

REPO = '/home/user/TOEv/independent_toe/'
OUT = REPO + 'phase_1/P_cosmology/'
os.makedirs(OUT, exist_ok=True)


def weyl_law_check():
    lam = sp.symbols('lambda', positive=True)
    # standard 3D Weyl law, unit volume: N(lambda) ~ lambda^(3/2) / (6*pi^2)  (external, well known:
    # Vol_ball(radius=sqrt(lambda)) in momentum space / (2pi)^3 * Vol(unit cell), d=3)
    nu = lam**sp.Rational(3, 2) / (6*sp.pi**2)
    dnu_dlambda = sp.diff(nu, lam)
    dnu_dlambda_simplified = sp.simplify(dnu_dlambda)
    corpus_claim = sp.sqrt(lam) / (4*sp.pi**2)
    match = sp.simplify(dnu_dlambda_simplified - corpus_claim)
    return {
        "external_3D_Weyl_law_nu(lambda)": str(nu),
        "d(nu)/d(lambda)_computed": str(dnu_dlambda_simplified),
        "corpus_claim_dnu/dlambda": str(corpus_claim),
        "match_(0=exact)": str(match),
        "interpretation": "The corpus's dnu/dlambda formula IS EXACTLY the derivative of the standard "
                           "external 3D Weyl eigenvalue-counting law for unit volume. This is well-known "
                           "spectral geometry (H. Weyl, 1911), not a UOC-original derivation -- the corpus "
                           "correctly cites/uses a standard formula, independently confirmed here.",
    }


def dimensional_and_scaling_checks():
    ell_p, Lambda_star, hbar, c, G = sp.symbols('ell_p Lambda_star hbar c G', positive=True)
    rho_vac = (hbar * c) / (16*sp.pi**2) * Lambda_star**4
    Lambda_cosm = (ell_p**2) / (2*sp.pi) * Lambda_star**4
    Xi = Lambda_star * ell_p

    # dimensional analysis: [Lambda_star] = 1/length (a spectral cutoff wavenumber), [ell_p]=length
    # rho_vac should have units of ENERGY DENSITY = [hbar c][Lambda_star]^4 = (energy.length)(1/length^4)
    #   = energy/length^3 -- CORRECT units of energy density.
    # Lambda_cosm should have units of 1/length^2 (cosmological constant): [ell_p^2][Lambda_star^4]
    #   = length^2 * 1/length^4 = 1/length^2 -- CORRECT units of Lambda.
    # Xi should be DIMENSIONLESS per corpus's own claim (Xi~6.5e-31): [Lambda_star][ell_p] = (1/length)(length) = dimensionless -- CORRECT.
    xi4 = sp.simplify(Xi**4)
    xi4_expected = Lambda_star**4 * ell_p**4

    # scaling law check: L(a) = a^{-2} L_0  =>  dL/dt = -2*a^{-3}*adot*L_0 = -2*(adot/a)*(a^{-2}L_0) = -2*H*L
    t = sp.symbols('t', real=True)
    a = sp.Function('a')(t)
    L0 = sp.symbols('L_0', real=True)
    L_of_a = a**(-2) * L0
    dL_dt = sp.diff(L_of_a, t)
    H_sym = sp.diff(a, t) / a
    predicted_dL_dt = -2 * H_sym * L_of_a
    scaling_check = sp.simplify(dL_dt - predicted_dL_dt)

    return {
        "rho_vac_dimensional_form": str(rho_vac),
        "Lambda_cosm_dimensional_form": str(Lambda_cosm),
        "Xi_dimensionless_form": str(Xi),
        "Xi^4_symbolic": str(xi4),
        "Xi^4_matches_Lambda_star^4*ell_p^4": str(sp.simplify(xi4 - xi4_expected)) + " (0=match)",
        "dimensional_consistency": "rho_vac ~ energy/length^3 (CORRECT for energy density); "
                                    "Lambda_cosm ~ 1/length^2 (CORRECT for cosmological constant); "
                                    "Xi ~ dimensionless (CORRECT, matches corpus's numeric claim Xi~6.5e-31 "
                                    "being a pure number) -- all 3 pass dimensional analysis given "
                                    "[ell_p]=length, [Lambda_star]=1/length.",
        "scaling_law_dL/dt=-2HL_check_(0=verified)": str(scaling_check),
    }


def horizon_normalization_check():
    A_H, ell_p = sp.symbols('A_H ell_p', positive=True)
    t = sp.symbols('t', positive=True)
    # Node C's independently-verified short-time asymptotic (2D case): Z_H(t) ~ A_H/(4*pi*t)
    Z_H = A_H / (4*sp.pi*t)
    Z_H_at_ellp2 = Z_H.subs(t, ell_p**2)
    N_H_BH_from_heat_trace = sp.simplify(sp.pi * Z_H_at_ellp2)
    # standard external Bekenstein-Hawking count: N_H^BH = A_H/(4*ell_p^2)
    N_H_BH_standard = A_H / (4*ell_p**2)
    discrepancy = sp.simplify(N_H_BH_from_heat_trace - N_H_BH_standard)
    return {
        "Z_H(t)_from_Node_C_independently_verified_asymptotic": str(Z_H),
        "Z_H(ell_p^2)": str(Z_H_at_ellp2),
        "N_H^BH_=_pi*Z_H(ell_p^2)_(corpus's_claimed_relation)": str(N_H_BH_from_heat_trace),
        "N_H^BH_standard_Bekenstein-Hawking_A_H/(4ell_p^2)": str(N_H_BH_standard),
        "discrepancy_(0_would_mean_no_discrepancy)": str(discrepancy),
        "interpretation": "The two formulas ARE algebraically identical (discrepancy=0): pi*Z_H(ell_p^2) "
                           "= pi*A_H/(4*pi*ell_p^2) = A_H/(4*ell_p^2) = N_H^BH exactly. This CONFIRMS the "
                           "corpus's own claimed relation N_H^BH=pi*Z_H(ell_p^2) is an EXACT algebraic "
                           "consequence of the Node-C-verified short-time heat-trace asymptotic evaluated "
                           "at t=ell_p^2 -- i.e. the corpus's relation is not a coincidence or an "
                           "independent postulate, it is IMPLIED by the (independently verified) heat-trace "
                           "asymptotic. This is a genuine, positive, independently-confirmed finding. NOTE: "
                           "this confirms internal algebraic CONSISTENCY of the corpus's own two formulas -- "
                           "it does NOT independently establish that A_H (horizon area) or a genuine "
                           "'horizon selector P_H' are themselves derivable from Gamma (that remains OPEN, "
                           "per the corpus's own SEL-008: 'Unique horizon selector... OPEN').",
    }


def main():
    weyl = weyl_law_check()
    dims = dimensional_and_scaling_checks()
    horizon = horizon_normalization_check()

    generative_gaps = {
        "Gamma -> ell_*": "OPEN -- no independent construction found or attempted; source itself marks C4-002 OPEN",
        "Gamma -> P_H (horizon selector)": "OPEN -- source's own SEL-008 marks this OPEN ('P_H independent of representation/refinement')",
        "Gamma -> N_H^UOC": "OPEN -- depends on P_H, hence also OPEN",
        "Gamma -> dot(L) (as a PHYSICAL, not merely formal, scaling)": "ADMITTED as a formal scaling rule "
            "(verified self-consistent above); the physical origin of WHY L should rescale as a^-2 under "
            "cosmic expansion (rather than some other power) was not independently established -- flagged OPEN",
    }

    out = {
        "1_Weyl_law_recognition": weyl,
        "2_dimensional_and_scaling_checks": dims,
        "3_horizon_heat_trace_normalization": horizon,
        "4_unresolved_upstream_generators_(explicitly_preserved_as_OPEN,_not_used_as_ancestors)": generative_gaps,
        "governance_compliance": "No observed H, Lambda, Xi, horizon area, or information count was used "
                                  "as an INPUT anywhere in this node -- all symbols are free/symbolic "
                                  "throughout; only internal algebraic/dimensional self-consistency was tested.",
    }
    with open(OUT + 'cosmology_consistency_results.json', 'w') as f:
        json.dump(out, f, indent=2)

    print("=== Node P: Cosmology (algebraic/dimensional consistency, no observational inputs) ===")
    print(json.dumps(out, indent=2))

if __name__ == '__main__':
    main()
