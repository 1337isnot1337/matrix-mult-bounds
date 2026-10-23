"""Exact replay of four two-stage U/W split border families and anchor cap.

Requires only the standard library and the pinned predecessor modules.
Use --enumerate to compile anchor.c and replay every 23,426 anchor triple.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PRIOR=HERE.parent/"2026-10-23-mixed-leg-splits"
CLAIM="AI-EXTERNAL-DOUBLE-LEG-ANCHOR-012"
VARIANTS={"24-30":((24,26),(30,32)),
          "24-32":((24,26),(32,30)),
          "26-30":((26,24),(30,32)),
          "26-32":((26,24),(32,30))}
SOURCE_SHA="bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3"
BASIS_SHA="12cedfc73b6de98bb302b93941c05027b8acc41df03e4606b99363cb323e1c91"
EXPECTED_POSITIVE={"24-30":527,"24-32":513,"26-30":534,"26-32":533}

def req(cond,why):
    if not cond: raise AssertionError(why)

def import_file(label,path):
    spec=importlib.util.spec_from_file_location(label,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

M=import_file("prior_mixed_leg_seed",PRIOR/"verify.py")
V=M.V
G=M.G

def original_and_bases():
    M.check_source_pins()
    req(hashlib.sha256((ROOT/"research/ai/2026-10-21-external-grid-seed/factors.json").read_bytes()).hexdigest()==SOURCE_SHA,"source pin")
    basefile=HERE.parent/"2026-10-23-flip-escape"/"five_split_certificate.json"
    req(hashlib.sha256(basefile.read_bytes()).hexdigest()==BASIS_SHA,"basis pin")
    b=json.loads(basefile.read_text())
    bases=[[[Fraction(t) for t in row] for row in matrix] for matrix in b["basis_matrices"]]
    req([V.determinant(z) for z in bases]==[1,1,-1],"nonunimodular physical bases")
    return V.load_seed(),bases

def construct(original,pairs):
    surviving,discarded=M.mixed_seed(original)
    for i,j in pairs:
        req(i in (24,26,30,32) and j in (24,26,30,32) and i!=j,"unexpected W replacement")
        req(surviving[i][2]==original[i][2],"W already replaced")
        replacement=[row[:] for row in original[j][2]]
        diff=[[x-y for x,y in zip(row,other)] for row,other in zip(original[i][2],replacement)]
        req(any(x for row in diff for x in row),"zero W correction")
        error=[factor for factor in surviving[i]]
        error[2]=diff
        discarded.append(error)
        surviving[i][2]=replacement
    req(len(surviving)==76 and len(discarded)==15,"term count")
    return surviving,discarded

def polynomial_report(surviving,discarded,bases):
    s=V.parse_factors(V.transformed_factors(surviving,bases,M.WEIGHTS),76)
    e=V.parse_factors(V.transformed_factors(discarded,bases,M.WEIGHTS),15)
    minima=[[min(z for _,_,z in factor) for factor in term] for term in e]
    req(all(sum(v)>0 for v in minima),"noncontracting discarded term")
    out=V.contract(s)
    err=V.contract(e)
    req(all(k[0]>=0 for k in out),"negative survivor Laurent coefficient")
    req(all(k[0]>0 for k in err),"nonpositive complete error coefficient")
    const={k[1:]:v for k,v in out.items() if k[0]==0}
    req(const==V.target_tensor(),"constant tensor differs from M(4,5,5)")
    req({k:v for k,v in out.items() if k[0]>0}==
        {k:-v for k,v in err.items()},"incomplete Laurent error cancellation")
    for k in set(out)|set(err):
        target=V.target_tensor().get(k[1:],0) if k[0]==0 else 0
        req(out.get(k,0)+err.get(k,0)==target,"expanded tensor identity differs")
    degree_count=Counter(k[0] for k in out)
    req(degree_count[0]==100,"wrong constant nonzero positions")
    return minima,sum(v for k,v in degree_count.items() if k>0),len([k for k in degree_count if k>0])

def w_data(surviving,obstruction):
    classes={}
    for i,term in enumerate(surviving):
        row=M.direction(term[2])
        req(all(z.denominator==1 and int(z) in (-1,0,1) for z in row),"nonintegral W direction")
        classes.setdefault(tuple(int(z) for z in row),[]).append(i)
    vectors=[list(v) for v in classes]
    req(len(vectors)==54,"wrong W count")
    req(G.rank(vectors,101)==20,"W span collapsed")
    mapping={tuple(v):w for v,w in zip(obstruction["vectors"],obstruction["weights"])}
    req(len(mapping)==56 and sum(mapping.values())==152,"prior W weights changed")
    req(all(tuple(v) in mapping for v in vectors),"new W direction not inherited")
    weights=[mapping[tuple(v)] for v in vectors]
    req(sum(weights)==144 and max(weights)==4,"strong W-screen total differs")
    anchor=tuple(int(z) for z in M.direction(V.load_seed()[35][2]))
    a=vectors.index(list(anchor))
    req(a==28 and weights[a]==0,"anchor W35 missing or reindexed")
    req(all(abs(x)<=1 for v in vectors for x in v),"Hadamard rank transfer bound fails")
    req(G.rank([v for v,w in zip(vectors,weights) if w>0],101)==20,"positive-weight directions do not span dimension 20")
    return vectors,weights,classes,a

def anchor_replay(vectors,weights,anchor):
    compiler=shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")
    req(compiler is not None,"C99 compiler required for complete anchor enumeration")
    with tempfile.TemporaryDirectory(prefix="double-anchor-") as td:
        exe=Path(td)/"anchor"
        subprocess.run([compiler,"-std=c99","-O2",str(HERE/"anchor.c"),"-o",str(exe)],
                       check=True,capture_output=True,text=True)
        payload=str(len(vectors))+" 20\n"
        payload+="".join(" ".join(map(str,row))+" "+str(w)+"\n" for row,w in zip(vectors,weights))
        proc=subprocess.run([str(exe),str(anchor)],input=payload,capture_output=True,
                            text=True,check=True)
        stats=list(map(int,proc.stdout.split()))
    req(stats==[23426,23352,15],"anchor enumeration mismatch")
    return dict(triples_checked=stats[0],rank_four_triples=stats[1],
                maximum_weight_in_anchor_flat=stats[2],field_modulus=101)

def verify(enumerate_anchor=True):
    saved=json.loads((HERE/"certificate.json").read_text())
    req(saved["claim_id"]==CLAIM and saved["source_sha256"]==SOURCE_SHA and
        saved["basis_sha256"]==BASIS_SHA and
        saved["physical_weights"]==M.WEIGHTS and
        saved["surviving_terms"]==76 and saved["discarded_terms"]==15 and
        saved["expanded_exact_terms"]==91 and
        saved["rank_four_flat_weight_cap"]==16 and
        saved["anchor_maximum_flat_weight_mod101"]==15 and
        saved["variants"]=={k:[list(v) for v in p] for k,p in VARIANTS.items()} and
        saved["surviving_positive_coefficient_counts"]==EXPECTED_POSITIVE and
        saved["improves_omega"] is False,"saved certificate mismatch")
    original,bases=original_and_bases()
    old=json.loads((PRIOR/"w_obstruction.json").read_text())
    M.verify_w_obstruction(old,False)   # accepts the prior 56-vector cap16 certificate
    results={}
    for key,pairs in VARIANTS.items():
        s,e=construct(original,pairs)
        minima,count,degs=polynomial_report(s,e,bases)
        req(sum(sum(x)>0 for x in minima)==15 and [sum(x) for x in minima[-2:]]==[10,10],"the 15 prescribed errors do not contract with their recorded valuations")
        req(count==EXPECTED_POSITIVE[key],"saved full Laurent coefficient count differs")
        directions=[len({M.direction(term[leg]) for term in s}) for leg in range(3)]
        req(directions==[65,76,54],"projective direction counts differ")
        vectors,weights,classes,anchor=w_data(s,old)
        if enumerate_anchor:
            anchor_stats=anchor_replay(vectors,weights,anchor)
        else:
            anchor_stats={"not_run":True,"retained_exact_report":[23426,23352,15]}
        results[key]={"extra_W_replacements":[list(p) for p in pairs],
                      "surviving_terms":len(s),"discarded_terms":len(e),
                      "direction_counts_UVW":directions,
                      "minima":minima,"positive_Laurent_coefficients":count,
                      "positive_Laurent_degrees":degs,
                      "retained_mixed_W_weight":sum(weights),
                      "prior_W_four_flat_cap":16,
                      "W35_anchor_index":anchor,
                      "W35_anchor_bound":anchor_stats}
    return {"claim_id":CLAIM,"variants":results,
            "full_source_positions_checked":10000,
            "scope":"Four exact 76-term border families; static nine-four-flat W cover excluded for each. No Q(6,4) source maps or omega improvement.",
            "independent_review":False}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--no-enumerate",action="store_true",help="Recheck Laurent tensors but do not rerun the anchored F101 census")
    args=p.parse_args()
    print(json.dumps(verify(not args.no_enumerate),indent=2))
