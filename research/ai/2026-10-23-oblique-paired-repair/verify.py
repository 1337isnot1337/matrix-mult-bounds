"""Integer oblique paired-source repairs and exact residual certificates.

No numerical fitting or third-party package is used. The n=6,b=4 product
witness has a 19-term scalar repair; its nonproduct variant has a verified
24-term repair. Neither improves the matrix multiplication exponent.
"""

from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

from exact import (Field, contract, encode, flatten, matrix_multiplication,
                   minimum_first_residual, row_space, subtract, tensor_records,
                   verify as verify_maps)
from karatsuba_repair import certificate as karatsuba_certificate


def product_data(n,b):
    if type(n) is not int or type(b) is not int or b<2 or n<b+1:
        raise ValueError('Require integer b>=2 and n>=b+1')
    r,width,shift=n-1,n+b-1,b-1
    outer=[[0]*n for _ in range(r)]
    for i in range(r-1):
        outer[i][i+1]=1
    outer[-1][0],outer[-1][-1]=1,-1
    inner=[[int(y==0) for y in range(b)], [int(y==shift) for y in range(b)]]
    products=[[0]*width for _ in range(2*r)]
    for i,v,p,y in product(range(r),range(2),range(n),range(b)):
        products[2*i+v][p+y]+=outer[i][p]*inner[v][y]
    dual=[[0]*width for _ in range(2*r)]
    bad=list(range(b-1,n-2))
    for i in range(r-1):
        if i not in bad:
            exponent=i+1
            dual[2*i][exponent]=1
            if exponent==shift:
                dual[2*i][-1]=1
        exponent=i+b
        dual[2*i+1][exponent]=1
        if exponent==n-1:
            dual[2*i+1][0]=1
    dual[2*r-2][0]=1
    dual[2*r-1][-1]=-1
    projection=[[sum(x*y for x,y in zip(row,column)) for column in products]
                for row in dual]
    expected=[[int(i==j) for j in range(2*r)] for i in range(2*r)]
    for i in bad:
        expected[2*i][2*i]=0
        expected[2*(i-shift)+1][2*i]=1
    if projection!=expected:
        raise ArithmeticError('The complete oblique decoder identity failed')
    return outer,inner,products,dual,projection,bad


def product_maps(n,b):
    outer,inner,_,dual,_,_=product_data(n,b)
    r,width=n-1,n+b-1
    first=[[0]*(n*n) for _ in range(r*r)]
    second=[[0]*(b*width) for _ in range(4*r)]
    third=[[0]*(b*width) for _ in range(4*r)]
    for i,j,p,q in product(range(r),range(r),range(n),range(n)):
        first[r*i+j][n*p+q]=outer[j][p]*outer[i][q]
    for i,a,v,y,z in product(range(r),range(2),range(2),range(b),range(width)):
        second[4*i+2*a+v][width*y+z]=inner[a][y]*dual[2*i+v][z]
    for a,v,j,z,vv in product(range(2),range(2),range(r),range(width),range(b)):
        third[r*(2*a+v)+j][b*z+vv]=dual[2*j+a][z]*inner[v][vv]
    return [first,second,third]


def inverse(matrix):
    n=len(matrix)
    a=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)]
       for i,row in enumerate(matrix)]
    for column in range(n):
        pivot=next((i for i in range(column,n) if a[i][column]),None)
        if pivot is None:
            raise ArithmeticError('Singular selected product matrix')
        a[column],a[pivot]=a[pivot],a[column]
        scale=a[column][column]
        a[column]=[x/scale for x in a[column]]
        for i in range(n):
            if i!=column and a[i][column]:
                scale=a[i][column]
                a[i]=[x-scale*y for x,y in zip(a[i],a[column])]
    return [row[n:] for row in a]


def nonproduct_maps():
    n,b,r,width=6,4,5,9
    outer,inner,_,lb,_,_=product_data(n,b)
    h=[[[0]*2 for _ in range(4)] for _ in range(4)]
    h[0][0][0]=1
    h[1][0][1]=1
    h[1][1][0],h[1][2][0]=1,2
    h[2][3][0]=1
    h[3][3][1]=1
    dc=[[0]*18 for _ in range(20)]
    for j,a,p,y,v in product(range(r),range(4),range(n),range(b),range(2)):
        dc[4*j+a][2*(p+y)+v]+=outer[j][p]*h[a][y][v]
    selected=[index for index in range(20) if index not in (12,13)]
    selected_transpose=[[dc[index][column] for index in selected] for column in range(18)]
    inverse_selected=inverse(selected_transpose)
    lc=[[Fraction(0)]*18 for _ in range(20)]
    for index,row in zip(selected,inverse_selected):
        lc[index]=row
    first=product_maps(n,b)[0]
    second=[[0]*36 for _ in range(20)]
    third=[[Fraction(0)]*36 for _ in range(20)]
    for i,a,y,z,v in product(range(r),range(4),range(b),range(width),range(2)):
        second[4*i+a][width*y+z]+=h[a][y][v]*lb[2*i+v][z]
    for a,j,z,vv,v in product(range(4),range(r),range(width),range(b),range(2)):
        third[r*a+j][b*z+vv]+=lc[4*j+a][2*z+v]*inner[v][vv]
    if any(x.denominator!=1 for row in lc for x in row):
        raise ArithmeticError('The chosen nonproduct witness is not integral')
    third=[[int(x) for x in row] for row in third]
    return [first,second,third], {'middle_space':h,'middle_products':dc,
                                'selected_product_rows':selected,
                                'omitted_product_rows':[12,13],
                                'middle_decoder':encode(lc)}


def formula_residual(n,b):
    """The explicit three-term formula, expanded in standard target bases."""
    r,shift=n-1,b-1
    bad=list(range(b-1,n-2))
    out={}
    def add(a,bs,cs,scale=1):
        for ib,cb in bs:
            for ic,cc in cs:
                key=(a,ib,ic)
                out[key]=out.get(key,0)+scale*cb*cc
    def x(i,a):
        return [(4*i+2*a,1),(4*(i-shift)+2*a+1,-1)]
    def y(j,v):
        return [(r*v+j,1),(r*(2+v)+j-shift,-1)]
    for i,j,a in product(bad,range(r),range(2)):
        add(r*i+j,x(i,a),[(r*(2*a)+j,1)])
    for i,j,v in product(range(r),bad,range(2)):
        add(r*i+j,[(4*i+v,1)],y(j,v))
    for i,j in product(bad,repeat=2):
        add(r*i+j,x(i,0),y(j,0),-1)
    return {key:value for key,value in out.items() if value}


def ranks(tensor,dimensions):
    return [row_space(flatten(tensor,dimensions,leg))[0] for leg in range(3)]


def scalar_decomposition(tensor,dimensions):
    """Factor every fixed-A matrix; replay every resulting rank-one term."""
    terms=[]
    slice_ranks=[]
    for a in range(dimensions[0]):
        matrix=[[0]*dimensions[2] for _ in range(dimensions[1])]
        for (aa,b,c),value in tensor.items():
            if aa==a:
                matrix[b][c]=value
        rank,_,basis,coefficients=row_space(matrix,factorization=True)
        if rank:
            slice_ranks.append([a,rank])
        for k in range(rank):
            terms.append({'a':a,
                          'b':[[i,encode(row[k])] for i,row in enumerate(coefficients) if row[k]],
                          'c':[[i,encode(value)] for i,value in enumerate(basis[k]) if value]})
    replay={}
    for term in terms:
        for (b,cb),(c,cc) in product(term['b'],term['c']):
            key=(term['a'],b,c)
            replay[key]=replay.get(key,0)+Fraction(cb)*Fraction(cc)
    replay={key:value for key,value in replay.items() if value}
    if replay!=tensor:
        raise ArithmeticError('The scalar repair decomposition failed')
    return {'rank_one_terms':terms,'scalar_rank_upper_bound':len(terms),
            'slice_matrix_ranks':slice_ranks,'complete_decomposition_replayed':True}


def piece_records(residual,r,bad):
    bad=set(bad)
    predicates=[('row',lambda i,j:i in bad and j not in bad),
                ('column',lambda i,j:i not in bad and j in bad),
                ('corner',lambda i,j:i in bad and j in bad)]
    pieces=[]
    for name,predicate in predicates:
        piece={key:value for key,value in residual.items() if predicate(*divmod(key[0],r))}
        rr=ranks(piece,(r*r,4*r,4*r))
        pieces.append({'name':name,'ranks':rr,'pair_product':min(rr[0]*rr[1],rr[0]*rr[2],rr[1]*rr[2]),
                       'nonzero_coefficients':len(piece),'coefficients':tensor_records(piece)})
    reconstructed={}
    for record in pieces:
        for a,b,c,value in record['coefficients']:
            key=(a,b,c)
            reconstructed[key]=reconstructed.get(key,0)+Fraction(value)
    if reconstructed!=residual:
        raise ArithmeticError('The three support pieces did not sum to the residual')
    return pieces


def verify_case(n,b,nonproduct=False,complete=True):
    r=n-1
    if nonproduct:
        if (n,b)!=(6,4):
            raise ValueError('The stored nonproduct variant is only n6,b4')
        maps,extra=nonproduct_maps()
    else:
        maps=product_maps(n,b)
        u,w,d,l,p,bad=product_data(n,b)
        extra={'outer_space':u,'inner_space':w,'product_matrix':d,
               'product_decoder':l,'product_projection':p}
    bad=list(range(b-1,n-2))
    actual,_=contract(n,b,(r,4,r),maps)
    residual=subtract(matrix_multiplication((r,4,r)),actual,Field())
    if not nonproduct and residual!=formula_residual(n,b):
        raise ArithmeticError('Full coefficient comparison with the family formula failed')
    report=verify_maps(n,b,(r,4,r),maps,include_witness=complete)
    if not nonproduct:
        expected_ranks=([r*r-b*b,3*r-b,3*r-b] if bad else [0,0,0])
        if report['exact_residual_flattening_ranks']!=expected_ranks:
            raise ArithmeticError('The family flattening-rank prediction failed')
    direct_scalar=scalar_decomposition(residual,(r*r,4*r,4*r))
    expected_scalar=24 if nonproduct else 4*r*len(bad)
    if direct_scalar['scalar_rank_upper_bound']!=expected_scalar:
        raise ArithmeticError('The scalar repair count changed')
    scalar=(karatsuba_certificate(n,b,residual) if not nonproduct and n==b+2
            else direct_scalar)
    pieces=piece_records(residual,r,bad)
    result={'variant':'nonproduct-middle' if nonproduct else 'product-oblique',
            'source':[n,b],'target':[r,4,r], 'maps':maps,
            'decoder_data':extra,'bad_outer_coordinates':bad,'verification':report,
            'residual_pieces':pieces,'scalar_repair':scalar,
            'new_target_identity_without_repair':not residual,
            'improves_omega':False,'historical_novelty_claimed':False}
    if scalar is not direct_scalar:
        result['direct_scalar_repair']=direct_scalar
    if n==6:
        first,optimal=minimum_first_residual(n,b,(r,4,r),*maps[1:])
        optimal_report=verify_maps(n,b,(r,4,r),[first,*maps[1:]],include_witness=False)
        if optimal_report['exact_residual_flattening_ranks'][0]!=optimal['minimum_first_residual_rank']:
            raise ArithmeticError('Attaining first-map reconstruction failed')
        result['free_first_map_optimum']=optimal
    if not complete:
        for key in ('maps','decoder_data'):
            result.pop(key)
        for record in result['residual_pieces']:
            record.pop('coefficients')
        result['scalar_repair'].pop('rank_one_terms')
        if 'direct_scalar_repair' in result:
            result['direct_scalar_repair'].pop('rank_one_terms')
    return encode(result)


def embedded_corner():
    r,bad=5,3
    residual={key:value for key,value in matrix_multiplication((r,4,r)).items()
              if key[0]//r==bad or key[0]%r==bad}
    return {'construction':'Existing exact M4 embedded into M5',
            'residual_ranks':ranks(residual,(25,20,20)),
            'scalar_rank_upper_bound':len(residual),
            'same_three_piece_ranks':[record['ranks'] for record in piece_records(residual,r,[bad])]}


def source_pins(repository):
    data=json.loads(Path(__file__).with_name('sources.json').read_text())
    for record in data['local_sources']:
        actual=hashlib.sha256((repository/record['path']).read_bytes()).hexdigest()
        if actual!=record['sha256']:
            raise ArithmeticError('Pinned source hash mismatch: '+record['path'])
    return {'repository_source_pins_checked':len(data['local_sources']),
            'pending_pr_sources_pinned':len(data.get('pending_pr_sources',[])),
            'pending_pr_sources_required_for_coefficient_replay':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--family-output',type=Path)
    parser.add_argument('--repository',type=Path)
    args=parser.parse_args()
    report={'cases':[verify_case(6,4),verify_case(6,4,nonproduct=True)],
            'baseline':embedded_corner(),'improves_omega':False}
    repository=args.repository
    if repository is None:
        repository=next((p for p in Path(__file__).resolve().parents if (p/'AGENTS.md').exists()),None)
    report['source_pin_verification']=(source_pins(repository) if repository is not None
                                     else {'repository_source_pins_checked':0})
    if args.output:
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    if args.family_output:
        family=[verify_case(n,4,complete=False) for n in range(5,11)]
        family.extend(verify_case(k+1,k-1,complete=False) for k in range(3,8) if k!=5)
        args.family_output.write_text(json.dumps({'cases':family,'improves_omega':False},indent=2)+'\n')
    print(json.dumps({'cases':[{'variant':case['variant'],
        'ranks':case['verification']['exact_residual_flattening_ranks'],
        'pieces':[p['ranks'] for p in case['residual_pieces']],
        'scalar_rank':case['scalar_repair']['scalar_rank_upper_bound'],
        'minimum_first_rank':case['free_first_map_optimum']['minimum_first_residual_rank']}
        for case in report['cases']], 'baseline':report['baseline'],'improves_omega':False},indent=2))
