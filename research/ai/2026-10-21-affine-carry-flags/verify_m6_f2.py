"""Independent literal replay of the C(9,23) finite-field sector witness."""
import json,hashlib
from pathlib import Path

def mul(x,y):
 z=0
 while y:
  if y&1:z^=x
  x<<=1;y>>=1
 return z
def rank(rows):
 piv={}
 for v in rows:
  while v:
   k=v.bit_length()-1
   if k in piv:v^=piv[k]
   else:piv[k]=v;break
 return len(piv)
def verify(w):
 m=w["m"];a,B=w["source"];out=a+B-1
 U,Y,Z,H=w["U"],w["Y"],w["Z"],w["H"]
 if w["field"]!=2:raise ValueError("field mismatch")
 if len(U)!=m or any(u<0 or u>=1<<a for u in U):raise ValueError("shared format")
 for L,n in [(Y,B),(Z,out)]:
  if len(L)!=m or any(len(row)!=p+1 for p,row in enumerate(L)):raise ValueError("degree format")
  if any(x<0 or x>=1<<n for row in L for x in row):raise ValueError("source format")
 if len(H)!=m or any(len(row)!=m or rank(row)!=m for row in H):raise ValueError("sector rank")
 N=m*(m+1)//2
 if (rank(U),rank(sum(Y,[])),rank(sum(Z,[])))!=(m,N,N):raise ValueError("map rank")
 counts={"all":0,"negative":0,"constant":0,"constant_nonzero":0,"positive_nonzero":0}
 for i,u in enumerate(U):
  for p,ys in enumerate(Y):
   for aa,y in enumerate(ys):
    uy=mul(u,y)
    for q,zs in enumerate(Z):
     for cc,z in enumerate(zs):
      val=(uy&z).bit_count()&1;counts["all"]+=1
      if p+q<m-1:
       counts["negative"]+=1
       if val:raise ValueError(("negative",i,p,aa,q,cc))
      elif p+q==m-1:
       counts["constant"]+=1;counts["constant_nonzero"]+=val
       if val!=(H[p][i]>>(aa+cc))&1:raise ValueError(("constant",i,p,aa,q,cc))
      else:counts["positive_nonzero"]+=val
 return counts
if __name__=="__main__":
 ROOT=Path(__file__).resolve().parents[3]
 path=ROOT/"results/affine-carry-flags-2026-10-21/m6-f2-witness.json";w=json.loads(path.read_text())
 counts=verify(w);bad=json.loads(path.read_text());bad["Z"][0][0]^=1
 try:verify(bad)
 except ValueError:tamper=True
 else:raise ValueError("tamper accepted")
 report={"field":2,"source":w["source"],"target":"T6 sectors with independent shared bases","counts":counts,
         "tamper_rejected":tamper,"witness_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
         "characteristic_zero_status":"not certified by this finite-field replay"}
 (ROOT/"results/affine-carry-flags-2026-10-21/m6-f2-replay.json").write_text(json.dumps(report,indent=2)+"\n")
 print(json.dumps(report))

