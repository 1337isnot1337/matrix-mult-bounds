"""Exploratory exact quantum Clebsch--Gordan bases, not a degeneration witness."""
from functools import lru_cache
from sympy.polys.fields import field
from sympy.polys.domains import QQ
from sympy import cyclotomic_poly, Symbol

K,q=field('q',QQ)
R=q.numer.ring

@lru_cache(None)
def qint(n):
    if n==0:return K.zero
    return sum((q**(n-1-2*i) for i in range(n)),K.zero)

def qchoose(n,k):
    out=K.one
    for i in range(1,k+1):out=out*qint(n-k+i)/qint(i)
    return out

def lowering(m,n,s,vector):
    out={}
    for i,c in vector.items():
        j=s-i
        if i<m:out[i+1]=out.get(i+1,K.zero)+c*qint(i+1)
        if j<n:out[i]=out.get(i,K.zero)+c*q**(-m+2*i)*qint(j+1)
    return {i:c for i,c in out.items() if c}

@lru_cache(None)
def cg(m,n):
    columns={}
    for k in range(min(m,n)+1):
        vector={0:K.one}
        for i in range(k):
            vector[i+1]=-vector[i]*qint(n-k+i+1)/qint(m-i)*q**(-n+2*k-2*i-2)
        for level in range(m+n-2*k+1):
            columns[k,level]=dict(vector)
            if level<m+n-2*k:
                vector={i:c/qint(level+1) for i,c in lowering(m,n,k+level,vector).items()}
    return columns

def determinant(matrix):
    a=[list(row) for row in matrix];out=K.one
    for col in range(len(a)):
        pivot=next((i for i in range(col,len(a)) if a[i][col]),None)
        if pivot is None:return K.zero
        if pivot!=col:a[col],a[pivot]=a[pivot],a[col];out=-out
        value=a[col][col];out*=value
        for i in range(col+1,len(a)):
            ratio=a[i][col]/value
            for j in range(col+1,len(a)):a[i][j]-=ratio*a[col][j]
    return out

def inverse(matrix):
    size=len(matrix)
    a=[list(row)+[K.one if i==j else K.zero for j in range(size)] for i,row in enumerate(matrix)]
    for col in range(size):
        pivot=next(i for i in range(col,size) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        value=a[col][col];a[col]=[x/value for x in a[col]]
        for i in range(size):
            if i==col or not a[i][col]:continue
            ratio=a[i][col]
            a[i]=[x-ratio*y for x,y in zip(a[i],a[col])]
    return [row[size:] for row in a]

@lru_cache(None)
def inverse_cg(m,n):
    cols=cg(m,n);out={}
    for s in range(m+n+1):
        indices=list(range(max(0,s-n),min(m,s)+1))
        labels=[(k,s-k) for k in range(min(m,n)+1) if 0<=s-k<=m+n-2*k]
        matrix=[[cols[label].get(i,K.zero) for label in labels] for i in indices]
        inv=inverse(matrix)
        for j,i in enumerate(indices):
            out[i,s-i]=[(label,inv[t][j]) for t,label in enumerate(labels) if inv[t][j]]
    return out

def invariant_coefficient(m,n,i,j):
    s=i+j;h=m+n
    return (-1)**s*q**(j*(i-m)+s*(h-s-1))/qchoose(h,s)

def paired_recoupled(a):
    D=a-1;h=2*D
    maps=[inverse_cg(D,D),inverse_cg(D,h),inverse_cg(h,D)]
    out={}
    for p in range(a):
        for q0 in range(a):
            for y in range(a):
                for v in range(a):
                    coeff=invariant_coefficient(D,D,p,y)*invariant_coefficient(D,D,q0,v)
                    for A,x in maps[0][p,q0]:
                        for B,z in maps[1][y,h-q0-v]:
                            for C,w in maps[2][h-p-y,v]:
                                key=(A,B,C)
                                out[key]=out.get(key,K.zero)+coeff*x*z*w
    return {key:value for key,value in out.items() if value}

def valuation(value,polynomial):
    if not value: return 10**9
    out=0
    for sign,poly in [(1,value.numer),(-1,value.denom)]:
        while True:
            quotient,remainder=poly.div(polynomial)
            if remainder:break
            poly=quotient;out+=sign
    return out

def initial_residue(value,polynomial):
    """Return uniformizer order and leading residue in QQ[q]/(polynomial)."""
    if not value:return None,None
    out=0;parts=[]
    for sign,poly in [(1,value.numer),(-1,value.denom)]:
        while True:
            quotient,remainder=poly.div(polynomial)
            if remainder:break
            poly=quotient;out+=sign
        parts.append(poly.rem(polynomial))
    return out,parts

def basis_defects(m,n,root_order):
    poly=R.from_expr(cyclotomic_poly(root_order,Symbol('q'))) if root_order else q.numer
    cols=cg(m,n);records=[]
    for s in range(m+n+1):
        indices=list(range(max(0,s-n),min(m,s)+1))
        labels=[(k,s-k) for k in range(min(m,n)+1) if 0<=s-k<=m+n-2*k]
        matrix=[[cols[label].get(i,K.zero) for label in labels] for i in indices]
        determinant_valuation=valuation(determinant(matrix),poly)
        minima=[min(valuation(cols[label].get(i,K.zero),poly) for i in indices) for label in labels]
        records.append({'weight_index':s,'dimension':len(indices),'determinant_valuation':determinant_valuation,
                        'column_valuation_sum':sum(minima),'coalescence_defect':determinant_valuation-sum(minima)})
    return records

def highest_projection(m,n,i,j):
    s=i+j
    return q**(i*(n-j))*qchoose(m,i)*qchoose(n,j)/qchoose(m+n,s)

def coefficient_controls(m,n):
    for i in range(m+1):
        for j in range(n+1):
            s=i+j;c=highest_projection(m,n,i,j)
            lhs=c*qint(m+n-s+1) if s else K.zero
            rhs=K.zero
            if i:rhs+=qint(m-i+1)*q**(n-2*j)*highest_projection(m,n,i-1,j)
            if j:rhs+=qint(n-j+1)*highest_projection(m,n,i,j-1)
            if lhs!=rhs:raise ArithmeticError(('E intertwiner',m,n,i,j))
            lhs=c*qint(s+1) if s<m+n else K.zero;rhs=K.zero
            if i<m:rhs+=qint(i+1)*highest_projection(m,n,i+1,j)
            if j<n:rhs+=q**(-m+2*i)*qint(j+1)*highest_projection(m,n,i,j+1)
            if lhs!=rhs:raise ArithmeticError(('F intertwiner',m,n,i,j))
    return (m+1)*(n+1)


def cyclic_local_map(a):
    D=a-1;h=2*D;first=inverse_cg(D,D)
    second={k:inverse_cg(2*D-2*k,h) for k in range(D+1)}
    labels=[(k,K,e) for k in range(D+1) for K in range(min(2*D-2*k,h)+1)
            for e in range(2*D-2*k+h-2*K+1)]
    label_index={label:i for i,label in enumerate(labels)}
    entries={}
    for i in range(a):
        for j in range(a):
            for z in range(h+1):
                s=h-z
                factor=q**(-i*(i-1)//2-D*j-j*(j-1)//2)*(-1)**s*q**(s*(s-1)//2+s*(h-s-1))/qchoose(h,s)
                for (k,d),x in first[i,j]:
                    for (K,e),y in second[k][d,z]:
                        entries[label_index[k,K,e],(i*a+j)*(h+1)+z]=x*y*factor
    return labels,entries

def invariant_controls(m,n):
    h=m+n;checks=0
    def c(i,j,k):
        return invariant_coefficient(m,n,i,j) if (0<=i<=m and 0<=j<=n and 0<=k<=h and i+j+k==h) else K.zero
    for i in range(m+1):
        for j in range(n+1):
            for k in range(h+1):
                if i+j+k==h-1:
                    value=c(i+1,j,k)*qint(m-i)*q**(n-2*j+h-2*k)+c(i,j+1,k)*qint(n-j)*q**(h-2*k)+c(i,j,k+1)*qint(h-k)
                    if value:raise ArithmeticError('invariant E equation')
                    checks+=1
                if i+j+k==h+1:
                    value=c(i-1,j,k)*qint(i)+c(i,j-1,k)*q**(-m+2*i)*qint(j)+c(i,j,k-1)*q**(-m+2*i-n+2*j)*qint(k)
                    if value:raise ArithmeticError('invariant F equation')
                    checks+=1
    return checks

def rank_over_field(matrix,zero):
    a=[list(row) for row in matrix];rank=0
    if not a:return 0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]!=zero),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        value=a[rank][j]
        for i in range(rank+1,len(a)):
            if a[i][j]==zero:continue
            ratio=a[i][j]/value
            for k in range(j+1,len(a[0])):a[i][k]-=ratio*a[rank][k]
            a[i][j]=zero
        rank+=1
        if rank==len(a):break
    return rank

def cyclic_regular_initial(a):
    """Exact rowwise-regular initial map over QQ(i); not a general q-family screen."""
    from sympy import I
    from collections import Counter
    field=QQ.algebraic_field(I);poly=q.numer**2+1
    labels,entries=cyclic_local_map(a)
    expansions={key:initial_residue(value,poly) for key,value in entries.items()}
    minima=[min(v for (i,j),(v,parts) in expansions.items() if i==row) for row in range(len(labels))]
    def residue(parts):
        values=[]
        for p in parts:
            value=sum((QQ.to_sympy(c)*I**e[0] for e,c in p.items()))
            values.append(field.from_sympy(value))
        return values[0]/values[1]
    initials={(i,j):residue(parts) for (i,j),(v,parts) in expansions.items() if v==minima[i]}
    D=a-1;h=2*D;records=[]
    for w in range(4*D+1):
        rows=[i for i,label in enumerate(labels) if sum(label)==w]
        cols=[(i*a+j)*(h+1)+z for i in range(a) for j in range(a) for z in range(h+1) if i+j+z==w]
        block=[[initials.get((i,j),field.zero) for j in cols] for i in rows]
        records.append({'weight_index':w,'dimension':len(rows),'rank_over_QQ_i':rank_over_field(block,field.zero)})
    return {'a':a,'format_leg_dimension':len(labels),'root':'i','uniformizer':'q^2+1',
            'row_minimum_valuation_histogram':dict(sorted(Counter(minima).items())),
            'constant_map_rank_over_QQ_i':sum(row['rank_over_QQ_i'] for row in records),'weight_blocks':records,
            'scope':'Only the rowwise-regular normalization. Its limit is an ordinary restriction; no singular tensor-level normalization is excluded.'}

def report():
    coefficients=sum(coefficient_controls(m,n) for m in range(1,5) for n in range(1,5))
    invariants=sum(invariant_controls(m,n) for m in range(1,5) for n in range(1,5))
    records=[]
    for m,n in [(1,1),(1,2),(2,2),(2,4),(3,3),(3,6)]:
        for order in [0,3,4,6,8]:
            rows=basis_defects(m,n,order)
            records.append({'m':m,'n':n,'root_order':order,
                            'total_coalescence_defect':sum(row['coalescence_defect'] for row in rows),'rows':rows})
    return {'highest_projection_positions_E_and_F':coefficients,'invariant_E_F_equations':invariants,
            'basis_controls':records,'cyclic_regular_initial_maps':[cyclic_regular_initial(a) for a in [2,3,4]],
            'improves_omega':False,'independent_review':False,
            'scope':'Exact generic coefficient controls and one ordinary-limit calibration. No surviving exponent-improving target is constructed.'}

if __name__=='__main__':
    import json,argparse
    from pathlib import Path
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report();args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['highest_projection_positions_E_and_F','invariant_E_F_equations','improves_omega']}))

