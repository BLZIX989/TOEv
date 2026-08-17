# Phase 1 Falsification Records

## FALS-P1-001 — the BARE graph Laplacian heat-trace does NOT match the continuum heat-trace asymptotic

**Claim tested:** Tr(exp(−tL)) ~ Len/√(4πt) (1D) / Area/(4πt) (2D) using the bare, unrescaled graph
Laplacian L directly at physical time t.

**Construction:** computed Tr(exp(−tL)) numerically for a 4096-vertex ring at t=0.001–0.02 and a
48×48 torus at t=0.05–0.5, using the BARE (unrescaled) graph Laplacian.

**Result: FALSIFIED.** Ratios of numeric-to-predicted ranged from 73× to 314× (1D) — wildly off,
not a small correction. The bare graph Laplacian's eigenvalues are O(1) (lattice units), not O(1/h²)
(physical units); Tr(exp(−tL)) at fixed physical t therefore probes a completely different
timescale than the continuum operator.

**Resolution (not silent — recorded as a methodological finding):** using the h²-rescaled
generator L/h_N² (justified independently in Node B) instead of the bare L, all ratios converge to
1.000–1.05 across all tested t. **This directly parallels PRF-PRIM's earlier finding that τ cannot
be identified with exp(−tL) without specifying which normalization is meant** — the same lesson
(bare graph-spectral quantities and their continuum counterparts are NOT interchangeable without
an explicit rescaling) recurs at the heat-trace level, independently, in this phase.

**Script:** `derivations/CDE_heatkernel_distance_metric.py` (see the `NOTE:` comment in `node_C()`
documenting the initial bare-L computation and its correction).

**Classification:** FALSIFIED for the naive/bare identification; SURVIVES (verified, see PROOF
context and Node C's derivation record) for the correctly-rescaled version.

---

## No other claim tested in Phase 1 was falsified.

Every other independently-attempted reconstruction (Nodes A, B [corrected], D, E, I, K, O, P items
1–3) either matched the corresponding source/external claim exactly or produced a genuinely new,
internally-consistent result with zero contradiction. Node F/G/H's smooth-curvature chain was
**blocked** (BLOCKER-001), not falsified — no claim was tested and found false; the construction
was never completed to the point of being testable. Node L's full non-Abelian covariance was
**not independently tested** (admitted, not falsified). Node M/N's toy-Hamiltonian correspondence
(λ_n↔E_n) was explicitly kept as CANDIDATE, never asserted as fact, so there was nothing to falsify.
