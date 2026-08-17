# Spreadsheet Source Records

Verbatim CSV export of every worksheet in the 4 uploaded xlsx files, one subfolder per workbook,
one CSV per worksheet, extracted with `openpyxl` (`data_only=True`) and no cell modified.
This preserves the source exactly as uploaded, per the Source Authority Rule (directive Section II)
which forbids overwriting or silently altering source files.

- `ToE_Gap_Matrix/` — 2 sheets (SOURCE-002)
- `UOC_Master_Closure_Updated/` — 12 sheets (SOURCE-003)
- `UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0/` — 90 sheets (SOURCE-004, the master compiled corpus)
- `UOC_ToE_Canonical_Calculated_Master_v1.0/` — 24 sheets (SOURCE-005, certified/calculated-only companion)

The reorganized, deduplicated, cross-referenced versions of this same data live in `registries/`
and `compiler/dag/` — those are derived exports built FROM these files, never the other way around.
