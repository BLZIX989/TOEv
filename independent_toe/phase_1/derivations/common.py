"""Shared helpers for Phase 1 independent reconstruction scripts."""
import json, os
import numpy as np
import networkx as nx

REPO = '/home/user/TOEv/independent_toe/'

def load_graph_families():
    with open(REPO + '../graphs/C0/PRF-PRIM/graph_families.json') as f:
        return json.load(f)

def laplacian(adj):
    A = np.array(adj, dtype=float)
    D = np.diag(A.sum(axis=1))
    return D - A

MASTER_ROWS = []  # accumulated across all node scripts; each is a dict matching the master schema

def add_row(**kw):
    MASTER_ROWS.append(kw)

def save_master_rows(path):
    import csv
    fields = ["Object_ID","Source_ID","Domain","Input_Dependencies","Output_Object","Equation",
              "Derivation","Assumptions","Source_Status","Independent_Status","Closure_Status",
              "Verification_Status","Numerical_Check","Symbolic_Check","Proof_Record",
              "Counterexample_Record","Provenance","Notes"]
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in MASTER_ROWS:
            w.writerow({k: r.get(k, '') for k in fields})
