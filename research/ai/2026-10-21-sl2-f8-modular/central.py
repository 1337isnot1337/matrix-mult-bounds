"""Exact central Steinberg block and exact modular source bound."""
from pathlib import Path
from fractions import Fraction
import json,time
from modules import group,bits,xor
from bit_permutations import route,apply
PACKAGE=Path(__file__).resolve().parent
HERE=PACKAGE.parents[2]/'results/sl2-f8-modular-2026-10-21'
G=group();T=G['mul'];start=time.monotonic()
networks=[route(row+list(range(504,512))) for row in T]
for g in range(504):
 for h in range(504):
  assert apply(1<<h,networks[g])==1<<T[g][h]
print('all action columns checked',time.monotonic()-start,flush=True)
def mul(a,b):return xor(apply(b,networks[g]) for g in bits(a))
def insert(value,span):
 while value:
  p=value.bit_length()-1
  if p not in span:span[p]=value;return True
  value^=span[p]
 return False
rep=json.loads((HERE/'modules-powers.json').read_text())
images=[1 | (sum(v<<(3*i) for i,v in enumerate(N))<<1)
          | (sum(v<<(3*i) for i,v in enumerate(A))<<13) | (S<<61)
          for N,A,S in zip(rep['natural'],rep['tensor'],rep['steinberg'])]
unseen=set(range(504));classes=[]
while unseen:
 g=min(unseen);C={T[T[h][g]][G['inv'][h]] for h in range(504)}
 classes.append(sum(1<<h for h in C));unseen-=C
rows={}
for i,c in enumerate(classes):
 v=xor(images[g] for g in bits(c));label=1<<i
 while v:
  p=v.bit_length()-1
  if p not in rows:rows[p]=v,label;break
  r,l=rows[p];v^=r;label^=l
v=sum(1<<(61+9*i) for i in range(8));label=0
while v:
 p=v.bit_length()-1;r,l=rows[p];v^=r;label^=l
x=xor(classes[i] for i in bits(label))
for _ in range(3):x=mul(x,x)
assert mul(x,x)==x
span={}
for g in range(504):
 v=apply(x,networks[g]);assert v==mul(x,1<<g)
 insert(v,span)
assert len(span)==64
assert xor(images[g] for g in bits(x))==sum(1<<(61+9*i) for i in range(8))
t=Fraction(3,4);layers=[61,60,63,72,63,60,61]
bound=sum(c*t**i for i,c in enumerate(layers))/t**2+64
value={'central_steinberg_idempotent':hex(x),'ideal_dimension':len(span),'principal_layers':layers,'parameter':str(t),'source_bound':str(bound),'below450':bound<450,'packet_lower_score':493,'packet_score_lower_certificate':{'rational_term':74,'cube':74**3,'squared_volume':648**2},'field_scope':'Coordinate/potential constructions, not arbitrary complex maps.'}
(HERE/'central.json').write_text(json.dumps(value,indent=2)+'\n')
print(value,flush=True)
print('seconds',time.monotonic()-start,flush=True)
