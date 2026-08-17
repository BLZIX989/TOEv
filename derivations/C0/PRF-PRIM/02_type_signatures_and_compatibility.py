"""
PRF-PRIM Phase 2 -- Type-theoretic reconciliation.

Assigns a mathematical type (from the directive's own vocabulary: scalar, vector, tensor,
operator, relation, graph object, state transition, constraint, persistence operator,
set-valued object, functional, category/morphism, other) to every primitive in every grammar,
using the "type_hint_in_source" field recovered in Phase 1 plus the corpus's own Object Registry
(UOR, OBJ-001..011) where a direct match exists. Then builds the 4x4 grammar compatibility matrix
required by the directive.

This step is STRUCTURAL/QUALITATIVE (type-checking), separate from the computational tests
performed in derivations/03_* and calculations/*, which actually construct and test candidate
morphisms. The compatibility-matrix entries here are refined/overwritten by those later tests --
this script records the FIRST-PASS, type-only judgment, before any morphism is constructed.

Run: python3 02_type_signatures_and_compatibility.py
"""
import json, csv, os

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, 'output')

with open(os.path.join(OUT, 'primitive_systems.json')) as f:
    data = json.load(f)
GRAMMARS = data['grammars']

# Type assignment. Each entry: (grammar_key, primitive_id) -> type
TYPES = {
    ("A_DTC", "PRIM-G-001"): "relation / boundary-operator condition (asserts d^2=0 on some complex; NOT itself a vector/tensor -- a structural condition on an operator)",
    ("A_DTC", "PRIM-G-002"): "operator (volume-preserving map on state space)",
    ("A_DTC", "PRIM-G-003"): "operator (idempotent projector, P^2=P)",
    ("A_DTC", "PRIM-G-004"): "persistence operator (kernel / fixed-point subspace of an operator -- a SET-VALUED object, a subspace, not an operator itself)",
    ("B_Physical", "PRIM-P-001"): "scalar (energy, capacity to do work)",
    ("B_Physical", "PRIM-P-002"): "vector (gradient of a scalar potential field)",
    ("C_Computational", "PRIM-C-001"): "graph object (bipartite graph, a SET-VALUED/relational object: (U,V,E))",
    ("D_Extended", "PRIM-X-001"): "relation / boundary-operator condition (same as PRIM-G-001)",
    ("D_Extended", "PRIM-X-002"): "operator (same as PRIM-G-002)",
    ("D_Extended", "PRIM-X-003"): "operator (same as PRIM-G-003)",
    ("D_Extended", "PRIM-X-004"): "relation (reachability structure -- a subset of StatexState, i.e. a directed graph on the state space)",
    ("D_Extended", "PRIM-X-005"): "persistence operator (same as PRIM-G-004)",
    ("D_Extended", "PRIM-X-006"): "state transition (state variable -- an ELEMENT of the state space, not an operator on it)",
}

rows = [["Grammar", "Primitive_ID", "Symbol", "Assigned_Type", "Type_class_per_directive_vocabulary"]]
type_class_map = {
    "scalar": "scalar", "vector": "vector", "operator": "operator", "relation": "relation",
    "graph object": "graph object", "state transition": "state transition",
    "persistence operator": "persistence operator", "set-valued": "set-valued object",
}
for (gkey, pid), t in TYPES.items():
    prim = next(p for p in GRAMMARS[gkey]['primitives'] if p['id'] == pid)
    tclass = next((v for k, v in type_class_map.items() if k in t), "other/structural condition")
    rows.append([gkey, pid, prim['symbol'], t, tclass])

with open(os.path.join(OUT, 'type_signatures.csv'), 'w', newline='') as f:
    csv.writer(f).writerows(rows)

# ---- First-pass (type-only) 4x4 compatibility matrix ----
# Grammars: A=DTC(4 prims: Delta,tau,kappa,Pi), B=Physical(2: E,gradPhi), C=Computational(1: B=(U,V,E)),
# D=Extended(6: Delta,tau,kappa,Theta,Pi,Omega)
matrix_notes = {
    ("A_DTC", "A_DTC"): "IDENTITY",
    ("A_DTC", "B_Physical"): ("PARTIAL / TYPE MISMATCH ON Delta. B has only 2 primitives (E scalar, gradPhi vector) "
        "vs A's 4 (Delta relation, tau operator, kappa operator, Pi persistence-operator). Source explicitly "
        "states B 'inherits' tau,kappa from A unchanged (Combined Compiler Theories Whitepaper para. 471) -- "
        "so tau,kappa correspond by STIPULATION, not independent derivation. Delta (relation/boundary condition) "
        "vs gradPhi (vector field) are DIFFERENT TYPES -- a relation is not a vector. B has NO analogue of Pi "
        "at all (not registered). Provisional: MANY-TO-ONE REDUCTION for {tau,kappa} (identified by stipulation), "
        "TYPE MISMATCH for Delta vs gradPhi, NO CORRESPONDENCE for Pi."),
    ("A_DTC", "C_Computational"): ("NO CORRESPONDENCE ESTABLISHED IN SOURCE. PRIM-C-001 (B=(U,V,E), a graph object) "
        "has no source-registered mapping to any of Delta/tau/kappa/Pi. A graph object is a SET-VALUED/relational "
        "object, structurally closer to Delta's 'boundary/relation' type than to tau or kappa's operator type, but "
        "no explicit source correspondence exists -- this is a CANDIDATE mapping to be tested computationally, not "
        "an established one."),
    ("A_DTC", "D_Extended"): ("DEFINITIONAL EQUIVALENCE on Delta,tau,kappa,Pi (D_Extended's own source text says "
        "'same as PRIM-G-00X' for all 4 -- this is a direct textual identification, not merely a candidate). "
        "ONE-TO-MANY EXPANSION overall: D adds Theta (relation) and Omega (state transition/element) with NO "
        "analogue in A. So A embeds INJECTIVELY into D (A's 4 primitives are literally a named subset of D's 6), "
        "but D is not reducible to A without loss (Theta, Omega have no A-side counterpart)."),
    ("B_Physical", "B_Physical"): "IDENTITY",
    ("B_Physical", "C_Computational"): ("NO CORRESPONDENCE ESTABLISHED IN SOURCE between {E,gradPhi} and B=(U,V,E). "
        "TYPE-LEVEL CANDIDATE exists and is tested computationally below: standard spectral graph theory defines "
        "a Dirichlet energy E(phi)=phi^T L phi = ||grad_graph phi||^2 for a graph Laplacian L built from an "
        "incidence operator that plays the role of a discrete gradient. This is a DEFINITIONAL fact of standard "
        "mathematics (not a UOC-original derivation) and is registered as an ADMITTED EXTERNAL INPUT if used."),
    ("B_Physical", "D_Extended"): ("TYPE MISMATCH / NO SOURCE CORRESPONDENCE. D has no Energy or Gradient primitive; "
        "B has no Theta or Omega. Only the inherited tau,kappa (stipulated identical to A) are shared indirectly "
        "through both grammars' common ancestry in A."),
    ("C_Computational", "C_Computational"): "IDENTITY",
    ("C_Computational", "D_Extended"): ("NO CORRESPONDENCE ESTABLISHED IN SOURCE. PRIM-C-001 is never mentioned "
        "alongside PRIM-X-001..006 in any recovered source passage."),
    ("D_Extended", "D_Extended"): "IDENTITY",
}

with open(os.path.join(OUT, 'compatibility_matrix_firstpass.json'), 'w') as f:
    json.dump({f"{a}|{b}": v for (a, b), v in matrix_notes.items()}, f, indent=2)

# CSV grid form
keys = ["A_DTC", "B_Physical", "C_Computational", "D_Extended"]
grid_rows = [["(row -> col)"] + keys]
def lookup(a, b):
    if (a, b) in matrix_notes:
        return matrix_notes[(a, b)]
    if (b, a) in matrix_notes:
        return "SYMMETRIC: " + matrix_notes[(b, a)]
    return "UNSET"
for a in keys:
    grid_rows.append([a] + [lookup(a, b)[:120] for b in keys])
with open(os.path.join(OUT, 'compatibility_matrix_firstpass.csv'), 'w', newline='') as f:
    csv.writer(f).writerows(grid_rows)

print("Wrote type_signatures.csv and compatibility_matrix_firstpass.{json,csv}")
for r in rows[1:]:
    print(r[1], r[2], '->', r[3])
