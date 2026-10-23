"""Exact small controls for the equality crossed-flattening claim."""
import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('crossed_equality_rank',Path(__file__).with_name('equality_counterexample.py'))
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
rank=helper.rank
from itertools import product
import random

def matrices(F,a,b):
 m=a+b-1
 def f(i,k,s):return F[(i*m+k)*b+s] if 0<=i<a and 0<=s<b else 0
 rows=list(product(range(b),range(a),range(m)))
 cols=list(product(range(m),range(b),range(a)))
 full=[[f(H-j,p+q,L-t) for H,q,t in cols] for j,p,L in rows]
 cross=[[f(i,p+q,s) for q,i in product(range(b),range(a))]
        for p,s in product(range(a),range(b))]
 symbol=[[sum(f(i,p+q,s)*2**i*3**s for i,s in product(range(a),range(b)))
          for q in range(b)] for p in range(a)]
 return full,cross,symbol

def controls():
 rng=random.Random(271828);checked=0;equalities=0
 for a,b in [(2,2),(2,3),(3,3)]:
  m=a+b-1
  for _ in range(32):
   F=[rng.choice((0,0,0,1,-1)) for _ in range(a*b*m)]
   full,cross,symbol=matrices(F,a,b)
   R=rank(full);r=rank(symbol);checked+=1
   assert R>=(a*b-1)*r+rank(cross)
   if R==a*b*r:
    assert rank(cross)==r
    equalities+=1
 # A nonseparable biform times a constant rank-two Hankel sequence.
 a=b=3;m=5;F=[0]*(a*b*m)
 for k in (0,2,4):
  F[k*b]=1;F[(m+k)*b+1]=1
 full,cross,symbol=matrices(F,a,b)
 nonequality={'full_rank':rank(full),'symbol_rank':rank(symbol),'crossed_rank':rank(cross)}
 assert nonequality['symbol_rank']==2 and nonequality['crossed_rank']==4
 assert nonequality['full_rank']>a*b*2
 # Actual frontier equality family; avoid constructing its 1152-square matrix.
 a=8;b=9;m=16
 def f(i,k,s):
  if s:return 0
  return sum(t**k for t in range(1,a+1)) if i==0 else (a+1)**k if i==1 else 0
 cross=[[f(i,p+q,s) for q,i in product(range(b),range(a))]
        for p,s in product(range(a),range(b))]
 assert rank(cross)==8
 return {'rational_examples_checked':checked,'quantitative_bound_checks':checked,'equality_cases':equalities,
         'strict_inequality_control':nonequality,'A89_equality_crossed_rank':rank(cross)}

if __name__=='__main__':
 import json
 print(json.dumps(controls(),indent=2))
