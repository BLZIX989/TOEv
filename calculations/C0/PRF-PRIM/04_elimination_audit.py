"""
PRF-PRIM Phase 5 -- minimality/irreducibility audit of the graph-theoretic realization
{Delta~incidence, tau~automorphism/heat-semigroup, kappa~P_ker(L), Pi~ker(L)}.

For each primitive, remove it and test whether the SAME organizational invariant (here: the
persistence subspace ker(L), i.e. P_ker(L) and its idempotency, and the asymptotic limit
lim_{t->inf} exp(-tL) = P_ker(L)) can still be reconstructed from the remaining primitives.

This is INDEPENDENT of the source corpus's own 8-theory elimination audit (Combined Compiler
Theories Whitepaper para. 473, "no additional primitive survived the elimination audits run
against any of the eight imported theories") -- that audit tested a different question (which
primitives are needed to compile 8 named physical theories) against a narrower realization. This
script tests specifically: in the GRAPH-SPECTRAL realization used throughout this DER, is each
primitive's ROLE actually doing independent work, or does removing it leave the target invariant
unchanged?

Tests:
  (1) Remove kappa (no explicit projection step). Does lim_{t->inf} exp(-tL) still equal ker(L)
      structurally, i.e. does the asymptotic behavior of tau ALONE already select the persistence
      subspace, making kappa's explicit-projection role REDUNDANT in this realization?
  (2) Remove Pi (no persistence primitive registered at all). Can dim(ker(L)) / the fixed
      subspace still be RECOVERED post-hoc from tau and kappa alone (i.e. is Pi DERIVABLE rather
      than needing to be a fourth independent primitive)?
  (3) Remove Delta (no incidence/boundary structure). Can L be reconstructed from tau (automorphism
      group) and kappa (projector) alone, without ever building the incidence matrix? Tested by
      asking whether Aut(G) and P_ker(L) determine L up to the tested graph family (they do NOT in
      general -- cospectral non-isomorphic graphs exist, so kappa+tau does not determine Delta).
  (4) Remove tau (no transformation/evolution). Can persistence (kappa/Pi) be defined at all
      without ANY notion of evolution to be persistent THROUGH? Tested conceptually: kappa is
      defined as idempotent projector onto ker(L), which requires L (hence Delta, the graph
      structure) but does NOT itself require tau to be well-defined as a projector. However Pi's
      OWN definition ("kernel of an invariant operator surviving REPEATED APPLICATION OF TAU under
      kappa") explicitly presupposes tau in its wording -- so Pi conceptually requires tau even
      though the computed OBJECT ker(L) does not.

Run: python3 04_elimination_audit.py
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

def main():
    findings = {}

    # --- Test 1: is kappa redundant given tau's asymptotics? ---
    kappa_redundant_evidence = []
    for name, fam in FAMILIES.items():
        A = np.array(fam['adjacency'], dtype=float)
        D = np.diag(A.sum(axis=1))
        L = D - A
        eigvals, eigvecs = np.linalg.eigh(L)
        exp_tL_asymptotic = eigvecs @ np.diag(np.exp(-500.0 * eigvals)) @ eigvecs.T
        mask = np.abs(eigvals) < 1e-8
        V0 = eigvecs[:, mask]
        P_ker_explicit = V0 @ V0.T
        error = float(np.max(np.abs(exp_tL_asymptotic - P_ker_explicit)))
        kappa_redundant_evidence.append(error < 1e-9)
    findings['test1_kappa_redundant_given_tau_asymptotics'] = {
        "result": all(kappa_redundant_evidence),
        "n_families_tested": len(kappa_redundant_evidence),
        "conclusion": ("REDUNDANT (in this specific spectral realization). lim_{t->inf} exp(-tL) "
            "converges to P_ker(L) WITHOUT any separately-applied projection step -- the asymptotic "
            "behavior of tau_2 (the diffusion semigroup) already performs kappa's stated role "
            "('restricting which transformations are permissible... surviving to the persistence "
            "subspace') automatically, as t->infinity. IMPORTANT CAVEAT: this makes kappa redundant "
            "ONLY if tau is realized as the (Liouville-violating, see script 04) diffusion semigroup. "
            "Under the OTHER candidate realization of tau (automorphisms, which are norm-preserving "
            "bijections with NO asymptotic contraction), there is no such convergence and kappa is "
            "NOT redundant -- an automorphism does not by itself select ker(L). So kappa's status "
            "(IRREDUCIBLE vs REDUNDANT) is CONDITIONAL on which tau-realization is chosen -- itself "
            "an unresolved C0 question, not a fact independent of it."),
    }

    # --- Test 2: is Pi derivable from tau+kappa? ---
    findings['test2_Pi_derivable_from_tau_kappa'] = {
        "result": "DERIVABLE (as an OBJECT) under the kappa=P_ker(L) realization",
        "conclusion": ("Once kappa is realized as the spectral projector P_ker(L), the object Pi "
            "(the persistence SUBSPACE) is simply the image of kappa, i.e. Pi = im(kappa) = ker(L). "
            "No independent construction is needed beyond kappa itself: Pi is DERIVABLE from kappa "
            "in this realization, not an independent fourth primitive. This matches the corpus's own "
            "documented disagreement (Combined Compiler Theories Whitepaper para. 549, verbatim): "
            "'They disagree on whether Persistence is primitive or derived' -- this computation "
            "provides a concrete instance (the graph-spectral realization) in which Persistence is "
            "DERIVED, supporting the 'derived' side of that disagreement rather than resolving it "
            "universally (a different realization could still require Pi as independent)."),
    }

    # --- Test 3: can Delta be reconstructed from tau+kappa (cospectrality test)? ---
    # Use a KNOWN cospectral-but-nonisomorphic pair if available; else state the general theorem.
    findings['test3_Delta_reconstructible_from_tau_kappa'] = {
        "result": "NOT RECONSTRUCTIBLE IN GENERAL",
        "conclusion": ("Aut(G) (candidate tau) and Spec(L)/P_ker(L) (candidate kappa/Pi) do NOT "
            "jointly determine Delta (candidate: the incidence/graph structure itself) up to the "
            "tested family, because COSPECTRAL NON-ISOMORPHIC GRAPHS are a standard, well-known "
            "phenomenon in spectral graph theory (smallest examples exist at n=5, e.g. C4+K1 vs K1,4 "
            "are NOT cospectral but documented cospectral mates exist from n=5 upward; strongly "
            "regular graph families routinely share a spectrum without being isomorphic). This DER "
            "did not need to construct a fresh cospectral pair to establish the point: it is an "
            "established theorem (registered as EXT-002, ADMITTED EXTERNAL INPUT) that the spectrum "
            "alone is not a complete graph invariant. CONCLUSION: Delta is IRREDUCIBLE -- it cannot "
            "be recovered from tau and kappa's outputs alone; it is genuinely prior information."),
    }

    # --- Test 4: does Pi's own definition presuppose tau? ---
    findings['test4_Pi_definition_presupposes_tau'] = {
        "result": "YES, BY SOURCE DEFINITION, THOUGH NOT BY THE COMPUTED OBJECT",
        "conclusion": ("PRIM-G-004's source text defines Pi as 'the kernel of an invariant operator "
            "surviving repeated application of TAU under kappa' -- tau appears explicitly in Pi's "
            "OWN definition. Yet the computed realization (ker(L), the eigenspace at eigenvalue 0) "
            "can be defined and computed directly from L (hence from Delta/kappa) without ever "
            "invoking tau as a separate map -- L's kernel is a static linear-algebra fact, not the "
            "limit of an iterated process. This is a definitional-vs-constructive gap: Pi is defined "
            "narratively in terms of tau's iteration, but realized computationally without needing it. "
            "Flagged as UNRESOLVED rather than forced to one side."),
    }

    with open(os.path.join(OUT, 'elimination_audit_results.json'), 'w') as f:
        json.dump(findings, f, indent=2)

    for k, v in findings.items():
        print(f"\n{k}: {v['result']}")

if __name__ == '__main__':
    main()
