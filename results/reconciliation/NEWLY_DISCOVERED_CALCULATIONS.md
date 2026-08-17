# Newly Discovered Calculations — Phase 1.5 Corpus Expansion

Per directive Section 5: an exhaustive search of all 5 newly-uploaded files (including cell
values, and manual inspection of every worksheet in `UOC_ToE_Open_Closure_Master_v1.0.xlsx`, the
only file with genuinely new content — see `SYNCHRONIZATION_HISTORY.md` for why the other 4 add
no new cells beyond what Phase 1 already ingested via SOURCE-004) for executed symbolic
derivations, numerical experiments, benchmark calculations, falsification tests, no-go results, or
any other calculation not yet in the Phase-1 registries.

## Headline finding: no new executed calculation was found

`UOC_ToE_Open_Closure_Master_v1.0.xlsx` is, by its own stated purpose (`00_README`), a **"Master
closure program"** cataloging *"everything that remains open, partial, conditional, proposed,
version-sensitive, or not yet explicitly addressed."* Every one of its 30 sheets was read. None
contains a symbolic derivation, a numerical experiment with reproducible inputs/outputs, a
benchmark test executed against a graph/parameter family, or a falsification test that was
actually run. This was verified both by direct reading and by a keyword scan: status values across
all 30 sheets are dominated by `OPEN` (>540 occurrences) versus `CERTIFIED`/`CALCULATED`/`DERIVED`
(~300 occurrences combined) — and every occurrence of the latter three, checked by hand, refers
**narratively** to an EXISTING Phase-1 result (e.g. "Certified UCG spine" in `04_OPEN_MASTER_INTERNAL`
row INT-001), never to a new one computed inside this workbook.

**This is not a failure of the search — it is the correct reading of a document whose name is
literally "Open Closure Master."** Per governance rule ("do NOT classify something as OPEN merely
because it was not previously registered" / "if the document contains an actual executed
derivation, classify it accordingly") — the check was performed in the other direction too: no
row in this workbook was found that should be reclassified UP from OPEN to CALCULATED/DERIVED/
CERTIFIED. Every open item genuinely is open in its own source.

## What IS genuinely new (planning/registry material, not calculations)

| Category | Sheets | Content | Status classification |
|---|---|---|---|
| External ToE completeness benchmark | `01_TOE_BENCHMARK` (18 items, TOE-001..018) | What a complete theory must deliver (QG, SM recovery, UV completion, unitarity, etc.) mapped to UOC closure layers | ADMITTED EXTERNAL — reference checklist, not a UOC result |
| Successful-theory architecture comparison | `02_SUCCESSFUL_THEORIES` (8 theories, ST-001..008) | GR/SM/QCD/EW/QM/StatMech/Thermo/Newtonian core structure + what UOC must recover | ADMITTED EXTERNAL |
| External QG program comparison | `03_EXTERNAL_PROGRAMS` (8 programs, EXT-001..008) | String theory, LQG, asymptotic safety, CDT, causal sets, GUT, holography, asymptotic-safety+matter — what each achieved and what to reuse/avoid | ADMITTED EXTERNAL |
| Internal open-problem registry | `04_OPEN_MASTER_INTERNAL` (24 items, INT-001..024) | UOC-internal open closure problems by layer, **INT-001 = C0 primitive/grammar reconciliation** (directly PRF-PRIM's own obligation, restated) | OPEN (cross-references existing PRF-PRIM, not new) |
| Open bridges/theorems/proofs/equations/variables/simulations | `05`–`10` | Re-registers EXISTING BR-*, and NEW theorem targets (TH-001..~024), NEW numeric-ID proof obligations (PRF-001..~018, **different ID scheme** from the existing named PRF-PRIM/PRF-BORN/etc.), NEW open-equation targets (EQ-OPEN-001..~026), NEW open-variable targets (VAR-O-001..~022), NEW simulation *specifications* (SIM-O-001..~019, **none executed**) | All OPEN / PROPOSED, zero executed |
| Domain-specific closure sheets | `11`–`17` | SM closure, quantum gravity, cosmology closure, black-hole information, selection/uniqueness (`15_SELECTION_UNIQUENESS`, **SEL-001 = "Unique grammar... C0... OPEN"**, directly relevant to PRF-PRIM), compiler closure, biology/organization | All OPEN targets |
| Gap Matrix (own copy) + per-question closure audit | `18_GAP_164`, `25_NOT_YET_ADDRESSED` | Second copy of the 164-question matrix, PLUS a genuinely new **per-question closure-flag audit** ("NOT EXPLICITLY CLOSED" etc. for all 164 questions) | Directly extends Phase 1's own flagged gap — see below |
| Past-attempts recommendation log | `19_PAST_ATTEMPTS_RECOMMENDATIONS` (19 rows, ATT-001..019) | Retrospective on DTC, UDP, MDCL, ARBS/UPG, **TDIC (new proposal)**, SEIT, TNDS/NEDS, NCG route, H-003/004/006, COSMO-DYN, and 9 external benchmarks, each with a recommendation | Recommendations, not executed work — see TDIC below |
| External closure program | `20_EXTERNAL_CLOSURE_PROGRAM` | Further external-program detail | ADMITTED EXTERNAL |
| Theorem-target dependency DAG | `21_MASTER_CLOSURE_DAG` (30 edges, D-001..D-030) | A PARALLEL, theorem-target-granularity dependency graph (Parent→Child→Layer→Unlock Theorem), **D-001 = "Primitive reconciliation → Γ, C0, TH-001"** | New edges, all pointing at OPEN theorem targets — see Section 6/MASTER_DAG_vNEXT |
| Priority execution plan | `22_PRIORITY_EXECUTION_PLAN` (26 tasks, P0-01..P3-02) | Task-level plan with explicit stop/falsifier criteria, finer-grained than the existing `DAG_27_PHASE_EXECUTION_PLAN` (layer-level only) | Planning artifact, not executed |
| Research source register | `23_RESEARCH_SOURCE_REGISTER` (15 rows, SRC-WEB-001..015) | arXiv/PDG/CERN references used as external benchmarks | ADMITTED EXTERNAL INPUT (registered as EXT sources, see below) |
| Audit dashboard | `24_AUDIT_DASHBOARD` | Summary counts. Contains one VERIFIED reproducible arithmetic value: Ξ_UOC⁴ = (6.50×10⁻³¹)⁴ = 1.7850625×10⁻¹²¹ — **independently recomputed and confirmed exact** (this is arithmetic on the EXISTING PRED-004 value from `registries/MASTER_PREDICTIONS.csv`, not a new physical result) | VERIFIED (trivial arithmetic reproduction only, per Execution Firewall) |
| Standard equation targets | `26_STANDARD_EQUATION_TARGETS` (16 rows) | Textbook GR/SM equations UOC "must recover" | ADMITTED EXTERNAL (textbook equations) |
| Research synthesis | `27_RESEARCH_SYNTHESIS` (10 rows, R-001..010) | Web-research notes on external QG programs, with AI-search citation markers (e.g. "turn2academia36") | ADMITTED EXTERNAL, informal citation format |
| Standard completeness checklist | `28_STANDARD_COMPLETENESS_CHECKLIST` (27 items, CHK-001..027) | Generic ToE completeness checklist (state space, dynamics, symmetry, gauge, anomaly, unitarity, causality, Lorentz, renormalization, ...), all UOC status = OPEN | ADMITTED EXTERNAL checklist, applied |
| Candidate scorecard | `29_CANDIDATE_SCORECARD` | UOC/SEIT vs. 6 external QG programs across 7 criteria | ADMITTED EXTERNAL comparison |

## The one substantive new proposal: TDIC

`ATT-005` (`19_PAST_ATTEMPTS_RECOMMENDATIONS`) proposes **TDIC — "Typed Dependency Incidence
Complex"** as a candidate canonical substrate, explicitly recommended to **replace ARBS** ("ATT-004:
ARBS/UPG... Retire as canonical; preserve transferable results; re-derive ARBS-dependent claims in
TDIC"). TDIC is referenced in `00_README`, `03_EXTERNAL_PROGRAMS`, `12_QUANTUM_GRAVITY`,
`16_COMPILER_CLOSURE`, `19_PAST_ATTEMPTS_RECOMMENDATIONS`, and `22_PRIORITY_EXECUTION_PLAN` (task
P0-01: "Freeze canonical substrate... TDIC/UOC/MDCL; ARBS legacy only").

**No formal mathematical definition of TDIC (primitives, types, operators) was found anywhere in
the newly ingested corpus** — every occurrence is a name and a role ("proposed canonical
substrate," "implement as normalized table/executable substrate"), never a specification. Per
governance rule 2 ("do not import a desired answer") and the Execution Firewall (no new hypothesis
exploration), **TDIC is registered here as PROPOSED / NOT EXECUTED and NOT tested against
PRF-PRIM's findings.** See `C0_Impact` in the reconciliation workbook and Section 7 below.

## Relevant but not a "calculation": ARBS status conflict

`00_README` states plainly: **"ARBS is LEGACY ONLY. It is not canonical. Preserve non-ARBS results;
re-derive ARBS-dependent results in TDIC/UOC/MDCL."** This directly conflicts with SOURCE-004's own
characterization of ARBS ("the most formally rigorous component of the compiler architecture,"
Section 16 of the embedded UCG Specification text) and with `registries/MASTER_THEOREM_REGISTRY.csv`,
which carries 8 ARBS-derived theorems (RF-001..005, RK-001..003) at status **CERTIFIED**. This is a
genuine, material conflict — not a calculation — and is recorded in full in
`CONFLICTS_AND_VERSION_RESOLUTION.md` (CONFLICT-002). **No registry status was changed as a result
of this finding** (governance rule: never silently resolve a version conflict; never downgrade a
certified result without an executed falsification).

## Section 7 answer: does anything here strengthen, weaken, or change the scope of PRF-PRIM?

Per the directive's 8-way classification:

- **D. Changes the scope of the C0 result** — **YES.** `TH-001` (`06_OPEN_THEOREMS`) gives the
  formal target PRF-PRIM approximates: *"Show the canonical grammar is an equivalence class or
  strict reduction of **DTC/UDP/gradient/MDCL/NCG** realizations."* PRF-PRIM (executed in the prior
  phase) tested 4 systems: DTC (A), Physical/gradient (B), Computational B=(U,V,E) (C), Extended
  MDCL (D). It did **not** independently test **UDP** (the 16-phase canonical reduction protocol)
  or **NCG** (non-commutative geometry) as their own primitive-grammar realizations — PRF-PRIM used
  NCG only as an equation-source label (EQ-001..EQ-174's "NCG" section code), not as a primitive
  system. TH-001's target is therefore *broader* than what was executed. This does not invalidate
  any PRF-PRIM result; it clarifies that PRF-PRIM answered a subset of TH-001.
- **A/B/C (strengthens / provides missing lemma / provides counterexample)** — **NO.** No new
  lemma, proof, or counterexample relevant to Δ/τ/κ/Π/Θ/Ω was found.
- **E (resolves the Delta type mismatch)** — **NO.** Not mentioned or addressed anywhere in the new
  corpus.
- **F (establishes a previously missing mapping)** — **NO** new tested mapping. TDIC is a *proposed*
  additional structure, not a mapping between the 4 systems PRF-PRIM already tested.
- **G (creates a new contradiction)** — **NO** contradiction with PRF-PRIM's specific findings. (The
  ARBS conflict above is unrelated to PRF-PRIM's content.)
- **H (leaves C0 unchanged)** — **Effectively YES** for PRF-PRIM's actual computed content; its
  status, lemmas, and falsifications stand exactly as executed. Only the *stated scope* of the
  parent theorem (TH-001) is now more precisely known.

**Conclusion: PRF-PRIM is NOT rerun. Its result stands unmodified.** See `results/reconciliation/
PHASE_1_5_CORPUS_EXPANSION_REPORT.md` Section 7 for the full writeup and `CONFLICTS_AND_VERSION_
RESOLUTION.md` for the ARBS finding.
