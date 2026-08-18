# Governing-Corpus Reconstruction

**Mode:** Document-Derivation (reconstruction only — no new derivations, no reconciliation-by-
invention, no extension of the theory) &nbsp;|&nbsp; **Date:** 2026-08-17

**Scope:** five governing documents, supplied as the primary corpus for this analysis and treated
as authoritative over any prior extraction of the same material elsewhere in this repository:

| ID | File | SHA-256 (short) |
|---|---|---|
| D1 | Combined_Compiler_Theories_Whitepaper.docx | `a85fe31a…` |
| D2 | CVR001_Compiler_Verification_Report.docx | `a34e74ae…` |
| D3 | Distinction_to_Persistence_Analysis.docx | `b2b09cbc…` |
| D4 | SEIT_Updated_Whitepaper.docx | `11ba6f28…` |
| D5 | SEIT_Compiler.docx | `91125b6d…` |

Full text extracted verbatim (python-docx, paragraph+table order preserved) to
`source_records/spreadsheets/GOVERNING_CORPUS_DOCX/*.md`. Every claim below cites a document and
section; anything this reconstruction could not trace to the text is marked as such rather than
silently filled in (§14). Backing data tables: `governing_corpus/registries/`,
`governing_corpus/dag/`, `governing_corpus/matrices/`.

**Relationship to this repository's other work:** D1 (in part) was previously accessible in this
project only as raw-text paragraph/table extraction embedded inside the UOC_ToE spreadsheet corpus
analyzed in earlier phases (`source_records/.../UOC_ToE_Canonical_Bridge_Closure_Execution_v2.0/`).
This reconstruction works from the **complete original documents**, is more precise than that
earlier embedded extraction, and supersedes it as a citation source for D1's content. This report
does not modify, extend, or re-run any of the computational work done in `derivations/C0/`,
`independent_toe/`, or `results/PHASE_2_C0_REPORT.md` — it is a standalone reconstruction of what
five specific documents claim, per the governing directive's explicit restriction.

---

## 01. Corpus Inventory

Full detail: `governing_corpus/registries/SOURCE_INDEX.csv`.

| Doc | Internal structure | Genre |
|---|---|---|
| D1 | Part 0 (Compiler Certification Registry, a 5-state taxonomy: Certified/Candidate/Open/Retired/Research Objective) + Part I (*This from That* — DTC grammar, graph-category compiler) + Part II (Universal Derivation Protocol, 16 phases + Test Field Manual + Derivation Manual) + Part III (Organizational Hierarchy, worked/textbook) + Part IV (MDCL v1.0/v2.0 validation campaign + Lorentzian program) + Part V (Universal Organizational Foundation, algebraic substrate for one grammar) | Primary theory text, internally self-auditing for Parts IV–V only |
| D2 | 6-dimension formal audit (Existence, Dependency Completeness, Acyclicity, Certification Consistency, Registry Ownership, External Ancestry) of a 30-row Master Certification Table + 8-item Open Problems Register + Conditional Certification Tracker | Independent audit report of an infrastructure whose object names overlap D1 Part IV/Part I but are not textually confirmed identical |
| D3 | Stage-by-stage data-analysis/visualization specification for an 18-poster series (QM, Universal Laplacian Compiler pipeline, cosmology, brane-bulk, TOEv/SEIT/TEDS/URS, far future) | Analytical/visualization companion, not a derivation document |
| D4 | Prefatory Note (explicit revision purpose) + two-layer architecture (USC/SEIT) + a 40-row self-audit derivation matrix with a 5-code status system + explicit retraction record + ranked open-research targets | Self-critical audited revision — the most epistemically disciplined document in the set |
| D5 | 13-phase "Universal Compiler Architecture" (Born rule → inverse spectral problem) + 3 falsifiable predictions + 5 self-declared open problems + Rosetta Grammar | Earlier, unaudited, high-confidence presentation — superseded on specific points by D4 |

**Chronology (established from content dependency, not from date fields):** D5 precedes D4's audit
(D4 explicitly retracts D5-specific claims). D4 explicitly post-dates and partially revises D1. D2
and D3's position relative to D1/D4/D5 is not stated by any document and is not inferred here.

---

## 02. Document Authority / Provenance Matrix

For every document, this reconstruction records what kind of authority it claims for itself —
never a stronger authority than the document claims for itself.

| Doc | Self-declared epistemic posture | Verification protocol stated? | Authority over other docs |
|---|---|---|---|
| D1 | Parts I–III: prose-level hedging ("remains conjectural"). Parts IV–V: formal 5-state CCR taxonomy with an explicit 3-stage verification protocol (symbolic derivation → canonical-case check → random/numerical check), Part 0 §0.2. D1 §12 (Part I conclusion) explicitly: "central claims... remain open mathematical conjectures rather than established results." | Yes, for Parts IV–V only (Part 0 §0.2) | None claimed over D2/D3/D4/D5 |
| D2 | Formal audit report; verdicts are Pass/Fail per dimension, sourced from MCT/MCL/POL ledgers it treats as given inputs, not as its own theory | Yes — the audit *is* the protocol (6 dimensions, §2–§7) | Audits infrastructure whose relationship to D1 is name-overlap only (§11 below); claims no authority over D1's actual mathematical content |
| D3 | No explicit certification language; presents equations and protocols as given, for the purpose of specifying *how to analyze/visualize* them | No | None |
| D4 | Explicit self-declared authority over its own predecessor claims: "This document updates the Combined Compiler Theories Whitepaper... Items that were previously mislabeled as derived are now accurately labeled as open" (Prefatory Note) | Yes — 5-code status system (🟢🟡🔴⚫🔵), Sec1 | Explicit, scoped authority over D1 (λ_c and SEIT-Layer-II items only) and over D5 (specific named retractions, §11 below) |
| D5 | Confident derivation language throughout ("derived, not postulated"); Sec XIII names 5 open problems but does not flag any of its main-text claims as provisional | No explicit multi-stage protocol; Sec XIII is a self-declared open-problems list, not a status audit of the main text | None claimed; superseded by D4 on specific points (§11) |

---

## 03. Canonical Object Registry

Full backing data: `governing_corpus/dag/GOVCORPUS_DAG_NODES.csv` (44 objects). Selected
highest-leverage objects, cited to source:

| Object | Definition (verbatim/near-verbatim) | Source | Status per source |
|---|---|---|---|
| Critical Attractor Set 𝒦crit | Fixed point of the compiler's gradient-descent optimization loop, conditional on Strict Convexity λ_min(H)≥m>0 | D1 §3.2 | CANDIDATE (conditional on stated convexity assumption) |
| Persistence threshold λ_c | The root of a restoration-to-degradation ratio; "a full derivation of λ_c from the spectral data of D_Gn remains an open problem and is not claimed here" | D1 §10.2 | OPEN (D1's own words) |
| Γ(λ) = Restoration(λ)/Degradation(λ) | Candidate closure object for λ_c; λ_c defined by Γ(λ_c)=1 | D4 §2.2 | PARTIAL — "projection integral not yet evaluated" |
| Π₀ = (δ_spec − λ_c)/σ | Persistence order parameter | D3 §IX | OPEN (depends on the same unresolved λ_c) |
| Ω (Master Attractor) | lim_{n→∞} exp(−nβ(D−A))·U | D5 §II.4, §XII | Stated as derived in D5; D4 does not independently confirm this specific limit object (only the general "Ω attractor" row, marked Derived with "formal convergence proof still needed") |
| ARBS-DEF-001 | Object with bipartite/shell structure; certified definition, two locked theorems (bipartite reciprocity, shell nilpotency) both OPEN | D2 §2–§8 (OP-001, OP-002) | CERTIFIED (definition) / OPEN (both governing locks) |
| K-DEF-001 (Constraint Core K) | Referenced but not defined in the text available to this reconstruction | D2 §3 | DEFINED (per D2's own ledger); definitional content not recovered |
| CMRC-001…019 chain | Configuration domain → worldsheet → Polyakov action → Virasoro algebra → central charge → β(g)=0 → vacuum Einstein Rμν=0 | D1 Part IV §1 | CERTIFIED (VAL-001), with 3 explicit scoping refinements (§09 below) |
| MDCL-0001 | Typed compiler object 𝔐 = (V, E, ⪯𝔐, ∘), built bottom-up from UGAS…UTS | D1 Part V §8 | CERTIFIED (framework); explicitly *not* shown identical to Part IV's MDCL object (§9 caveat) |
| Persistence Cost Functional C_Π | ∫_T[−τ²(∂²S/∂y^a∂y^b)y′_a y′_b + 2τ I_F(ρ‖y)]dt | D5 §VI.1 (eqn 6.1), independently confirmed "Derived, Fisher metric choice justified" by D4 §1 | DERIVED (agreement across D4 and D5, a genuine cross-document convergence — see §11) |
| Universal Persistence Field Equation | y″_c + Γ^c_{ab}y′_a y′_b = −g^{ca}∇_a I_F | D5 §VI.2 (eqn, boxed) | Both D5 ("Derived by full Euler-Lagrange variation") and D4 ("Field equation SEIT.1 \| Derived \| Full derivation complete") independently agree — genuine convergence |
| G_SM = SU(3)×SU(2)×U(1) | Claimed unique minimal anomaly-free fixed point via N_c=3 from three independent anomaly-cancellation conditions | D5 §VIII.2 | D5: "derived, not postulated." D4 §1: **Open** — "Inclusion asserted, not derived; E8/SO(10) alternatives not ruled out." **SUPERSEDED** (§11) |

---

## 04. Primitive / Grammar Reconstruction

Full data: `governing_corpus/registries/PRIMITIVE_GRAMMAR_REGISTRY.csv` (11 distinct grammars/
primitive-sets recovered). This is the single largest reconstruction finding of this pass: the
corpus does **not** contain one primitive grammar. It contains at least eleven distinct, mostly
unreconciled proposals, several of which the source documents themselves explicitly refuse to
adjudicate between. None is merged here.

| ID | Primitives | Composition | Source | Reconciliation status per source |
|---|---|---|---|---|
| GR-01 | Δ, τ, κ, Π (DTC) | Γ ≡ κ∘τ∘Δ | D1 Part I §9 | — |
| GR-02 | D, T, C (+Π later) | Γ = C∘T∘Δ (same order as GR-01) | D1 Part IV Preface | "not claimed here to be formally identical" to GR-01 |
| GR-03 | Δ, τ, κ, Θ, Π, Ω | not stated as a single composition | D1 Part IV §7.2 | Δ,τ,κ,Π "directly identified" with GR-01's; "This paper does not adjudicate between the three versions [GR-01/02/03]" |
| GR-04 | Σ₀={D,T,C,Π} | free algebra, not a single Γ formula | D1 Part V | Formalizes GR-02's *symbol set* only; explicitly **not** shown identical to GR-01 or GR-03; not shown identical to Part IV's own MDCL object either |
| GR-05 | Δ, R, T, C, Π (5, "TOEv") | dO/dt = T(O) − ∇·J(O) + C(O) | D3 §VII.A | No cross-reference to GR-01…04 found in any document |
| GR-06 | ∇, κ, 𝒪, F, W_c, Π, Ψ, E (8-stage, revised from a 10-stage Δ-based chain) | linear pipeline | D1 Part III §2 | "This paper does not adjudicate between them [GR-06 and GR-01]; a reconciliation, if one exists, is future work" |
| GR-07 | (Σ,Γ,Π) SEIT.0 | chain Σ→Γ→Π→A→σ(A)→Θ→g→R→ℱ | D4 §0 | Explicitly labeled "proposed primitives"; Γ here is a *generator*, a different object from GR-01's composed Γ (symbol collision, not identity) |
| GR-08 | Δ, τ, κ (Rosetta Grammar) | (Δ,τ,κ) ⇒ 𝒜 ⇒ Π | D5 §XIV | No formal identification with GR-01 stated; Π omitted from the active composed triple |
| GR-09 | Γ(λ) = Restoration/Degradation | λ_c defined by Γ(λ_c)=1 | D4 §2.2 | Fourth distinct use of the symbol Γ in this corpus |
| GR-10 | PR-001…004 | not stated in text available | D2 | Probable, **unconfirmed** overlap with GR-01/02 (name-overlap only) |
| GR-11 | Object, Relation, Operator, Constraint, State (UDP) | Object→State→Relation→Operator→Transformation→Constraint→Dynamics→Persistence→Equation→Theory | D1 Part II Phase I | D1's own Conclusion: Parts I and II "independently arrive at a discrete-to-continuum compiler picture... Part I builds it from a pointed graph category, while Part II builds it from operator algebras and category theory" — explicitly parallel, not shown equivalent |

**Symbol collision, flagged not resolved:** the letter **Γ** denotes four distinct objects across
this corpus with no source-stated identification between any pair: (1) GR-01's composed grammar
operator κ∘τ∘Δ; (2) GR-06's retracted-within-D1 "Generative Capacity" primitive; (3) GR-07's
evolution *generator*; (4) GR-09's scalar function of an eigenvalue. Treating any two of these as
"the same Γ" would be an unauthorized silent merge.

---

## 05. Operator and Transformation Registry

Every operator below is used consistently within its own source document; no cross-document
identification is asserted unless the source states one.

| Operator | Formula | Domain→Codomain | Source | Role |
|---|---|---|---|---|
| Graph Laplacian L | L = D − A | R^n → R^n | D1, D3, D4, D5 (shared vocabulary, not shown to be literally the same construction object in every document) | Central spectral generator across all five documents |
| Heat kernel / semigroup | e^{−tL} = Σ e^{−tλ_n}ψ_nψ_n^T | R^n → R^n | D1 §1.3 (DEC form), D3 stage 6, D4 canonical spine, D5 §III | Diffusion bridge, "connects graph Laplacian to continuum spacetime Laplacian" (D5) |
| Discrete exterior derivative d, codifferential δ, Hodge star ⋆ | δ = ±⋆d⋆ | Ω^k(G_n) → Ω^{k±1}(G_n) | D1 §1.3, §2.2 | DEC operator algebra underlying the compiler's Discrete Geometry Category |
| Discrete Dirac operator 𝒟 | Assembled from bipartite γ-operators and the discrete Lie derivative ℒ_e | spinor bundle → spinor bundle | D1 §5.1–5.2 | Self-adjointness proven via Discrete Cartan Identity (§09 below) |
| Regeneration operator R (Kraus form) | R(ρ) = Σ_k M_kρM_k†, Σ_k M_k†M_k = I | density-matrix space → itself | D5 §VII.2 | 4 axioms stated (non-unitary, monic identity, strict contraction, sub-unitary spectrum); convergence R^n(X)→Δ* via Banach fixed-point |
| Fokker-Planck operator ℒ* | ∂_tP = ℒ*P = −∇·(P∇log P_ss) | probability densities → probability densities | D3 stage 8 | Persistence/dissipation dynamics |
| Connection Γ^a_{bc}, Riemann/Ricci/Einstein tensors | Standard differential-geometry formulas, computed from a *spectrally-derived* metric g_μν | tensor fields on the emergent manifold | D1 §7.4, D3 §IV.A, D5 §IV.2 | Curvature hierarchy; Einstein tensor "selected, not merely written down, by an explicit constraint set" (D1 §7.4) |
| Continuization functor 𝔓𝒯 = C_e∘C_π∘C_t∘C_p | 4-gate composition | discrete configuration space → physically observed reality | D1 §11 | "the precise sense in which §9–11 are a refinement of, rather than an alternative to, the compiler pipeline of §1" |

---

## 06. Master Dependency DAG

Full data: `governing_corpus/dag/GOVCORPUS_DAG_NODES.csv` / `GOVCORPUS_DAG_EDGES.csv` (44 nodes, 36
edges, **0 cycles** — audit: `governing_corpus/dag/GOVCORPUS_DAG_CYCLE_AUDIT.txt`). Every edge
carries an explicit source-quoted justification in the CSV; none was added on inferred relatedness
alone. High-level shape:

```
D1 Pointed Graph Category ──R(refinement)──► Discrete Geometry Category ──► Optimization Operator ──► 𝒦crit
        │
        ├──(DTC-level description)──► GR-01 Γ=κ∘τ∘Δ
        │                                    │
        │                    (extended, 6-primitive) ──► GR-03 (MDCL v2.0) ──► graph-spectral Einstein tensor (vacuum)
        │                                                                              │
        │                                                                   (Layer VII, matter coupling) ──► OPEN target set
        │
        ├──(compiler instantiation)──► CMRC-001..019 ──► VAL-004 (QM) ──► VAL-005 (Hamiltonian) [shared variational core]
        │
        └──(algebraic foundation, Σ0={D,T,C,Π} only)──► UGAS→UGCT→UGUP→UGNT(open)→UGIT→UOLS→UTS→MDCL-0001

D2  PR-001..004 ──► TH-PR-005 ──► OR-001 ──► THERMO-TAX chain
        │
        ├──► K-DEF-001 ──► TH-K-001 (open)
        └──► ARBS-DEF-001 ──► {TH-ARBS-001A, TH-ARBS-001B} (both OPEN, block RF-001..004)
                                        │
                                RF-001..004 (Conditional-Certified) ──► CMRC-CHAIN-001, VAL-004, VAL-005
                                        (inherited conditional dependency, D2's own flag)

D4  SEIT.0 (Σ,Γ,Π) ──► canonical spine (Phase XII) ──► C_Π / SEIT.1 ──► Γ(λ) ── λ_c(OPEN) ──► [entire downstream closure chain, D4 §3]

D5  G=(V,E) ──► Heat Kernel Bridge ──► Spectral Metric Formula ──► Persistence Field Equation
                                                                          (independently confirmed by D4 — cross-document AGREEMENT)
```

**Cross-document links present in the DAG (not internal to any one document):** D1↔D3↔D4 all
converge on the *same* open λ_c object without ever fully identifying their own respective
definitions of it as identical (edges E-25, E-29 in the CSV); D4↔D5 share the persistence field
equation as an independently-confirmed result (edge E-33); D5's Sec VIII.2 gauge-derivation node is
directly superseded by D4's audit (edge E-35).

---

## 07. Morphism / Translation Matrix

Full data: `governing_corpus/matrices/MORPHISM_TRANSLATION_MATRIX.csv` (11 pairs, covering the
grammars of §04). Classifications used strictly per the directive's taxonomy — most pairs classify
as **OPEN** or **UNDEFINED**, which is itself the correct, source-grounded finding, not a gap in
this reconstruction:

| Pair | Classification | One-line basis |
|---|---|---|
| GR-01 ↔ GR-02 | OPEN | Same composition order, "not claimed... to be formally identical" |
| GR-01 ↔ GR-03 | EMBEDDING (partial) | 4 of 6 primitives "directly identified" by source text |
| GR-02 ↔ GR-04 | UNDEFINED | Symbol-set match explicitly not treated as object identity by D1 itself |
| GR-01 ↔ GR-04 | OPEN | "this part does not attempt it" (D1 Part V §9, verbatim) |
| GR-03 ↔ GR-04 | OPEN | Same as above |
| GR-01 ↔ GR-06 | OPEN | "This paper does not adjudicate between them" (D1 Part III §5) |
| GR-05 ↔ {GR-01,02,03} | UNDEFINED | No claimed relationship found in any source |
| GR-08 ↔ GR-01 | UNDEFINED | Surface notational overlap only, no identification statement |
| GR-07 ↔ {GR-01,GR-09} | TYPE MISMATCH | Same symbol Γ, three distinct referents |
| GR-10 ↔ {GR-01,GR-02} | UNRESOLVED IDENTIFICATION | Name-overlap evidence only |
| GR-11 ↔ GR-01 | OPEN | "independently arrive at" — explicitly parallel per D1's own Conclusion |

No pair in this corpus is classified EXACT, ISOMORPHIC, or (unconditionally) EQUIVALENT. This is a
direct, load-bearing finding: **the corpus does not establish that any two of its primitive
grammars are the same grammar.**

---

## 08. Invariant and Preservation Matrix

| Invariant | Statement | Source | Status |
|---|---|---|---|
| Chain-complex nilpotency | d(dΩ) = ∂(∂Ω) = ∅ (Δ's own defining condition) | D1 §9.1 | DEFINED as an axiom of Δ; not independently re-derived in this document set |
| Liouville / volume preservation | τ's defining condition: preserves the phase-space volume element | D1 §9.1 | DEFINED as an axiom of τ. **Cross-reference to this repository's own prior computational work**: `derivations/C0/PRF-PRIM/04_tau_liouville_and_kappa_commutation.py` independently *falsified* τ=exp(−tL) against exactly this Liouville condition (FALS-001) — that finding is prior computational work on the spreadsheet corpus, not part of this document-only reconstruction, and is noted here only as a pointer, not re-asserted as a claim of these 5 documents |
| Idempotency | P_κ² = P_κ (κ's defining condition) | D1 §9.1 | DEFINED as an axiom |
| Bianchi identity | ∇^μG_μν = 0 | D1 Test Field Manual §8, D3 §IV.B | Standard differential-geometry identity, cited as a falsification-diagnostic invariant, not independently re-derived |
| DAG acyclicity | GDG = Graph(MCT, MCL) has no backward edges across topological layers | D2 §4 | PASS — explicit 14-layer topological assignment given and checked |
| Certification-level inheritance | COR-MDCL-002: certification level of a result is bounded above by the minimum certification level of its dependency ancestry | D2 §5 | PASS with one presentation note (CMRC-CHAIN-001 inherits a conditional dependency via RF-004 despite being marked Certified itself) |
| Closure-operator termination | Every equivalence class of 𝒢 contains exactly one normal form (NF idempotent + irreducible) | D1 Part V §4 (UGNT) | CONDITIONAL — "certified as a framework; the termination and confluence theorems themselves remain open" |
| Data-processing inequality | S(R(ρ_1)‖R(ρ_2)) ≤ S(ρ_1‖ρ_2) | D5 §IX | Stated as the mechanism deriving the thermodynamic arrow of time from spectral structure; standard inequality, not independently re-derived here |

---

## 09. Equation-by-Equation Derivation Recovery

Four of the corpus's most completely worked derivations, reconstructed in the required
INPUTS→…→STATUS form. Each traces every step to its source; nothing here is a
`RECONSTRUCTIONAL FORMALIZATION` (no undocumented equation was needed to state any of these
precisely).

### (a) CMRC / VAL-001 — Virasoro central charge and the critical dimension

```
INPUTS        Embedding field X^μ: Σ → ℳ (worldsheet Σ, target ℳ, flat background g_μν=η_μν)
DEFINITIONS   Pullback metric h_ab = ∂_aX·∂_bX  (Grammar: Distinction ⊗ Transformation)
ASSUMPTIONS   Flat target space g_μν=η_μν (explicitly flagged, D1 §1.3)
OPERATORS     Area functional A[Σ]; auxiliary intrinsic metric γ_ab (removes the Nambu-Goto square root)
TRANSFORMATION  Vary Polyakov action S_P[X,h] w.r.t. X^μ (fixed γ) → free wave equation
              Vary S_P w.r.t. γ_ab → worldsheet stress tensor T_ab
INVARIANT     Require T_ab = 0 identically (Constraint primitive) → classical Virasoro constraint surface
DERIVATION    Fourier-mode expansion of the constraint → classical Virasoro generators L_n;
              quantization → central extension [L_m,L_n]=(m−n)L_{m+n}+(c/12)m(m²−1)δ_{m+n}
              Ghost-elimination (no negative-norm physical states) fixes c to a specific value
RESULT        Critical spacetime dimension D=26 (bosonic string)
STATUS        CERTIFIED (D1 Part 0 §0.5 CCR ledger), with 3 explicit scoping refinements: (i) c=26 is
              bosonic-specific, not a universal compiler invariant; (ii) flat-background assumption
              stated explicitly, not hidden; (iii) the chain to General Relativity runs through
              β(g)=0 → R_μν=0 as a downstream consequence, NOT a direct algebraic output of the
              Virasoro algebra alone — this distinction is the source's own certification refinement
```

### (b) MDCL v2.0 — Einstein tensor selection (graph-spectral route)

```
INPUTS        Organizational graph G=(V,E,W), Laplacian L=D−A
OPERATORS     Spectral decomposition {λ,ψ}; heat kernel; diffusion distance d(i,j)
TRANSFORMATION  Continuum limit asserted to recover metric g_μν; Levi-Civita connection and
              Riemann/Ricci curvature follow by standard differential geometry
INVARIANT     Constraint set: symmetric, rank-2, covariant, divergence-free — applied to the space
              of tensors built from R_μν and R
DERIVATION    Selection-by-constraint singles out exactly one combination: G_μν = R_μν − ½g_μν R
              (D1 §7.4 calls this "in substance, the classical Lovelock-style uniqueness argument")
RESULT        Vacuum Einstein tensor, recovered as a SELECTED object, not merely postulated
STATUS        CERTIFIED (vacuum only). Layer VII (coupling to a matter source T_μν, the full
              G_μν+Λg_μν=8πG/c⁴·T_μν, the geodesic equation, and the Newtonian limit) is explicitly
              labeled by the source itself: "Target — not yet recovered" for all 5 listed objects
              (D1 §7.5 table) — this reconstruction preserves that boundary exactly as stated
```

### (c) D5 — Universal Persistence Field Equation (Euler-Lagrange of C_Π)

```
INPUTS        Persistence cost functional C_Π[y] = ∫_T[−τ²(∂²S/∂y^a∂y^b)y′_ay′_b + 2τI_F(ρ‖y)]dt
DEFINITIONS   Fisher transport cost I_F; Hessian metric g_ab = −(∂²S/∂y^a∂y^b)
TRANSFORMATION  Full variation δC_Π, integration by parts on the kinetic term
INVARIANT     Christoffel identification Γ_{cab} = ½(∂g_{ca}/∂y^b + ∂g_{cb}/∂y^a − ∂g_{ab}/∂y^c)
DERIVATION    Collecting terms yields the field equation directly (D5 §VI.2, eqn boxed in source)
RESULT        y″_c + Γ^c_{ab}y′_ay′_b = −g^{ca}∇_aI_F ("reduces exactly to the Einstein geodesic
              equation" when I_F=0)
STATUS        DERIVED — and this is a genuine CROSS-DOCUMENT AGREEMENT, not merely D5's own claim:
              D4's independent audit (§1 matrix) marks the same object "Field equation SEIT.1 |
              Derived | Full derivation complete" without citing D5's derivation steps directly.
              Two independently-authored status judgments concur on this one specific result.
```

### (d) D1 — Discrete Cartan Identity and self-adjointness of the discrete Dirac operator

```
INPUTS        Hodge adjoints d, δ (⟨dα,β⟩=⟨α,δβ⟩); contraction adjoint (e∧·)†=ι_e
OPERATORS     Discrete Lie derivative ℒ_e; bipartite gamma operators γ^a_n (Hermitian, (γ^a_n)†=γ^a_n)
TRANSFORMATION  Evaluate the inner-product sum over arbitrary test cochains α, β for both identity
              components, then sum
DERIVATION    By Riesz representation, the summed identity holds exactly, proving the Discrete
              Cartan Identity
RESULT        Self-adjointness of the discrete Lie derivative (ℒ_e†=ℒ_e); combined with Hermitian
              γ's, this completes self-adjointness of the discrete Dirac operator
STATUS        CERTIFIED — full symbolic derivation given in the source text (D1 §5.1); this
              reconstruction traced every step to the source and introduced no additional formula
```

No `RECONSTRUCTIONAL FORMALIZATION` labels were needed for these four; every equation used is
either given verbatim in a source document or is a direct restatement (e.g. Bianchi identity,
idempotency) that the sources themselves invoke by name without restating.

---

## 10. Status Ledger

Full data: `governing_corpus/registries/STATUS_LEDGER.csv` — **88 items**, transcribed as close to
verbatim as possible from each source's own status system (D4's 🟢🟡🔴⚫🔵 audit matrix, D1's
Certified/Candidate/Open/Retired/Research-Objective CCR ledger, D2's Open Problems Register and
Conditional Certification Tracker, D5's self-declared open problems, and D5→D4 retraction records).
This registry is not this reconstruction's invention — every status value is a direct transcription
of a status the corpus already assigned to itself. Summary counts:

| Status class | Count | Dominant source |
|---|---|---|
| DERIVED/CALCULATED (with residual caveats in most rows) | 20 | D4 audit matrix |
| CONDITIONAL/CANDIDATE/PARTIAL | 18 | D4 audit matrix, D1 CCR ledger, D2 conditional tracker |
| OPEN | 32 | D1 CCR ledger, D2 Open Problems Register, D4 audit matrix, D5 self-declared |
| RETIRED | 3 | D1 CCR ledger (Lorentzian program's 3 closed approaches) |
| SUPERSEDED/RETRACTED | 4 | D4's explicit retractions of D5 content |
| UNDECIDABLE (structural) | 1 | D4/D5, citing Cubitt–Perez-Garcia-Wolf 2015 |
| ADMITTED EXTERNAL INPUT | 1 (ħ,c,G_N as a group) | D4 audit matrix |

**Governance note carried through every row:** no status in this ledger was promoted, demoted, or
re-derived by this reconstruction. Where a document's own status language was ambiguous (e.g. D1's
"Derived, formal convergence proof still needed" for the Ω attractor), the full qualifying phrase
was preserved rather than collapsed to a bare "Derived."

---

## 11. Cross-Document Consistency Matrix

Full data: `governing_corpus/matrices/CROSS_DOCUMENT_CONSISTENCY_MATRIX.csv` (10 pairs). The one
**ACTUAL CONFLICT** found, and its resolution basis:

> **D4 vs D5 — ACTUAL CONFLICT, explicitly resolved by supersession.** D4 explicitly names and
> retracts four specific claims that appear with full, unqualified confidence in D5: (1) λ_c=λ₁
> (Fiedler value) — retracted, "gives Π = {zero mode only} — the vacuum... the entire downstream
> cascade collapses"; (2) the 166.48 Hz monochromatic gravitational-wave prediction — retracted,
> "conflicts with fuzzy-DM physics. Dropped"; (3) the ~135 pc dwarf-galaxy soliton core radius
> prediction — retracted, "inconsistent with observed diversity"; (4) the SU(3)×SU(2)×U(1)
> anomaly-cancellation derivation, which D5 calls "derived, not postulated" but D4's audit marks
> **Open** ("inclusion asserted, not derived; E8/SO(10) alternatives not ruled out"). D4's own
> Prefatory Note frames itself explicitly as the correcting document. This reconstruction follows
> D4 on every one of these four points and does **not** apply D4's correction to any D5 content D4
> does not itself touch (e.g. the Heat Kernel Bridge, the Spectral Metric Formula, and the
> Euler-Lagrange field-equation derivation of §09(c) above — D4 independently *confirms*, rather
> than revises, that last one).

All other pairs classify as OPEN / DIFFERENT REPRESENTATION / UNRESOLVED-but-probable overlap
(D1↔D2), or NO OVERLAP ESTABLISHED (D2↔D3, D2↔D5) — no other pair rises to the level of a
genuine, source-documented contradiction.

---

## 12. Closure Architecture

Three closure architectures coexist in this corpus, unreconciled with each other, exactly as
Part I of this reconstruction found for the grammars themselves. None is invented here; all three
are the documents' own stated systems.

**(a) D1 Part 0's Compiler Certification Registry (CCR)** — governs Parts IV–V only:
`input → symbolic derivation → canonical-case verification → random/numerical verification →
Certified`, with Candidate/Open/Retired/Research-Objective as the non-terminal states. Certification
condition = passing all three named checks in order (§0.2). Downstream dependency = the CCR ledger
itself (§0.5), which this reconstruction transcribed in full into the status ledger.

**(b) D2's MCT/MCL/POL audit architecture** — a Defined→Proven→Certified→Verified 4-level scale
(named in D1 §5 as MDCL's own certification discipline, and independently audited by D2), governed
by explicit dependency-ancestry columns, a proven acyclicity theorem (TH-MDCL-002), and a
certification-inheritance rule (COR-MDCL-002: a result's certification level is capped by its
weakest ancestor). Closure criterion for any given row = all six of D2's own audit dimensions
passing. D2's audit does not certify new mathematics; it certifies that the *bookkeeping* of an
already-built registry is internally consistent.

**(c) D4's 5-color derivation-audit matrix** — Derived/Partial/Open/Undecidable/Empirical, applied
specifically to the SEIT Layer-II physical-emergence hypothesis. Closure criterion = an object's
row has no open dependency in the "Resolution / Open Problem" column. D4's own §3 ("The Closure
Chain") states explicitly, in dependency order, what becomes derivable once λ_c is closed — this is
the *only* place in the corpus where a closure chain is stated as an ordered, numbered sequence of
"what becomes derivable next," and it is preserved verbatim in §16 below.

**No single unified closure layer spans all three.** D1's Part IV §7.5 example is instructive: the
vacuum Einstein tensor is CCR-Certified (system (a)) while the same object's coupling to matter
(Layer VII) is explicitly labeled "not yet recovered" — and this status is never run through either
D2's or D4's systems, because D2 audits a different (though name-overlapping) registry and D4 audits
only the SEIT Layer-II material. This is preserved as a genuine architectural gap, not bridged.

---

## 13. Strongest Formally Justified Master Claim

> **THE CORPUS ESTABLISHES:**
> A family of compiler-style research programs (at least four distinct primitive grammars, §04)
> that each independently attempt to recover established mathematics (string theory, Hamiltonian
> and quantum mechanics via CMRC/VAL-001/004/005; the vacuum Einstein tensor via a graph-spectral
> route; the self-adjointness of a discrete Dirac operator via a Discrete Cartan Identity; the
> Universal Persistence Field Equation via Euler-Lagrange variation of a stated cost functional)
> from small compositional primitive sets, with several of these specific recovery chains carrying
> complete, source-verifiable, step-by-step derivations (§09) and, in one case (the Persistence
> Field Equation, §09(c)), independent cross-document confirmation of the same result. A formal
> algebraic foundation (free algebra → congruence → universal property → conditional normal forms →
> intrinsic invariants → semantics → typing → single compiler object) has been built for exactly one
> of these primitive sets (Σ₀={D,T,C,Π}, D1 Part V). An independent formal audit (D2) confirms the
> internal bookkeeping consistency (existence, dependency-completeness, acyclicity, certification
> consistency, registry ownership, external-citation validity) of a further, name-overlapping but
> not textually identical, registry of 30 certified/candidate/open results. One of the corpus's own
> prior claims (a specific λ_c=λ₁ identification, a specific gravitational-wave-frequency
> prediction, a specific dwarf-galaxy core-radius prediction, and a specific unconditional gauge-
> group-derivation claim) has been explicitly retracted by a later, more rigorously audited revision
> within the same corpus (D4), and that retraction is documented rather than hidden.
>
> **THE CORPUS DOES NOT YET ESTABLISH:**
> That any two of its (at least eleven) distinct primitive-grammar proposals are the same grammar
> (§07 — no pair classifies EXACT, ISOMORPHIC, or unconditionally EQUIVALENT); that the persistence
> threshold λ_c can be derived from spectral data without an external parameter (the corpus's own
> stated #1-ranked open problem, D4 §6); that gravity couples to a matter source within the
> graph-spectral route (D1 Layer VII, explicitly "not yet recovered"); that the Standard Model gauge
> group SU(3)×SU(2)×U(1) is uniquely selected rather than merely consistent with the anomaly
> conditions checked (D4's explicit downgrade of D5's stronger claim); that an indefinite,
> Lorentzian-signature metric can be recovered from positive-definite graph-spectral data beyond a
> single certified rank-one-perturbation negative eigenvector (D1 §8, everything past "Localization"
> is Open); or that Part V's algebraic foundation object 𝔐 is the same object as Part IV's MDCL
> compiler (D1's own explicit non-claim, §9 of Part V).
>
> **THE CORPUS LEAVES OPEN:**
> 32 explicitly enumerated open items (§10), most centrally the λ_c/Γ(λ) closure (D4's own #1
> priority, with a stated but unevaluated target integral), the bipartite-reciprocity and
> shell-nilpotency locks blocking D2's RF-001…004 chain (OP-001/OP-002), the UGNT termination and
> confluence theorems underlying Part V's conditional normal-form theorem, and whether Part I's DTC
> composition order or Part IV's six-primitive extension could support the same rigorous algebraic
> foundation Part V built for a third, distinct primitive set.
>
> **THE CORPUS EXPLICITLY FALSIFIES (retracts as incorrect within its own later revision):**
> λ_c = λ₁ (Fiedler value); a 166.48 Hz monochromatic gravitational-wave background; ~135 pc dwarf-
> spheroidal soliton core radii; and the claim that SU(3)×SU(2)×U(1) is *derived, not postulated*
> from anomaly cancellation alone.

This statement is deliberately no stronger than its weakest necessary dependency: it does not
declare a Theory of Everything, and it does not claim any cross-grammar equivalence the sources
themselves decline to claim.

---

## 14. Explicit Non-Claims

Applying the negative-capability rule directly:

- This reconstruction does **not** assert that GR-01 and GR-03 are equivalent — only that 4 of 6
  primitives are textually identified as the same objects; Θ, Ω, and the composed Γ_C have no
  source-stated relationship to GR-01 at all.
- It does **not** assert that Part V's foundation generalizes to Part I's or Part IV §7.2's
  grammars — D1 itself states this is open and unattempted.
- It does **not** assert that D2's PR-001…004 are the same as any named primitive set in D1 — the
  name-overlap in downstream objects (CMRC-CHAIN-001, VAL-004, VAL-005, K-DEF-001) is evidence of a
  probable shared underlying project, not proof of identical primitive definitions.
- It does **not** assert that D5's 13-phase architecture, taken as a whole, is validated — D5's
  own Sec XIII names 5 open problems, and D4's independent audit downgrades a 6th claim
  (gauge-group derivation) that D5's own text did not flag as provisional.
- It does **not** repair the internal ambiguity between D5 §IV's spectral metric g_μν and D5 §VI's
  Hessian metric g_ab — both are called "the metric" in different sections of the same document
  with no explicit unification statement; this reconstruction flags the ambiguity (DAG edge E-32)
  rather than assuming they are the same object or inventing a bridge between them.
- It does **not** promote the Ω attractor's convergence, the diffusion-limit metric embedding, or
  any other item D4 marks "Derived" with a stated residual caveat, to unconditional CERTIFIED
  status — every such row's caveat is preserved verbatim in the status ledger.
- It does **not** extend, correct, or complete any open derivation (e.g. it does not attempt to
  evaluate D4's Γ(λ) projection integral, does not attempt a graph Clifford-structure proof for the
  gauge group, and does not attempt the UGNT termination/confluence proofs) — per the directive's
  explicit prohibition on filling gaps.
- It does **not** merge this reconstruction's findings into the pre-existing PRF-PRIM / Phase II
  computational work in this repository (`derivations/C0/`, `results/PHASE_2_C0_REPORT.md`) — those
  are a separate, prior, computational reconstruction of a *different* corpus (spreadsheet-based
  calculation packages), referenced only as a pointer in §08 above, not incorporated as evidence
  for or against any claim in this document-only pass.

---

## 15. Unresolved Dependencies

Ranked by how many downstream items each blocks, per the sources' own stated dependency structure
(not by this reconstruction's independent judgment of importance):

1. **λ_c / Γ(λ) closure** (D4 §2, §3, §6 rank 1; same object as D1 §10.2's open TRL parameter and
   D2's OP-007; also D3's Π₀ functional). Blocks, per D4's own explicit closure chain (§3): the
   non-trivial boundary of the persistence sector Π, the mass-scale normalization m₀, the projector
   boundaries P_k (hence force-sector count and coupling constants α_k), and the cosmological
   sector N_sub (hence the CMB-tilt prediction).
2. **OP-001 / OP-002** (D2): the Bipartite Reciprocity Lock and Shell Nilpotency Lock. Block D2's
   entire RF-001…004 chain and, through it, the "presentation-note" conditional status silently
   inherited by CMRC-CHAIN-001, VAL-004, and VAL-005 even though those three are marked Certified.
3. **UGNT termination and confluence theorems** (D1 Part V §4). Block the *unconditional* form of
   the normal-form theorem underlying Part V's entire foundation; currently the theorem holds only
   conditionally.
4. **Layer VII matter coupling** (D1 §7.5): T_μν, ∇^μT_μν=0, the full Einstein field equation with
   matter, the geodesic equation, and the Newtonian limit — all five explicitly "Target — not yet
   recovered." Blocks any claim that the graph-spectral route reproduces observable gravitational
   physics, not merely the vacuum tensor equation.
5. **Lorentzian signature recovery beyond the negative eigenvector** (D1 §8.7): localization,
   indefinite bilinear form assembly, continuum limit, and the final Lorentzian metric tensor — all
   four Open, with no Candidate construction on record for any of them.
6. **Gauge group uniqueness** (D4, downgrading D5): whether the graph's Clifford structure actually
   selects SU(3)×SU(2)×U(1) to the exclusion of E8, SO(10), or F4 is unproven; blocks any coupling-
   constant or mass-spectrum claim that presupposes the gauge group is closed.
7. **Whether GR-04's algebraic foundation generalizes to GR-01 or GR-03** (D1 Part V §9): stated
   as open and explicitly unattempted; blocks any claim that a rigorous algebraic substrate exists
   for the DTC grammar (GR-01) or the six-primitive extension (GR-03) actually used in most of the
   corpus's physical-recovery work.

---

## 16. Exact Document-Grounded Next Dependency

This is not a recommendation from this reconstruction's own research judgment. It is the corpus's
own stated next step, taken directly from its own ranked-target list — the only place in the entire
five-document corpus where a single, explicitly ordered "what to do next" is given with a stated
priority rank and a stated unlock consequence:

> **D4 §6, Open Research Program — Ranked Targets, Rank 1:**
> **"Evaluate Γ(λ) projection integral from C_Π."** Method (as stated): "Compute
> ⟨ψ_n\|g^{ca}∇_aI_F\|ψ_n⟩ and scattering complement." What it unlocks (as stated): **"λ_c, Π, all
> downstream objects."**
>
> Stated in full at D4 §2.5: "One calculation unlocks everything downstream: Γ(λ_n) =
> ⟨ψ_n\|g^{ca}∇_aI_F\|_{y=ψ_n}⟩ / ⟨ψ_{m>n}\|g^{ca}∇_aI_F\|_{y=ψ_n}⟩. Numerator: restoring projection
> back onto mode n. Denominator: scattering projection into higher modes. If this ratio is
> computable from C_Π, is monotonically decreasing in λ, and equals 1 at a unique finite λ_c, then
> the persistence threshold is derived without free parameters. Until that integral is evaluated,
> every claim downstream of λ_c carries the status 🟡 or 🔴."

This single item is independently corroborated as the correct next dependency by three separate
sources in this corpus, converging without cross-citation: D1 §10.2 flags λ_c as the one explicitly
open item in its own Thermodynamic Realization Layer; D2's OP-007 registers the identical open
problem under its own registry ID with "Low" priority *relative to OP-001/OP-002* (which block a
different, independent chain — the graph-morphism locks, §15 item 2 — not this one); and D3's
closing paragraph independently states, in its own words, "the research program's central open
problem is the derivation of λ_c from Spec(L) without external parameters." D4 is the only document
that supplies a stated, precise, evaluable target (the ratio integral above) rather than only naming
the gap — which is why D4 §6 Rank 1 is recorded here as the exact next dependency, not D1's, D2's,
or D3's less specific statements of the same open problem.

Per the directive's C0-style governance carried over from this repository's own prior conventions:
this reconstruction does **not** attempt to evaluate that integral, does **not** propose a
computational plan for doing so, and does **not** advance any downstream claim that depends on it.

---

## Addendum — Cross-Repository Findings: `BLZIX989/URSP`, "Given a seed, can we reproduce the
## Standard Model?"

**Added 2026-08-18**, in response to a direct follow-up question and a third-party (ChatGPT) reply
citing prior project work this reconstruction had not yet located. Investigated by cloning
`https://github.com/BLZIX989/URSP` (a separate, sibling repository — not part of this repository's
Git history, not covered by §01–§16 above) at branch `claude/rosetta-stone-derivation-by6j3l`,
commit `f05606c3f5f663028875cab940757a46deab7f57`. Full citation table:
`governing_corpus/registries/URSP_CROSS_REPO_FINDINGS.csv` (7 rows, IDs URSP-01…07). This addendum
does not modify §01–§16; it adds a second, independently-conducted line of evidence that bears
directly on one specific question those sections could not answer from the 5-document corpus alone.

### A1. Provenance correction

The third-party reply described a "recent NCG bridge experiment" (grading/J-structure/order-zero/
first-order tests) as if freshly run in this conversation. It was not — no such computation was
performed in this session or its recorded history. It is real work, but it lives entirely in the
separate `URSP` repository, on a branch this session had not been given and had to locate and fetch
independently (`git ls-remote` surfaced it; the repo's default `main` branch contains only a stub
`README.md`). The third-party description was also **already one step behind** that repository's
actual head commit — it matched the second of three chained experiments below, not the third
(most recent) one, which reverses which specific axiom fails.

### A2. The finite-spectral-triple bridge chain (URSP-01, URSP-02, URSP-03)

Three chained experiments, each explicitly built on the previous one's proof rather than repeating
it, form a single line of inquiry: can a Connes-style finite noncommutative-geometry spectral triple
be built canonically from a Track-A seed (a structure-derived, self-relating finite relation), with
no Standard-Model content assumed in the construction?

| Run | Algebra tested | Order-zero | First-order | Proof status |
|---|---|---|---|---|
| `SEMANTIC-FUNCTOR-BRIDGE-001` (URSP-01) | Maximal abelian, **symmetric** particle/antiparticle representation | PASS (259/259) | FAIL (0/259) | General theorem: identical representations force `D_F=0` |
| `OPEN-024B` asymmetric (URSP-02) | Maximal abelian, 4 **asymmetric** representation candidates | PASS (universal) | FAIL (0/2072 test instances) | `THM-ASYM-BRIDGE-OBSTRUCTION-001`, proven: any representation of an abelian algebra forces `D_F=0`, symmetric or not — root cause is that every irrep of an abelian algebra is 1-dimensional |
| `OPEN-024B` non-abelian (URSP-03) | `A_seed = Comm(D_F)`, the seed's own Dirac-operator commutant, **non-abelian for 56/259 seeds** | **FAIL (0/56, exact)** | **PASS (56/56, exact)** | `THM-NAB-ORDER-ZERO-OBSTRUCTION-001`, proven: for any conjugation-closed subalgebra with the standard real structure, order-zero holds *iff* the algebra is abelian |

The three runs are not three independent attempts landing on the same wall — they are a single proof
tightening around the same obstruction: abelian algebras satisfy order-zero and fail first-order;
the one non-abelian algebra reachable from the seed's own structure satisfies first-order and fails
order-zero; nothing tested satisfies both. Both directions are now closed by **proven general
theorems**, not merely by exhausted search.

### A3. Even where non-abelian structure appears, it is not the Standard Model gauge group (URSP-04)

At the one place a non-abelian algebra was found (`Comm(D_F)`), its unitary group is
`U(1)×U(1)×U(2)` (N=4 seeds) or `U(1)×U(1)×U(3)` (N=5 seeds) — not `SU(2)` or `SU(3)`, which are
simple and determinant-constrained. Only the bare irrep *dimension* (2, 3) coincidentally matches.
The source's own verdict: "**STRUCTURAL COMPARISON ONLY — no DERIVED MATCH claim**." A
target-independence firewall (scanning the construction code itself for `SU(3)/SU(2)/U(1)/G_SM/
color/generations/…`) returned zero hits, supporting that this negative result was not produced by
(or in spite of) reaching for the Standard Model.

### A4. Independent, cross-repository corroboration of §11's D4-vs-D5 finding (URSP-05)

Separately from the NCG-bridge chain, `URSP`'s own `UOC-TOE-MASTER-CLOSURE-001.md` records that a
prior run's governance instruction *explicitly warned against* downgrading the SM gauge-group claim
"merely because a later source document rejected one specific route" — the same caution ChatGPT's
reply raised in this conversation, already anticipated and guarded against inside `URSP` itself.
Despite that explicit caution, a dedicated independent search (Clifford structures, commutants,
Lie-algebra recovery, representation decomposition) found **four independent source documents** —
including, per that file, "the project's own official *Status Report*" — concurring the gauge-group
result was never derived; only the single oldest document claims otherwise, and that is exactly the
claim the other four retract. `URSP` draws the precise distinction this reconstruction's §11 also
drew: falsifying one derivation *route* establishes `¬(Route A ⇒ G_SM)`, not `¬G_SM` — the physics
is unaffected, only this project's specific claimed derivation of it.

This is the same conclusion §11 of this report reached independently, from a different corpus (5
docx files vs. `URSP`'s own broader source set) and a different method (document reading vs. a
dedicated code search) — two independently-conducted investigations converging on the same finding.
`URSP`'s "project's own official Status Report" plausibly refers to the same
`Theory_of_Everything_Status_Report.docx` uploaded as one of this repository's own original five
Phase-0 source files (SHA-256 `7369a4eb…`) — noted as a filename match only; this reconstruction did
not independently confirm the two are byte-identical.

### A5. There is no single seed to begin with (URSP-06, URSP-07)

Bearing directly on the literal premise of "given *a* seed": `URSP` proves seed existence but
disproves seed uniqueness at every tested scale, on two separate counting schemes. The
NCG-bridge-relevant family (`F_N^derived_v2`) grows **1, 4, 23, 231** across N=2,3,4,5, with the
growth rate *accelerating* through N=5 rather than leveling off — reported as evidence against, not
proof against, eventual convergence. A separate, less-restricted enumeration (raw self-relating
fixed points of the structure-derived operator Γ) finds **6, 70, 2462** nonisomorphic fixed points
at N=2,3,4. `URSP`'s own final status line: **"OPEN / PROVEN NON-IDENTIFIABLE, since its premise (a
unique minimal kernel) remains false."**

### A6. Updated answer to "given a seed, can we reproduce the Standard Model?"

Combining §04–§16 above with A2–A5: the answer is still no, and it is now supported by considerably
more than corpus incompleteness. For the one concrete, executable construction that has actually
been tried (the finite Connes-style spectral-triple bridge from a Track-A seed), both of the two
live options — abelian algebra, non-abelian commutant algebra — are now closed by **proven general
theorems**, not unexplored gaps; where a non-abelian structure does appear, it provably is not the
Standard Model's gauge group; the only located derivation route for the gauge group itself is
empirically rejected across four independent source documents in a search designed specifically not
to prematurely discard it; and the seed the question presupposes is provably not unique at any
tested scale, with no convergence in sight. None of this is a claim that the underlying mathematics
*cannot* produce the Standard Model in principle (§14's negative-capability rule still applies) — it
is a claim that every concrete route tried so far, across two independent repositories and multiple
independently-authored runs, closes with a proven obstruction rather than an open question.

### A7. Next dependency, per `URSP`'s own stated next step

`OPEN-024B_NONABELIAN_BRIDGE.md` §S states the precise, minimal condition its own theorem identifies
as necessary before this specific route could have any chance of closing: either (a) a real
structure `J` not of the standard swap-conjugate form, or (b) an algebra with multiple
*inequivalent* irreducible representations of compatible dimension — a structure "none of the 259
admissible seeds through N=5 possess." Per that file's own stop condition, this was not attempted in
`URSP`, and it is not attempted here.
