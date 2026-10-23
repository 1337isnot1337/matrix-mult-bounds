"""An exact six-term polynomial degeneration of the oblique repair core.

Polynomial vectors use sparse (coordinate, t-degree) keys.  All arithmetic
is over the integers.  The identity therefore holds over every field.
The six-term sum is t^2*(1-t)*(K+t*H), with no lower-order coefficient.
"""

from itertools import product
from pathlib import Path
import argparse
from fractions import Fraction
import hashlib
import json
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from grid_karatsuba import (PACKAGE, slice_terms, formula_residual, product_maps,
                           Field, contract, matrix_multiplication, subtract)


def vec(entries):
    """Accept (coordinate,degree,coefficient) records and collect exactly."""
    out={}
    for i,d,v in entries:
        if type(i) is not int or type(d) is not int or type(v) is not int or d<0:
            raise ValueError('Require integer coordinates, degrees and coefficients')
        out[i,d]=out.get((i,d),0)+v
    return {key:value for key,value in out.items() if value}


def add(*vectors):
    return vec([(i,d,v) for x in vectors for (i,d),v in x.items()])


def scale(x,poly):
    return vec([(i,d+e,v*w) for (i,d),v in x.items() for e,w in poly.items()])


def basis(i):
    return {(i,0):1}


def difference(x,y):
    return add(x,scale(y,{0:-1}))


def expand(terms):
    out={}
    for aa,bb,cc in terms:
        for ((a,da),x),((b,db),y),((c,dc),z) in product(aa.items(),bb.items(),cc.items()):
            key=(a,b,c,da+db+dc)
            out[key]=out.get(key,0)+x*y*z
    return {key:value for key,value in out.items() if value}


def layers(expansion):
    result={}
    for (a,b,c,d),value in expansion.items():
        result.setdefault(d,{})[a,b,c]=value
    return result


def polynomial_core(u,v,w,xx,zz,aa,eta,yy,pp,qq,rr,ss,tt):
    """Six rank-one polynomial terms, in any substituted linear coordinates."""
    q={2:1,3:-1}
    return [
        (add(u,w),add(xx,zz),scale(add(qq,rr),q)),
        (u,xx,scale(difference(difference(pp,qq),rr),q)),
        (add(w,scale(v,{1:1})),zz,
         add(scale(difference(tt,qq),q),scale(rr,{1:-1,2:-1}),scale(ss,{0:-1,2:-1}))),
        (add(v,w),add(scale(eta,q),scale(zz,{1:1,3:1})),add(rr,ss)),
        (add(v,scale(u,{1:1})),
         add(scale(difference(aa,eta),q),scale(zz,{1:-1,2:1})),rr),
        (w,add(scale(difference(yy,eta),q),scale(zz,{0:1,1:-1,2:1,3:-1})),ss),
    ]


def canonical_core():
    # A=(u,v,w), B=(X,Z,a,eta,y), C=(P,Q,R,S,T).
    u,v,w=[basis(i) for i in range(3)]
    xx,zz,aa,eta,yy=[basis(i) for i in range(5)]
    pp,qq,rr,ss,tt=[basis(i) for i in range(5)]
    terms=polynomial_core(u,v,w,xx,zz,aa,eta,yy,pp,qq,rr,ss,tt)
    core={(0,0,0):1,(0,1,1):1,(1,2,2):1,(1,3,3):1,
          (2,0,1):1,(2,1,4):1,(2,3,2):1,(2,4,3):1,(2,0,2):1}
    error={(1,1,4):1,(1,1,1):-1,(0,2,2):1,(0,3,2):-1}
    return terms,core,error


def substituted_core(r,s,i,j):
    k,ell=i-s,j-s
    u,v,w=basis(r*i+ell),basis(r*k+j),basis(r*i+j)
    xx=difference(basis(4*i),basis(4*k+1))
    zz=difference(basis(4*i+2),basis(4*k+3))
    aa,eta,yy=basis(4*k),basis(4*k+1),basis(4*i+1)
    pp,qq=basis(ell),basis(2*r+ell)
    rr=difference(basis(j),basis(2*r+ell))
    ss=difference(basis(r+j),basis(3*r+ell))
    tt=basis(2*r+j)
    terms=polynomial_core(u,v,w,xx,zz,aa,eta,yy,pp,qq,rr,ss,tt)
    error=layers(expand([(v,zz,difference(tt,qq)),(u,difference(aa,eta),rr)]))[0]
    return terms,error


def dictionary_add(a,b,factor=1):
    out=dict(a)
    for key,value in b.items():
        out[key]=out.get(key,0)+factor*value
    return {key:value for key,value in out.items() if value}


def verify_identity(terms,target,error):
    expected={2:target,3:dictionary_add(error,target,-1),4:{k:-v for k,v in error.items()}}
    expected={d:x for d,x in expected.items() if x}
    actual=layers(expand(terms))
    if actual!=expected:
        raise ArithmeticError('The complete integer polynomial identity is false')
    return {"rank_one_polynomial_terms":len(terms),"first_nonzero_degree":min(actual) if actual else None,
            "identity":"sum terms = t^2*(1-t)*(target+t*error)",
            "complete_polynomial_identity_replayed":True,"all_fields":True}


def repair_family(n,b,raw=False):
    if type(n) is not int or type(b) is not int or b<2 or n<b+1:
        raise ValueError('Require integers b>=2 and n>=b+1')
    r,s,d=n-1,b-1,n-b-1
    bad=set(range(s,r-1)); boundary=[i for i in sorted(bad) if i-s not in bad]
    covered,terms,error=set(),[],{}
    for i,j in product(boundary,repeat=2):
        points={(i,j-s),(i-s,j),(i,j)}
        if points&covered:
            raise ArithmeticError('Core supports overlap')
        covered.update(points)
        core,tail=substituted_core(r,s,i,j)
        terms.extend(core);error=dictionary_add(error,tail)
    for i,j in product(range(r),repeat=2):
        if (i,j) not in covered:
            for term in slice_terms(r,s,bad,i,j):
                a,bv,c=[vec([(k,0,v) for k,v in term[axis]]) for axis in ('a','b','c')]
                terms.append((scale(a,{2:1,3:-1}),bv,c))
    if len(terms)!=4*r*d-2*min(d,s)**2:
        raise ArithmeticError('The polynomial term count changed')
    target=formula_residual(n,b)
    result=verify_identity(terms,target,error)
    if raw:
        image,_=contract(n,b,(r,4,r),product_maps(n,b))
        if target!=subtract(matrix_multiplication((r,4,r)),image,Field()):
            raise ArithmeticError('Native source does not have the claimed residual')
    result.update(n=n,b=b,target=[r,4,r],border_rank_upper_bound=len(terms),
                  cores=len(boundary)**2,native_source_replayed=raw)
    return result,terms,error


def serializable_terms(terms):
    return [{axis:[[i,d,v] for (i,d),v in sorted(vector.items())]
             for axis,vector in zip(('a','b','c'),term)} for term in terms]


def combined_source_witness(n,b):
    """Export and replay all polynomial maps on Q(n,b) direct-sum D_cost."""
    report,terms,error=repair_family(n,b,raw=True)
    ordinary=product_maps(n,b)
    columns=[]
    for axis,matrix in enumerate(ordinary):
        current=[vec([(i,0,row[j]) for i,row in enumerate(matrix) if row[j]])
                 for j in range(len(matrix[0]))]
        if axis==0:
            current=[scale(x,{2:1,3:-1}) for x in current]
        current.extend(term[axis] for term in terms)
        columns.append(current)
    width=n+b-1;source_shape=(n*n,b*width,b*width)
    native=[]
    for p,q,y,v in product(range(n),range(n),range(b),range(b)):
        indices=(p*n+q,y*width+q+v,(p+y)*b+v)
        native.append(tuple(columns[axis][j] for axis,j in enumerate(indices)))
    for ell in range(len(terms)):
        native.append(tuple(columns[axis][source_shape[axis]+ell] for axis in range(3)))
    replay=verify_identity(native,matrix_multiplication((n-1,4,n-1)),error)
    replay['native_source_terms']=n*n*b*b
    replay['added_diagonal_terms']=len(terms)
    replay.pop('rank_one_polynomial_terms')
    records=[]
    for current in columns:
        records.append([[i,j,d,value] for j,col in enumerate(current)
                        for (i,d),value in sorted(col.items())])
    report.update(source_format=[x+len(terms) for x in source_shape],
                  target_format=[(n-1)**2,4*(n-1),4*(n-1)],
                  polynomial_local_maps=records,
                  local_map_record_convention=['target coordinate','source coordinate','t degree','coefficient'],
                  complete_source_degeneration=replay,
                  deformation_error_H=[[a,bb,c,v] for (a,bb,c),v in sorted(error.items())],
                  residual_polynomial_terms=serializable_terms(terms),
                  whole_residual_border_rank_optimality_claimed=False,
                  improves_omega=False)
    replay_combined_record(report)
    return report


def replay_combined_record(record):
    """Read the exported sparse polynomial maps and reconstruct every term."""
    n,b,cost=record['n'],record['b'],record['border_rank_upper_bound']
    width=n+b-1;ordinary_shape=(n*n,b*width,b*width)
    source_shape=tuple(x+cost for x in ordinary_shape)
    target_shape=((n-1)**2,4*(n-1),4*(n-1))
    if tuple(record['source_format'])!=source_shape or tuple(record['target_format'])!=target_shape:
        raise ArithmeticError('Incorrect source or target format')
    maps=[]
    for axis,records in enumerate(record['polynomial_local_maps']):
        inputs=[[] for _ in range(source_shape[axis])]
        for target,source,degree,value in records:
            if not(0<=source<source_shape[axis] and 0<=target<target_shape[axis]):
                raise ArithmeticError('Map coordinate outside its specified factor')
            inputs[source].append((target,degree,value))
        maps.append([vec(x) for x in inputs])
    if len(maps)!=3:
        raise ArithmeticError('Three local maps are required')
    terms=[]
    for p,q,y,v in product(range(n),range(n),range(b),range(b)):
        indices=(p*n+q,y*width+q+v,(p+y)*b+v)
        terms.append(tuple(maps[axis][j] for axis,j in enumerate(indices)))
    terms.extend(tuple(maps[axis][ordinary_shape[axis]+ell] for axis in range(3))
                 for ell in range(cost))
    error={(a,bb,c):value for a,bb,c,value in record['deformation_error_H']}
    verify_identity(terms,matrix_multiplication((n-1,4,n-1)),error)
    return True


def determinant(matrix):
    """Small exact determinant, used only to replay the supplied unit minor."""
    a=[[Fraction(x) for x in row] for row in matrix]
    if any(len(row)!=len(a) for row in a):
        raise ValueError('Require a square matrix')
    result=Fraction(1)
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k]),None)
        if pivot is None:
            return Fraction(0)
        if pivot!=k:
            a[pivot],a[k]=a[k],a[pivot];result=-result
        value=a[k][k];result*=value
        for i in range(k+1,len(a)):
            coefficient=a[i][k]/value
            a[i]=[x-coefficient*y for x,y in zip(a[i],a[k])]
    return result


def koszul_certificate(path=None):
    path=path or Path(__file__).with_name('core-koszul.json')
    saved=json.loads(path.read_text())
    _,core,_=canonical_core();pairs=[(0,1),(0,2),(1,2)]
    matrix=[[0]*15 for _ in range(15)]
    for (a,b,c),value in core.items():
        for i in range(3):
            if i==a:
                continue
            pair=tuple(sorted((a,i)))
            matrix[5*pairs.index(pair)+c][5*i+b]+=value*(1 if a<i else -1)
    if matrix!=saved['koszul_matrix']:
        raise ArithmeticError('The saved Koszul map is not the core Koszul map')
    rows,cols=saved['minor_rows'],saved['minor_columns']
    if len(rows)!=11 or len(cols)!=11 or len(set(rows))!=11 or len(set(cols))!=11:
        raise ArithmeticError('The Koszul minor is not eleven by eleven')
    det=determinant([[matrix[i][j] for j in cols] for i in rows])
    if det!=1 or saved['minor_determinant']!=1:
        raise ArithmeticError('The supplied Koszul minor is not a unit minor')
    return {'minor_size':11,'minor_determinant':1,'rank_one_koszul_rank':2,
            'border_rank_lower_bound':6,'core_border_rank_over_C':6,
            'formal_lower_bound_in_every_characteristic':True,
            'complete_koszul_matrix_reconstructed':True}


def source_pins(repository):
    if repository is None:
        return {'checked':0,'reason':'Supply --repository for pinned source replay'}
    source=json.loads(Path(__file__).with_name('sources.json').read_text())
    for record in source['local_sources']:
        path=repository/record['path']
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        if digest!=record['sha256']:
            raise ArithmeticError('Source hash mismatch: '+record['path'])
    return {'checked':len(source['local_sources']),'all_match':True}


def build_certificate(repository=None):
    """Regenerate every saved core, family, map and pinned-source record."""
    terms,target,error=canonical_core()
    core=verify_identity(terms,target,error)
    core['terms']=serializable_terms(terms)
    controls=[repair_family(b+1+d,b,raw=(b,d) in {(4,1),(4,2),(4,3),(2,3),(3,5)})[0]
              for b in range(2,10) for d in range(9)]
    witness=combined_source_witness(6,4)
    return {'core':core,'family_formula':'4*r*d-2*min(d,b-1)^2',
            'controls':controls,'n6_witness':witness,'koszul':koszul_certificate(),
            'source_pin_verification':source_pins(repository),
            'ordinary_rank_upper_bound_n6':19,'border_rank_upper_bound_n6':18,
            'improves_omega':False}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    parser.add_argument('--repository',type=Path)
    args=parser.parse_args()
    result=build_certificate(args.repository)
    if args.output: args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'core':{k:v for k,v in result['core'].items() if k!='terms'},
          'controls':len(result['controls']),
          'source_pins':result['source_pin_verification'],
          'examples':[x for x in result['controls'] if x['b']==4]},indent=2))


if __name__=='__main__':
    main()
