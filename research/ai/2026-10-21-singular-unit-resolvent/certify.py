"""Standard-library exact witness for a singular-unit resolvent chart."""
import argparse, importlib.util, json
from pathlib import Path
from itertools import product
PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
SOURCE=ROOT/'research/ai/2026-10-21-cyclic-slice-determinants/certify.py'
spec=importlib.util.spec_from_file_location('cyclic_source_calibration',SOURCE)
src=importlib.util.module_from_spec(spec);spec.loader.exec_module(src)


def axpy(v,c,w,p=None):
    if not c:return
    for j,x in w.items():
        y=v.get(j,0)+c*x
        if p:y%=p
        if y:v[j]=y
        elif j in v:del v[j]


def multiply(A,B):
    out=[]
    for row in A:
        v={}
        for k,x in row.items():axpy(v,x,B[k])
        out.append(v)
    return out


def literal(a,i,k,s):
    n=a*a*(2*a-1);M=[{} for _ in range(n)]
    for j,p,r in product(range(a),repeat=3):
        q=k-p
        if 0<=q<a:
            row=(j*a+p)*(2*a-1)+s+r
            column=((i+j)*a+q)*a+r
            M[row][column]=1
    return M


def rank_witness(rows,p):
    basis=[];chosen=[]
    for index,row in enumerate(rows):
        v={j:x%p for j,x in row.items() if x%p}
        for pivot,w in basis:axpy(v,-v.get(pivot,0),w,p)
        if v:
            pivot=min(v);scale=pow(v[pivot],-1,p)
            basis.append((pivot,{j:x*scale%p for j,x in v.items()}));chosen.append(index)
    return chosen,[pivot for pivot,_ in basis]


def build():
    a=4;n=112;R=110;p=1009
    M0=src.source_matrix(a,src.integer_slice(a))
    modular_inverse=src.inverse(M0,p)
    integer_inverse=[[x if x<=p//2 else x-p for x in row] for row in modular_inverse]
    inv=[{j:x for j,x in enumerate(row) if x} for row in integer_inverse]
    frame=[{j:x for j,x in enumerate(row) if x} for row in M0]
    identity=[{i:1} for i in range(n)]
    if multiply(inv,frame)!=identity or multiply(frame,inv)!=identity:
        raise ValueError('lifted source inverse is not exact over Z')
    labels=list(product(range(a),range(2*a-1),range(a)))
    H=[multiply(inv,literal(a,*label)) for label in labels]
    N=H[0]
    if any(multiply(N,N)):raise ValueError('source coordinate nilpotent is not square zero')
    rankN=len(rank_witness(N,p)[0])
    if rankN!=16:raise ValueError('coordinate rank witness is wrong')
    # In normalized column order (H,q,r), a source middle coefficient k
    # gives row q' minus column q = 3-k.
    for (i,k,s),X in zip(labels,H):
        for row,v in enumerate(X):
            for column in v:
                if (row//a)%a-(column//a)%a!=a-1-k:
                    raise ValueError('normalized source does not have the stated grade shift')
    removed=[4,5];kept=[j for j in range(n) if j not in removed];pos={j:i for i,j in enumerate(kept)}
    def compress(X):
        return {pos[i]*R+pos[j]:x for i in kept for j,x in X[i].items() if j in pos}
    low=[compress(X) for (_,k,_),X in zip(labels,H) if k<3]
    high=[compress(multiply(N,X)) for (_,k,_),X in zip(labels,H) if k>=3]
    target_unit={i*(R+1):1 for i in range(R)}
    candidates=high+low+[target_unit]
    rows,columns=rank_witness(candidates,p)
    if len(rows)!=n:raise ValueError('resolvent limiting candidate span has wrong dimension')
    # Exact integer invariance at the explicit nonempty-open witness.
    # Prove invariance over Q by exact vector elimination; all pivots here are units.
    Ubasis=[]
    for j in range(n):
        v={pos[i]:N[i][j] for i in kept if j in N[i]}
        for pivot,w in Ubasis:axpy(v,-v.get(pivot,0),w)
        if v:
            pivot=min(v)
            if v[pivot] not in [-1,1]:raise ValueError('nonunit invariant-space pivot')
            Ubasis.append((pivot,{i:x//v[pivot] for i,x in v.items()}))
    if len(Ubasis)!=16:raise ValueError('wrong invariant dimension')
    for X in candidates:
        for _,u in Ubasis:
            v={}
            for ij,x in X.items():
                i,j=divmod(ij,R)
                if j in u:v[i]=v.get(i,0)+x*u[j]
            v={i:x for i,x in v.items() if x}
            for pivot,w in Ubasis:axpy(v,-v.get(pivot,0),w)
            if v:raise ValueError('candidate does not preserve the exact invariant space')
    certificate={'schema':'cyclic-singular-unit-resolvent-v1','size':a,'prime':p,
       'source_dimension':n,'target_long_dimension':R,'removed_coordinates':removed,
       'candidate_order':'64 high-middle NH slices,48 low-middle H slices,identity',
       'minor_rows':rows,'minor_columns':columns,'rank':n,
       'nilpotent_rank':rankN,'nilpotent_square_zero':True,
       'invariant_dimension_at_witness':len(Ubasis),
       'possible_invariant_dimensions_under_rank_hypothesis':[14,15,16,27,28,55,56,83,84],
       'target_module_dimension':10,'requires_full_candidate_rank':True,
       'requires_fixed_unit_resolvent_ansatz':True,'all_singular_units_excluded':False,
       'independent_review':False,'lean_formalized':False,'improves_omega':False}
    return certificate,candidates


def verify(certificate):
    expected,candidates=build()
    if certificate!=expected:raise ValueError('certificate mismatch or omitted scope constraint')
    p=certificate['prime'];rows=certificate['minor_rows'];cols=certificate['minor_columns']
    if len(set(rows))!=112 or len(set(cols))!=112:raise ValueError('minor indices repeat')
    minor=[{j:candidates[i].get(column,0) for j,column in enumerate(cols)} for i in rows]
    if len(rank_witness(minor,p)[0])!=112:raise ValueError('saved minor is singular')
    if any(d%10==0 for d in certificate['possible_invariant_dimensions_under_rank_hypothesis']):
        raise ValueError('module dimension divisibility does not obstruct the target')
    return {'verified':True,'integer_source_inverse':True,'minor_rank_mod_1009':112,
      'candidate_span_exact_over_C':112,'explicit_invariant_dimension':16,
      'all_finite_first_map_poles':True,'all_compression_pairs':False,
      'general_A4_excluded':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify',type=Path);parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.verify:print(json.dumps(verify(json.loads(args.verify.read_text())),indent=2))
    else:
        certificate,_=build()
        text=json.dumps(certificate,indent=2)+'\n'
        if args.output:args.output.write_text(text)
        else:print(text,end='')
