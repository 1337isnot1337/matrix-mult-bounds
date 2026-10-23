"""Exact affine families obtained by varying only one factor at a time."""
from pathlib import Path
import importlib.util,json,argparse
spec=importlib.util.spec_from_file_location('fixed_pencil_data',Path(__file__).with_name('fixed_pencil_tangent.py'));t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
def control(a,b):
 C,D,k=t.linearization_data(a,b);out=[]
 for name,cs,ds in [('vary_U',C[:k],D[:k]),('vary_V',C[k:],D[k:])]:
  jr=t.rank_sparse(cs);dr=t.rank_sparse(ds);out.append({'varied_factor':name,'parameters':len(cs),'exact_derivative_rank':jr,'exact_hankel_constraint_rank':dr,'affine_source_image_dimension':jr-dr})
 return {'a':a,'b':b,'families':out,'integrability_reason':'With the other factor fixed, the product and Hankel constraints are linear, so the affine kernel is an exact family.'}
def report():return {'status':'exact one-factor affine families within the fixed-pencil source slice ansatz; no target tensor','controls':[control(a,b) for a,b in [(2,3),(3,4),(8,10)]]}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=report();a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
