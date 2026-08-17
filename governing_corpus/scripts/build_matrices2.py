import csv, os
REPO = '/home/user/TOEv/governing_corpus/'

# ---------------- MORPHISM / TRANSLATION MATRIX (between the 11 grammars) ----------------
header = ["PAIR_ID", "Grammar_A", "Grammar_B", "Claimed_Relationship_Per_Source", "Classification",
          "Source_Citation"]
rows = [
["M-01","GR-01 (D1 Part I DTC)","GR-02 (D1 Part IV MDCL v1.0)",
 "Same composition ORDER (apply Delta, then tau/T, then kappa/C) and same 3 active primitives; "
 "developed independently. Source: 'The two grammars were developed independently and are not "
 "claimed here to be formally identical, but the convergence... is exactly the kind of "
 "cross-validation this paper series treats as evidence worth taking seriously'.",
 "OPEN (convergence noted, identity NOT claimed or proven)", "D1 Part IV Preface + Sec6"],
["M-02","GR-01 (D1 Part I DTC)","GR-03 (D1 Part IV v2.0, 6-primitive)",
 "GR-03's Delta,tau,kappa,Pi are 'directly identified' with GR-01's own by source text ('same as "
 "PRIM-G-00X' per prior PRF-PRIM computational work citing this identification). Theta,Omega are "
 "NEW additions with no GR-01 counterpart.",
 "EMBEDDING (partial, textual/direct -- confirmed computationally in this repository's own prior "
 "Phase-II PRF-PRIM work: F_AC/F_CA exact reconstruction; NOT re-derived in this document-only "
 "reconstruction pass)", "D1 Part IV Sec7.2"],
["M-03","GR-02 (D1 Part IV MDCL v1.0)","GR-04 (D1 Part V Sigma_0)",
 "Sigma_0={D,T,C,Pi} 'matches Part IV's v1.0 primitive set exactly' in SYMBOL SET, but D1's own "
 "Sec9 (Part V) states: 'Part V's canonical MDCL object M has not been shown to be the same object "
 "as the MDCL compiler documented throughout Part IV Sec1-Sec7... this paper does not assert their "
 "identity.'",
 "UNDEFINED / OPEN -- symbol-set match explicitly NOT treated as object identity by the source "
 "itself", "D1 Part V Sec9 (verbatim quote in table)"],
["M-04","GR-01 (D1 Part I DTC)","GR-04 (D1 Part V Sigma_0)",
 "Explicitly stated NOT to be a foundation for GR-01's composition order: 'it is not a foundation "
 "for either of the other two primitive grammars used elsewhere in this paper -- Part I Sec9's DTC "
 "composition... A reader could reasonably ask whether UGAS through MDCL-0001 could be rebuilt over "
 "either of those alphabets... That question is open; this part does not attempt it.'",
 "OPEN (explicitly unattempted by the source, not merely unresolved)", "D1 Part V Sec9"],
["M-05","GR-03 (D1 Part IV v2.0)","GR-04 (D1 Part V Sigma_0)",
 "Same as M-04: explicitly stated the foundation does not cover GR-03's six-primitive set either.",
 "OPEN (explicitly unattempted)", "D1 Part V Sec9"],
["M-06","GR-01 (D1 Part I DTC)","GR-06 (D1 Part III gradient chain)",
 "'They agree on more than they disagree: both treat constraint as generative rather than merely "
 "restrictive, both terminate in a persistence condition... They disagree on the starting primitive "
 "(a measurable gradient versus an abstract distinction) and on the number and ordering of "
 "intermediate stages. This paper does not adjudicate between them; a reconciliation, if one "
 "exists, is future work.'",
 "OPEN (source explicitly declines to adjudicate)", "D1 Part III Sec5"],
["M-07","GR-05 (D3 TOEv 5-primitive)","GR-01/GR-02/GR-03 (D1's DTC-family)",
 "No explicit cross-reference given in D3's own text; D3 promotes Relation to a primitive where "
 "D1's families derive relational structure from tau/edge-weights implicitly. No document in this "
 "corpus states or tests a translation between GR-05 and GR-01/02/03.",
 "UNDEFINED (no claimed relationship recovered from any source in this set)", "absence noted "
 "across D1, D3"],
["M-08","GR-08 (D5 Rosetta Grammar)","GR-01 (D1 Part I DTC)",
 "Shares symbols Delta,tau,kappa and the general 'distinction/transform/constrain' narrative but "
 "GR-08 omits Pi from the active composed triple (Pi appears only as pipeline output) and gives no "
 "formal definitions matching GR-01's homological/Liouville/idempotent-projector definitions. No "
 "explicit identification statement found in D5.",
 "UNDEFINED (surface notational overlap only; no source-stated identification)", "D5 Sec XIV vs D1 "
 "Sec9.1"],
["M-09","GR-07 (D4 SEIT.0 triple)","GR-01 (D1 Part I DTC) / GR-09 (Gamma(lambda))",
 "GR-07's Gamma (a generator/operator) is explicitly a DIFFERENT mathematical object from GR-01's "
 "composed Gamma=kappa.tau.Delta and from GR-09's scalar function Gamma(lambda) -- no source "
 "document identifies any two of these three uses of the symbol Gamma with each other.",
 "TYPE MISMATCH / SYMBOL COLLISION (same symbol, three distinct referents, no source-stated "
 "identification between any pair)", "D1 Sec9.2, D4 Sec0, D4 Sec2.2 (cross-read by this "
 "reconstruction; no single source states the collision)"],
["M-10","GR-10 (D2 PR-001..004)","GR-01/GR-02 (D1 DTC/MDCL-v1)",
 "PROBABLE but UNCONFIRMED: D2's downstream object names (K-DEF-001='Constraint Core K', "
 "CMRC-CHAIN-001, VAL-004, VAL-005, THERMO-TAX) are IDENTICAL strings to D1 Part IV/Part I object "
 "names, strongly suggesting D2 audits the same or a closely related underlying registry as D1's "
 "Part IV/Part I -- but D2's own text never gives PR-001..004 explicit mathematical definitions, so "
 "no formal identification with GR-01's Delta,tau,kappa,Pi (or GR-02's D,T,C,Pi) can be confirmed "
 "from the text available to this reconstruction.",
 "UNRESOLVED IDENTIFICATION (name-overlap evidence only, not a proof or explicit textual "
 "identification)", "cross-read D1 Part IV vs D2 throughout; see cross-document matrix"],
["M-11","GR-11 (D1 Part II UDP 5-primitive)","GR-01 (D1 Part I DTC)",
 "D1's own Conclusion to the whitepaper states both Part I and Part II 'independently arrive at a "
 "discrete-to-continuum compiler picture of physical law; Part I builds it from a pointed graph "
 "category, while Part II builds it from operator algebras and category theory' -- explicitly "
 "presented as two INDEPENDENT constructions, not shown equivalent.",
 "OPEN (explicitly parallel, independent constructions per the source's own framing)", "D1 Part II "
 "Abstract"],
]
os.makedirs(REPO + 'matrices', exist_ok=True)
with open(REPO + 'matrices/MORPHISM_TRANSLATION_MATRIX.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(header); w.writerows(rows)
print("Morphism matrix:", len(rows))

# ---------------- CROSS-DOCUMENT CONSISTENCY MATRIX ----------------
header2 = ["PAIR_ID", "Doc_A", "Doc_B", "Relationship", "Basis"]
rows2 = [
["C-01","D1","D2","DIFFERENT REPRESENTATION / PROBABLE REFINEMENT (unconfirmed)","D2 audits a "
 "registry (PR-001..004, K-DEF-001, ARBS-DEF-001, CMRC-CHAIN-001, VAL-004, VAL-005, THERMO-TAX) "
 "whose downstream object NAMES exactly match D1 Part IV/Part I objects, but D2 never gives "
 "primitive-level mathematical definitions matching D1's, so identity cannot be confirmed from text "
 "alone -- classified as probable same-underlying-project, different presentation layer (formal "
 "audit vs narrative derivation), not confirmed identical content."],
["C-02","D1","D3","REFINEMENT / DIFFERENT REPRESENTATION","D3 explicitly built as an "
 "analysis/visualization companion to 'eighteen research posters' spanning the same Laplacian-"
 "compiler and TOEv/SEIT material D1 covers narratively; D3 introduces its own 5-primitive TOEv "
 "set (GR-05) not identified with D1's DTC grammar (GR-01) by either document."],
["C-03","D1","D4","REFINEMENT (explicit, source-stated)","D4's own Prefatory Note: 'This document "
 "updates the Combined Compiler Theories Whitepaper in light of the full derivation audit... "
 "installs the Gamma(lambda) = Restoration/Degradation framework as the correct closure candidate "
 "for the persistence threshold lambda_c, replacing the earlier and incorrect identification "
 "lambda_c=lambda_1.' Scope of the update is EXPLICITLY LIMITED to lambda_c and SEIT-Layer-II "
 "derivation statuses -- D1 Parts I-III, IV Sec1-6, and V are NOT touched by D4."],
["C-04","D1","D5","CONDITIONAL RELATION / PARTIAL OVERLAP","D5's Sec II.4 Pi definition "
 "(lambda_n<lambda_c) and D1's Sec10.2 TRL both invoke the same lambda_c object without resolving "
 "it; D5's 13-phase architecture is a DIFFERENT, more recent construction than D1's Parts I/II/IV "
 "compiler pipelines, sharing vocabulary (graph Laplacian, heat kernel, spectral action) but not "
 "textually identified as the same pipeline by either document."],
["C-05","D2","D3","APPARENT CONFLICT / NO OVERLAP ESTABLISHED","No shared object names or explicit "
 "cross-reference found between D2's formal MCT/MCL audit registry and D3's poster-analysis "
 "content; treated as addressing different (or at least not textually connected) layers of the "
 "overall research program."],
["C-06","D2","D4","NO OVERLAP ESTABLISHED (with one narrow exception)","D2's OP-007 ('Spectral "
 "persistence threshold: derive lambda_c from the spectral data of D_Gn') is THE SAME open problem "
 "D4's entire Sec2-3 addresses (the Gamma(lambda)=1 closure attempt), even though D2 and D4 use "
 "different registry ID schemes and neither document cross-references the other by name -- "
 "identified here by CONTENT MATCH, not by an explicit source citation linking the two documents."],
["C-07","D2","D5","NO OVERLAP ESTABLISHED","No shared object names, registry IDs, or explicit "
 "cross-reference found."],
["C-08","D3","D4","SPECIAL CASE / PARTIAL OVERLAP","D3's Pi_0=(delta_spec-lambda_c)/sigma "
 "persistence functional (Sec VII.D, Sec IX) and D4's Gamma(lambda)-based lambda_c closure attempt "
 "both target the SAME open lambda_c quantity; D3 states 'the research program's central open "
 "problem is the derivation of lambda_c from Spec(L)' near-verbatim matching D4's own framing, "
 "though D3 gives no candidate closure route (Gamma(lambda) is D4-only) and D4 gives no explicit "
 "citation back to D3's Pi_0 formula."],
["C-09","D3","D5","DIFFERENT REPRESENTATION","D3's 5-level SEIT hierarchy (L0-L5) and D5's SEIT "
 "framing overlap in NAME (both titled/labeled 'SEIT') and in core apparatus (graph Laplacian, heat "
 "kernel, persistence sector) but D3 is presented as a poster/visualization companion while D5 "
 "presents a 13-phase 'Universal Compiler Architecture' with explicit derivation claims; neither "
 "document cross-references the other explicitly."],
["C-10","D4","D5","ACTUAL CONFLICT, EXPLICITLY RESOLVED BY SUPERSESSION","D4 explicitly names and "
 "retracts multiple specific claims that appear with full confidence in D5 (lambda_c=lambda_1; the "
 "166.48 Hz GW prediction; the ~135pc dwarf-core-radius prediction; the SU(3)xSU(2)xU(1) anomaly-"
 "cancellation derivation labeled 'derived, not postulated'). D4's Prefatory Note frames itself "
 "explicitly as the corrective audit: 'Items that were previously mislabeled as derived are now "
 "accurately labeled as open.' Per D4's own SUPERSEDED framing, this reconstruction treats D4 as "
 "authoritative over D5 on every point D4 explicitly revises, and preserves D5's un-revised content "
 "(Heat Kernel Bridge, Spectral Metric Formula, Euler-Lagrange field-equation derivation) at its "
 "own originally-stated status -- D4 does not touch these, so they are NOT silently downgraded."],
]
with open(REPO + 'matrices/CROSS_DOCUMENT_CONSISTENCY_MATRIX.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(header2); w.writerows(rows2)
print("Cross-doc matrix:", len(rows2))
