"""Export numerical maps as exact binary64 coordinates, not as a solution."""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
from intertwiners import source_data
p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args();raw=a.input.read_bytes()
import io
z=np.load(io.BytesIO(raw));M=[z[n] for n in 'ABC'];W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);P=[np.einsum('st,sab->tab',m,W,optimize=True) for m in M];T=np.einsum('iab,jbc,kca->ijk',*P,optimize=True);w=M[1].shape[1]//5;target=np.zeros_like(T)
for i in range(5):
 for j in range(5):
  for k in range(w):target[5*i+j,w*j+k,5*k+i]=1
payload={n:{'shape':list(m.shape),'coordinates':[[float(v.real).hex(),float(v.imag).hex()] for v in m.ravel()]} for n,m in zip('ABC',M)}
encoded=json.dumps(payload,separators=(',',':'),sort_keys=True).encode();result={'status':'nonzero-residual numerical discovery checkpoint, not an exact restriction','input_npz_sha256':hashlib.sha256(raw).hexdigest(),'coordinate_payload_sha256':hashlib.sha256(encoded).hexdigest(),'source':'A(3,3), uniform physical trace source order','target':[5,5,w],'full_relative_error':float(np.linalg.norm(T-target)/np.linalg.norm(target)),'leg_norms':[float(np.linalg.norm(m)) for m in M],'payload':payload}
a.output.write_text(json.dumps(result,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in result.items() if k!='payload'},indent=2))
