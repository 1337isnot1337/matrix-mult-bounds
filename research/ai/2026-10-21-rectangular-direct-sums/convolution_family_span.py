import json

def span(a,b):
 Bs=[];Ds=[]
 for ss in range(b-1):Bs.append(({ss:1},{(a-1,ss+1):1}))
 for k in range(a-1):
  for ss in range(b):Bs.append(({}, {(k,ss):1}))
 for i in range(a-1):Ds.append(({i:1},{(a-1,i+1):1}))
 for k in range(a-1):
  for i in range(a):Ds.append(({}, {(k,i):1}))
 vectors=[];support=set()
 for A,B in Bs:
  for C,D in Ds:
   row={}
   for (r,ss),v in B.items():
    for (s,i),w in D.items():
     k=r+s-(a-1)
     if k>=0:row[i,k,ss]=row.get((i,k,ss),0)+v*w
   for ss,v in A.items():
    for i,w in C.items():row[i,0,ss]=row.get((i,0,ss),0)+v*w
   support.update(row);vectors.append(row)
 index={key:i for i,key in enumerate(sorted(support))};pivots={}
 for row in vectors:
  v=sum(1<<index[k] for k,x in row.items() if x%2)
  while v:
   k=v.bit_length()-1
   if k in pivots:v^=pivots[k]
   else:pivots[k]=v;break
 return {'a':a,'b':b,'parameter_pair_products':len(vectors),'coordinate_support_size':len(support),'rank_mod_2':len(pivots),'expected_span_dimension':a*a*b-a-b}
def report():
 rows=[span(a,b) for a,b in [(3,4),(8,10)]]
 assert all(r['rank_mod_2']==r['coordinate_support_size']==r['expected_span_dimension'] for r in rows)
 return {'status':'exact linear-span certificates for the fixed-support family; no target construction','controls':rows}

if __name__=='__main__':
 import argparse
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=report();a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
