import csv, os
REPO = '/home/user/TOEv/governing_corpus/'

header = ["ITEM_ID", "Source_Doc", "Object", "Status_As_Stated_By_Source", "Status_Normalized",
          "Dependency", "Note"]
rows = []

# --- D4 Sec1 Derivation Audit Matrix (verbatim transcription, its own 5-code system) ---
d4_matrix = [
("Distinction Delta","Primitive axiom","Derived","Complete"),
("Graph G=(V,E)","Primitive ontology","Derived","Complete"),
("Adjacency A","From G","Derived","Complete"),
("Degree D","From A","Derived","Complete"),
("Laplacian L=D-A","From A, D","Derived","Complete"),
("Spectrum {lambda,psi}","Eigenproblem of L","Derived","Complete"),
("Heat kernel e^{-beta L}","Spectral theorem","Derived","Complete"),
("Omega attractor","beta->inf limit","Derived","Formal convergence proof still needed"),
("Spectral distance d(i,j)","Spectrum -> distance","Derived","Continuum limit; mostly complete"),
("Metric g_mu_nu","From d(i,j)","Derived","Smooth embedding assumed; mostly complete"),
("Curvature R_mu_nu","Differential geometry","Derived","Standard geometry; complete"),
("Einstein tensor G_mu_nu","From metric","Derived","Complete"),
("Persistence functional C_Pi","Variational definition","Derived","Fisher metric choice justified"),
("Field equation SEIT.1","Euler-Lagrange from C_Pi","Derived","Full derivation complete"),
("GR limit","SEIT.1, I_F=0","Derived","Complete"),
("Replicator limit","SEIT.1, Shahshahani g","Derived","Complete"),
("Diffusion limit","SEIT.1, Wasserstein g","Derived","Complete"),
("FEP limit","SEIT.1, Fisher g","Derived","Complete"),
("R(lambda)=e^{-beta lambda}","Heat kernel","Derived","Complete -- no new parameters"),
("D1(lambda)=lambda","Heat-kernel decay rate","Derived","Falls directly from -d/dbeta ln R_n"),
("D2(lambda)=beta*lambda^2","Entropy production","Partial","lambda = transition rate assumption needs proof"),
("D3(lambda)=sqrt(lambda)","Cheeger leakage","Partial","Nodal-domain scaling not yet proven"),
("Gamma(lambda) = Resto./Degr.","C_Pi projection","Partial","Correct target; projection integral not yet evaluated"),
("lambda_c existence","R=D crossing","Partial","Exists if R down, D up; monotonicity not proven"),
("lambda_c uniqueness","Monotonic crossing","Partial","Requires Gamma strictly decreasing"),
("lambda_c != lambda_1 (Fiedler)","CORRECTED","Partial","lambda_c=lambda_1 gives trivial Pi={zero mode}. Retracted."),
("lambda_c running with beta","Root of e^{-beta lambda}=D(lambda)","Partial","beta is the filtering depth; flow equation not explicit"),
("Persistence sector Pi","lambda<lambda_c","Partial","Depends on lambda_c closure"),
("Mass formula m_n=m0*sqrt(lambda_n)","Spectral sector","Partial","Formula motivated; m0 normalization open"),
("Couplings alpha_k=<psi|P_k|psi>","Spectral overlap","Partial","Correct form; P_k boundaries not derived"),
("Electroweak boundary","UTT phase transition","Partial","Scale imported; internal derivation needed"),
("QCD boundary","UTT phase transition","Partial","Scale imported; internal derivation needed"),
("Anomaly cancellation","Algebraic consistency","Partial","Depends on gauge derivation"),
("RG flow SEF.24","Callan-Symanzik","Partial","beta-function form not yet specified"),
("CMB tilt n_s","N_sub constraint","Partial","n_s and N_sub are locked; neither derived independently"),
("Mass scale m0","Planck closure attempt","Open","Unit audit incomplete; full closure required"),
("Projectors P_k","Spectral sector boundaries","Open","Boundaries asserted; must derive from UTT transitions"),
("Force sector count = 3","Low/Mid/High lambda","Open","Classification only; theorem not proven"),
("Gauge group SU(3)xSU(2)xU(1)","Octonion/Spin(8) route","Open","Inclusion asserted, not derived; E8/SO(10) alternatives not ruled out"),
("N_sub","Cosmological sector","Open","Not closed; may be derivable from spectral dimension at Hubble radius"),
("Graph G reconstruction","Inverse spectral problem","Undecidable","Cubitt-Perez-Garcia-Wolf; likely impossible"),
("hbar, c, G_N","Physical constants","Empirical","External measurements; framework inputs"),
]
for i, (obj, src, stat, res) in enumerate(d4_matrix, 1):
    norm = {"Derived": "CALCULATED/DERIVED (source's own 'Derived' tag; NOTE: not equivalent to "
            "this repository's UNIVERSALLY DERIVED -- most 'Derived' rows carry a residual caveat "
            "in the Resolution column, e.g. 'proof still needed', 'mostly complete')",
            "Partial": "CONDITIONAL/CANDIDATE", "Open": "OPEN", "Undecidable": "NO-GO (structural, "
            "cited external theorem)", "Empirical": "ADMITTED EXTERNAL INPUT"}[stat]
    rows.append([f"D4-{i:02d}", "D4", obj, f"{stat} -- {res}", norm, src, "Verbatim from D4 Sec1 "
                 "Derivation Audit Matrix (SEIT v4.0), the source's own self-audit."])

# --- D1 Part 0 Sec0.5 CCR Ledger (verbatim) ---
d1_ccr = [
("MDCL v1.0 -- Primitive Grammar","Part IV, Preface","Certified","--"),
("CMRC-001-019 (String Theory Recovery Core)","Part IV Sec1","Certified","CMRC-001"),
("VAL-005 (Hamiltonian Mechanics)","Part IV Sec2","Certified","MDCL-1015"),
("VAL-004 (Quantum Mechanics)","Part IV Sec3","Certified","VAL-005"),
("MDCL v2.0, Layers 0-VI (Graph-Spectral GR Recovery)","Part IV Sec7.1-7.4","Certified","Primitive Kernel"),
("MDCL v2.0, Layer VII (Physical Recovery Core)","Part IV Sec7.5","Research Objective","Layer VI"),
("MDCL v2.0, Layers VIII-XIII (Architecture Roadmap)","Part IV Sec7.6","Research Objective","Layer VII"),
("UGAS (Free Grammar Algebra)","Part V Sec1","Certified","Sigma_0"),
("UGCT (Congruence & Quotient)","Part V Sec2","Certified","UGAS"),
("UGUP (Universal Mapping Property)","Part V Sec3","Certified","UGCT"),
("UGNT (Normal Form Theory)","Part V Sec4","Certified (framework); theorems Open","UGUP"),
("UGIT (Intrinsic Grammar Theory)","Part V Sec5","Certified","UGNT"),
("UOLS (Organizational Semantics)","Part V Sec6","Certified","UGIT"),
("UTS (Universal Type System)","Part V Sec7","Certified","UOLS"),
("MDCL-0001 (Canonical MDCL Object)","Part V Sec8","Certified","UTS"),
("MDCL-0002 (Category of MDCL Objects)","not received","Research Objective","MDCL-0001"),
("LOR-002 (Negative Eigenvector)","Part IV Sec8.3","Certified","LOR-001"),
("LOR-001 (Resistance Threshold)","Part IV Sec8.4","Candidate","Effective Resistance, Rank-One Inertia"),
("IOC Rank-One (Index Classification)","Part IV Sec8.5","Certified target","LOR-001"),
("IOC Rank-Two","Part IV Sec8.5","Open","IOC Rank-One"),
("IOC Rank-k","Part IV Sec8.5","Research Objective","IOC Rank-Two"),
("Fisher Information Route","Part IV Sec8.6","Retired","--"),
("Standard Signed Laplacian","Part IV Sec8.6","Retired","--"),
("Classical Balance-Theory Route","Part IV Sec8.6","Retired","--"),
]
for i, (obj, loc, stat, dep) in enumerate(d1_ccr, 1):
    rows.append([f"D1-CCR-{i:02d}", "D1", obj, stat, stat.upper().split(' ')[0].split('(')[0].strip() or stat,
                 dep, f"Verbatim from D1 Part 0 Sec0.5 CCR Ledger, location {loc}."])

# --- D2 CVR-001 open problems + conditional certifications ---
d2_open = [
("OP-001","TH-ARBS-001A: Bipartite Reciprocity Lock -- prove ARBS bipartite structure preserved "
 "under all admissible graph morphisms","Open -- no partial proof","High"),
("OP-002","TH-ARBS-001B: Shell Nilpotency Lock -- prove shell adjacency satisfies nilpotency "
 "conditions required for the recovery functor domain category","Open -- no partial proof","High"),
("OP-003","R -> D transition: what structure generates distinguishability from relational structure "
 "without presupposing distinguishability?","Open -- symmetry breaking is partial candidate","Medium"),
("OP-004","Organizational tensor -> metric derivation: close pipeline from ARBS tensor T to "
 "Riemannian metric g_mu_nu","Blocked by OP-001 and OP-002","High"),
("OP-005","Symmetry Characterization Conjecture: does Ce=0 imply an automorphism fixing both p_0 "
 "and e?","Open -- 300 random trials show no counterexample","Medium"),
("OP-006","M* quantitative scaling law: functional relationship between M* and K-reconstruction "
 "time","Open -- qualitative relationship supported","Medium"),
("OP-007","Spectral persistence threshold: derive lambda_c from spectral data of D_{G_n}","Open -- "
 "physical interpretation established","Low"),
("OP-008","Constraint Core K self-grounding: prove K is sufficient for existence of a symmetry "
 "group","Open -- hypothesis stated, derivation not begun","Medium"),
]
for opid, stmt, res, prio in d2_open:
    rows.append([f"D2-{opid}", "D2", stmt, res, "OPEN", "priority=" + prio, "Verbatim from D2 CVR-001 "
                 "Sec8 Open Problems Register. NOTE: D2-OP-007 is the SAME lambda_c object as D1's "
                 "Sec10.2 open item and D4's entire Sec2-3 (Central Lock). D4 supplies a candidate "
                 "closure route (Gamma(lambda)=1) but D4 itself still marks it Partial/Open -- this "
                 "does not close D2-OP-007, it refines what closing it would require."])

d2_cond = [
("RF-001", "OP-001, OP-002", "Both TH-ARBS-001A and TH-ARBS-001B proven and admitted to MCT"),
("RF-002", "OP-001, OP-002 (via RF-001)", "RF-001 upgraded to Certified"),
("RF-003", "OP-001, OP-002 (via RF-001, RF-002)", "RF-002 upgraded to Certified"),
("RF-004", "OP-001, OP-002 (via RF-001-003)", "RF-003 upgraded to Certified"),
]
for rid, opdep, upgrade in d2_cond:
    rows.append([f"D2-{rid}", "D2", f"{rid} (Recovery Registry theorem)", "Conditional-Certified",
                 "CONDITIONAL", opdep, f"Upgrade condition: {upgrade}. Verbatim from D2 Sec9 "
                 "Conditional Certification Tracker. CMRC-CHAIN-001/VAL-004/VAL-005 are marked "
                 "Certified in D2's own MCT but D2 Sec5 explicitly flags they carry an INHERITED "
                 "conditional dependency via RF-004 on OP-001/OP-002 -- 'a presentation note, not a "
                 "certification failure' in D2's own words, but preserved here as a genuine "
                 "CALCULATED-vs-UNIVERSALLY-DERIVED distinction, not smoothed over."])

# --- D5 self-declared open problems ---
d5_open = [
("OPEN-1","Born Rule (Phase II): rigorous proof that the R-invariant measure on the persistence "
 "sector is unique and equals |psi|^2 -- existence outlined, uniqueness proof incomplete"),
("OPEN-2","Lorentz Signature (Phase III): more rigorous treatment of the relationship between the "
 "compression functional Gamma=-dS/dt and the signature of the emergent metric"),
("OPEN-3","Three Generations: anomaly cancellation derives N_c=3 but does not explain exactly "
 "three fermion generations"),
("OPEN-4","Universal Constants (Phase I): explicit computation of fixed-point functions "
 "f_k in c=f_1(rho), G=f_2(rho), hbar=f_3(rho) -- pipeline defined, functions not yet computed"),
("OPEN-5","G_Nature (Phase XIII): identifying the specific adjacency matrix A such that "
 "Spec(L)=Spec(Nature) -- may have no finite algorithmic solution (Cubitt-Perez-Garcia-Wolf)"),
]
for oid, stmt in d5_open:
    rows.append([f"D5-{oid}", "D5", stmt, "Open (self-declared)", "OPEN", "-", "Verbatim from D5 "
                 "Sec XIII Open Problems, stated by the source itself as part of its 'scientific "
                 "integrity'."])

# --- D5 predictions later retracted by D4 ---
retracted = [
("D5-RETR-01","166.48 Hz monochromatic gravitational-wave background (D5 Sec XI, XII)",
 "D5: live falsifiable prediction, no caveat. D4 Sec7: 'GW line at 166 Hz (retracted). Axion mass "
 "ansatz not derivable from SEIT.1 and conflicts with fuzzy-DM physics. Dropped.'"),
("D5-RETR-02","Dwarf spheroidal soliton core radii 120-150 pc (D5 Sec XI)",
 "D5: live falsifiable prediction. D4 Sec7: 'Dwarf galaxy core radii ~135 pc (retracted). "
 "Inconsistent with observed diversity (Fornax ~700 pc, Draco <50 pc). Dropped.'"),
("D5-RETR-03","lambda_c implicit as lambda_1 (Fiedler value) via Pi={psi_n: lambda_n<lambda_c} "
 "(D5 Sec II.4, no caveat stated)",
 "D4 Sec2.4: 'This derivation attempt was incorrect and is retracted... gives Pi = {zero mode "
 "only} -- the vacuum. The persistence sector is trivial and the entire downstream cascade "
 "collapses.'"),
("D5-RETR-04","G_SM=SU(3)xSU(2)xU(1) 'derived, not postulated' via anomaly cancellation "
 "(D5 Sec VIII.2)",
 "D4 Sec1 matrix: 'Gauge group SU(3)xSU(2)xU(1) | Octonion/Spin(8) route | Open | Inclusion "
 "asserted, not derived; E8/SO(10) alternatives not ruled out'."),
]
for rid, obj, note in retracted:
    rows.append([rid, "D5 (superseded by D4)", obj, "SUPERSEDED / RETRACTED", "SUPERSEDED", "D4",
                 note])

os.makedirs(REPO + 'registries', exist_ok=True)
with open(REPO + 'registries/STATUS_LEDGER.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
print("Status ledger written:", len(rows))
