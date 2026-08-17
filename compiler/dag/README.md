# Master Dependency DAG (compiler/dag/)

The 9 files required by the master directive (Section IV), each copied verbatim from the
corresponding sheet in `UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0.xlsx` (SOURCE-004):

| Required file | Source sheet |
|---|---|
| master_nodes.csv | DAG_01_NODE_REGISTRY (779 nodes) |
| master_edges.csv | DAG_02_EDGE_REGISTRY (320 edges) |
| equations_dag.csv | DAG_03_EQUATION_DEPENDENCIES |
| bridge_dag.csv | DAG_04_BRIDGE_DEPENDENCIES |
| theorem_dag.csv | DAG_23_THEOREM_INDEX |
| proof_dag.csv | DAG_24_PROOF_INDEX |
| prediction_dag.csv | DAG_25_PREDICTION_INDEX |
| dependency_cycles.csv | DAG_12_CYCLE_AUDIT |
| topological_order.csv | DAG_11_TOPOLOGICAL_ORDER |

**Cycle audit result (already run by the source corpus, re-verified here):** PASS — no explicit
cycles found; all internal dependency edges admit a topological ordering (779 nodes ordered, 106
of the 320 edges are "internal" i.e. both endpoints resolve to canonical nodes usable for strict
topological analysis; the remaining edges reference source-registered but not-yet-canonicalized
endpoints and were excluded from the strict cycle check rather than silently forced in).

The `supplementary_DAG_*.csv` files are the rest of the DAG_* sheet family from SOURCE-004
(closure obligations, critical frontier, impact map, phase execution plan, etc.) — not required by
the directive's file list, but kept because they are direct dependents of the same DAG construction
and are referenced by `PHASE_1_REPORT.md` and the ledger.
