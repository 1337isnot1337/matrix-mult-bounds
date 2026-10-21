from itertools import product
from pathlib import Path
import numpy as np,json,time,os
root=Path('results/local/cyclic-equivariant');root.mkdir(parents=True,exist_ok=True);a=4;m=7;d=112;shape=(100,110,110);T=np.zeros((d,d,d))
for i,j,p,q,r,s in product(range(a),repeat=6):T[(i*m+p+q)*a+s,(j*a+p)*m+r+s,((i+j)*a+q)*a+r]=1
U=np.repeat(np.arange(7),[1,1,2,2,2,1,1]);V=U.copy();W=np.repeat(np.arange(7),[1,2,2,1,2,2,1]);sizes=(10,10,11)
sw=[np.array([k-i-s for i,k,s in product(range(a),range(m),range(a))]),np.array([l-j-p for j,p,l in product(range(a),range(a),range(m))]),np.array([h-q-r for h,q,r in product(range(m),range(a),range(a))])]
tw=[(U[:,None]-V[None,:]).ravel(),(V[:,None]-W[None,:]).ravel(),(W[:,None]-U[None,:]).ravel()]
# Reverse all target vertex signs to match the natural embedded M4 control.
tw=[-v for v in tw]
sg=[{w:np.flatnonzero(ws==w) for w in range(-6,7)} for ws in sw];tg=[{w:np.flatnonzero(ws==w) for w in range(-6,7)} for ws in tw]
M=np.zeros(shape)
for i,j,k in product(range(10),range(10),range(11)):M[10*i+j,11*j+k,10*k+i]=1
base=[np.zeros((n,d)) for n in shape];ui=[int(np.flatnonzero(U==i)[0]) for i in range(4)];vi=ui;wi=[int(np.flatnonzero(W==i)[0]) for i in range(4)]
for i,j in product(range(4),repeat=2):
 base[0][10*ui[i]+vi[j],((3-j)*7+3)*4+i]=1
 base[1][11*vi[i]+wi[j],(i*4+3-j)*7+3]=1
 base[2][10*wi[i]+ui[j],(3*4+i)*4+3-j]=1
allowed=[tx[:,None]==sx[None,:] for tx,sx in zip(tw,sw)];assert all(np.array_equal(f*ok,f) for f,ok in zip(base,allowed))
control=np.zeros(shape)
for i,j,k in product(range(4),repeat=3):control[10*ui[i]+vi[j],11*vi[j]+wi[k],10*wi[k]+ui[i]]=1
assert np.array_equal(np.einsum('abc,ia,jb,kc->ijk',T,*base,optimize=True),control)
# Group every source and target contraction by the conserved Cartan weight.
blocks=[]
for axis in range(3):
 others=[k for k in range(3) if k!=axis];tensor=T.transpose([axis]+others);out={}
 for wa in range(-6,7):
  chunks=[];offset=0
  for wb in range(-6,7):
   wc=-wa-wb
   if wc not in sg[others[1]]:continue
   rb,rc=tg[others[0]][wb],tg[others[1]][wc];sb,sc=sg[others[0]][wb],sg[others[1]][wc]
   if not len(rb) or not len(rc):continue
   block=tensor[np.ix_(sg[axis][wa],sb,sc)];coords=(rb[:,None]*shape[others[1]]+rc[None,:]).ravel()
   chunks.append((block,rb,rc,sb,sc,coords,offset));offset+=len(coords)
  out[wa]=(chunks,offset)
 blocks.append(out)
def contracted(F,axis,wa):
 others=[k for k in range(3) if k!=axis];chunks,width=blocks[axis][wa];out=np.empty((len(sg[axis][wa]),width),dtype=np.result_type(*F))
 for block,rb,rc,sb,sc,coords,offset in chunks:
  partial=np.tensordot(block,F[others[0]][np.ix_(rb,sb)].T,axes=(1,0))
  values=np.tensordot(partial,F[others[1]][np.ix_(rc,sc)].T,axes=(1,0)).reshape(len(sg[axis][wa]),-1)
  out[:,offset:offset+len(coords)]=values
 return out
def loss(F,masks):
 sq=0.;fullsq=0.;maximum=0.
 axis=0;tm=M.reshape(shape[0],-1)
 for wa,(chunks,width) in blocks[axis].items():
  rows=tg[axis][wa];cols=np.concatenate([ch[5] for ch in chunks]);actual=F[axis][np.ix_(rows,sg[axis][wa])]@contracted(F,axis,wa);delta=actual-tm[np.ix_(rows,cols)]
  sq+=np.linalg.norm(delta[masks[axis][wa]])**2;fullsq+=np.linalg.norm(delta)**2;maximum=max(maximum,float(np.max(abs(actual))))
 return (sq/1100)**.5,(fullsq/1100)**.5,maximum
def balance(F):
 for _ in range(20):
  before=sum(np.linalg.norm(f)**2 for f in F)
  e=[np.sum(abs(f)**2,axis=1).reshape(n,k) for f,(n,k) in zip(F,((10,10),(10,11),(11,10)))];u=(e[2].sum(0)/e[0].sum(1))**.25
  F[0]*=np.repeat(u,10)[:,None];F[2]/=np.tile(u,11)[:,None]
  e=[np.sum(abs(f)**2,axis=1).reshape(n,k) for f,(n,k) in zip(F,((10,10),(10,11),(11,10)))];v=(e[1].sum(1)/e[0].sum(0))**.25
  F[0]*=np.tile(v,10)[:,None];F[1]/=np.repeat(v,11)[:,None]
  e=[np.sum(abs(f)**2,axis=1).reshape(n,k) for f,(n,k) in zip(F,((10,10),(10,11),(11,10)))];w=(e[2].sum(1)/e[1].sum(0))**.25
  F[1]*=np.tile(w,10)[:,None];F[2]/=np.repeat(w,10)[:,None]
  after=sum(np.linalg.norm(f)**2 for f in F)
  if before-after<1e-10*after:break
 return F
# Independent full-contraction control for the optimized weight-block assembly.
rng=np.random.default_rng(202610460);controlF=[f+rng.normal(size=f.shape)*.01*ok for f,ok in zip(base,allowed)];direct=np.einsum('abc,ia,jb,kc->ijk',T,*controlF,optimize=True)
for axis in range(3):
 other=[k for k in range(3) if k!=axis];actual=np.moveaxis(direct,axis,0).reshape(shape[axis],-1)
 for wa,(chunks,width) in blocks[axis].items():
  rows=tg[axis][wa];cols=np.concatenate([ch[5] for ch in chunks]);pred=controlF[axis][np.ix_(rows,sg[axis][wa])]@contracted(controlF,axis,wa)
  assert np.max(abs(pred-actual[np.ix_(rows,cols)]))<1e-10
records=[];best=float('inf');started=time.monotonic();starts=int(os.environ.get('CARTAN_STARTS','6'));iterations=int(os.environ.get('CARTAN_ITERATIONS','200'))
print('allowed entries',list(map(lambda t:int(t.sum()),allowed)),'starts',starts,'iterations',iterations,flush=True)
for trial in range(starts):
 seed=202610461+trial;rng=np.random.default_rng(seed);complex_run=trial>=4;scale=(.03,.1,.3,1.)[trial%4]
 secondary=[rng.choice(np.arange(-20,21),size=n,replace=False) for n in sizes]
 lw=[(secondary[0][:,None]-secondary[1][None,:]).ravel(),(secondary[1][:,None]-secondary[2][None,:]).ravel(),(secondary[2][:,None]-secondary[0][None,:]).ravel()];masks=[];targets=[]
 for axis in range(3):
  others=[k for k in range(3) if k!=axis];byweight={};tgvalues={};tm=np.moveaxis(M,axis,0).reshape(shape[axis],-1)
  for wa,(chunks,width) in blocks[axis].items():
   rows=tg[axis][wa];cols=np.concatenate([ch[5] for ch in chunks]);wb=np.concatenate([np.repeat(lw[others[0]][ch[1]],len(ch[2])) for ch in chunks]);wc=np.concatenate([np.tile(lw[others[1]][ch[2]],len(ch[1])) for ch in chunks]);degrees=lw[axis][rows,None]+wb[None,:]+wc[None,:];selected=tm[np.ix_(rows,cols)];assert np.all(degrees[selected!=0]==0);byweight[wa]=degrees<=0;tgvalues[wa]=selected
  masks.append(byweight);targets.append(tgvalues)
 F=[f.astype(complex if complex_run else float)+(rng.normal(size=f.shape)+(1j*rng.normal(size=f.shape) if complex_run else 0))*scale*ok for f,ok in zip(base,allowed)]
 for iteration in range(iterations):
  for axis in range(3):
   for wa in range(-6,7):
    sourcecols=sg[axis][wa];rows=tg[axis][wa];v=contracted(F,axis,wa)
    for local,row in enumerate(rows):
     keep=masks[axis][wa][local];F[axis][row,sourcecols]=np.linalg.lstsq(v[:,keep].T,targets[axis][wa][local,keep],rcond=1e-12)[0]
  norms=[np.linalg.norm(f) for f in F];common=np.exp(np.mean(np.log(norms)));F=balance([f*common/n for f,n in zip(F,norms)])
  if iteration%10==0 or iteration==iterations-1:
   err,fullerr,maximum=loss(F,masks)
   if err<best:best=err;np.savez(root/'cyclic-cartan-h1100-best.npz',A=F[0],B=F[1],C=F[2],u=secondary[0],v=secondary[1],w=secondary[2],seed=seed,error=err,iteration=iteration)
   print('progress',trial,iteration,err,fullerr,'seconds',time.monotonic()-started,flush=True)
   if err<1e-10:break
 rec={'seed':seed,'complex':complex_run,'noise':scale,'secondary_vertex_weights':[v.tolist() for v in secondary],'iterations':iteration+1,'masked_relative_error':float(err),'full_relative_error':float(fullerr),'maximum_full_coefficient':maximum,'map_norms':[float(np.linalg.norm(f)) for f in F]};records.append(rec);print(rec,flush=True)
 (root/'cyclic-cartan-h1100-progress.json').write_text(json.dumps(records,indent=2)+'\n')
(root/'cyclic-cartan-h1100.json').write_text(json.dumps({'source':'A4','target':'M(10,10,11)','class':'Cartan-intertwining constant maps followed by independent secondary vertex weights','starts':starts,'maximum_iterations':iterations,'allowed_entries_per_map':[int(ok.sum()) for ok in allowed],'records':records,'best_masked_error':float(best),'exact_certificate':False,'general_exclusion':False},indent=2)+'\n')
