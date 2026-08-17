"""
PRF-PRIM -- append versioned records to the master registries. NEVER modifies or deletes an
existing row; every write is a new row appended at the end, tagged with this execution's
provenance so the append is auditable. Existing PRF-PRIM row in MASTER_PROOF_REGISTRY.csv is
left exactly as-is (status stays "Open" -- PRF-PRIM is NOT closed by this execution).

Run: python3 09_update_registries.py
"""
import csv, os

REG = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'registries'))
TAG = "PRF-PRIM-EXEC-2026-08-17"

def append_rows(path, rows):
    with open(path, 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(rows)
    print(f"Appended {len(rows)} row(s) to {os.path.basename(path)}")

# --- MASTER_THEOREM_REGISTRY.csv: ID,Theorem,Basis / Statement,Status ---
append_rows(os.path.join(REG, 'MASTER_THEOREM_REGISTRY.csv'), [
    ["LEMMA-AUT-PROJ-001",
     "Graph automorphisms commute with every spectral projector of L (incl. P_ker(L) and exp(-tL))",
     f"P A P^T=A (automorphism) => P D P^T=D => PL=LP => P preserves every eigenspace of L. "
     f"Standard linear algebra, general proof + verified 9/9 benchmark families (max err 3.9e-16). "
     f"Proof: proofs/C0/PRF-PRIM/LEMMA_automorphism_commutes_with_spectral_projector.md. "
     f"Derived in {TAG} while testing candidate kappa=P_ker(L), tau=automorphism (PRF-PRIM).",
     "CERTIFIED"],
    ["LEMMA-INC-001",
     "L = Inc * Inc^T for the oriented incidence matrix Inc of any graph",
     f"Standard algebraic graph theory (Godsil & Royle Ch.13); ADMITTED EXTERNAL INPUT EXT-001. "
     f"Verified exactly (sympy integer arithmetic) on 9/9 benchmark families. "
     f"Proof: proofs/C0/PRF-PRIM/LEMMA_L_equals_incidence_incidence_transpose.md. "
     f"Applied in {TAG} while testing candidate grad(Phi)<->Delta structural correspondence (PRF-PRIM).",
     "CERTIFIED (external theorem, admitted)"],
])

# --- MASTER_PROOF_REGISTRY.csv: PRF ID,For,Missing,Closes  (new SUB-obligations, PRF-PRIM row itself untouched) ---
append_rows(os.path.join(REG, 'MASTER_PROOF_REGISTRY.csv'), [
    ["PRF-PRIM-TAU-REALIZATION",
     "Which realization of tau (PRIM-G-002/PRIM-X-002) is intended",
     f"{TAG} tested 2 candidates: graph automorphism (satisfies tau's own Liouville-condition "
     f"definition, 9/9) vs. diffusion semigroup exp(-tL) (FALSIFIES the same definition, 9/9). "
     f"Source does not specify which. Neither proven to be the unique intended realization.",
     "PRF-PRIM"],
    ["PRF-PRIM-DELTA-TYPE",
     "Type-theoretic reconciliation of Delta's two source formulations",
     f"{TAG} showed PRIM-G-001's literal formula (boundary operator, d^2=0, a map between DIFFERENT "
     f"graded spaces C_1->C_0) is type-incompatible with DER-ORG-002's required usage (an endomorphism "
     f"X->X for Psi_(t+1)=kappa(tau(Delta(Psi_t))) to be iterable). Demonstrated concretely on the K4 "
     f"tetrahedron complex (derivations/C0/PRF-PRIM/05_composition_type_check.py). Missing: an explicit "
     f"reconciled definition of Delta that satisfies both roles, or an explanation of why they need not agree.",
     "PRF-PRIM"],
    ["PRF-PRIM-OMEGA-PSI-IDENTITY",
     "Whether Omega (PRIM-X-006, Organizational State) is the same object as Psi (grammar A's state variable, DER-ORG-002)",
     f"{TAG} found no computation or recovered source text (Combined Compiler Theories Whitepaper "
     f"para. 550-553 asserts Omega has 'its own evolution law and variational structure' but the exact "
     f"functional form was not present in the extracted text corpus available to this session) that "
     f"distinguishes Omega from Psi as a different type of object. Not merged by assumption.",
     "PRF-PRIM"],
    ["PRF-PRIM-PRIMC-LINK",
     "How PRIM-C-001 (B=(U,V,E), Computational realization) relates to grammars A, B, or D",
     f"{TAG} found ZERO tested computation or source-documented correspondence between PRIM-C-001 and "
     f"any primitive in A/B/D. The corpus's own downstream pipeline (DER-SPC-001 'Graph G=(V,E)') is "
     f"sourced from DER-ORG-001, not from PRIM-C-001, suggesting PRIM-C may not actually be used "
     f"downstream despite being registered. Missing: either a constructive link or an explicit admission "
     f"that PRIM-C is currently disconnected from the rest of the architecture.",
     "PRF-PRIM"],
])

# --- MASTER_DER_REGISTRY.csv: Entry ID,Statement (abbreviated),Direct Predecessors,Status ---
append_rows(os.path.join(REG, 'MASTER_DER_REGISTRY.csv'), [
    ["DER-C0-PRIMGRAPH-001",
     "Graph-spectral realization test of {Delta,tau,kappa,Pi} against PRF-PRIM (kappa=P_ker(L) idempotent+commutes with automorphism tau; Pi=ker(L) derivable; tau=exp(-tL) FALSIFIED; Delta type-mismatch found)",
     "PRF-PRIM, DER-SPC-002..005",
     "CALCULATED/PARTIAL"],
])

# --- MASTER_BRIDGE_REGISTRY.csv: (Source_Field_1..6 = Bridge_ID,From-To,Name,Form,Deriv.Status,Closure Note),Derivation_Status,Closure_Status,Registry_Status,Falsification_Target ---
append_rows(os.path.join(REG, 'MASTER_BRIDGE_REGISTRY.csv'), [
    ["BR-PRF-PRIM-001", "kappa[A/D] -> P_ker(L)", "Constraint-to-spectral-projector bridge",
     "kappa candidate realized as idempotent spectral projector onto ker(L)",
     "CANDIDATE, SURVIVES 9/9", "commutes exactly with tau=automorphism (proven+verified)",
     "CALCULATED", "UNADJUDICATED", "CANDIDATE",
     f"Falsified if a graph found where P_ker(L)^2 != P_ker(L) beyond float tolerance (none found, 9/9; theoretically impossible by spectral theorem)"],
    ["BR-PRF-PRIM-002", "Pi[A/D] -> ker(L)", "Persistence-to-kernel bridge",
     "Pi = im(kappa) once kappa=P_ker(L)",
     "CANDIDATE, SURVIVES (derivable) 9/9", "consistent with DER-SPC-005 naming R=exp(-beta L) the persistence operator",
     "CALCULATED", "UNADJUDICATED", "CANDIDATE",
     "Falsified if lim_(t->inf) exp(-tL) != P_ker(L) for some graph (none found, 9/9; theoretically guaranteed by spectral theorem for connected-component structure)"],
    ["BR-PRF-PRIM-003", "Theta[D] -> reachability-classes(G)", "Accessibility-to-connectivity bridge",
     "Theta's reachability structure coincides with connected-component partition",
     "CALCULATED, SURVIVES 9/9", "= N - rank(L) = dim ker(L)",
     "CALCULATED", "UNADJUDICATED", "CANDIDATE",
     "Falsified if a graph found where reachability-class count != connected-component count (none found, 9/9; theoretically guaranteed for undirected graphs)"],
])

# --- MASTER_OPEN_PROPOSED_NO_GO.csv: Layer,Problem,Closure Requirement,Status,Source / Dependency ---
append_rows(os.path.join(REG, 'MASTER_OPEN_PROPOSED_NO_GO.csv'), [
    ["C0", "tau realized as diffusion semigroup exp(-tL)", "N/A -- ruled out as a candidate realization of tau",
     "NO-GO", f"{TAG}: violates tau's own Liouville-condition definition on 9/9 benchmark families (FALS-001)"],
    ["C0", "Delta realized as I-P_ker(L) endomorphism, composed as kappa o tau o Delta", "N/A -- ruled out",
     "NO-GO", f"{TAG}: composition degenerates to the identically-zero map on 9/9 families (FALS-002)"],
    ["C0", "Gamma_graph (graph-spectral realization) conjugate to exp(-hL) via orthogonal transform", "A different conjugacy criterion or realization, if one exists",
     "NO-GO (for tested criterion)", f"{TAG}: no near-conjugacy found on 9/9 families, Procrustes residuals 0.88-0.97 (FALS-003)"],
    ["C0", "Delta reconstructible from tau(automorphism)+kappa(spectrum) alone", "N/A -- ruled out by external theorem",
     "NO-GO", f"{TAG}: cospectral non-isomorphic graphs are a standard counterexample (FALS-004, EXT-002)"],
    ["C0", "Common minimal grammar Gamma_min across all 4 registered primitive systems (A,B,C,D)", "A tested structure-preserving embedding from each of A,B,C,D into a single candidate",
     "OPEN", f"{TAG}: not established; closest result is a 3-slot reduction WITHIN grammar A/D alone (Delta,tau-slot,kappa), not a 4-grammar unification. See Common_Grammar sheet, results/workbooks/C0_PRF_PRIM_Primitive_Reconciliation.xlsx"],
])

# --- MASTER_EQUATION_REGISTRY.csv: Equation_ID,Section_Code,Section,Local_ID,Equation,Meaning,Source,Status Note ---
append_rows(os.path.join(REG, 'MASTER_EQUATION_REGISTRY.csv'), [
    ["EQ-PRF-PRIM-001", "C0", "C0", "1", "L = Inc * Inc^T", "Graph Laplacian as Gram matrix of the discrete gradient (incidence operator)",
     "EXT-001 (Godsil & Royle, Algebraic Graph Theory Ch.13)", f"PROVEN + verified exact on 9/9 families in {TAG}"],
    ["EQ-PRF-PRIM-002", "C0", "C0", "2", "det(exp(-tL)) = exp(-t*trace(L)) = exp(-2t|E|)", "Determinant of the diffusion semigroup -- shows exp(-tL) is NOT volume-preserving for any graph with an edge",
     f"{TAG} (derived while testing tau candidate realizations)", "PROVEN + verified exact on 9/9 families; falsifies tau=exp(-tL) under PRIM-G-002's Liouville-condition definition"],
])

print("\nAll registry appends complete. No existing row was modified or deleted.")
