"""Numerical discovery only; no nonzero residual is a restriction certificate."""
from pathlib import Path
import argparse,json,time
import numpy as np
from intertwiners import source_data,representation,target_actions


def main(starts,sweeps,output,rectangular=False,warm=None):
 vertex_w=3 if rectangular else 5
 invariant_dimension=33 if rectangular else 101
 basis_file='rectangular-bases.json' if rectangular else 'intertwiner-bases.json'
 started=time.monotonic();root=Path(__file__).resolve().parents[3]
 exact=json.loads((root/'results/asymmetric-sl2-seed-20261021'/basis_file).read_text())
 wb,actions=source_data(3);W=np.array([np.array(x).astype(np.float64) for x in wb])
 bases=[];transforms=[];physical=[]
 for name in 'ABC':
  raw=np.array(exact[name],dtype=float);r,S,T=raw.shape
  Q,R=np.linalg.qr(raw.reshape(r,-1).T,mode='reduced')
  basis=Q.T.reshape(r,S,T);bases.append(basis);transforms.append(np.linalg.inv(R))
  physical.append(np.einsum('rst,sab->rtab',basis,W))
 U=representation([4]);V=representation([2] if rectangular else [2,0,0])
 target=[target_actions(U,U),target_actions(U,V),target_actions(V,U)]
 weights=[np.array([int(T[2][i,i]) for i in range(T[2].rows)]) for T in target]
 triples=np.array([(i,j,k) for i in range(25) for j in range(5*vertex_w) for k in range(5*vertex_w)
                   if weights[0][i]+weights[1][j]+weights[2][k]==0],dtype=int)
 desired=np.array([float(i%5==j//vertex_w and j%vertex_w==k//5 and k%5==i//5) for i,j,k in triples])
 assert desired.sum()==25*vertex_w
 core=np.stack([np.einsum('iab,jbc,kca->ijk',physical[0][:,i],physical[1][:,j],physical[2][:,k],optimize=True)
                for i,j,k in triples])
 flat=core.reshape(len(triples),-1);rng=np.random.default_rng(271828)
 Y=flat@rng.normal(size=(flat.shape[1],128));Q,s,_=np.linalg.svd(Y,full_matrices=False)
 dimension=int((s>s[0]*1e-11).sum());Q=Q[:,:dimension]
 compressed=(Q.T@flat).reshape(dimension,*core.shape[1:]);rhs=Q.T@desired
 projection_error=float(np.linalg.norm(flat-Q@(Q.T@flat))/np.linalg.norm(flat))
 target_projection_error=float(np.linalg.norm(desired-Q@rhs)/np.linalg.norm(desired))
 assert dimension<=invariant_dimension and projection_error<1e-10
 output.mkdir(parents=True,exist_ok=True)
 report={'status':'numerical discovery only','seed':271828,'starts':starts,'sweeps':sweeps,
         'intertwiner_dimensions':[len(b) for b in bases],'weight_zero_equations':len(triples),
         'numerical_core_dimension':dimension,'predicted_invariant_space_dimension':invariant_dimension,'vertex_dimensions':[5,5,vertex_w],
         'core_projection_error':projection_error,'target_projection_error':target_projection_error,
         'runs':[],'no_exact_restriction_claimed':True}
 (output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
 print('CORE',dimension,projection_error,target_projection_error,round(time.monotonic()-started,2),flush=True)
 np.savez_compressed(output/'discovery-problem.npz',core=core,compressed=compressed,rhs=rhs,desired=desired,triples=triples,W=W,vertex_w=vertex_w,**{f'{name}_basis':b for name,b in zip('ABC',bases)},**{f'{name}_transform':t for name,t in zip('ABC',transforms)})
 best=float('inf')
 for start in range(starts):
  pars=[rng.normal(size=n)+1j*rng.normal(size=n) for n in [len(b) for b in bases]]
  if start==0 and warm is not None:
   loaded=np.load(warm);warm_maps=[loaded[name] for name in 'ABC']
   if rectangular and warm_maps[1].shape[1]==25:
    warm_maps[1]=warm_maps[1].reshape(45,5,5)[:,:,:3].reshape(45,15)
    warm_maps[2]=warm_maps[2].reshape(45,5,5)[:,:3,:].reshape(45,15)
   pars=[np.einsum('rst,st->r',b,M) for b,M in zip(bases,warm_maps)]
   assert all(np.linalg.norm(np.einsum('r,rst->st',x,b)-M)<1e-9 for x,b,M in zip(pars,bases,warm_maps))
  history=[]
  for step in range(sweeps):
   for leg in range(3):
    if leg==0:A=np.einsum('tijk,j,k->ti',compressed,pars[1],pars[2],optimize=True)
    elif leg==1:A=np.einsum('tijk,i,k->tj',compressed,pars[0],pars[2],optimize=True)
    else:A=np.einsum('tijk,i,j->tk',compressed,pars[0],pars[1],optimize=True)
    pars[leg]=np.linalg.lstsq(A,rhs,rcond=1e-12)[0]
   norms=[np.linalg.norm(x) for x in pars]
   if min(norms)==0:break
   common=np.prod(norms)**(1/3);pars=[x*common/n for x,n in zip(pars,norms)]
   if step%10==0 or step+1==sweeps:
    residual=np.einsum('tijk,i,j,k->t',core,*pars,optimize=True)-desired
    err=float(np.linalg.norm(residual)/np.linalg.norm(desired));history.append([step,err,max(float(np.linalg.norm(x)) for x in pars)])
    if err<best:
     best=err
     maps=[np.einsum('r,rst->st',p,b) for p,b in zip(pars,bases)]
     physical_maps=[np.einsum('st,sab->tab',M,W) for M in maps]
     full=np.einsum('iab,jbc,kca->ijk',*physical_maps,optimize=True)
     target_full=np.zeros((25,5*vertex_w,5*vertex_w))
     for i in range(5):
      for j in range(5):
       for k in range(vertex_w):target_full[5*i+j,vertex_w*j+k,5*k+i]=1
     full_error=float(np.linalg.norm(full-target_full)/np.linalg.norm(target_full))
     assert abs(full_error-err)<1e-9
     np.savez_compressed(output/'best.npz',**{name:M for name,M in zip('ABC',maps)})
     report['best_full_relative_error']=full_error;report['best_start']=start;report['best_sweep']=step
    if err<1e-11:break
  report['runs'].append({'start':start,'history':history,'final_parameter_norms':[float(np.linalg.norm(x)) for x in pars]})
  report['elapsed_seconds']=time.monotonic()-started
  (output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
  print('RUN',start,'best',best,'last',history[-1] if history else None,round(time.monotonic()-started,2),flush=True)
  if best<1e-11:break

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--starts',type=int,default=8);p.add_argument('--sweeps',type=int,default=300)
 p.add_argument('--output',type=Path,default=Path('results/local/asymmetric-sl2-seed/search'))
 p.add_argument('--rectangular',action='store_true');p.add_argument('--warm',type=Path)
 a=p.parse_args();main(a.starts,a.sweeps,a.output,a.rectangular,a.warm)
