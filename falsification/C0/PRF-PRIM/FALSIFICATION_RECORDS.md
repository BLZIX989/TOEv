# PRF-PRIM Falsification Records

Every entry below is an explicit counterexample or failed construction, preserved regardless of
whether it supports or undermines the UOC architecture, per directive Section XXI / governance
rule 6 ("preserve all existing calculations even when their universality is limited") and rule 13
("if C0 fails, do not fabricate a common grammar; record the obstruction").

---

## FALS-001 — tau realized as the diffusion semigroup exp(-tL) violates its own source definition

**Claim tested:** tau (PRIM-G-002 / PRIM-X-002), defined in source as "any lawful evolution ...
preserving phase-space volume (discrete Liouville condition)," can be realized as `exp(-tL)`, the
heat/diffusion semigroup used throughout the corpus's COSMO-DYN branch.

**Construction:** `det(exp(-tL)) = exp(-t * trace(L)) = exp(-t * 2|E|)` (exact, any square real `L`).

**Counterexample family:** all 9 benchmark graphs (K4, K3,3, C6, P5, disjoint K4⊔K3,3, two disjoint
triangles, 4×4 periodic torus, Petersen graph, star K1,5) — every graph with at least one edge.

**Result:** `det(exp(-tL))` → 0 as `t`→∞ for every family tested (e.g. K4 at t=1: 6.1×10⁻⁶; torus
4×4 at t=1: 1.6×10⁻²⁸). Volume preservation requires `|det|=1`. **FALSIFIED on 9/9 families.**

**Classification:** FALSIFIED (for this specific candidate realization of tau; does not falsify
tau itself, only this reading of it).

**Preserved existing result:** this does NOT touch the corpus's own COSMO-DYN calculations (which
never claim `exp(-tL)` is volume-preserving) — it falsifies only the CANDIDATE identification
`tau = exp(-tL)` that this DER was asked to test (directive Phase 4), consistent with the corpus's
own governance caution (`MASTER_CURRENT_CHAT_CANONICAL_RULES.csv`, C7-001: "Do not assume
Fix(Γ)=Fix(e^{-βL})").

**Script:** `derivations/C0/PRF-PRIM/04_tau_liouville_and_kappa_commutation.py`

---

## FALS-002 — Gamma_graph (Delta_alt_1 = I−P_ker(L)) is identically the zero map

**Claim tested:** Delta can be realized as the endomorphism `I − P_ker(L)` ("distinguish the
non-persistent directions"), composed as `Gamma_graph = kappa ∘ tau ∘ Delta_alt_1` with
`kappa=P_ker(L)`, `tau`=graph automorphism.

**Result:** `Gamma_graph ≡ 0` on 9/9 families, because `P_ker(L)` and `I−P_ker(L)` are exactly
complementary commuting projectors (Lemma, `proofs/.../LEMMA_automorphism_commutes...md`), so
`P_ker(L)·P_tau·(I−P_ker(L)) = P_tau·P_ker(L)·(I−P_ker(L)) = P_tau·0 = 0` identically.

**Classification:** FALSIFIED / NO-GO for this specific reading of Delta as an endomorphism.

**Script:** `derivations/C0/PRF-PRIM/06_grammar_recursion_conjugacy_test.py`

---

## FALS-003 — no orthogonal conjugacy found between Gamma_graph and exp(-hL)

**Claim tested:** there exists an orthogonal transform `T` with `T·Gamma_graph·T⁻¹ ≈ exp(-hL)` for
`Gamma_graph = kappa∘tau∘Delta_alt_2` (Delta_alt_2 = single-vertex indicator projector).

**Method:** best-case orthogonal Procrustes alignment (`argmin_T ||T·Gamma_graph − exp(-hL)·T||_F`,
`h=1.0`), tested on all 9 benchmark families.

**Result:** residuals ranged 0.882–0.971 (normalized; 0 = perfect conjugacy). **No family came
close to conjugate.** Additionally, `Gamma_graph`'s fixed-point subspace was empty (dimension 0)
on every family, meaning this realization has NO analogue of Pi at all under this specific Delta
reading.

**Classification:** FALSIFIED (for the tested Delta_alt_2 realization and Procrustes-conjugacy
criterion; a weaker semiconjugacy on a smaller invariant subspace was not separately tested and is
left OPEN, not claimed either way).

**Script:** `derivations/C0/PRF-PRIM/06_grammar_recursion_conjugacy_test.py`

---

## FALS-004 (external, admitted) — spectrum does not determine a graph up to isomorphism

**Claim tested:** Delta (the graph/incidence structure) is reconstructible from tau (Aut(G)) and
kappa (Spec(L)/P_ker(L)) alone.

**Counterexample:** cospectral non-isomorphic graphs are a standard, well-documented phenomenon in
spectral graph theory (smallest known examples from n=5 upward; e.g. many pairs of cospectral trees
exist at small n). This DER did not need to construct a fresh example — it is an established
external theorem, registered as `EXT-002` (ADMITTED EXTERNAL INPUT).

**Result:** Delta is NOT reconstructible from tau+kappa's outputs in general.

**Classification:** FALSIFIED (external, admitted — not independently re-derived here).

**Consequence:** Delta is IRREDUCIBLE in the graph-spectral realization (see minimality table,
`derivations/C0/PRF-PRIM/07_minimal_grammar_and_graph_representation.py`).

---

## Summary

| ID | What was falsified | Families tested | Result |
|---|---|---|---|
| FALS-001 | tau = exp(-tL) (Liouville condition) | 9/9 | FALSIFIED, all 9 |
| FALS-002 | Delta = I−P_ker(L) (composition) | 9/9 | FALSIFIED (zero map), all 9 |
| FALS-003 | Gamma_graph conjugate to exp(-hL) | 9/9 | FALSIFIED (no near-conjugacy), all 9 |
| FALS-004 | Delta reconstructible from tau+kappa | external/admitted | FALSIFIED |

No universal claim in this DER survived on a single example alone — every surviving positive
result (Lemma files in `proofs/C0/PRF-PRIM/`) was checked across all 9 families spanning regular/
irregular, tree/cyclic, connected/disconnected, degenerate/non-degenerate spectrum, and a periodic
lattice topology.
