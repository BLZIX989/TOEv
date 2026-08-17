# Closure Layer C0

## PRF-PRIM (executed 2026-08-17)

The first derivation against this layer has been executed: **`PRF-PRIM/`** — primitive/grammar
reconciliation across the 4 registered primitive systems (DTC, Physical, Computational, Extended
MDCL v2.0). Result: **PARTIALLY ADVANCED, remains OPEN.** Full report: `results/C0_PRF_PRIM_REPORT.md`.
Full workbook: `results/workbooks/C0_PRF_PRIM_Primitive_Reconciliation.xlsx`. Supporting artifacts:
`calculations/C0/PRF-PRIM/`, `proofs/C0/PRF-PRIM/`, `falsification/C0/PRF-PRIM/`, `graphs/C0/PRF-PRIM/`.

Key results: 2 new CERTIFIED lemmas (automorphism-projector commutation; L=Inc·Inc^T), 4 candidate
mappings FALSIFIED (τ=exp(-tL); Δ=I-P_ker(L) composition; Γ_graph conjugate to exp(-hL); Δ
reconstructible from τ+κ), 1 surviving 3-slot reduction within grammar A/D only (no 4-grammar
Γ_min established). C0's status in `registries/MASTER_CLOSURE_LAYERS_C0_C10.csv` is unchanged
(still OPEN THEOREM) — this execution adds computed sub-results underneath it, it does not close it.

---

See `registries/MASTER_CLOSURE_LAYERS_C0_C10.csv` for this layer's core target, what is already
preserved/calculated, its open structural questions, and its closure criterion. See
`registries/MASTER_OPEN_PROPOSED_NO_GO.csv` and `compiler/dag/supplementary_DAG_14_CRITICAL_FRONTIER.csv`
for this layer's specific open theorem obligations.

Further derivations executed against this layer get their own subfolder here named by their DER-ID,
following the schema in `results/workbooks/TOEV_DERIVATION_TEMPLATE.xlsx` and the folder layout
specified in the master directive Section VII.
