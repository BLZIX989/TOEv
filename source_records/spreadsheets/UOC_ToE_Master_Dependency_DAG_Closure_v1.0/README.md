# UOC_ToE_Master_Dependency_DAG_Closure_v1.0.xlsx (SOURCE-009)

**Deduplication note:** 102 worksheets. 101 are byte-identical to sheets already present in
`source_records/spreadsheets/UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0/` (SOURCE-004, which
= this file + 8 new BRIDGE_* sheets). Only `DAG_00_DASHBOARD.csv` differs (SOURCE-004's version has
2 additional summary rows for the Bridge extension) and is preserved here as the pre-Bridge
snapshot. This file IS the source that `compiler/dag/master_nodes.csv`, `master_edges.csv`, etc.
were built from in Phase 1 (via SOURCE-004's identical copy) -- confirmed exact provenance.
Full diff: `results/reconciliation/SYNCHRONIZATION_HISTORY.md`.
