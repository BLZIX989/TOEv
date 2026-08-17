"""
PRF-PRIM Phase 2/3/4 -- concrete type-check of the certified composition

    Gamma = kappa o tau o Delta            (BR-001, CERTIFIED SPINE)
    Psi_{t+1} = kappa(tau(Delta(Psi_t)))    (DER-ORG-002, CERTIFIED)

PRIM-G-001's OWN formal definition of Delta is: "a hypersurface satisfying the homological
closure condition d(d Omega) = 0" -- i.e. Delta is characterized via a simplicial/differential-
form BOUNDARY OPERATOR d, an object that maps between DIFFERENT graded pieces of a chain complex
(d_k : C_k -> C_{k-1}), not an endomorphism of a single space.

But DER-ORG-002 requires Delta: X -> X (same X that Psi_t and Psi_{t+1} both live in), because
the state-evolution equation Psi_{t+1}=kappa(tau(Delta(Psi_t))) must be ITERABLE (Psi_{t+1} must
be a valid input to the same equation at the next step).

This script builds an ACTUAL simplicial complex (the tetrahedron: K4's vertices+edges+its 4
triangular faces) and computes the two candidate readings of Delta explicitly, to make the type
mismatch concrete and checkable rather than asserted:

  READING 1 (literal, per PRIM-G-001's stated formula): Delta ~ the boundary operator d_1 (or d_2)
    of the simplicial complex. Domain and codomain are DIFFERENT vector spaces (different
    dimension), so d cannot be composed with kappa/tau (both endomorphisms of the SAME vertex
    space X=R^N) to form kappa(tau(Delta(x))) for x in X. TYPE ERROR, demonstrated concretely.

  READING 2 (functionally required, per DER-ORG-002's usage): Delta ~ some endomorphism of X
    (e.g. an idempotent "distinguishing" projector onto a marked subspace of R^N, structurally
    identical in TYPE to kappa). This type-checks but is NOT what PRIM-G-001 literally defines.

CONCLUSION: PRIM-G-001's formal definition and DER-ORG-002's usage of Delta are TYPE-INCOMPATIBLE
as literally stated in the source corpus. This is an internal inconsistency this DER's Phase 2
type-audit is specifically designed to catch (directive: "Reject equations whose operands are
type-incompatible"). It does not mean Gamma=kappa o tau o Delta is meaningless -- it means the
source corpus is using "Delta" in (at least) two different formal senses that have never been
reconciled, exactly the kind of ambiguity PRF-PRIM exists to surface.

Run: python3 05_composition_type_check.py
"""
import numpy as np
import json, os

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, 'output')
os.makedirs(OUT, exist_ok=True)

def main():
    # Tetrahedron complex: 4 vertices, 6 edges (K4's edge set), 4 triangular faces
    vertices = [0, 1, 2, 3]
    edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]   # 6 edges, indices 0..5
    faces = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]        # 4 faces, indices 0..3

    edge_index = {e: i for i, e in enumerate(edges)}

    # boundary d1: edges (C1, dim 6) -> vertices (C0, dim 4). d1(u,v) = v - u (signed)
    d1 = np.zeros((4, 6))
    for j, (u, v) in enumerate(edges):
        d1[v, j] += 1
        d1[u, j] -= 1

    # boundary d2: faces (C2, dim 4) -> edges (C1, dim 6). For face (a,b,c) with a<b<c:
    # d2(face) = (b,c) - (a,c) + (a,b)   (standard simplicial boundary with alternating sign)
    d2 = np.zeros((6, 4))
    for k, (a, b, c) in enumerate(faces):
        for sign, e in [(+1, (b, c)), (-1, (a, c)), (+1, (a, b))]:
            d2[edge_index[e], k] += sign

    d1d2 = d1 @ d2
    d1d2_is_zero = np.allclose(d1d2, 0.0)

    report = []
    report.append("READING 1 -- literal PRIM-G-001 formula, d(dOmega)=0, tested on the tetrahedron complex:")
    report.append(f"  d1 : C1(edges, dim=6) -> C0(vertices, dim=4)   shape={d1.shape}")
    report.append(f"  d2 : C2(faces, dim=4) -> C1(edges, dim=6)     shape={d2.shape}")
    report.append(f"  d1 @ d2 = 0 ?  {d1d2_is_zero}   (max abs entry: {np.max(np.abs(d1d2)):.2e})")
    report.append(f"  ==> PRIM-G-001's own formula IS satisfiable and verified exactly: d1 o d2 = 0.")
    report.append("")
    report.append("TYPE CHECK: is d1 (candidate Delta) an endomorphism of a single space X, as required")
    report.append("by DER-ORG-002's Psi_{t+1}=kappa(tau(Delta(Psi_t)))?")
    report.append(f"  domain dim = {d1.shape[1]} (edge space C1)")
    report.append(f"  codomain dim = {d1.shape[0]} (vertex space C0)")
    is_endomorphism = (d1.shape[0] == d1.shape[1])
    report.append(f"  domain == codomain ?  {is_endomorphism}")
    report.append("  ==> FALSE for this (or any nontrivial) simplicial complex whenever #edges != #vertices.")
    report.append("  ==> d1 CANNOT be composed with kappa,tau (both endomorphisms of the vertex space X)")
    report.append("      to form kappa(tau(Delta(x))) for a fixed x in X, as DER-ORG-002 requires.")
    report.append("")
    report.append("READING 2 -- functionally required reading (Delta as an endomorphism of X, e.g. an")
    report.append("idempotent 'distinguishing' projector D_hat: X->X with D_hat^2=D_hat, structurally")
    report.append("IDENTICAL in type to kappa). This type-checks against DER-ORG-002 but is NOT the")
    report.append("boundary-operator formula literally given in PRIM-G-001.")
    report.append("")
    report.append("CONCLUSION: TYPE MISMATCH confirmed between PRIM-G-001's stated definition of Delta")
    report.append("(a boundary map between graded spaces) and DER-ORG-002's required usage of Delta")
    report.append("(an endomorphism of the state space X). This is an internal inconsistency in the")
    report.append("source corpus's own primitive definitions, not an artifact of this DER's realization")
    report.append("choices -- it is demonstrated directly from the source formulas.")

    text = '\n'.join(report)
    print(text)
    with open(os.path.join(OUT, 'composition_type_check.txt'), 'w') as f:
        f.write(text)
    with open(os.path.join(OUT, 'composition_type_check.json'), 'w') as f:
        json.dump({
            "d1_shape": list(d1.shape), "d2_shape": list(d2.shape),
            "d1_d2_is_zero": bool(d1d2_is_zero),
            "d1_is_endomorphism_of_single_space": bool(is_endomorphism),
            "type_mismatch_confirmed": bool(not is_endomorphism),
        }, f, indent=2)

if __name__ == '__main__':
    main()
