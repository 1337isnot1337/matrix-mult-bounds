from pathlib import Path
exec(Path(__file__).with_name('refine_cyclic_234.py').read_text().split('rng=np.random')[0])
from fractions import Fraction
w=np.load(root/'cyclic-als-a2-m234-sparse.npz');current=np.concatenate([w[k].ravel() for k in ('A','B','C')]);fixed={j:0. for j,v in enumerate(current) if abs(v)<1e-10};tried=set(fixed);records=[];started=time.monotonic()
for j,v in fixed.items():current[j]=v
while len(tried)<len(current):
 index=min((j for j in range(len(current)) if j not in tried),key=lambda j:abs(abs(current[j])-1));tried.add(index);before=float(current[index]);trial_fixed=dict(fixed);trial_fixed[index]=float(np.sign(current[index]));free=np.asarray([j for j in range(len(current)) if j not in trial_fixed],dtype=int);base=current.copy()
 for j,v in trial_fixed.items():base[j]=v
 def unpack(y):
  x=base.copy();x[free]=y;return x
 r=least_squares(lambda y:residual(unpack(y)),current[free],jac=lambda y:jacobian(unpack(y))[:,free],method='lm',max_nfev=300,ftol=1e-13,xtol=1e-13,gtol=1e-13)
 candidate=unpack(r.x);err=float(np.linalg.norm(r.fun)/np.linalg.norm(M));accepted=err<1e-11 and np.linalg.norm(candidate)<100
 if accepted:
  current=candidate;fixed=trial_fixed
  F=split(current);np.savez(root/'cyclic-als-a2-m234-normalized.npz',A=F[0],B=F[1],C=F[2],fixed=np.asarray(sorted(fixed)))
 record={'index':int(index),'previous_value':before,'accepted':bool(accepted),'nfev':r.nfev,'relative_error':err,'fixed_count':len(fixed)};records.append(record)
 print(record,'attempts',len(tried),'seconds',time.monotonic()-started,flush=True)
(root/'cyclic-als-a2-m234-normalized.json').write_text(json.dumps({'fixed_count':len(fixed),'records':records,'full_relative_error':float(np.linalg.norm(residual(current))/np.linalg.norm(M)),'exact_certificate':False,'elapsed_seconds':time.monotonic()-started},indent=2)+'\n')
for k,F in zip(('A','B','C'),split(current)):
 print(k)
 for i,row in enumerate(F):print(i,[(j,str(Fraction(float(v)).limit_denominator(1000)),float(v)) for j,v in enumerate(row) if abs(v)>1e-10])
