# Independent Derivation Ledger

`INDEPENDENT_DERIVATION_LEDGER.csv` is intentionally **empty (header row only)**. Per the master
directive's execution order, Phase 0 builds architecture and registries only — "do not execute the
first physical derivations until Phase 0 architecture and registries are complete and validated."
No independent derivation (Phase 1 "reconstruct established physics" onward) has been attempted.

**ID scheme (reserved, not yet used):** `IDER-<PHASE>-<DOMAIN>-<NNN>`, e.g. `IDER-P3A-CLASSICAL-001`
for the first Classical Mechanics derivation in Phase 3A. This is deliberately a **different
namespace from the canonical `DER-*` IDs** in `registries/MASTER_DER_REGISTRY.csv` — an independent
derivation ledger entry is never assumed equivalent to an existing `DER-*` entry until Phase 13's
explicit comparison step classifies the relationship (EXACT EQUIVALENCE / ISOMORPHIC / CONDITIONAL /
PARTIAL / DIFFERENT / CONTRADICTORY / UNRESOLVED).

Columns: `IDER_ID, Title, Phase, Domain, Direct_Predecessors, Input_Objects, Output_Objects,
Assumptions, Derivation_Status, Universality_Status, Verification_Method, Falsification_Test,
Provenance`. `Input_Objects`/`Output_Objects` reference `OBJ-*` IDs from
`source_extract/ONTOLOGY_NEUTRAL_OBJECT_REGISTRY.xlsx` or newly-introduced `IOBJ-*` IDs for objects
constructed for the first time during independent reconstruction.
