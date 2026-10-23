"""Exact integer-bit permutation networks."""
from collections import deque


def scatter(mask,parity):
 out=0
 while mask:
  b=mask&-mask
  out|=1<<(2*(b.bit_length()-1)+parity)
  mask^=b
 return out


def route(p):
 n=len(p)
 if n<1 or sorted(p)!=list(range(n)) or n&(n-1):raise ValueError('power-of-two permutation required')
 if n==1:return []
 inverse=[0]*n
 for i,j in enumerate(p):inverse[j]=i
 color=[None]*n
 for seed in range(n):
  if color[seed] is not None:continue
  color[seed]=0;q=deque([seed])
  while q:
   x=q.popleft()
   for y in [x^1,inverse[p[x]^1]]:
    value=1-color[x]
    if color[y] is None:color[y]=value;q.append(y)
    elif color[y]!=value:raise ArithmeticError('routing graph is not bipartite')
 first=sum(1<<(2*i) for i in range(n//2) if color[2*i]==1)
 last=sum(1<<(2*i) for i in range(n//2) if color[inverse[2*i]]==1)
 children=[]
 for c in [0,1]:
  sub=[p[2*i+(color[2*i]!=c)]//2 for i in range(n//2)]
  children.append(route(sub))
 middle=[(2*s,scatter(a,0)|scatter(b,1))
         for (s,a),(t,b) in zip(*children)]
 return [(1,first)]+middle+[(1,last)]


def apply(v,network):
 for shift,mask in network:
  delta=((v>>shift)^v)&mask
  v^=delta^(delta<<shift)
 return v


if __name__=='__main__':
 from itertools import permutations
 from random import Random
 for n in [1,2,4]:
  for p in permutations(range(n)):
   net=route(p)
   for i,j in enumerate(p):assert apply(1<<i,net)==1<<j
 r=Random(20261021)
 for n in [8,16,512]:
  for _ in range(20):
   p=list(range(n));r.shuffle(p);net=route(p)
   for i,j in enumerate(p):assert apply(1<<i,net)==1<<j
 print('exact routing controls passed')
