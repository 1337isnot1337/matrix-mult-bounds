from itertools import product
from pathlib import Path
import numpy as np,json,time
root=Path('results/local/cyclic-equivariant');root.mkdir(parents=True,exist_ok=True);a=3;m=2*a-1;d=a*a*m;l=h=6;n=7;shape=(l*h,h*n,n*l);radius=2*a-2;weights=range(-radius,radius+1)
U=np.repeat(np.arange(5),[1,1,2,1,1]);V=U.copy();W=np.repeat(np.arange(5),[1,2,1,2,1]);vertices=(U,V,W);P=np.convolve(np.convolve(np.ones(a,dtype=int),np.ones(a,dtype=int)),np.ones(m,dtype=int))
for x,y in ((U,V),(V,W),(W,U)):
 c=np.array([np.count_nonzero(y[None,:]-x[:,None]==w) for w in weights]);assert np.all(c<=P)
T=np.zeros((d,d,d));M=np.zeros(shape)
for i,j,p,q,r,s in product(range(a),repeat=6):T[(i*m+p+q)*a+s,(j*a+p)*m+r+s,((i+j)*a+q)*a+r]=1
for i,j,k in product(range(l),range(h),range(n)):M[i*h+j,j*n+k,k*l+i]=1
sw=[np.array([k-i-s for i,k,s in product(range(a),range(m),range(a))]),np.array([k-j-p for j,p,k in product(range(a),range(a),range(m))]),np.array([k-q-r for k,q,r in product(range(m),range(a),range(a))])];tw=[(y[None,:]-x[:,None]).ravel() for x,y in ((U,V),(V,W),(W,U))];sg=[{w:np.flatnonzero(ws==w) for w in weights} for ws in sw];tg=[{w:np.flatnonzero(ws==w) for w in weights} for ws in tw];allowed=[tx[:,None]==sx[None,:] for tx,sx in zip(tw,sw)]
base=[np.zeros((b,d)) for b in shape];ui,vi,wi=[[int(np.flatnonzero(v==i)[0]) for i in range(a)] for v in vertices]
for i,j in product(range(a),repeat=2):
 base[0][h*ui[i]+vi[j],((a-1-j)*m+a-1)*a+i]=1
 base[1][n*vi[i]+wi[j],(i*a+a-1-j)*m+a-1]=1
 base[2][l*wi[i]+ui[j],((a-1)*a+i)*a+a-1-j]=1
control=np.zeros(shape)
for i,j,k in product(range(a),repeat=3):control[h*ui[i]+vi[j],n*vi[j]+wi[k],l*wi[k]+ui[i]]=1
assert all(np.array_equal(f*ok,f) for f,ok in zip(base,allowed));assert np.array_equal(np.einsum('abc,ia,jb,kc->ijk',T,*base,optimize=True),control)
blocks=[]
for axis in range(3):
 others=[k for k in range(3) if k!=axis];tensor=T.transpose([axis]+others);out={}
 for wa in weights:
  chunks=[];offset=0
  for wb in weights:
   wc=-wa-wb
   if wc not in sg[others[1]]:continue
   rb,rc=tg[others[0]][wb],tg[others[1]][wc];sb,sc=sg[others[0]][wb],sg[others[1]][wc]
   if not len(rb) or not len(rc):continue
   block=tensor[np.ix_(sg[axis][wa],sb,sc)];coords=(rb[:,None]*shape[others[1]]+rc[None,:]).ravel();chunks.append((block,rb,rc,sb,sc,coords,offset));offset+=len(coords)
  out[wa]=(chunks,offset)
 blocks.append(out)
def contracted(F,axis,wa):
 others=[k for k in range(3) if k!=axis];chunks,width=blocks[axis][wa];out=np.empty((len(sg[axis][wa]),width),dtype=np.result_type(*F))
 for block,rb,rc,sb,sc,coords,offset in chunks:
  partial=np.tensordot(block,F[others[0]][np.ix_(rb,sb)].T,axes=(1,0));value=np.tensordot(partial,F[others[1]][np.ix_(rc,sc)].T,axes=(1,0)).reshape(len(sg[axis][wa]),-1);out[:,offset:offset+len(coords)]=value
 return out
coords=[{wa:np.concatenate([c[5] for c in chunks]) for wa,(chunks,width) in blocks[axis].items()} for axis in range(3)];targets=[{wa:np.moveaxis(M,axis,0).reshape(shape[axis],-1)[np.ix_(tg[axis][wa],coords[axis][wa])] for wa in weights} for axis in range(3)]
def loss(F):
 total=0
 for wa in weights:
  delta=F[0][np.ix_(tg[0][wa],sg[0][wa])]@contracted(F,0,wa)-targets[0][wa];total+=np.linalg.norm(delta)**2
 return (total/(l*h*n))**.5
rng=np.random.default_rng(202610480);test=[f+rng.normal(size=f.shape)*.01*ok for f,ok in zip(base,allowed)];direct=np.einsum('abc,ia,jb,kc->ijk',T,*test,optimize=True)
for axis in range(3):
 mat=np.moveaxis(direct,axis,0).reshape(shape[axis],-1)
 for wa in weights:assert np.max(abs(test[axis][np.ix_(tg[axis][wa],sg[axis][wa])]@contracted(test,axis,wa)-mat[np.ix_(tg[axis][wa],coords[axis][wa])]))<1e-10
records=[];started=time.monotonic();best=float('inf');print('allowed entries',[int(ok.sum()) for ok in allowed],flush=True)
for trial in range(32):
 seed=202610481+trial;rng=np.random.default_rng(seed);complex_run=trial>=16;scale=(.03,.1,.3,1.)[trial%4];F=[f.astype(complex if complex_run else float)+(rng.normal(size=f.shape)+(1j*rng.normal(size=f.shape) if complex_run else 0))*scale*ok for f,ok in zip(base,allowed)]
 for iteration in range(1000):
  for axis in range(3):
   for wa in weights:
    v=contracted(F,axis,wa);F[axis][np.ix_(tg[axis][wa],sg[axis][wa])]=np.linalg.lstsq(v.T,targets[axis][wa].T,rcond=1e-12)[0].T
  norms=[np.linalg.norm(f) for f in F];common=np.exp(np.mean(np.log(norms)));F=[f*common/z for f,z in zip(F,norms)]
  if iteration%10==0 or iteration==999:
   err=loss(F)
   if err<best:best=err;np.savez(root/'cyclic-cartan-a3-m667-best.npz',A=F[0],B=F[1],C=F[2],seed=seed,error=err,iteration=iteration)
   if err<1e-11:break
 rec={'seed':seed,'complex':complex_run,'noise_scale':scale,'iterations':iteration+1,'full_relative_error':float(err),'map_norms':[float(np.linalg.norm(f)) for f in F]};records.append(rec);print(rec,'best',best,'seconds',time.monotonic()-started,flush=True)
 (root/'cyclic-cartan-a3-m667-progress.json').write_text(json.dumps(records,indent=2)+'\n')
(root/'cyclic-cartan-a3-m667.json').write_text(json.dumps({'source':'A3','target':'M(6,6,7)','class':'Full-coefficient Cartan-intertwining maps','starts':32,'maximum_iterations':1000,'allowed_entries_per_leg':[int(ok.sum()) for ok in allowed],'records':records,'best_full_relative_error':float(best),'exact_certificate':False,'general_exclusion':False},indent=2)+'\n')
