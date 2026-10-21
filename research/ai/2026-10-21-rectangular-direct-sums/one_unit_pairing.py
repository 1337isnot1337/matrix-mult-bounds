"""Exact finite pairing-rank controls for the one-unit factor criterion."""
import importlib.util,json,argparse
from pathlib import Path
spec=importlib.util.spec_from_file_location('atom_rank_control',Path(__file__).with_name('distinct_atoms.py'));r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
def pairing(a,b,delta,g):
 rows=[(u,rr) for u in range(b-delta) for rr in range(a)];cols=[(j,v) for j in range(b) for v in range(a-1)]
 M=[[g.get((j-u,rr-v),0) for j,v in cols] for u,rr in rows]
 exact=int(r.s.Matrix(M).rank());lower=r.rank_mod(M);assert exact==lower
 return {'a':a,'b':b,'delta':delta,'g':[[i,j,c] for (i,j),c in sorted(g.items())],'pairing_rank':exact,'rank_lower_mod_65519':lower,'source_rank_from_factor_formula':a*(a+1)*b-a*(b-delta)-b*(a-1)+exact}
def coefficient_model(a,b,nonseparable=False,delta=1):
 # Minimal factor pencils for B=I+x^delta*z*E01 (separable pairing)
 # or diag(1+x*z,1,...,1) (nonseparable pairing). Not assumed Hankel.
 n=a+1;m=a+b-1
 U={(0,0,1):1,(1,0,0):-1}
 for p in range(1,a):U[0,p,p+1]=1
 V={(0,1,0):1}
 for q in range(1,a):V[0,q+1,q]=1
 V[delta,0,0 if nonseparable else 1]=-1
 UF=[[U.get((ss,p,h),0) for h in range(n)] for p in range(a) for ss in range(b)];VF=[[V.get((i,h,q),0) for q in range(b) for i in range(a)] for h in range(n)]
 assert r.rank_mod(UF)==n and r.rank_mod(VF)==n
 P=r.s.zeros(b*a*m,n*b*a);Q=r.s.zeros(n*b*a,m*b*a)
 for (ss,p,h),value in U.items():
  for j in range(b):
   for rr in range(a):P[(j*a+p)*m+ss+rr,(h*b+j)*a+rr]=value
 for (i,h,q),value in V.items():
  for j in range(b):
   for rr in range(a):Q[(h*b+j)*a+rr,((i+j)*b+q)*a+rr]=value
 M=P*Q;expected={}
 for p in range(a):expected[0,p,p,0]=1
 expected[delta,0,0 if nonseparable else 1,1]=1
 for j in range(b):
  for p in range(a):
   for L in range(m):
    for H in range(m):
     for q in range(b):
      for rr in range(a):assert M[(j*a+p)*m+L,(H*b+q)*a+rr]==expected.get((H-j,p,q,L-rr),0)
 exact=int(M.rank());assert exact==r.rank_mod(M.tolist());wanted=a*a*b+(a if nonseparable else delta);assert exact==wanted
 return {'a':a,'b':b,'delta':delta,'nonseparable_pairing':nonseparable,'hankel_source_claim':False,'full_coefficient_model_rank':exact,'expected_rank':wanted,'factorization_entries_checked':M.rows*M.cols}
def report():
 pairs=[]
 for a,b in [(2,3),(3,4),(4,5)]:
  for g in [{(0,0):1},{(1,1):1},{(0,0):1,(1,1):1}]:
   z=pairing(a,b,1,g);assert z['source_rank_from_factor_formula']==a*a*b+(a if len(g)==2 else 1);pairs.append(z)
 higher=pairing(3,4,2,{(2,0):1,(0,1):1});assert higher['source_rank_from_factor_formula']>=38;pairs.append(higher)
 return {'status':'exact finite controls, written general proof unreviewed, no target maps','pairing_controls':pairs,'coefficient_models':[coefficient_model(2,3),coefficient_model(2,3,True),coefficient_model(3,4,False,2)]}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();v=report();a.output.write_text(json.dumps(v,indent=2)+'\n');print('Pairing controls passed.')
