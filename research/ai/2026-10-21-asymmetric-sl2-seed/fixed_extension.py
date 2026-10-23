"""Exact modular full-rank certificates for mixed-channel annihilators."""
from pathlib import Path
import importlib.util,json
from math import lcm
P=Path(__file__).with_name('rectangular_exact.py');spec=importlib.util.spec_from_file_location('rectangular_exact_local',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
def rank_witness(matrix,prime=1000003):
 basis={};selected=[]
 for index,raw in enumerate(matrix):
  row=[v%prime for v in raw]
  for pivot,b in sorted(basis.items()):
   factor=row[pivot]
   if factor:row=[(x-factor*y)%prime for x,y in zip(row,b)]
  pivot=next((i for i,x in enumerate(row) if x),None)
  if pivot is not None:
   inv=pow(row[pivot],-1,prime);basis[pivot]=[(x*inv)%prime for x in row];selected.append(index)
 return {'prime':prime,'rank':len(basis),'independent_rows':selected}
def verify():
 M=e.maps();denoms=[lcm(*(v.denominator for row in m for v in row)) for m in M];rows=[[[ (j,int(v*d)) for j,v in enumerate(row) if v] for row in m] for d,m in zip(denoms,M)];B=[[0]*45 for _ in range(375)];C=[[0]*45 for _ in range(375)]
 def ix(i,k,s):return (i*5+k)*3+s
 for i in range(3):
  for j in range(3):
   for p in range(3):
    for q in range(3):
     for r in range(3):
      for s in range(3):
       ia,ib,ic=ix(i,p+q,s),ix(p,r+s,j),ix(r,i+j,q)
       for a,x in rows[0][ia]:
        for c,z in rows[2][ic]:B[15*a+c][ib]+=x*z
        for b,y in rows[1][ib]:C[15*a+b][ic]+=x*y
 result={name:rank_witness(m) for name,m in [('B',B),('C',C)]}
 assert result['B']['rank']==result['C']['rank']==45
 return result
if __name__=='__main__':print(json.dumps(verify(),indent=2))
