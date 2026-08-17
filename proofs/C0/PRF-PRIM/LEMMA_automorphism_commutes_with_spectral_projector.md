# Lemma: graph automorphisms commute with every spectral projector of L (and with exp(-tL))

**Status: PROVEN (general argument below) + VERIFIED (9/9 benchmark families, `derivations/C0/PRF-PRIM/04_tau_liouville_and_kappa_commutation.py`, max numerical error 3.9e-16).**

## Statement

Let `G=(V,E)` be a finite graph with Laplacian `L=D-A`. Let `P` be a permutation matrix representing
a graph automorphism, i.e. `P A P^T = A`. Then `P` commutes with every spectral projector of `L`,
including `P_ker(L)` (candidate realization of **kappa**) and `exp(-tL)` for every `t`.

## Proof

1. If `P A P^T = A`, then `P` also preserves the degree sequence in the sense that `P D P^T = D`
   (since `D` is diagonal with `D_ii = deg(i)`, and a graph automorphism maps each vertex to a
   vertex of the same degree by definition of automorphism — it preserves adjacency counts).

2. Hence `P L P^T = P(D-A)P^T = PDP^T - PAP^T = D - A = L`, i.e. **`P` commutes with `L`**: `PL = LP`.

3. Since `L` is real symmetric, it has a spectral decomposition `L = sum_k lambda_k E_k` where `E_k`
   is the orthogonal projector onto the eigenspace for eigenvalue `lambda_k`. Because `PL=LP` and `P`
   is orthogonal, `P` maps each eigenspace of `L` to itself (a standard fact: if `PL=LP` and `Lv =
   lambda v`, then `L(Pv) = P(Lv) = lambda (Pv)`, so `Pv` is again in the `lambda`-eigenspace).

4. Therefore `P` commutes with each spectral projector `E_k`, in particular with `E_0 = P_ker(L)`
   (**kappa**'s candidate realization), and with any function of `L` applied via its spectral
   decomposition, including `exp(-tL) = sum_k e^{-t lambda_k} E_k`.

`QED.`

## Consequence for PRF-PRIM

This is the one positive, exactly-provable, multi-family-verified structural fact connecting two
candidate primitive realizations found in this DER: **kappa (as P_ker(L)) and tau (as a graph
automorphism) are compatible in the strongest possible sense — they commute exactly, for every
graph, unconditionally.** This does NOT extend to tau realized as the diffusion semigroup in the
same strong sense of "independently established primitive" — `exp(-tL)` trivially commutes with
`P_ker(L)` too (it's built from the same spectral decomposition), but that realization of tau fails
its own Liouville-condition definition (see `falsification/C0/PRF-PRIM/`), so this commutation fact
does not rescue it as a valid tau candidate.

## Scope / limitations

- Proven only for **graph automorphisms**, i.e. tau realized as `P PermutedInc(G) P^T = Inc(G)`-type
  symmetries. Not a general claim about arbitrary "lawful, volume-preserving" transformations.
- Does not by itself establish that kappa (defined in source as "the rules restricting which
  transformations are permissible") is *correctly* realized as `P_ker(L)` — that is a CANDIDATE
  mapping (Phase 3), not a source-given identity.

## Provenance

Derived and verified in this execution (session `session_01UBKp9Jq2qXFgravroyUp32`) from
`derivations/C0/PRF-PRIM/04_tau_liouville_and_kappa_commutation.py`. General linear-algebra
argument (steps 1-4) is standard algebraic graph theory, not UOC-original; registered as
`EXT-003` (see registries update).
