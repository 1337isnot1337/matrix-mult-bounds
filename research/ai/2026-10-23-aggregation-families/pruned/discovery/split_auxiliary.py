from itertools import product
from pathlib import Path
import json,time
from explore import rows22,Q22,mask
GRADES=[(111,0,-111),(70,80,-150),(102,8,-110),(112,99,-211),(60,51,-111),(71,64,-135),(56,64,-120),(55,42,-97),(0,77,-77),(59,53,-112),(20,102,-122),(78,101,-179),(87,83,-170),(85,68,-153),(69,72,-141),(34,57,-91),(43,111,-154),(70,36,-106),(46,87,-133),(69,54,-123),(70,42,-112),(60,52,-112)]

def patterns(rows,grades):
 d=1+max(v for row in rows for part in row for v in part);families=[[set(p) for p in row] for row in rows];out=set();ignored=0
 for i,j,k in product(range(len(rows)),repeat=3):
  if i==j==k:continue
  if grades[i][0]+grades[j][1]+grades[k][2]>0:ignored+=1;continue
  local=[]
  for r in range(d):
   active=[]
   if r not in families[i][0]:active.append('E')
   if r not in families[j][1]:active.append('E' if r in families[j][0] else 'D')
   if r not in families[k][2]:active.append('D')
   if not active:local.append(('R',))
   elif len(active)==1:local.append((active[0],))
   elif len(active)==2 and len(set(active))==1:local.append(('O','A' if active[0]=='E' else 'B'))
   else:local.append(('O',))
  out.update(product(*local))
 return sorted(out),ignored

def variables(d,qs,n):
 result=[]
 for p in [0]+[mask(x) for x in qs]:
  remain=[r for r in range(d) if not p>>r&1]
  for state in product(range(3),repeat=len(remain)):
   full=[-1]*d
   for r,s in zip(remain,state):full[r]=s
   result.append((p,tuple(full),n**state.count(0)))
 result.sort(key=lambda x:(x[2],-x[0].bit_count(),x[0],x[1]))
 return result

def row_dictionary(pattern,lookup,ps,n,mod):
 opts={'O':[(0,1)],'A':[(1,1)],'B':[(2,1)],'E':[(0,1),(1,-1)],'D':[(0,1),(2,-1)],'R':[(0,n),(1,1),(2,1)]}
 out={};R=mask([r for r,t in enumerate(pattern) if t=='R'])
 for p in ps:
  if p&R!=p:continue
  remain=[r for r in range(len(pattern)) if not p>>r&1]
  for choices in product(*(opts[pattern[r]] for r in remain)):
   full=[-1]*len(pattern);coeff=1
   for r,(s,c) in zip(remain,choices):full[r]=s;coeff=coeff*c%mod
   out[lookup[p,tuple(full)]]=coeff
 return out

def solve(rows,grades,qs,n,mod=1000003):
 d=len(set.union(*(set(p) for p in rows[0])))
 pats,ignored=patterns(rows,grades);var=variables(d,qs,n);lookup={(p,s):i for i,(p,s,c) in enumerate(var)};ps=[0]+[mask(x) for x in qs]
 z=lookup[0,(0,)*d]
 basis={};equations=0;start=time.monotonic()
 # RHS stored as variable len(var), after every actual variable.
 for pat in pats+[None]:
  row={z:1,len(var):1} if pat is None else row_dictionary(pat,lookup,ps,n,mod)
  while row:
   pivot=min(row)
   if pivot==len(var):
    return {'n':n,'rank':len(basis),'variables':len(var),'patterns':len(pats),'consistent_mod_prime':False,'prime':mod,'seconds':time.monotonic()-start}
   if pivot not in basis:
    inv=pow(row[pivot],-1,mod);row={k:v*inv%mod for k,v in row.items()};basis[pivot]=row;break
   scale=row[pivot]
   for col,value in basis[pivot].items():
    new=(row.get(col,0)-scale*value)%mod
    if new:row[col]=new
    else:row.pop(col,None)
  equations+=1
 values={}
 for pivot in sorted(basis,reverse=True):
  row=basis[pivot]
  values[pivot]=(row.get(len(var),0)-sum(value*values.get(j,0) for j,value in row.items() if j!=pivot and j!=len(var)))%mod
 for pat in pats:
  check=row_dictionary(pat,lookup,ps,n,mod)
  if sum(coef*values.get(col,0) for col,coef in check.items())%mod:
   raise ValueError('Modular coefficient-pattern residual')
 if values.get(z)!=1:raise ValueError('Diagonal coefficient residual')
 active=[i for i,v in values.items() if v]
 budget=sum(var[i][2] for i in active)
 return {'n':n,'rank':len(basis),'variables':len(var),'patterns':len(pats),'consistent_mod_prime':True,'prime':mod,'budget':budget,'mass_float':len(rows)*n**(.75*d),'ratio_float':budget/(len(rows)*n**(.75*d)),'checked_zero_coefficient_patterns':len(pats),'diagonal_coefficient_checked':True,'nonzero_orbit_weights':len(active),'weights':[{'P':[r for r in range(d) if var[i][0]>>r&1],'states':var[i][1],'coefficient_mod_prime':values[i],'position_cost':var[i][2]} for i in active],'seconds':time.monotonic()-start}

if __name__=='__main__':
 report={'hypothesis_escaped':'Two centered n-dimensional spaces in q=n+2 whose extra supports are disjoint; target uses only n ordinary diagonal positions','source':'general22 graded complete tripartitions; all nonpositive mixed grades constrained','scope':'Modular discovery only; no characteristic-zero or all-n acceptance','runs':[]}
 for qs in ([],Q22):
  for n in (2,3,4):
   ans=solve(rows22,GRADES,qs,n);ans['included_standard_corrections']=bool(qs);report['runs'].append(ans)
   print({k:v for k,v in ans.items() if k!='weights'},flush=True)
   Path('results/local/pruned-grid/split_auxiliary_discovery.json').write_text(json.dumps(report,indent=2)+'\n')
