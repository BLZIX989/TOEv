# Source Inventory

- `SOURCE_INVENTORY.csv` — the 5 files uploaded directly to this session (SOURCE-001..005), each with a verified SHA256/byte-count and cross-check against the corpus's own internal provenance records.
- `UPSTREAM_REFERENCED_SOURCES.csv` — the 17 upstream documents (SRC-001..017) that `UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0.xlsx` (SOURCE-004) claims to have synchronized from. Only 3 of the 17 (SRC-002, SRC-004, SRC-007) are independently present and hash-verified in this workspace, matching SOURCE-003, SOURCE-002, and SOURCE-001 respectively. The other 14 originals are NOT present as standalone files here; their content survives only as extracted text/table fragments embedded inside SOURCE-004 (see `03_RAW_DOC_TABLES.csv`, `04_RAW_DOC_PARAGRAPHS.csv`, `54_SOURCE_TEXT_CORPUS.csv`, `55_SOURCE_XLSX_SNAPSHOTS.csv` in `source_records/spreadsheets/UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0/`).

See `registries/RECONCILIATION_RECORDS.csv` (RECON-006) for the governance rule this implies: claims attributed to an absent upstream original must be traced to the embedded extraction, not treated as independently re-verified.
