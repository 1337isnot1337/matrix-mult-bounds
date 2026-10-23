"""Exact circuit-count and Hermite controls for the scoped linearity proof."""
from pathlib import Path
from itertools import combinations
from math import factorial
import argparse,json
import sympy as s
from sympy.polys.matrices import DomainMatrix

def report():
 bounds=[]
 for k in range(3,8):
  vals=[l*(8+k-l)+10*(k-l)-1+(7-k)*17 for l in range(1,k)]
  bounds.append({'circuit_size':k,'bounds_by_factor_rank':vals,'maximum':max(vals)})
 assert [x['maximum'] for x in bounds]==[97,91,85,80,75]
 def jet(t,d):return s.Matrix([factorial(k)//factorial(k-d)*t**(k-d) if k>=d else 0 for k in range(17)])
 multiplicities=[2]+[1]*6
 base=s.Matrix.hstack(*[jet(t,d) for t,e in enumerate(multiplicities) for d in range(e+1)])
 assert DomainMatrix.from_Matrix(base).convert_to(s.QQ).rank()==15
 extras=[jet(t,e+1) for t,e in enumerate(multiplicities)];records=[]
 for i,j in combinations(range(7),2):
  det=int(base.row_join(extras[i]).row_join(extras[j]).det());assert det!=0;records.append({'pair':[i,j],'determinant':str(det)})
 basis=base.row_join(extras[0]).row_join(extras[1]);coordinates=basis.inv()*s.Matrix.hstack(*extras);quotient=coordinates[15:,:];stationarity=[]
 for kind in ['independent','one_pair','triple']:
  weights=s.eye(7)
  if kind!='independent':weights[:,1]=weights[:,0]
  if kind=='triple':weights[:,2]=weights[:,0]
  matrix=s.Matrix.hstack(*[s.kronecker_product(weights[:,i],quotient[:,i]) for i in range(7)]);rank=int(matrix.rank());assert rank==(6 if kind=='triple' else 7);stationarity.append({'weight_pattern':kind,'velocity_square_map_rank':rank})
 return {'status':'finite controls for written scoped linearity obstruction; no exponent gain','stationarity_controls':stationarity,'circuit_bounds':bounds,'two_proportional_dependencies_bound':87,'nongood_family_dimension_bound':121,'rank_two_parameter_dimension':126,'fixed_scheme_image_dimension_bound':640,'required_injective_leg_dimension':1056,'base_jet_rank':15,'pair_independence_certificates':records}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=report();a.output.write_text(json.dumps(r,indent=2)+'\n');print('Circuit and Hermite controls passed.')
