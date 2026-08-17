# PHASE 0 REPORT — Independent Theory Reconstruction Experiment

**Scope: architecture only.** No physical derivation has been attempted. This report answers only
the 7 questions the master directive poses for Phase 0.

## Governing stance

The existing TOEv/UOC corpus is treated here strictly as **data**: a set of mathematical objects
with provenance, not as a validated theory. Every object below is described first by what it
mathematically *is*; its UOC project label (Delta, tau, Pi, Gamma, ...) is recorded only as
metadata. Nothing here assumes DTC, UOC, SEIT, ARBS, MDCL, UCG, UCCP, Γ=κ∘τ∘Δ, or any proposed
persistence functional / spectral cutoff / horizon-information law / particle-spectrum mapping /
universal functional — each is either re-derived from the underlying mathematics or explicitly
flagged as an unproven UOC claim.

## What mathematical content actually exists in the corpus?

**36 distinct, well-defined mathematical objects** were extracted (full detail:
`source_extract/ONTOLOGY_NEUTRAL_OBJECT_REGISTRY.xlsx`), spanning:

- A genuine, internally coherent **spectral graph theory core**: graph → adjacency/degree/incidence
  matrices → Laplacian → spectral decomposition → heat semigroup → spectral projector. This is the
  most complete, most rigorously connected chain in the whole corpus.
- **Admitted, not independently re-derived, chains into standard physics**: differential geometry
  (metric → connection → curvature → Einstein tensor), gauge theory (connection → curvature →
  Yang-Mills), quantum mechanics (Hilbert space → unitary evolution), thermodynamics (entropy,
  first/second law) — all standard mathematics, claimed by the source to be *recovered from* the
  spectral core, but that recovery step itself was not independently re-verified in this phase.
- A **categorical/functorial layer** (ARBS's recovery functor) whose own canonical status is
  disputed within the corpus itself (see below).
- **3 explicit gap markers** for content that does NOT exist anywhere in the ingested corpus:
  no independent Lagrangian/Poisson-bracket construction, no dark matter/inflation candidate, no
  quantum-gravity bridge beyond a single, partially self-rejected NCG/spectral-triple route.

## What is already calculated (vs. merely proposed)?

Of the 36 objects, status breakdown (`source_extract/ONTOLOGY_NEUTRAL_OBJECT_REGISTRY.xlsx`,
`Summary` sheet):

| Status (primary) | Count | Meaning |
|---|---|---|
| CALCULATED | 10 | Independently computed and verified in THIS repository (PRF-PRIM scripts) — the graph/adjacency/incidence/Laplacian/spectral/projector/automorphism core, plus the tetrahedron boundary-operator check |
| ADMITTED | 18 | Recovered/copied from the source corpus, not independently re-derived here (several carry qualifiers, e.g. "source claims CERTIFIED" or "CANONICITY DISPUTED") |
| OPEN | 6 | Explicitly unresolved in the source corpus itself (Born rule, Π_O functional, horizon normalization) plus the 3 explicit gap markers (no Lagrangian/Poisson-bracket construction, no dark matter/inflation, no independent quantum-gravity bridge) |
| CANDIDATE | 2 | UOC-proposed identifications not established as fact (fundamental constants as Seeley-DeWitt fixed points; the incidence-Dirac operator, itself partially rejected by its own source) |

**Only the spectral-graph-theory core is independently CALCULATED.** Everything downstream of it
(geometry, gauge, quantum, thermodynamics, cosmology) is ADMITTED — taken from the source corpus on
trust, not re-derived — which is exactly what Phase 1 onward of this experiment must now test.

## Which structures recur across domains?

12 candidate recurring structures were identified (`registries/CANDIDATE_PRIMITIVE_REGISTRY.csv`).
The three strongest recurrence signals:

1. **Self-adjoint operator + spectral theorem** (CAND-PRIM-001/005) — underlies the graph Laplacian,
   the candidate quantum Hamiltonian, and the candidate Dirac operator. The single most-repeated
   mathematical pattern in the corpus.
2. **Kernel/fixed-point subspace** (CAND-PRIM-004) — appears under *three different names* in the
   *same* source corpus: "persistence" (ker(L)), "universality" (RG-style fixed-point termination
   in the T0–T20 hierarchy), and the still-unexecuted "Fix(Γ)" target of DER-ORG-006. This is a
   genuine, non-trivial recurrence, not an artifact of relabeling.
3. **Connection + curvature pair** (CAND-PRIM-006) — the *identical* structural pattern (a
   connection whose curvature is its own commutator/exterior derivative) appears independently in
   general relativity (Levi-Civita/Riemann) and gauge theory (A_μ/F_μν). This is standard physics,
   not a UOC discovery, but its presence in the corpus is a legitimate recurrence candidate.

**One important negative finding:** CAND-PRIM-002 (one-parameter operator semigroup/group) recurs
in *two mathematically inequivalent forms* — the heat semigroup exp(−tL) (a contraction, PROVEN not
volume-preserving) and quantum unitary evolution exp(−iHt/ℏ) (a genuine unitary group). PRF-PRIM
already proved these are different object classes generated from the same operator family by a
sign choice (real vs. imaginary exponent). Recurrence of a *name* does not imply recurrence of a
*structure* — this is exactly the trap Phase 0's ontology-neutral approach is designed to catch.

## Which candidate primitives survive (Phase 0 only — Necessity testing is Phase 4, not yet run)?

None have been tested for necessity yet — that is explicitly Phase 4's job. What Phase 0 **can**
report, from PRF-PRIM's already-completed work (carried into this branch as prior evidence, not
re-litigated):

- **Delta** (as literally defined, a chain-complex boundary operator) is **type-inconsistent** with
  its own required role in the corpus's composed dynamics — proven concretely on a tetrahedron
  complex. This is carried forward as CAND-PRIM-008's central caveat.
- **Tau** has two non-interchangeable candidate realizations (automorphism vs. diffusion semigroup);
  only one (automorphism) satisfies tau's own stated definition.
- **Kappa/Pi** are CONDITIONAL — derivable from each other under one specific realization, not
  independently established as primitive.

None of this privileges or excludes UOC's own primitive set — it is prior, already-computed
evidence, registered here (CAND-PRIM-012) exactly as computed, for Phase 13's eventual comparison.

## Which mathematical bridges already exist?

Two genuinely **proven** (not merely admitted) bridges exist in this repository, both from
PRF-PRIM: **L = Inc·Inc^T** (graph substrate ↔ Laplacian, exact identity) and **automorphisms
commute with spectral projectors** (transformation-candidates ↔ constraint-candidates, general
proof). Every *other* bridge in the corpus (spectral → geometry, geometry → gauge, spectral →
quantum, spectral → cosmology) is **admitted from source, not independently re-verified** — this is
the single most important finding of Phase 0 for planning Phase 1 onward: the corpus's downstream
physics chains rest on bridge claims that have not yet been independently tested by this
experiment.

## What are the highest-leverage independent derivations?

Ranked by (a) how many downstream domains depend on it and (b) how tractable an independent test
is given only the tools already available in this repository:

1. **Test the spectral-to-geometry bridge independently** (KERNEL-CAND-001/002's central claim:
   does `L_N/h_N² → −Δ_g` actually hold as a continuum limit for concrete graph refinement
   sequences, or is it merely asserted?). This is the single highest-leverage open bridge — nearly
   every other ADMITTED object (geometry, gauge, cosmology) depends on it.
2. **Test whether a genuine quantum Hamiltonian (unitary, OBJ-019) can be independently constructed
   from the same Laplacian used for OBJ-007** (the contraction semigroup), without assuming they are
   "the same operator with i inserted" — this directly tests whether CAND-PRIM-001's recurrence is
   substantive or coincidental.
3. **Test KERNEL-CAND-003 (variational unification)**: do the 3 admitted action functionals
   (persistence cost, Einstein-Hilbert, classical Hamiltonian) share any actual mathematical
   structure beyond "some functional is stationary," or is this recurrence purely nominal? This
   is Phase 6's explicit question and can be attacked directly with the tools already in this repo.

## Architecture delivered

- `independent_toe/` — full 33-subfolder tree (Phase 0 scope: `README.md`, `MANIFEST.yaml`,
  `source_extract/`, `registries/`, `ledgers/` populated; all physics-domain folders created empty,
  awaiting Phase 1 onward).
- `source_extract/ONTOLOGY_NEUTRAL_OBJECT_REGISTRY.xlsx` — 36 objects, full schema.
- `source_extract/INDEPENDENT_SOURCE_INDEX.csv` — 11 sources (10 corpus + EXT admissions), density-rated.
- `registries/MATH_OBJECT_DEPENDENCY_NODES.csv` / `_EDGES.csv` — 36 nodes, 45 edges, 0 cycles.
- `registries/CANDIDATE_PRIMITIVE_REGISTRY.csv` — 12 recurring-structure candidates.
- `registries/CANDIDATE_COMMON_KERNEL_REGISTRY.csv` — 6 candidate kernels (including the explicit
  null hypothesis "no common kernel exists").
- `registries/MASTER_INDEPENDENT_TOE_DAG_NODES.csv` / `_EDGES.csv` — 54 nodes (36 objects + 12
  candidate primitives + 6 candidate kernels), 78 edges, **0 cycles (verified)**.
- `ledgers/INDEPENDENT_DERIVATION_LEDGER.csv` — empty (header only), ID scheme reserved (`IDER-*`).
- `ledgers/TOEV_IDER_{DERIVATION,CALCULATION,PROOF,FALSIFICATION}_TEMPLATE.xlsx` — 4 templates,
  ready for Phase 1 onward use.

## What Phase 0 explicitly did NOT do

Per the master directive's execution order: no physical derivation (Phase 1 onward), no necessity
testing of candidate primitives (Phase 4), no kernel selection (Phase 5), no comparison against
UOC/SEIT/ARBS (Phase 13, deliberately last), no `THEORY_OF_EVERYTHING_CANDIDATE.md` (Phase 14).
Nothing in the canonical UOC closure records (`registries/*.csv` outside `independent_toe/`,
`compiler/dag/*.csv`, `derivations/C0/`, etc.) was read for anything beyond extraction, and nothing
there was modified.

**Waiting for authorization to proceed to Phase 1 (reconstruct established physics, domains A–K).**
