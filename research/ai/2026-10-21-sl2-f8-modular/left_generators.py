"""Shorten radical power replay using left ideal generators."""
import json
from collections import deque
from pathlib import Path
from modules import group,bits,xor

PACKAGE=Path(__file__).resolve().parent
HERE=PACKAGE.parents[2]/'results/sl2-f8-modular-2026-10-21'
G=group();table=G['mul'];n=504
report=json.loads((HERE/'modules-powers.json').read_text())
J=[int(v,16) for v in report['powers'][0]]


def insert(v,span):
    while v:
        p=v.bit_length()-1
        if p not in span:
            span[p]=v
            return v
        v^=span[p]
    return 0


def translate(g,v):
    return xor(1<<table[g][h] for h in bits(v))


def mul(a,b):
    return xor(translate(g,b) for g in bits(a))


lookup={m:i for i,m in enumerate(G['matrices'])}
gens=[lookup[(1,1,0,1)],lookup[(2,0,0,5)],lookup[(0,1,1,0)]]
# 2*5=1 in the fixed F8 model.
assert all(g in range(504) for g in gens)
seen={0};q=deque([0])
while q:
 h=q.popleft()
 for g in gens:
  k=table[g][h]
  if k not in seen:seen.add(k);q.append(k)
assert len(seen)==504

def closure(vectors):
 span={};q=deque()
 for v in vectors:
  new=insert(v,span)
  if new:q.append(new)
 while q:
  v=q.popleft()
  for g in gens:
   new=insert(translate(g,v),span)
   if new:q.append(new)
 return span

L=[];span={}
for v in sorted(J,key=int.bit_count):
 probe=dict(span)
 if insert(v,probe):
  L.append(v)
  span=closure([*span.values(),v])
  print('generators',len(L),'span',len(span),'supports',[l.bit_count() for l in L],flush=True)
 if len(span)==len(J):break
assert len(span)==379
previous=J;dims=[504,379]
for k in range(2,8):
 current=closure(mul(l,v) for l in L for v in previous)
 dims.append(len(current));previous=list(current.values())
 print('power',k,len(current),flush=True)
assert dims==report['power_dimensions']
(HERE/'left-generators.json').write_text(json.dumps({'group_generators':gens,'radical_left_generators':[hex(v) for v in L],'dimensions':dims},indent=2)+'\n')
