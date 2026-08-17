# UOC_ToE_Canonical_Synchronization_Master_v1.0.xlsx (SOURCE-006)

**Deduplication note:** this workbook has 50 worksheets. 49 of them are byte-identical (verified
by SHA-256 per-sheet CSV hash) to sheets already present in
`source_records/spreadsheets/UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0/` (SOURCE-004), which
is 3 synchronization generations downstream of this file (v1.0 → v2.0 → v3.0 → +DAG layer →
+Bridge layer = SOURCE-004). Only `00_DASHBOARD.csv` differs (it is a rolling summary that was
updated at every synchronization step) and is preserved here as the historical v1.0 snapshot.

Full sheet-by-sheet diff: `results/reconciliation/SYNCHRONIZATION_HISTORY.md`.
