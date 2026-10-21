"""Exact first-jet diagnostics for an M(2,4,2) lead in Q64 plus one scalar."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import importlib.util,json

ROOT=Path(__file__).resolve().parents[3]
PATH=ROOT/'research/ai/2026-10-20-paired-construction/outer_product_boundary.py'
SPEC=importlib.util.spec_from_file_location('small_lead_helpers',PATH)
BASE=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(BASE)
OUT=Path(__file__).resolve().parent

def kernel(matrix,columns=None):
    if not matrix:
        return [[Fraction(i==j) for i in range(columns)] for j in range(columns)],[]
    a=[[Fraction(x) for x in row] for row in matrix]
    n=len(a[0]);r=0;piv=[]
    for col in range(n):
        p=next((i for i in range(r,len(a)) if a[i][col]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        value=a[r][col];a[r]=[x/value for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][col]:
                value=a[i][col];a[i]=[x-value*y for x,y in zip(a[i],a[r])]
        piv.append(col);r+=1
        if r==len(a):break
    result=[]
    for f in range(n):
        if f in piv:continue
        v=[Fraction(0)]*n;v[f]=1
        for i,p in enumerate(piv):v[p]=-a[i][f]
        result.append(v)
    return result,piv

def leading_maps():
    oa,ob,oc=BASE.SEED.maps(2)
    a=[[0]*37 for _ in range(4)]
    b=[[0]*37 for _ in range(8)]
    c=[[0]*37 for _ in range(8)]
    for row,p,q in product(range(4),range(3),range(3)):
        a[row][6*p+q]=oa[row][3*p+q]
    for row,y,s in product(range(8),range(2),range(4)):
        b[row][9*y+s]=ob[row][4*y+s]
    for row,z,v in product(range(8),range(4),range(2)):
        c[row][4*z+v]=oc[row][2*z+v]
    for row in range(8):
        b[row][36]=b[row][3]
        c[row][36]=c[row][12]
    return a,b,c

def source_terms():
    return [(6*p+q,9*y+q+v,4*(p+y)+v)
            for p,q,y,v in product(range(6),range(6),range(4),range(4))]+[(36,36,36)]

def k0_basis():
    result=[];labels=[]
    for p,q in product(range(6),repeat=2):
        if p>=4 or q>=4:
            result.append({6*p+q:1});labels.append(f'A{p}{q}')
    result.append({36:1,21:-1});labels.append('scalar-A33')
    return result,labels

def source_slices(b,c):
    s=[[0]*64 for _ in range(37)]
    bc=BASE.SEED.sparse_columns(b);cc=BASE.SEED.sparse_columns(c)
    for ia,ib,ic in source_terms():
        for (jb,xb),(jc,xc) in product(bc[ib],cc[ic]):
            s[ia][8*jb+jc]+=xb*xc
    return s

def jet_operator(leg,b,c):
    kb,_=k0_basis()
    lift=[]
    for vec in kb:
        m=[[0]*37 for _ in range(8)]
        for ia,ib,ic in source_terms():
            if ia not in vec:continue
            if leg=='B':
                for out in range(8):m[out][ib]+=vec[ia]*c[out][ic]
            else:
                for out in range(8):m[out][ic]+=vec[ia]*b[out][ib]
        lift.append(m)
    equations=[]
    coefficient_rows=[]
    for a in range(21):
        # B: rows are new j, old C index 2*j'+k.
        # C: columns are new j, old B index 4*i+j'.
        index=(lambda j,k:2*j+k) if leg=='B' else (lambda j,k:4*k+j)
        for j,jj,k in product(range(4),range(4),range(2)):
            if j==jj:continue
            row=[0]*148
            row[37*j:37*(j+1)]=lift[a][index(jj,k)]
            if any(row):equations.append(row)
        for j,k in product(range(1,4),range(2)):
            row=[0]*148
            row[37*j:37*(j+1)]=lift[a][index(j,k)]
            for col,x in enumerate(lift[a][index(0,k)]):row[col]-=x
            if any(row):equations.append(row)
        for k in range(2):
            row=[0]*148;row[:37]=lift[a][index(0,k)]
            coefficient_rows.append(row)
    ns,piv=kernel(equations,148)
    image=[[sum(x*y for x,y in zip(row,vec)) for row in coefficient_rows] for vec in ns]
    image=[row for row in image if any(row)]
    zero_columns=([9*y+s for y,s in product(range(4),range(4,7))] if leg=='B'
                  else [4*z+v for z,v in product(range(4,7),range(4))])
    copied_column=3 if leg=='B' else 12
    for vec in ns:
        if any(vec[37*j+col] for j,col in product(range(4),zero_columns)):
            raise ArithmeticError('The computed kernel violates a claimed zero column')
        if any(vec[37*j+36]!=vec[37*j+copied_column] for j in range(4)):
            raise ArithmeticError('The computed kernel violates the scalar copy relation')
    if len(ns)!=96 or image:
        raise ArithmeticError('The stated exact first-jet obstruction failed')
    action_rows=[]
    for row in image:
        action_rows.extend([[row[2*a+k] for a in range(21)] for k in range(2)])
    return {'equations':equations,'kernel':ns,'pivot_columns':piv,'coefficient_image':image,
            'possible_action_row_rank':len(BASE.pivots(action_rows)) if action_rows else 0,
            'nonzero_image_vectors':len(image),'action_rows':action_rows,
            'forced_zero_source_columns':zero_columns,'scalar_copies_source_column':copied_column,
            'canonical_kernel_conditions_checked':True,'nullity':len(ns),
            'nonzero_equations':len(equations)}

def enc(x):
    if isinstance(x,Fraction):return int(x) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
    if isinstance(x,list):return [enc(v) for v in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x

def certificate(include_linear_systems=True):
    a,b,c=leading_maps();s=source_slices(b,c)
    piv=BASE.pivots(s)
    if len(piv)!=16:raise ArithmeticError('Wrong leading source rank')
    active_rows=[6*p+q for p,q in product(range(4),repeat=2)]
    rank_minor=[[s[row][column] for column in piv] for row in active_rows]
    rank_det=BASE.determinant(rank_minor)
    if not rank_det:raise ArithmeticError('The saved rank minor is zero')
    kb,labels=k0_basis()
    for vec in kb:
        if any(sum(coef*s[row][col] for row,coef in vec.items()) for col in range(64)):
            raise ArithmeticError('Wrong K0 generator')
    for ia,ib,ic in product(range(4),range(8),range(8)):
        value=sum(a[ia][row]*s[row][8*ib+ic] for row in range(37))
        i,k=divmod(ia,2);ii,j=divmod(ib,4);jj,kk=divmod(ic,2)
        if value!=int(i==ii and j==jj and k==kk):raise ArithmeticError('Wrong M2 lead')
    data={};allrows=[]
    for leg in ['B','C']:
        d=jet_operator(leg,b,c)
        allrows.extend(d.pop('action_rows'))
        data[leg]=d
    unionrank=len(BASE.pivots(allrows)) if allrows else 0
    report={'leading_maps_target_by_source':[a,b,c], 'source':'Q_(6,4) direct_sum D1',
            'leading_target':'M(2,4,2)','source_A_dimension':37,'leading_source_A_rank':16,
            'target_M5_outside_old_A_dimension':21,'tight_saturated_dimension':37,
            'K0_labels':labels,'K0_sparse_basis':kb,'old_rank_output_pivots':piv,
            'old_rank_source_rows':active_rows,'old_rank_minor_determinant':rank_det,
            'first_jet_data':data,'joint_possible_action_row_rank':unionrank,
            'required_first_cross_jet_rank':12,'full_M5_certificate':False,
            'improves_omega':False,'all_leading_coefficients_checked':256,
            'fixed_sparse_leading_maps':True,'different_leading_maps_excluded':False,
            'arbitrary_higher_order_valuation_patterns_excluded':False,
            'external_review_claimed':False}
    if not include_linear_systems:
        for d in data.values():
            d.pop('equations');d.pop('kernel')
    return enc(report)

if __name__=='__main__':
    report=certificate()
    (OUT/'q64-m2-leading-first-jet.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['first_jet_data','leading_maps_target_by_source']},indent=2))
