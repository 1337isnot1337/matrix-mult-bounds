"""Exact sparse shifted-span controls; no numerical discovery dependencies."""
from pathlib import Path
import argparse,json

def control(r,T,degree):
 # Basis e0, t^degree e0, e1,...,e_(r-1), with all shifts 0,...,T-1.
 supports=[(0,0),(0,degree)]+[(j,0) for j in range(1,r)]
 columns=[(row,power+shift) for shift in range(T) for row,power in supports]
 image=set(columns);rank=len(image);expected=T*(r+1)-max(0,T-degree)
 assert rank==expected
 # Every column is an integer coordinate vector. Distinct coordinates give
 # matching identity minors and an exact support upper bound.
 pivots=[];seen=set()
 for i,c in enumerate(columns):
  if c not in seen:seen.add(c);pivots.append(i)
 return {'r':r,'T':T,'primitive_relation_degree':degree,'input_dimension':len(columns),'exact_rank':rank,'kernel_dimension':len(columns)-rank,'one_unit_equality':rank==T*r+1,'identity_minor_columns':pivots}

def source_control(a=8,b=10):
 m=a+b-1;F={(0,0,0):1,(1,a-1,1):1}
 columns={}
 for p in range(a):
  for L in range(m):
   column={(i,q*a+r):F.get((i,p+q,L-r),0) for i in (0,1) for q in range(b) for r in range(a)}
   column={key:value for key,value in column.items() if value}
   if column:columns[p,L]=column
 first=columns[0,0];second=columns[a-1,1]
 assert second=={(i+1,row):value for (i,row),value in first.items()}
 assert len(columns)==a*a+1
 def binary_rank(vectors):
  pivots={}
  for v in vectors:
   while v:
    k=v.bit_length()-1
    if k in pivots:v^=pivots[k]
    else:pivots[k]=v;break
  return len(pivots)
 const_rank=binary_rank([sum(1<<(i*a*b+row) for i,row in c) for c in columns.values()])
 shifted_rank=binary_rank([sum(1<<((i+shift)*a*b+row) for i,row in c) for shift in range(b) for c in columns.values()])
 assert const_rank==a*a+1 and shifted_rank==a*a*b+1
 return {'a':a,'b':b,'nonzero_K_columns':len(columns),'constant_coefficient_rank_mod_2':const_rank,'shifted_rank_mod_2':shifted_rank,'linear_relation':'x*K_column(0,0)-K_column(a-1,1)=0','relation_verified_over_Z':True,'kernel_upper_bound_from_b_minus_1_independent_shifts':b-1}

def report():
 rows=[control(r,T,d) for r,T in [(2,2),(3,4),(8,8),(64,10)] for d in (1,2)]
 assert all(x['one_unit_equality']==(x['primitive_relation_degree']==1) for x in rows)
 return {'status':'finite exact controls for written one-unit relation lemma; no exponent gain','controls':rows,'actual_rank641_source_control':source_control()}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=report();a.output.write_text(json.dumps(r,indent=2)+'\n');print('Exact shifted-span controls passed.')
