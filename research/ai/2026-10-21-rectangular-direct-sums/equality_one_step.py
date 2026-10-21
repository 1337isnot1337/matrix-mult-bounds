"""Exact support-cover and mod-two certificates against an equality rank gap."""
import json

def certificate(a=8,b=9):
 m=a+b-1;N=a*b*m;adj=[set() for _ in range(N)]
 for i,k,s in [(0,0,0),(1,a-1,1)]:
  for j in range(b):
   for p in range(a):
    q=k-p
    if not 0<=q<b:continue
    for r in range(a):
     H=i+j;L=s+r
     row=(j*a+p)*m+L;col=(H*b+q)*a+r
     adj[row].add(col)
 # A maximum matching and its deterministic Konig support cover.
 match={}
 def augment(u,seen):
  for v in sorted(adj[u]):
   if v in seen:continue
   seen.add(v)
   if v not in match or augment(match[v],seen):match[v]=u;return True
  return False
 for u in range(N):augment(u,set())
 reverse={u:v for v,u in match.items()};left=set(range(N))-set(reverse);right=set();todo=list(left)
 while todo:
  u=todo.pop()
  for v in adj[u]:
   if reverse.get(u)==v or v in right:continue
   right.add(v)
   if v in match and match[v] not in left:left.add(match[v]);todo.append(match[v])
 cover_left=set(range(N))-left;cover_right=right
 assert all(u in cover_left or v in cover_right for u in range(N) for v in adj[u])
 # Binary row elimination gives a lower bound over Q; the support cover gives the upper bound.
 pivots={}
 for row in adj:
  bits=sum(1<<j for j in row)
  while bits:
   j=bits.bit_length()-1
   if j in pivots:bits^=pivots[j]
   else:pivots[j]=bits;break
 upper=len(cover_left)+len(cover_right);lower=len(pivots)
 assert lower==upper==a*a*b+1
 return {'a':a,'b':b,'sequence':'f_0=1; f_(a-1)=xz; all other f_k=0',
         'symbol_rank':a,'baseline':a*a*b,'rank_mod_2':lower,'support_cover_size':upper,
         'cover_rows':sorted(cover_left),'cover_columns':sorted(cover_right),
         'crossed_rank':a+1,
         'conclusion':'A one-unit excess is possible; do not round the equality threshold upward.'}

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
