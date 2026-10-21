"""Finite arithmetic controls for the written two-ruling dimension lemma."""
import json,argparse
from pathlib import Path
from itertools import combinations_with_replacement
import sympy as sp

def bound(p,q,r=7):return min(p*q,p+(q-1)*(r-p),q+(p-1)*(r-q))
def ruling_bound(r,k):
 assert r>=1 and k>=2
 bounds=[]
 for p in range(1,r+1):
  for q in range(1,r+1):
   bounds.append(min(p*q,r) if min(p,q)<=k else min(p*q,r+(q-k)*((r-p)//(k-1)),r+(p-k)*((r-q)//(k-1))))
 cap=max(bounds)
 if k==2 and r>=6:cap=min(cap,r*r//4)
 return cap

def report():
 rows=[{'p':p,'q':q,'upper':bound(p,q)} for p in range(1,8) for q in range(1,8)];exceptions=[r for r in rows if r['upper']>=13];assert [(r['p'],r['q']) for r in exceptions]==[(4,4),(5,5)];cases=[]
 for entry in exceptions:
  p,q=entry['p'],entry['q'];r=2*p-7;row=p-r;dimension=13-r;assert dimension==row*q and row>=2 and 2*q>7
  cases.append({'p':p,'q':q,'p2':7,'forced_p3':14-p,'common_core':r,'quotient_dimension':dimension,'quotient_row_rank':row,'quotient_column_rank':q,'two_column_image_dimension':2*q})
 general=[]
 for r in range(6,21):
  maximum=r*r//4+1;exceptional=[]
  for p in range(1,r+1):
   for q in range(1,r+1):
    upper=bound(p,q,r);assert upper<=maximum
    if upper==maximum:
     assert p==q and abs(2*p-(r+2))<=1
     core=2*p-r;row=r-p;assert core in (1,2,3) and row>=2 and maximum-core==row*p and 2*p>r
     exceptional.append([p,q,core,row])
  general.append({'r':r,'integer_pairs':r*r,'preliminary_bound':maximum,'proved_bound':maximum-1,'exceptional_cases':exceptional})
 # Exact Sym^2(C4) multiplication coordinates, with unordered monomial basis.
 pairs=list(combinations_with_replacement(range(4),2))
 def image(i,j):
  v=sp.zeros(10,1);v[pairs.index(tuple(sorted((i,j))))]=1;return v
 one=sp.Matrix.hstack(*(image(0,j) for j in range(4)));two=sp.Matrix.hstack(*(image(i,j) for i in range(2) for j in range(4)));whole=sp.Matrix.hstack(*(image(i,j) for i in range(4) for j in range(4)))
 control={'one_ruling_rank':one.rank(),'two_ruling_rank':two.rank(),'full_image_rank':whole.rank()};assert control=={'one_ruling_rank':4,'two_ruling_rank':7,'full_image_rank':10}
 # The seven-coordinate cross example forbids extending the theorem to r=5.
 cross_pairs=[(0,j) for j in range(4)]+[(i,0) for i in range(1,4)]
 def cross(u,v):return sp.Matrix([u[i]*v[j] for i,j in cross_pairs])
 E=sp.eye(4);u=sp.Matrix([1,1,1,1]);v=sp.Matrix([1,2,3,4]);cross_two=sp.Matrix.hstack(*(cross(w,E[:,j]) for w in [u,v] for j in range(4)));cross_full=sp.Matrix.hstack(*(cross(E[:,i],E[:,j]) for i in range(4) for j in range(4)));assert cross_two.rank()==5 and cross_full.rank()==7
 assert ruling_bound(8,3)==11
 E6=sp.eye(6);cross6=[(0,j) for j in range(6)]+[(i,0) for i in range(1,6)]
 def c6(u,v):return sp.Matrix([u[i]*v[j] for i,j in cross6])
 U=[E6[:,0],E6[:,0]+E6[:,1],E6[:,0]+E6[:,2]];three=sp.Matrix.hstack(*(c6(u,E6[:,j]) for u in U for j in range(6)));whole=sp.Matrix.hstack(*(c6(E6[:,i],E6[:,j]) for i in range(6) for j in range(6)));assert three.rank()==8 and whole.rank()==11
 return {'three_ruling_control':{'r':8,'k':3,'bound':11,'cross_three_ruling_rank':8,'cross_full_dimension':11},'general_integer_controls':general,'r5_counterexample':{'two_ruling_rank':5,'full_dimension':7},'status':'finite controls; general proof written and unreviewed','integer_pairs':rows,'equality_cases':cases,'symmetric_product_control':control,'A89_M30':{'input_rank_cap':2,'lift_upper':564,'next_symbol_threshold':576,'scalar_image_cap':12,'coefficient_cap':864,'target_parameter_dimension':900},'improves_omega':False}
def exclusion(a,b,shapes,D):
 # Use only source formats with the already recorded top Hankel rank caps.
 if (a,b) not in {(7,9),(7,10),(8,8),(8,9),(8,10),(9,9)}:return None
 r=a-1;N=a*b*(a+b-1)
 for block,(m,n,p) in enumerate(shapes):
  for leg,(dimension,t,rows,cols) in enumerate(zip((m*n,n*p,p*m),(p,m,n),(m,n,p),(n,p,m))):
   for k in range(2,min(r,rows,cols)+1):
    cap=ruling_bound(r,k);lift=k*t+2*N-sum(D)+D[leg]
    if lift<(r+1)*a*b and dimension>cap*a*b:return {'block':block,'leg':leg,'input_rank_cap':k,'lift_upper':lift,'next_symbol_threshold':(r+1)*a*b,'scalar_image_cap':cap,'coefficient_cap':cap*a*b,'target_parameter_dimension':dimension}

 return None
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.write_text(json.dumps(report(),indent=2)+'\n')
