"""Exact sparse certificates for the cyclic and noncyclic sharp examples."""
from pathlib import Path
import importlib.util,json,argparse
spec=importlib.util.spec_from_file_location('one_step_source',Path(__file__).with_name('equality_one_step.py'));old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
def certificate(a,b):
 m=a+b-1;N=a*b*m;adj=[set() for _ in range(N)]
 for i,k,s in [(0,0,0),(0,a,1)]:
  for j in range(b):
   for p in range(a):
    q=k-p
    if not 0<=q<b:continue
    for r in range(a):adj[(j*a+p)*m+s+r].add(((i+j)*b+q)*a+r)
 match={}
 def augment(u,seen):
  for v in sorted(adj[u]):
   if v in seen:continue
   seen.add(v)
   if v not in match or augment(match[v],seen):match[v]=u;return True
  return False
 for u in range(N):augment(u,set())
 reverse={u:v for v,u in match.items()};left=set(range(N))-set(reverse);right=set();todo=list(left)
 while todo:
  u=todo.pop()
  for v in adj[u]:
   if reverse.get(u)==v or v in right:continue
   right.add(v)
   if v in match and match[v] not in left:left.add(match[v]);todo.append(match[v])
 cover=set(range(N))-left;assert all(u in cover or v in right for u in range(N) for v in adj[u]);pivots={}
 for row in adj:
  bits=sum(1<<j for j in row)
  while bits:
   j=bits.bit_length()-1
   if j in pivots:bits^=pivots[j]
   else:pivots[j]=bits;break
 rank=len(pivots);assert rank==len(cover)+len(right)==a*a*b+b
 return {'a':a,'b':b,'sequence':'f_0=1; f_a=z; all other f_k=0','state':'nilpotent Jordan block of size a+1','state_dimension':a+1,'symbol_rank':a,'crossed_rank':a+1,'rank_mod_2':rank,'support_cover_size':len(cover)+len(right),'cover_rows':sorted(cover),'cover_columns':sorted(right)}
def report():
 return {'status':'finite sharp controls for written unreviewed cyclic-state lemma; no exponent improvement','cyclic':[certificate(a,b) for a,b in [(2,3),(3,4),(8,10)]],'noncyclic_counterexample':old.certificate(8,10),'cyclicity_required':True}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=report();a.output.write_text(json.dumps(r,indent=2)+'\n');print('Verified cyclic sharp controls and preserved noncyclic counterexample.')
