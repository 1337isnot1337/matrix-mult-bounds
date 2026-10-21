"""Exact second-jet matrix blocks; extension data credited to PR45 at 5d4a941."""
from collections import defaultdict
from functools import lru_cache
import importlib.util
from itertools import product
import json
from pathlib import Path
import sympy as sp

_dependency=Path(__file__).resolve().parents[1]/'2026-10-20-graded-quantum-flags/one_leg.py'
_spec=importlib.util.spec_from_file_location('second_jet_previous',_dependency)
one=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(one)
V=112;LONG=(1,2,4,5)


def index(i,j,z):return (4*i+j)*7+z

def reverse(k):return index(k//7%4,k//28,k%7)

# Canonical extension basis from the concurrent worker. No new classification
# claim is made for these data. The rank certificates below replay completeness.
G=[{index(0,3,z):1,index(3,0,z):-1} for z in LONG]
EB=[{index(p,j,z):1} for p,j,z in product((0,3),(0,3),LONG)]
EB += [{index(0,j,z):1,index(3,j,z-3):1} for j,z in product((1,2),(4,5))]
EC=[{reverse(k):value for k,value in row.items()} for row in EB]
A0=sorted(index(i,s,z) for i,s,z in product((1,2),(1,2),(0,3,6)))
K=[i for i in range(V) if i not in A0]
TERMS=[(index(i,s,6-p-q),index(p,j,6-r-s),index(r,q,6-i-j))
       for i,j,p,q,r,s in product(range(4),repeat=6)]


def contract(left,right,first):
    """Full integer contraction, without modular coefficient masking."""
    B=defaultdict(list);C=defaultdict(list)
    for row,vector in enumerate(left):
        for col,value in vector.items():B[col].append((row,value))
    for row,vector in enumerate(right):
        for col,value in vector.items():C[col].append((row,value))
    positions={a:i for i,a in enumerate(first)};entries=defaultdict(int)
    for a,b,c in TERMS:
        if a not in positions:continue
        for j,x in B[b]:
            for k,y in C[c]:entries[positions[a],j*len(right)+k]+=x*y
    return sp.MutableSparseMatrix(len(first),len(left)*len(right),dict(entries))


def rational_rank(matrix):return len(matrix.to_DM().rref()[1])


def minor_certificate(matrix):
    rows=[{j:int(value)%one.PRIME for (r,j),value in matrix.todok().items() if r==i and value%one.PRIME}
          for i in range(matrix.rows)]
    rr,cc=one.independent_minor(rows)
    determinant=one.determinant_mod([[rows[i].get(j,0) for j in cc] for i in rr])
    exact=rational_rank(matrix)
    if exact!=len(rr) or not determinant:raise ArithmeticError('minor does not certify exact rational rank')
    return {'rank':exact,'minor_rows':rr,'minor_columns':cc,'minor_determinant_mod_prime':determinant}


@lru_cache(None)
def tensor():return contract(EB,EC,K)


def block_form():
    H=tensor()
    L_ids=sorted(index(i,s,z) for i,s,z in product((1,2),(0,3),(0,3,6)))
    M_ids=sorted(index(i,s,z) for i,s,z in product((0,3),(1,2),(0,3,6)))
    selected=[K.index(a) for a in L_ids]
    slices=[H.extract(selected,[b*20+c for b in range(16)]) for c in range(16,20)]
    base=slices[0]+slices[3]
    operators=[]
    for i in range(4):
        O=sp.zeros(12)
        row,col=[(1,1),(0,1),(1,0),(0,0)][i]
        for j in range(6):O[6*row+j,6*col+j]=1
        operators.append(O)
    if not all(A==O*base for A,O in zip(slices,operators)):
        raise ArithmeticError('matrix-unit factorization failed')
    for a,b,c in product(range(100),range(16),range(4)):
        if H[a,b*20+16+c] and K[a] not in L_ids:raise ArithmeticError('left cross support failed')
        if H[a,(16+c)*20+b] and K[a] not in M_ids:raise ArithmeticError('right cross support failed')
        a_reversed=K.index(reverse(K[a]))
        if H[a,(16+c)*20+b]!=H[a_reversed,b*20+16+c]:
            raise ArithmeticError('cross-block reversal identity failed')
    return L_ids,M_ids,base


def rank_two_spanning_witnesses():
    """Thirteen rank-two slices and their reversed copies span all of H."""
    L=sorted(index(i,s,z) for i,s,z in product((1,2),(0,3),(0,3,6)))
    def make(alpha,beta,w,z=0):
        result={index(0,0,6):z}
        for j in range(6):
            result[L[j]]=alpha*w[j]
            result[L[6+j]]=beta*w[j]
        return {i:value for i,value in result.items() if value}
    witnesses=[]
    for j in [0,1,3,5]:
        w=[0]*6;w[j]=1;witnesses.append(make(1,0,w))
    w=[0]*6;w[2]=1;w[4]=-1;witnesses.append(make(1,0,w))
    for j in [0,2,4,5]:
        w=[0]*6;w[j]=1;witnesses.append(make(0,1,w))
    w=[0]*6;w[1]=1;w[3]=-1;witnesses.append(make(0,1,w))
    for rate in [1,-1,2]:
        w=[0]*6;w[2]=1;w[1]=rate**3
        witnesses.append(make(rate,1,w,rate**2))
    witnesses += [{reverse(i):value for i,value in row.items()} for row in list(witnesses)]
    H=tensor();records=[];flat=[]
    for coefficients in witnesses:
        row=sum((value*H[K.index(i),:] for i,value in coefficients.items()),sp.zeros(1,400))
        matrix=sp.Matrix(20,20,lambda b,c:row[0,b*20+c])
        certificate=minor_certificate(matrix)
        if certificate['rank']!=2:raise ArithmeticError('slice does not have rank two')
        rr,cc=certificate['minor_rows'],certificate['minor_columns']
        middle=matrix.extract(rr,cc)
        # This full coefficient identity supplies an exact rank-two upper bound.
        if matrix!=matrix[:,cc]*middle.inv()*matrix[rr,:]:
            raise ArithmeticError('rank-two factorization failed')
        records.append({'source_first_coefficients':[[i,value] for i,value in sorted(coefficients.items())],
                        'matrix_rank':certificate,'full_factorization_verified':True})
        flat.append(row)
    span=minor_certificate(sp.Matrix.vstack(*flat))
    if span['rank']!=25:raise ArithmeticError('low-rank slices do not span H')
    return {'slices':records,'span':span,'matrix_rank_upper_bound':2}


def report():
    H=tensor();L_ids,M_ids,base=block_form()
    if any(H[a,b*20+c] for a,b,c in product(range(100),range(16),range(16))):
        raise ArithmeticError('nonzero boundary-by-boundary block')
    leading=contract(G,G,list(range(V)))
    controls=[]
    identity=[{i:1} for i in range(V)]
    for name,extension,is_left in [('EB',EB,True),('EC',EC,False)]:
        C=contract(identity,G,K) if is_left else contract(G,identity,K)
        matrix=sp.Matrix(400,V,lambda row,col:C[row//4,col*4+row%4] if is_left else C[row//4,(row%4)*V+col])
        E=sp.Matrix(20,V,lambda i,j:extension[i].get(j,0))
        if matrix*E.T!=sp.zeros(400,20):raise ArithmeticError('extension inclusion failed')
        if rational_rank(E)!=20:raise ArithmeticError('dependent canonical extension basis')
        controls.append({'name':name,'constraint':minor_certificate(matrix),'basis_dimension':20})
    phases=[]
    field,_=one.quadratic_field()
    for phase in [(6,1),(3,1),(3,2),(6,5)]:
        actual=one.exact_phase_map(phase)
        for row,expected in zip([70,71,73,74],G):
            chosen=min(expected);scale=actual.get((row,chosen),field.zero)/expected[chosen]
            if not scale:raise ArithmeticError('zero root row')
            normalized={j:value/scale for (i,j),value in actual.items() if i==row and value}
            if normalized!={j:field.convert(value) for j,value in expected.items()}:
                raise ArithmeticError('canonical root normalization failed')
        phases.append(list(phase))
    columns=[0,1,2,3,4,5,6,7,12,13,14,15]
    determinant=int(base[:,columns].det())
    if determinant!=-1:raise ArithmeticError('cross block base is not surjective')
    return {'prime':one.PRIME,'canonical_extension_credit':'PR45 at 5d4a941930a61a195342acfac50045384f5361e4',
            'normalized_root_phases':phases,'leading_tensor':minor_certificate(leading),
            'extension_completeness_controls':controls,'canonical_bilinear_tensor':minor_certificate(H),
            'zero_boundary_block_coefficients_checked':100*16*16,
            'left_first_coordinate_indices':L_ids,'right_first_coordinate_indices':M_ids,
            'first_coordinate_supports_disjoint':not bool(set(L_ids)&set(M_ids)),
            'left_matrix_slice_formula':'[[v3,v1],[v2,v0]] tensor I6 times base',
            'base_sparse_entries':[[i,j,int(value)] for (i,j),value in sorted(base.todok().items()) if value],
            'base_minor_columns':columns,'base_minor_determinant':determinant,
            'all_four_full_slice_identities':True,'all_cross_reversal_coefficients_checked':100*16*4,
            'rank_two_spanning':rank_two_spanning_witnesses(),
            'necessary_bilinear_first_rank_upper_bound':0,
            'necessary_second_partial_space_dimension_upper_bound':12,
            'necessary_effective_first_row_rank_sum_upper_bound':24,
            'rank_sum_ceiling_if_any_mixed_component_occurs':20,
            'proof_status':'Written and unreviewed; no exponent improvement.'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(report(),indent=2)+'\n')
