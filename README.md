# TOEv
Theory of Organizational Evolution

Computational research environment for determining, by explicit derivation, calculation,
simulation, proof, and falsification, whether the UOC/SEIT/ARBS/MDCL architecture can be closed
into a unified physical theory. See **`PHASE_1_REPORT.md`** for the current status.

## Layout

- `source_records/` — verbatim, loss-free export of every uploaded source file (docx + xlsx), plus
  the source inventory and provenance/reconciliation records. Nothing here is ever silently modified.
- `registries/` — 61 master CSV registries (equations, variables, constants, primitives, operators,
  theorems, proofs, derivations, bridges, closure layers, predictions, open/falsification items,
  the 164-question map) consolidated from the source corpus.
- `compiler/dag/` — the Master Dependency DAG: nodes, edges, equation/bridge/theorem/proof/prediction
  sub-DAGs, cycle audit (0 cycles found), topological order.
- `derivations/C0/` … `derivations/C10/` — one folder per closure layer; empty of individual DER-ID
  work until a derivation is actually executed.
- `calculations/` — one folder per calculation domain (symbolic, numerical, spectral, cosmological, …).
- `domains/` — one folder per physics/mathematics domain in the master question set, each with
  `source/ definitions/ equations/ derivations/ calculations/ simulations/ proofs/ falsification/
  results/ references/` subfolders.
- `results/workbooks/` — the 6 canonical `.xlsx` deliverables: the master derivation ledger, the
  dependency DAG workbook, the source corpus index, the 164-question-to-closure-layer map, and the
  derivation/calculation templates used for all future work.

## Status

Phase 0–1 (corpus ingestion + architecture construction) is complete. No derivation has been
executed yet. See `PHASE_1_REPORT.md` for what is CERTIFIED, CALCULATED, OPEN, and the first
recommended derivation (C0 — primitive/grammar reconciliation).
