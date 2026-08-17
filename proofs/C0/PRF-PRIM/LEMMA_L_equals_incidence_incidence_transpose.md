# Lemma: L = Inc · Inc^T (the graph Laplacian is the Gram matrix of the discrete gradient)

**Status: PROVEN (general argument below) + VERIFIED exactly (sympy exact integer arithmetic,
9/9 benchmark families, `derivations/C0/PRF-PRIM/03_incidence_gradient_identity.py`).**

## Statement

Let `Inc` be the `n x m` oriented incidence matrix of a graph `G=(V,E)` (`|V|=n`, `|E|=m`): for
edge `j=(u,v)`, column `j` has `+1` at row `u` and `-1` at row `v` (arbitrary fixed orientation).
Then `L = Inc · Inc^T`, independent of the chosen orientation.

## Proof

`(Inc · Inc^T)_{ik} = sum_j Inc_{ij} Inc_{kj}`. For `i=k`: each edge incident to vertex `i`
contributes `(+-1)^2=1`, so the diagonal entry is `deg(i) = D_ii`. For `i != k`: a term is nonzero
only for the (at most one) edge `j=(i,k)`, contributing `(+1)(-1)=-1` if that edge exists, else 0.
This is exactly `-A_{ik}`. Hence `Inc Inc^T = D - A = L`. Orientation-independence follows because
flipping a column's sign leaves `Inc_{ij} Inc_{kj}` unchanged (both entries flip together). `QED.`

## Consequence for PRF-PRIM

This gives an EXACT, unconditional structural bridge between grammar B's `grad(Phi)` (realized as
`Inc^T`, the discrete gradient) and the Laplacian `L` that grammar A's downstream chain (DER-SPC-002
onward) is built from — `E(Phi) = Phi^T L Phi = ||Inc^T Phi||^2` is the discrete Dirichlet energy,
giving `PRIM-P-001` (Energy) a derivable, non-primitive status GIVEN `PRIM-P-002` (grad Phi) and the
graph structure. See `derivations/C0/PRF-PRIM/07_minimal_grammar_and_graph_representation.py`,
minimality table row "E".

## Important caveat (what this does NOT prove)

This does **not** prove `grad(Phi) = Delta`. It proves `grad(Phi)`'s natural graph realization
(`Inc^T`) feeds the SAME Laplacian that Delta's downstream chain uses — a structural parallel, not
an identity. `Inc^T` is neither globally injective (`ker(Inc^T) = ker(L)`, nontrivial whenever the
graph is connected) nor surjective onto the full edge space for any graph containing a cycle. This
is registered as CANDIDATE, not CERTIFIED, in the compatibility matrix.

## Provenance

Standard result of algebraic graph theory (e.g. Godsil & Royle, *Algebraic Graph Theory*, Ch. 13).
Registered as `EXT-001` (ADMITTED EXTERNAL INPUT, see registries update) — not a UOC-original
derivation. Applied and verified against the UOC primitive registry in this execution.
