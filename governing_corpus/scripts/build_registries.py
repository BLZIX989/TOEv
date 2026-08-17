import csv, os

REPO = '/home/user/TOEv/governing_corpus/'
TAG = "GOVCORPUS-RECON-2026-08-17"

# ---------------- 01 SOURCE INDEX ----------------
src_header = ["DOC_ID", "Filename", "SHA256", "Author/Program", "Approx_Date", "Internal_Structure",
              "Relationship_to_Other_Docs"]
sources = [
    ["D1", "Combined_Compiler_Theories_Whitepaper.docx",
     "a85fe31a180dd9de355379997ea20e4430799163246c824bd381975d87fb5b6c",
     "Keith I. Blaze, Independent Research",
     "undated in text; referenced by D4 as predecessor",
     "Part 0 (Compiler Certification Registry) + Parts I-V: I=This from That/DTC/TOEv, II=UDP v2.0, "
     "III=Organizational Hierarchy (worked/textbook), IV=MDCL v1.0+v2.0 validation campaign + "
     "Lorentzian program, V=Universal Organizational Foundation (algebraic substrate)",
     "D4 explicitly updates this document's lambda_c identification and SEIT-layer derivation "
     "statuses (D4 Prefatory Note). D2 (CVR001) audits infrastructure with strong name-overlap "
     "to D1 Part IV (CMRC-CHAIN-001, VAL-004, VAL-005, THERMO-TAX)."],
    ["D2", "CVR001_Compiler_Verification_Report.docx",
     "a34e74ae897b55bd56b959ea9b383dc907e7d7af2484179c0f8a31747e7ce08f",
     "Universal Organizational Compiler / Certification Registry (author not named in text)",
     "undated", "Formal 6-dimension audit (Existence, Dependency, Acyclicity, Certification "
     "Consistency, Registry Ownership, External Ancestry) of MCT rows 001-030 (Foundation + "
     "Discrete Architecture layers), an 8-item Open Problems Register, Conditional Certification "
     "Tracker, Infrastructure Readiness Assessment",
     "Audits a registry (PR-001-004, K-DEF-001, ARBS-DEF-001, CMRC-CHAIN-001, VAL-004, VAL-005, "
     "THERMO-TAX-001-003) whose object names overlap with, but are not textually confirmed "
     "identical to, D1 Part IV's MDCL/CMRC objects and Part I's ARBS/thermodynamic-axiom objects. "
     "Relationship recorded as PROBABLE, NOT CONFIRMED (see cross-document matrix)."],
    ["D3", "Distinction_to_Persistence_Analysis.docx",
     "b2b09cbc723346956c6201add1f958140e7c2f0479588f2ece757a5e5822636b",
     "Keith I. Blaze, DTC/Rosetta Stone Protocol Research Program, Montclair State University",
     "undated (references 18 source posters, not independently dated)",
     "Poster-companion analytical/visualization treatment: QM, Universal Laplacian Compiler "
     "pipeline stage-by-stage, cross-domain compiler matrix, geometry/curvature registry, Big Bang "
     "timeline, brane-bulk framework, TOEv/SEIT/TEDS/URS, Heat Death vs Big Rip",
     "Introduces a 5-primitive TOEv set (Delta,R,T,C,Pi) distinct from D1's 4-primitive DTC set; "
     "introduces SEIT L0-L5 hierarchy and persistence functional Pi_0=(delta_spec-lambda_c)/sigma, "
     "the same lambda_c object D1 Sec10.2 and D4 both discuss as open."],
    ["D4", "SEIT_Updated_Whitepaper.docx",
     "11ba6f285665f9e95b384fe023239b71cdec7d280ddedd2d072f9a79f4a097e2",
     "Keith I. Blaze, DTC/Rosetta Stone Protocol Research Program, Wavefront/UCDP OS",
     "June 2026 (explicit)",
     "Self-critical audited revision: Prefatory Note states purpose explicitly; Sec0 two-layer "
     "architecture (USC/SEIT); Sec1 full derivation audit matrix with 5-state color codes; Sec2 "
     "central lambda_c derivation attempt + explicit retraction; Sec3 closure chain; Sec4 canonical "
     "reconstruction from established math; Sec5 DTC grammar updated role; Sec6 ranked open "
     "research targets; Sec7 updated falsifiability status",
     "Explicitly supersedes specific claims in D5 (SEIT_Compiler): retracts lambda_c=lambda_1 "
     "(Fiedler value), retracts the 166.48 Hz GW prediction and ~135 pc dwarf-galaxy core radius "
     "prediction that D5 presents as live falsifiable predictions. Also updates D1's lambda_c "
     "treatment (D1 Sec10.2 leaves lambda_c fully open with no candidate; D4 supplies the "
     "Gamma(lambda)=Restoration/Degradation candidate framework, itself still Partial/Open)."],
    ["D5", "SEIT_Compiler.docx",
     "91125b6d63d23527ae6f88081d36a2ff9d7bd108e84b7fad42ce1ebcd5f2eecd",
     "Keith I. Blaze, Montclair State University / DTC-Rosetta Stone Protocol Research Program",
     "June 2026 (explicit, same month label as D4)",
     "13-phase 'Universal Compiler Architecture': Born rule, Lorentz signature, Noether/conservation "
     "laws, stress-energy, Maxwell, Dirac, renormalization, partition function, path integral, "
     "cosmology, organizational evolution, inverse spectral problem; XI Falsifiable Predictions "
     "(3, parameter-free); XIII Open Problems (5, self-declared); XIV Rosetta Grammar",
     "Chronologically/logically PRECEDES D4's audit despite the same month label: D4 explicitly "
     "names and retracts specific claims that appear in D5 with full confidence (lambda_c=lambda_1 "
     "implicit in D5 Sec II.4's Pi definition; 166.48 Hz GW line; ~135 pc dwarf core radii; "
     "G_SM anomaly-cancellation derivation labeled 'derived, not postulated' in D5 Sec VIII.2 vs "
     "D4's Sec1 matrix marking the same object Partial/Open). Treated here as SUPERSEDED BY D4 "
     "on every point D4 explicitly revises; D5 content NOT explicitly touched by D4 (e.g. the "
     "Heat Kernel Bridge Sec III, Spectral Metric Formula Sec IV, Euler-Lagrange field-equation "
     "derivation Sec VI) is preserved at its own originally-stated status, not silently downgraded."],
]

os.makedirs(REPO + 'registries', exist_ok=True)
with open(REPO + 'registries/SOURCE_INDEX.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(src_header)
    w.writerows(sources)

print("Source index written:", len(sources))
