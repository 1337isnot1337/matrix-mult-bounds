"""Independent canonical integer maps and original-source boundary-pair replay."""
from fractions import Fraction
from pathlib import Path
import argparse
import json

def inverse_integer(matrix):
    n=len(matrix)
    work=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)]
          for i,row in enumerate(matrix)]
    determinant=Fraction(1)
    for k in range(n):
        p=next(i for i in range(k,n) if work[i][k])
        if p!=k:
            work[p],work[k]=work[k],work[p];determinant=-determinant
        v=work[k][k];determinant*=v;work[k]=[x/v for x in work[k]]
        for i in range(n):
            if i==k:continue
            v=work[i][k]
            work[i]=[a-v*b for a,b in zip(work[i],work[k])]
    assert abs(determinant)==1
    answer=[row[n:] for row in work]
    assert all(x.denominator==1 for row in answer for x in row)
    return [[int(x) for x in row] for row in answer],int(determinant)

def multiply(A,B):
    return [[sum(a*b for a,b in zip(row,column)) for column in zip(*B)]
            for row in A]

def transpose(A):return [list(row) for row in zip(*A)]

def construct(m):
    assert isinstance(m,int) and m>=3
    n=m-1;a=m+2;b=m+1;out=2*m+2
    def monomial(k,size=a):
        row=[0]*size;row[k]=1;return row
    def form(terms,size=a):
        row=[0]*size
        for k,v in terms:row[k]+=v
        return row
    U=[monomial(k) for k in range(2,m-1)]
    U += [form([(1,1),(m-1,1)]),form([(0,1),(1,1),(m,1)]),
          form([(1,1),(m+1,1)])]
    R=[]
    R.append(form([(m-3,1),(m-2,-1)],m))
    R.extend(monomial(m-j-2,m) for j in range(2,m-1))
    R.extend([monomial(m-2,m),monomial(m-1,m)])
    _,r_det=inverse_integer(R)
    # D_n(lambda)=det(I+lambda J), by the tridiagonal determinant recurrence.
    prev=[1];current=[1,1]
    if n==1:D=current
    else:
        for k in range(2,n+1):
            new=[0]*(k+1)
            for j,v in enumerate(current):new[j]+=v;new[j+1]+=v
            for j,v in enumerate(prev):new[j+2]-=v
            prev,current=current,new
        D=current
    J=[[int(abs(i-j)<=1) for j in range(n)] for i in range(n)]
    e=[int(i==n-1) for i in range(n)]
    xs=[[0]*n]
    for k in range(1,n+1):
        xs.append([-sum(J[i][j]*xs[-1][j] for j in range(n))+D[k-1]*e[i]
                   for i in range(n)])
    assert [sum(J[i][j]*xs[-1][j] for j in range(n)) for i in range(n)]==[D[n]*v for v in e]
    V=transpose([xs[k]+[D[k]] for k in range(n+1)])
    _,v_det=inverse_integer(V)
    X=transpose(xs[1:])
    X_inverse,x_det=inverse_integer(X)
    W=multiply(transpose(V),R)
    W_inverse,w_det=inverse_integer(W)
    shared=multiply(W,U)
    # The new boundary Y basis is -X^{-T} applied to (t,...,t^n).
    Y=[monomial(0,b),monomial(m,b)]
    Y += [[0]+[-v for v in row]+[0] for row in X_inverse]
    d=[monomial(i+2,out) for i in range(m-3)]
    ee=[monomial(m+i+2,out) for i in range(m-3)]
    d += [monomial(m-1,out),monomial(0,out),
          form([(1,1),(0,-1),(m-1,-1)],out)]
    ee += [monomial(2*m-1,out),monomial(2*m,out),monomial(2*m+1,out)]
    dual_change=transpose(W_inverse)
    dd=multiply(dual_change,d);ee=multiply(dual_change,ee)
    Z=[[dd[j][k]+ee[j+1][k] for k in range(out)] for j in range(n)]
    E0=form([(0,1),(m,-1),(2*m,1)],out)
    E1=form([(1,1),(m-1,-1),(m,-1),(m+1,-1),(2*m-1,1),
             (2*m,2),(2*m+1,1)],out)
    Z += [[-v for v in E1],E0]
    assert len(shared)==m and len(Y)==len(Z)==m+1
    return {"m":m,"source":[a,b],"shared":shared,"Y":Y,"Z":Z,
            "weights_Y":[0,0]+[1]*n,"weights_Z":[0]*n+[-1,-1],
            "unimodular_determinants":{"R":r_det,"V":v_det,"X":x_det,"W":w_det},
            "coefficient_ring":"integers","improves_omega":False}

def verify(data):
    m=data["m"];n=m-1;a,b=data["source"]
    assert [a,b]==[m+2,m+1]
    U,Y,Z=(data[key] for key in ("shared","Y","Z"))
    assert len(U)==m and all(len(row)==a for row in U)
    assert len(Y)==m+1 and all(len(row)==b for row in Y)
    assert len(Z)==m+1 and all(len(row)==a+b-1 for row in Z)
    assert all(isinstance(x,int) for M in (U,Y,Z) for row in M for x in row)
    negative=constant=nonzero=positive=0
    for i,u in enumerate(U):
        for j,y in enumerate(Y):
            product=[0]*(a+b-1)
            for r,ur in enumerate(u):
                if ur:
                    for s,ys in enumerate(y):product[r+s]+=ur*ys
            for k,z in enumerate(Z):
                value=sum(c*d for c,d in zip(product,z))
                degree=data["weights_Y"][j]+data["weights_Z"][k]
                if degree<0:
                    assert value==0,("negative",i,j,k,value);negative+=1
                elif degree==0:
                    expected=int(i==j+k) if j<2 else int(i==(j-2)+(k-n))
                    assert value==expected,("constant",i,j,k,value,expected)
                    constant+=1;nonzero+=value
                elif value:positive+=1
    assert negative==4*m and constant==4*m*n and nonzero==4*n
    return {"m":m,"source":[a,b,a+b-1],"target":[m,m+1,m+1],
            "positions":m*(m+1)**2,"negative":negative,"constant":constant,
            "retained_monomials":nonzero,"positive_nonzero":positive,
            "unimodular_determinants":data["unimodular_determinants"],
            "maximum_absolute_entry":max(abs(v) for M in (U,Y,Z) for row in M for v in row)}

def report():
    cases=[verify(construct(m)) for m in range(3,21)]
    return {"status":"exact canonical integer source replay passed", "cases":cases,
            "total_positions":sum(c["positions"] for c in cases),
            "all_fields":True,"common_shared_basis":True,
            "external_mathematical_review":False,"improves_omega":False}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args();text=json.dumps(report(),indent=2)+"\n"
    if args.output:args.output.write_text(text)
    print(text)
