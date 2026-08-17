# Node I — Variational Structures, Node J — Classical Mechanics

**Closes Phase-0 gap OBJ-GAP-001** ("no independent Lagrangian mechanics / Poisson-algebra
construction").

## Independent reconstruction (fully symbolic, SymPy, zero UOC import)

Worked example: 1D harmonic oscillator, but every step is generic calculus-of-variations, not
specific to this example.

1. **Action** S[q]=∫L(q,q̇)dt with L=½mq̇²−½kq².
2. **Euler-Lagrange** derived by direct functional differentiation: d/dt(∂L/∂q̇)−∂L/∂q=0 →
   simplifies to mq̈+kq=0 (Newton's second law / SHM), verified symbolically to reduce to exactly
   this after substitution — **not assumed**, derived.
3. **Legendre transform**: p:=∂L/∂q̇=mq̇ (invertible), H(q,p):=pq̇−L, solved symbolically to
   H=(p²+kmq²)/(2m).
4. **Hamilton's equations derived FROM H** (not imported): q̇=∂H/∂p=p/m (checked identical to the
   Legendre-transform relation q̇=p/m, error=0); ṗ=−∂H/∂q=−kq (checked identical to the
   Euler-Lagrange force term, error=0).
5. **Canonical Poisson bracket**: {q,p}=∂q/∂q·∂p/∂p−∂q/∂p·∂p/∂q=1 (computed directly from the
   definition, not postulated). Verified {q,H}=q̇ and {p,H}=ṗ **exactly** (both checks return 0).

Every "check" above returned exactly 0 (SymPy `simplify`), i.e. the entire chain
S→δS=0→Euler-Lagrange→Legendre transform→H(q,p)→Hamilton's equations→canonical symplectic
structure was independently constructed and is internally 100% consistent.

Output: `../I_variational/variational_structure_results.json`. Script: `I_variational.py`.

## Node J (Classical Mechanics) — status

Node J is not a separate computation: it *is* the content of Node I (a Lagrangian/Hamiltonian
system with canonical Poisson structure **is** classical mechanics). No further independent work
was needed to populate this node beyond Node I's derivation.

## Status separation

| Field | Value |
|---|---|
| SOURCE_STATUS | ADMITTED — source's own content here is a single validation-branch claim (OBJ-032/VAL-005, "Hamiltonian Mechanics... CERTIFIED") with **no shown construction** of the Poisson bracket or Euler-Lagrange machinery; Phase 0 flagged this as GAP OBJ-GAP-001 |
| INDEPENDENT_DERIVATION_STATUS | **DERIVED** (full symbolic chain, zero gaps, zero imports, all consistency checks exactly 0) |
| CLOSURE_STATUS | CALCULATED-UNIVERSAL for the calculus-of-variations machinery itself (standard, general — not specific to the harmonic-oscillator example used to make it checkable) |
| VERIFICATION_STATUS | VERIFIED (deterministic symbolic algebra, every intermediate step checked) |
| PROVENANCE | phase_1/I_variational/variational_structure_results.json |

## Comparison classification
**D → resolved.** This was a genuine **missing dependency** in the source (Phase 0's OBJ-GAP-001);
this node **closes it independently**, upgrading the corpus's own OBJ-032 claim from "ADMITTED,
unconstructed" to having an independent construction available (though the corpus's own construction
route, via the persistence cost functional OBJ-014, remains separately ADMITTED/unverified — this
node did not verify THAT specific route, only that Hamiltonian mechanics as such is independently
constructible from first principles).
