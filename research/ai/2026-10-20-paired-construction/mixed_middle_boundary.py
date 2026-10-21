"""Exact controls for the scoped mixed-middle boundary obstruction."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import importlib.util
import json

SPEC=importlib.util.spec_from_file_location('mixed_boundary_helpers',Path(__file__).with_name('outer_product_boundary.py'))
BASE=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
SEED=BASE.SEED

def inverse(matrix):
    n=len(matrix)
    a=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        value=a[col][col]
        a[col]=[x/value for x in a[col]]
        for row in range(n):
            if row!=col and a[row][col]:
                value=a[row][col]
                a[row]=[x-value*y for x,y in zip(a[row],a[col])]
    result=[row[n:] for row in a]
    if any(x.denominator!=1 for row in result for x in row):
        raise ArithmeticError('Expected the specific integer control to be unimodular')
    return [[int(x) for x in row] for row in result]

def middle_space(singular=False):
    h=[[[0]*2 for _ in range(4)] for _ in range(4)]
    h[0][0][0]=1
    if singular:
        h[1][1][0]=1
    else:
        h[1][0][1]=1
        h[1][1][0]=1
        h[1][2][0]=2
    h[2][3][0]=1
    h[3][3][1]=1
    return h

def product_middle(outer,h):
    d=[[0]*16 for _ in range(16)]
    for i,j,p,y,b in product(range(4),range(4),range(5),range(4),range(2)):
        d[4*i+j][2*(p+y)+b]+=outer[i][p]*h[j][y][b]
    return d

def maps():
    outer,inner=SEED.subspaces(4)
    _,lb=SEED.product_matrix_and_dual(4)
    h=middle_space()
    dc=product_middle(outer,h)
    lc=inverse(list(map(list,zip(*dc))))
    a=[[0]*36 for _ in range(16)]
    b=[[0]*36 for _ in range(16)]
    c=[[0]*36 for _ in range(16)]
    for i,k,p,q in product(range(4),range(4),range(5),range(5)):
        a[4*i+k][6*p+q]=outer[k][p]*outer[i][q]
    for i,j,y,s,w in product(range(4),range(4),range(4),range(8),range(2)):
        b[4*i+j][9*y+s]+=h[j][y][w]*lb[2*i+w][s]
    for j,k,z,v,w in product(range(4),range(4),range(8),range(4),range(2)):
        c[4*j+k][4*z+v]+=lc[4*k+j][2*z+w]*inner[w][v]
    pb=[[int(row==4*i+j) for row in range(16)] for i,j in product(range(4),range(2))]
    pc=[[dc[4*k+j][2*z] for j,k in product(range(4),range(4))] for z in range(8)]
    return a,b,c,pb,pc,dc,lc

def apply_projection(pb,pc,slices):
    result=[]
    bs=SEED.sparse_columns(pb)
    cs=SEED.sparse_columns(pc)
    for row in slices:
        out=[0]*64
        for ib,ic in product(range(16),repeat=2):
            value=row[16*ib+ic]
            if not value:
                continue
            for (jb,xb),(jc,xc) in product(bs[ib],cs[ic]):
                out[8*jb+jc]+=value*xb*xc
        result.append(out)
    return result

def certificate():
    a,b,c,pb,pc,dc,lc=maps()
    slices=BASE.source_slices(4,b,c)
    failures=[]
    for ia,ib,ic in product(range(16),repeat=3):
        value=sum(a[ia][s]*slices[s][16*ib+ic] for s in range(36))
        i,k=divmod(ia,4);ii,j=divmod(ib,4);jj,kk=divmod(ic,4)
        expected=int(i==ii and j==jj and k==kk)
        if value!=expected:
            failures.append([ia,ib,ic,value,expected])
    if failures:
        raise ArithmeticError(f'Complete tensor identity failed: {failures[:3]}')
    projected=apply_projection(pb,pc,slices)
    pivots=BASE.pivots(projected)
    if len(pivots)!=36:
        raise ArithmeticError('Projected mixed source is not injective')
    minor=[[row[col] for col in pivots] for row in projected]
    det=BASE.determinant(minor)
    b2=[row[:] for row in b];c2=[row[:] for row in c]
    for row,y in product(range(16),range(4)):
        b2[row][9*y+8]=(3*row+2*y+1)%7-3
        c2[row][32+y]=(5*row+3*y+2)%11-5
    changed_projection=apply_projection(pb,pc,BASE.source_slices(4,b2,c2))
    changed=[i for i in range(36) if projected[i]!=changed_projection[i]]
    if changed!=[35]:
        raise ArithmeticError('A noncorner projected slice changed')
    bx=[sum(pb[i][r]*b2[r][35] for r in range(16)) for i in range(8)]
    cx=[sum(pc[i][r]*c2[r][35] for r in range(16)) for i in range(8)]
    if [x-y for x,y in zip(changed_projection[35],projected[35])]!=[x*y for x,y in product(bx,cx)]:
        raise ArithmeticError('Wrong boundary outer-product update')
    outer,_=SEED.subspaces(4)
    singular=product_middle(outer,middle_space(True))
    # R=(-t^2,t,0,0): component H0 uses -U1; component H1 uses U0.
    kernel=[0]*16
    kernel[4*1+0]=-1
    kernel[4*0+1]=1
    if any(sum(kernel[i]*singular[i][j] for i in range(16)) for j in range(16)):
        raise ArithmeticError('The deliberately singular middle module did not have the stated syzygy')
    return {
        'source':'Q_(6,4)','retained_target':'M(4,4,4)',
        'all_target_coefficients_checked':4096,'target_nonzero_coefficients':64,
        'coefficient_failures':0,'nonproduct_middle_space':middle_space(),
        'product_middle_determinant':BASE.determinant(dc),
        'projected_source_A_rank':36,'rank_minor_columns':pivots,'rank_minor_determinant':det,
        'all_boundary_columns_modified':True,'projected_slices_changed':changed,
        'corner_outer_product_update_checked':True,
        'singular_middle_space':middle_space(True),'singular_middle_syzygy_U_by_H':kernel,
        'singular_middle_product_rank':len(BASE.pivots(singular)),
        'maps_target_by_source':[a,b,c],'B_projection':pb,'C_projection':pc,
        'D_C':dc,'L_C':lc,'integer_certificate':True,
        'generic_P5_outer_subspaces_excluded':False,'general_degeneration_excluded':False,
        'improves_omega':False,'external_review_claimed':False,
    }

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report=certificate()
    if args.output:
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['maps_target_by_source','B_projection','C_projection','D_C','L_C']},indent=2))
