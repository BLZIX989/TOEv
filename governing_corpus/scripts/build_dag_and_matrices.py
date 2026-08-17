import csv, os
REPO = '/home/user/TOEv/governing_corpus/'

# ---------------- DAG ----------------
node_header = ["NODE_ID", "Source_Doc", "Name", "Type", "Status"]
nodes = [
["N-D1-01","D1","Pointed Graph Category (G-bullet)","CATEGORY","DEFINED"],
["N-D1-02","D1","Refinement Endofunctor R","FUNCTOR","DEFINED"],
["N-D1-03","D1","Graph-Theoretic Axiom Set A-star","AXIOM_SET","DEFINED"],
["N-D1-04","D1","Discrete Geometry Category (Discrete Exterior Calculus)","CATEGORY","DEFINED"],
["N-D1-05","D1","Compiler functor c: G-bullet -> Discrete-Geom","FUNCTOR","DEFINED"],
["N-D1-06","D1","Optimization Operator O_opt / Action Functional","FUNCTIONAL","DEFINED"],
["N-D1-07","D1","Critical Attractor Set K_crit (fixed point)","FIXED_POINT","CANDIDATE (conditional "
 "on Strict Convexity lambda_min(H)>=m>0)"],
["N-D1-08","D1","DTC Grammar Gamma=kappa.tau.Delta (GR-01)","OPERATOR","DEFINED"],
["N-D1-09","D1","Thermodynamic Realization Layer (TRL) axioms","AXIOM_SET","DEFINED"],
["N-D1-10","D1","Persistence threshold lambda_c (TRL reading)","PARAMETER","OPEN (explicit: 'A full "
 "derivation of lambda_c from the spectral data of D_Gn remains an open problem and is not claimed "
 "here')"],
["N-D1-11","D1","Organizational Selection Cascade (4-gate P_T = Ce.Cpi.Ct.Cp)","OPERATOR_CHAIN",
 "DEFINED (identity with P_T of Sec1 stated as 'the precise sense' of refinement, not proven "
 "independently)"],
["N-D1-12","D1","Discrete Cartan Identity / Weitzenboeck-Lichnerowicz Formula","THEOREM","CERTIFIED "
 "(complete derivation shown in text, Sec5.1-5.2)"],
["N-D1-13","D1","Strong Resolvent / Heat Kernel / Atiyah-Singer continuization theorems","THEOREM",
 "CERTIFIED (proof sketches given, standard theorems cited: Kato, Trotter-Kato, McKean-Singer)"],
["N-D1-14","D1","Compiler Completeness Conjecture (existence of A-star, c)","CONJECTURE","OPEN"],
["N-D1-15","D1","Structural Minimality Conjecture","CONJECTURE","OPEN"],
["N-D1-16","D1","CMRC-001..019 chain (worldsheet to vacuum Einstein eqns)","DERIVATION_CHAIN",
 "CERTIFIED (VAL-001, with 3 explicit certification refinements)"],
["N-D1-17","D1","VAL-004 Quantum Mechanics (canonical quantization)","DERIVATION_CHAIN","CERTIFIED "
 "(2 explicit refinements: Groenewold-Van Hove obstruction scoping, representation-choice scoping)"],
["N-D1-18","D1","VAL-005 Hamiltonian Mechanics (symplectic/Poisson)","DERIVATION_CHAIN","CERTIFIED"],
["N-D1-19","D1","MDCL v2.0 Einstein tensor recovery (graph-spectral route)","DERIVATION_CHAIN",
 "CERTIFIED (vacuum only)"],
["N-D1-20","D1","MDCL v2.0 Layer VII (matter coupling, Tmunu, EFE-with-matter, geodesic eqn, "
 "Newtonian limit)","TARGET_SET","OPEN (explicit 'Target -- not yet recovered', all 5 rows)"],
["N-D1-21","D1","Lorentzian Metric Recovery Program dependency tree","DERIVATION_CHAIN","PARTIAL -- "
 "certified through negative eigenvector (LOR-002); 'Localization' onward fully OPEN"],
["N-D1-22","D1","Universal Organizational Foundation spine (UGAS..MDCL-0001, Sigma_0)","ALGEBRAIC_"
 "FOUNDATION","CERTIFIED framework / OPEN termination-confluence theorems (see GR-04)"],
["N-D2-01","D2","PR-001..004 (4 primitives)","PRIMITIVE_SET","DEFINED (Layer 0)"],
["N-D2-02","D2","TH-PR-005 / TH-PR-005-L1 (theorem+lemma)","THEOREM","PROVEN"],
["N-D2-03","D2","K-DEF-001 (Constraint Core K)","OBJECT","DEFINED"],
["N-D2-04","D2","TH-K-001","CONJECTURE","OPEN"],
["N-D2-05","D2","ARBS-DEF-001 (+scaling laws, TH-ARBS-001A/B)","OBJECT+THEOREM_SET","CERTIFIED "
 "(definition) / OPEN (both locks, OP-001/OP-002)"],
["N-D2-06","D2","CE-THM-001..005, SCC-001","THEOREM_CHAIN","CERTIFIED (001-005) / OPEN (SCC-001)"],
["N-D2-07","D2","RF-001..004 (Recovery Functor chain)","THEOREM_CHAIN","CONDITIONAL-CERTIFIED"],
["N-D2-08","D2","CMRC-CHAIN-001, VAL-004, VAL-005 (as audited)","RECOVERY_MODULE","CERTIFIED with "
 "inherited conditional dependency (via RF-004 on OP-001/OP-002)"],
["N-D2-09","D2","THERMO-TAX-001..003","OBJECT+THEOREM_SET","CERTIFIED/PROVEN"],
["N-D3-01","D3","Delta/G/A/D/L/{lambda,psi}/H(t)/g_ij/L*/P_ss/sigma/Pi_0 pipeline (11 stages)",
 "DERIVATION_CHAIN","PROPOSED (analysis/visualization protocol, not itself a proof chain)"],
["N-D3-02","D3","Pi_0 = (delta_spec - lambda_c)/sigma (persistence order parameter)","FUNCTIONAL",
 "OPEN (depends on lambda_c, same open object as N-D1-10, D2-OP-007)"],
["N-D4-01","D4","SEIT.0 triple (Sigma,Gamma,Pi) (GR-07)","PRIMITIVE_SET","PROPOSED"],
["N-D4-02","D4","Canonical reconstruction spine (Phase XII)","DERIVATION_CHAIN","stage-by-stage "
 "status recorded in STATUS_LEDGER D4-01..D4-18 (mostly Derived, with residual caveats)"],
["N-D4-03","D4","Persistence Cost Functional C_Pi / Field equation SEIT.1","FUNCTIONAL+EQUATION",
 "DERIVED (per D4's own audit, 'full derivation complete')"],
["N-D4-04","D4","Gamma(lambda)=Restoration/Degradation, lambda_c (GR-09)","FUNCTION+PARAMETER",
 "PARTIAL/OPEN -- ranked priority-1 target"],
["N-D5-01","D5","Universal Distinction Graph G=(V,E) (sole primitive object)","PRIMITIVE_OBJECT",
 "DEFINED"],
["N-D5-02","D5","Heat Kernel Bridge (graph Laplacian -> continuum Laplace-Beltrami)","THEOREM",
 "stated as proven in text (continuum convergence eqn 3.5); not independently re-verified by this "
 "reconstruction"],
["N-D5-03","D5","Spectral Metric Formula g_munu = sum_k lambda_k^-1 dpsi_k dpsi_k","EQUATION",
 "DEFINED/stated as derivation, not independently re-verified"],
["N-D5-04","D5","Universal Persistence Field Equation (Euler-Lagrange of C_Pi)","EQUATION","stated "
 "as 'Derived by full Euler-Lagrange variation' -- CONSISTENT with D4's independent 'Derived, full "
 "derivation complete' status for the same object (cross-document AGREEMENT, not merely D5's own "
 "claim)"],
["N-D5-05","D5","13-phase Universal Compiler Architecture (Born rule..inverse spectral)","DERIVATION_"
 "CHAIN_SET","MIXED -- individual phase status per D5's own Sec XIII (5 open problems named) and "
 "per D4's audit matrix where the SAME objects are covered (Born rule, Lorentz signature, gauge "
 "group; D4 assigns Partial/Open where D5's main text asserts completion)"],
["N-D5-06","D5","G_SM=SU(3)xSU(2)xU(1) anomaly-cancellation derivation","THEOREM_CLAIM","SUPERSEDED "
 "by D4 (see STATUS_LEDGER D5-RETR-04) -- D5's own text calls it 'derived, not postulated'; D4's "
 "audit downgrades to Open"],
["N-D5-07","D5","Falsifiable predictions (GW 166.48Hz, dwarf core radii, N_sub/CMB tilt)","PREDICTION_"
 "SET","2 of 3 SUPERSEDED/RETRACTED by D4 (see STATUS_LEDGER D5-RETR-01/02); CMB tilt n_s prediction "
 "NOT retracted by D4, carried forward as Partial ('agreement... is real but derivation of N_sub is "
 "open')"],
]

edge_header = ["EDGE_ID", "UPSTREAM", "DOWNSTREAM", "RELATION", "SOURCE_STATEMENT", "SOURCE_DOC"]
edges = [
["E-01","N-D1-01","N-D1-02","refinement functor acts on","'strict covariant functor R: G-bullet -> "
 "G-bullet'","D1"],
["E-02","N-D1-02","N-D1-04","compiler maps refined graphs into","'algorithmic compiler c: G-bullet "
 "-> Discrete-Geom maps the pointed graph sequence directly into DEC'","D1"],
["E-03","N-D1-04","N-D1-06","Hilbert space of discrete geometry hosts","'Optimization Operator... "
 "running within the discrete Hilbert space'","D1"],
["E-04","N-D1-06","N-D1-07","gradient-descent convergence yields","'network is mathematically forced "
 "to converge to the unique macroscopic Fixed Point'","D1"],
["E-05","N-D1-08","N-D1-02","Gamma is the DTC-level description of","'Iterating this map is the "
 "DTC-level description of the same refinement functor R'","D1"],
["E-06","N-D1-09","N-D1-07","recasts critical attractor set in throughput terms","'Axiom 6 recasts "
 "the critical attractor set of Sec3.2 in thermodynamic terms'","D1"],
["E-07","N-D1-09","N-D1-10","persistence threshold given physical reading by","'This gives the "
 "persistence threshold lambda_c a physical reading'","D1"],
["E-08","N-D1-11","N-D1-05","four gates compose to reconstruct continuization functor","'Composing "
 "all four gates reconstructs the single continuization functor'","D1"],
["E-09","N-D1-05","N-D1-16","compiler pipeline instantiated as CMRC worldsheet chain","'CMRC is the "
 "recovery branch bridging the general mathematical kernel to physical ontology'","D1"],
["E-10","N-D1-16","N-D1-17","VAL-004 extends the Hamiltonian branch, itself downstream of variational "
 "core shared with CMRC","'VAL-005 is a specialization rooted in the variational core'","D1"],
["E-11","N-D1-18","N-D1-17","VAL-004 extends VAL-005 through canonical quantization","'VAL-004 "
 "extends the Hamiltonian branch through Dirac's canonical quantization'","D1"],
["E-12","N-D1-08","N-D1-19","MDCL v2.0 six-primitive extension of the DTC-adjacent grammar (Delta,"
 "tau,kappa carried over) underlies graph-spectral GR route","'v2.0 certifies six primitives rather "
 "than three or four... Delta,tau,kappa... carry over directly'","D1"],
["E-13","N-D1-19","N-D1-20","vacuum Einstein tensor certified; matter coupling explicitly NOT yet "
 "recovered downstream of it","'Layer VII, covering the coupling of geometry to matter, is labeled "
 "in the source material itself as not yet recovered'","D1"],
["E-14","N-D1-21","N-D1-08","Lorentzian program's dependency tree begins from the same Primitive "
 "Grammar node","'Primitive Grammar -> Graph -> Positive Laplacian -> ...'","D1"],
["E-15","N-D1-22","N-D1-08","Sigma_0={D,T,C,Pi} formalizes A grammar SHARING SYMBOLS with GR-02, "
 "NOT proven identical to GR-01/N-D1-08","'Sigma_0=Part IV's v1.0 primitive set... not a foundation "
 "for either of the other two primitive grammars'","D1"],
["E-16","N-D2-01","N-D2-02","TH-PR-005-L1/TH-PR-005 proven from PR-001..004 (Layer 0 -> Layer 1/2)",
 "MCL chain links CL-0001-0005, Dependency Completeness audit","D2"],
["E-17","N-D2-01","N-D2-03","K-DEF-001 depends on PR-003, PR-004","MCL CL-0007/0008","D2"],
["E-18","N-D2-03","N-D2-04","TH-K-001 depends on K-DEF-001","MCL CL-0009","D2"],
["E-19","N-D2-01","N-D2-05","ARBS-DEF-001 depends on PR-001..004","MCL CL-0010-0013","D2"],
["E-20","N-D2-05","N-D2-06","CE-THM-001 depends on ARBS-0006..0008 (synchronized w/ ARBS registry)",
 "MCL CL-0019-0021","D2"],
["E-21","N-D2-05","N-D2-07","RF-001 depends on TH-ARBS-001A/001B (both OPEN) + external imports",
 "MCL CL-0027-0028; Layer 9 'conditional' annotation","D2"],
["E-22","N-D2-07","N-D2-08","CMRC-CHAIN-001/VAL-004/VAL-005 depend on RF-004","MCL CL-0034 + "
 "extension; Dimension-4 audit note on inherited conditionality","D2"],
["E-23","N-D2-02","N-D2-09","THERMO-TAX chain depends on OR-001 line (itself from TH-PR-005)",
 "Dependency table, D2 Sec3","D2"],
["E-24","N-D3-01","N-D3-02","Pi_0 computed as final stage of the 11-stage pipeline","D3 Sec IX table, "
 "row 'Persistence | Pi_0'","D3"],
["E-25","N-D1-10","N-D3-02","SAME lambda_c object referenced across documents (not identical "
 "definitions given, but explicitly the same named open quantity)","D1 Sec10.2 + D3 Sec IX + "
 "D3 Summary ('central open problem... derivation of lambda_c from Spec(L)')","D1,D3"],
["E-26","N-D4-01","N-D4-02","canonical reconstruction spine grounds the SEIT.0 triple in established "
 "mathematics stage by stage","D4 Sec0 table + Sec4.1 spine","D4"],
["E-27","N-D4-02","N-D4-03","persistence functional stage of the spine yields C_Pi / SEIT.1",
 "D4 Sec0 chain 'Pi -> A -> sigma(A)...'; D4 Sec1 rows 'Persistence functional C_Pi', 'Field "
 "equation SEIT.1'","D4"],
["E-28","N-D4-03","N-D4-04","Gamma(lambda) is explicitly built FROM the SAME forcing term "
 "(g^{ca}grad_a I_F) that appears in SEIT.1","D4 Sec2.2: 'Both...are projections of the same "
 "object: the forcing term g^ca grad_a I_F in SEIT.1'","D4"],
["E-29","N-D1-10","N-D4-04","D4's Gamma(lambda) framework is explicitly presented as the corrected "
 "successor candidate for the SAME lambda_c object D1 Sec10.2 left fully open","D4 Prefatory Note: "
 "'installs the Gamma(lambda)... framework as the correct closure candidate for the persistence "
 "threshold lambda_c'","D1,D4"],
["E-30","N-D5-01","N-D5-02","heat kernel bridge built directly on the sole primitive graph object",
 "D5 Sec III: 'The heat kernel connects the graph Laplacian to the continuum spacetime Laplacian'",
 "D5"],
["E-31","N-D5-02","N-D5-03","spectral metric formula built on heat-kernel-derived diffusion distance",
 "D5 Sec IV.1 eqn 4.1 uses exp(-2t lambda_n) terms from the heat kernel","D5"],
["E-32","N-D5-03","N-D5-04","persistence field equation's Hessian metric g_ab is the SAME kind of "
 "object as (but not textually identified with) the spectral metric g_munu of Sec IV","D5 Sec VI.1 "
 "eqn 6.3 g_ab=-(d^2S/dy^a dy^b); NOT explicitly unified with Sec IV's g_munu in D5's own text -- "
 "flagged as an internal ambiguity, not resolved by this reconstruction"],
["E-33","N-D5-04","N-D4-03","SAME field equation independently confirmed 'Derived, full derivation "
 "complete' by D4's separate audit -- genuine cross-document AGREEMENT","D4 Sec1 row 'Field "
 "equation SEIT.1 | Euler-Lagrange from C_Pi | Derived | Full derivation complete'","D4,D5"],
["E-34","N-D5-05","N-D5-06","gauge-group derivation is one phase of the 13-phase architecture "
 "(Phase VIII/anomaly cancellation, Sec VIII.2)","D5 Sec VIII.2","D5"],
["E-35","N-D5-06","N-D4-01","D4's audit (rooted in the SAME SEIT.0-grounded reconstruction) "
 "downgrades this specific claimed theorem to Open","D4 Sec1 matrix row 'Gauge group...'; SUPERSEDES "
 "relation, see STATUS_LEDGER D5-RETR-04","D4"],
]
# fix truncated E-32 row (missing SOURCE_DOC)
edges[-4] = ["E-32","N-D5-03","N-D5-04","persistence field equation's Hessian metric g_ab is the "
 "SAME kind of object as (but not textually identified with) the spectral metric g_munu of Sec IV",
 "D5 Sec VI.1 eqn 6.3 g_ab=-(d^2S/dy^a dy^b); NOT explicitly unified with Sec IV's g_munu in D5's "
 "own text -- flagged as an internal ambiguity, not resolved by this reconstruction","D5"]

os.makedirs(REPO + 'dag', exist_ok=True)
with open(REPO + 'dag/GOVCORPUS_DAG_NODES.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(node_header); w.writerows(nodes)
with open(REPO + 'dag/GOVCORPUS_DAG_EDGES.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(edge_header); w.writerows(edges)

# cycle check
import collections
adj = collections.defaultdict(list)
node_ids = {n[0] for n in nodes}
for e in edges:
    u, d = e[1], e[2]
    if u in node_ids and d in node_ids:
        adj[u].append(d)
def find_cycles():
    WHITE,GRAY,BLACK=0,1,2
    color=collections.defaultdict(int); cycles=[]
    def dfs(u,path):
        color[u]=GRAY; path.append(u)
        for v in adj[u]:
            if color[v]==GRAY:
                idx=path.index(v); cycles.append(path[idx:]+[v])
            elif color[v]==WHITE:
                dfs(v,path)
        path.pop(); color[u]=BLACK
    for n in list(adj.keys()):
        if color[n]==WHITE: dfs(n,[])
    return cycles
cycles = find_cycles()
with open(REPO + 'dag/GOVCORPUS_DAG_CYCLE_AUDIT.txt','w') as f:
    f.write(f"Nodes: {len(nodes)}  Edges: {len(edges)}\n")
    if cycles:
        f.write(f"CYCLES DETECTED ({len(cycles)}):\n")
        for c in cycles: f.write("  " + " -> ".join(c) + "\n")
    else:
        f.write("No cycles detected.\n")
print("DAG written:", len(nodes), "nodes,", len(edges), "edges. Cycles:", len(cycles))
