"""Finite-field coefficient discovery; no complex degeneration certificate."""
import importlib.util,numpy as np,json,time
from pathlib import Path
path=Path(__file__).resolve().parents[2]/'2026-10-20-quantum-recoupling/discovery/cyclic_series.py'
spec=importlib.util.spec_from_file_location('qs',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
import argparse
_parser=argparse.ArgumentParser(description=__doc__)
_parser.add_argument('--output-dir',type=Path,required=True)
_args=_parser.parse_args();output_dir=_args.output_dir;output_dir.mkdir(parents=True,exist_ok=True)
p=786433;m.PRIME=p;a=4;L=12;order=6;V=112;assert V*(p-1)**2<2**53
root=pow(10,(p-1)//order,p)
labels,entries=m.cyclic_local_map(a)
expansions={key:m.series(value,root,L) for key,value in entries.items()};minimum=min(v for v,c in expansions.values())
matrices=np.zeros((L,V,V),dtype=np.int64)
for (i,j),(v,c) in expansions.items():
 for k in range(v-minimum,L):matrices[k,i,j]=c[k-v+minimum]
oldgrades=[i//7//4+i//7%4+i%7 for i in range(V)];newgrades=[sum(label) for label in labels]
flat_indices=[];blocks=[]
for w in range(13):
 rows=[i for i,g in enumerate(oldgrades) if g==w];columns=[(b,c) for b in range(V) for c in range(V) if newgrades[b]+newgrades[c]==18-w]
 start=len(flat_indices)
 flat_indices.extend([(i*V+b)*V+c for i in rows for b,c in columns])
 blocks.append((w,rows,columns,start,len(flat_indices)))
flat_indices=np.array(flat_indices,dtype=np.int64);M=len(flat_indices);N=1
while N<2*L-1:N*=2
omega=pow(10,(p-1)//N,p);assert pow(omega,N,p)==1 and pow(omega,N//2,p)!=1
source=m.source(a);evaluations=np.empty((N,M),dtype=np.int64)
def matrix_at(t):
 out=np.zeros((V,V),dtype=np.int64)
 for matrix in reversed(matrices):out=(out*t+matrix)%p
 return out.astype(float)
def project(B,C):
 t=np.remainder(np.rint(B@source.transpose(1,0,2).reshape(V,-1)),p).reshape(V,V,V).transpose(1,0,2)
 return np.remainder(np.rint(C@t.transpose(2,0,1).reshape(V,-1)),p).reshape(V,V,V).transpose(1,2,0).astype(np.int64)
for j in range(N):
 B=matrix_at(pow(omega,j,p));out=project(B,B);evaluations[j]=out.reshape(-1)[flat_indices]
 print('sample',j+1,'of',N,flush=True)
weights=np.array([[pow(N,-1,p)*pow(omega,-j*k,p)%p for j in range(N)] for k in range(L)],dtype=np.int64)
coefficients=np.rint(weights.astype(float)@evaluations.astype(float)).astype(np.int64)%p
control=project(matrices[0].astype(float),matrices[0].astype(float)).reshape(-1)[flat_indices]
assert np.array_equal(control,coefficients[0])
control=(project(matrices[1].astype(float),matrices[0].astype(float))+project(matrices[0].astype(float),matrices[1].astype(float)))%p
assert np.array_equal(control.reshape(-1)[flat_indices],coefficients[1])

def echelon_transform(matrix):
 A=np.concatenate([matrix.copy(),np.eye(len(matrix),dtype=np.int64)],axis=1);rank=0;ncols=matrix.shape[1]
 for j in range(ncols):
  choices=np.flatnonzero(A[rank:,j])
  if not len(choices):continue
  k=rank+int(choices[0]);A[[rank,k]]=A[[k,rank]];A[rank]=A[rank]*pow(int(A[rank,j]),-1,p)%p
  for i in range(len(A)):
   if i!=rank and A[i,j]:A[i]=(A[i]-A[i,j]*A[rank])%p
  rank+=1
  if rank==len(A):break
 return A[:,ncols:],rank

def saturate(C):
 rounds=[]
 while len(C):
  U,rank=echelon_transform(C[0]);rounds.append({'precision':len(C),'constant_rank':rank})
  C=np.array([np.rint(U.astype(float)@x.astype(float)).astype(np.int64)%p for x in C])
  if rank==len(U):return C[0],rounds
  if len(C)==1:return None,rounds
  C=np.concatenate([C[:-1,:rank,:],C[1:,rank:,:]],axis=1)
 return None,rounds

initial=np.zeros((V,V,V),dtype=np.int64);newrow=0;records=[];success=True
for w,rows,columns,start,end in blocks:
 C=coefficients[:,start:end].reshape(L,len(rows),len(columns))
 constant,rounds=saturate(C);record={'grade':w,'source_rows':len(rows),'rounds':rounds,'completed':constant is not None};records.append(record);print('saturation',record,flush=True)
 if constant is None:success=False;continue
 for i in range(len(rows)):
  for j,(b,c) in enumerate(columns):initial[newrow+i,b,c]=constant[i,j]
 newrow+=len(rows)
result={'scope':'Finite-field discovery only. Saturated coefficient limits need exact characteristic-zero reconstruction before acceptance.',
        'prime':p,'root_order':order,'root':root,'series_length':L,'Fourier_samples':N,'blocks':records,'completed':success}
if success:
 ranks=[m.matrix_rank_mod(initial.transpose(i,*[j for j in range(3) if j!=i]).reshape(V,-1)) for i in range(3)]
 result['flattening_ranks']=ranks;print('FINAL RANKS',ranks,flush=True)
 np.savez_compressed(output_dir/'root-six-saturated-matrixspace.npz',tensor=initial,matrices=matrices)
(output_dir/'root-six-saturated-matrixspace.json').write_text(json.dumps(result,indent=2)+'\n')
