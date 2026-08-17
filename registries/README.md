# Registries

Master, deduplicated, cross-referenced CSV registries built from the source corpus (primarily
`SOURCE-004` / `UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0.xlsx`, the most complete and most
recent synthesis in the uploaded corpus).

This folder is not explicitly named in the master directive, but was created to hold the
machine-readable CSV backing for the `TOEV_MASTER_DERIVATION_LEDGER.xlsx` and other canonical
workbooks in `results/workbooks/` — CSV-first so every registry is diffable and auditable before
being packaged into a spreadsheet.

- `MASTER_*.csv` — canonical registries sourced from SOURCE-004, one per entity type (equations,
  variables, constants, primitives, operators, theorems, proofs, DER entries, bridges, closure
  layers, COSMO-DYN results, predictions, open/no-go items, etc).
- `CALCULATED_ONLY_*_v1.csv` — the certified/calculated-only subset from SOURCE-005, kept as a
  SEPARATE cross-check registry rather than merged into MASTER_*, per the Source Authority Rule.
- `STANDALONE_TOE_GAP_MATRIX_SOURCE-002.csv` — the Gap Matrix as uploaded standalone, kept separate
  from its embedded copy inside SOURCE-004 for independent cross-check.
- `RECONCILIATION_RECORDS.csv` — explicit disagreement/consistency records between sources (Section
  II of the directive). All 6 recorded reconciliations were RESOLVED (subset/identical relationships)
  except RECON-004 (a cosmetic header defect in the source file) and RECON-006 (14 upstream originals
  not independently present), both left OPEN pending future correction/re-upload.
- `MASTER_QUESTION_TO_CLOSURE_LAYER_MAP.csv` / `QUESTION_SECTION_CLOSURE_LAYER_SUMMARY.csv` — the
  164-question-to-closure-layer mapping. SECTION-LEVEL only; per-question/per-edge mapping is
  explicitly NOT yet audited (directive Section XII).

No values were invented. Every registry here is either a verbatim copy of a source worksheet or a
mechanical recombination (concatenation, subset comparison, join on shared IDs) of verbatim source data.
