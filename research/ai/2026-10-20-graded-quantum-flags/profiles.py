"""Independent replay of canonical Cartan claim EXP-CYCLIC-CARTAN-FRONTIER-051."""
import json,time
from pathlib import Path
nodes=0

def nonnegative_factors(P,sumA=10,sumB=11):
 global nodes
 while P and not P[-1]:P=P[:-1]
 degree=len(P)-1
 def recurse(A,B,leftA,leftB,lastA,lastB):
  global nodes
  nodes+=1;n=len(A)
  if n>degree:
   if leftA==0 and leftB==0:
    yield A[:lastA+1],B[:lastB+1]
   return
  residual=P[n]-sum(A[i]*B[n-i] for i in range(1,n))
  for a in range(min(leftA,residual//B[0])+1):
   b,rem=divmod(residual-a*B[0],A[0])
   if rem or b<0 or b>leftB:continue
   da=n if a else lastA;db=n if b else lastB
   if da+db>degree:continue
   if leftA>a and n>=degree-lastB:continue
   if leftB>b and n>=degree-lastA:continue
   yield from recurse(A+[a],B+[b],leftA-a,leftB-b,da,db)
 for a0 in range(1,min(P[0],sumA)+1):
  if P[0]%a0:continue
  b0=P[0]//a0
  if b0<=sumB:yield from recurse([a0],[b0],sumA-a0,sumB-b0,0,0)


def convolution(A,B):
    out=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):out[i+j]+=a*b
    return out


def complete_profiles(records,source):
    solutions=[]
    for B in records:
        U=B['factor10'][::-1];V=B['factor11']
        for C in records:
            if C['factor11']!=V[::-1]:continue
            W=C['factor10']
            alpha=18-((len(U)-1)+(len(V)-1)+(len(W)-1))-B['shift']-C['shift']
            if alpha<0:continue
            product=[0]*alpha+convolution(U,W[::-1])
            if len(product)>len(source):continue
            product+=[0]*(len(source)-len(product))
            residual=[s-a for s,a in zip(source,product)]
            if min(residual)<0:continue
            solutions.append({'U10':U,'V11':V,'W10':W,'shifts':[alpha,B['shift'],C['shift']],
                              'large_leg_B_deficit':B['deleted'],'large_leg_C_deficit':C['deleted'],
                              'first_leg_deficit':residual})
    return solutions


def report():
    global nodes
    nodes=0;source=convolution(convolution([1]*4,[1]*4),[1]*7);records=[];valid=0
    for i in range(13):
        for j in range(i,13):
            P=list(source);P[i]-=1;P[j]-=1
            if min(P)<0:continue
            valid+=1;shift=next(k for k,c in enumerate(P) if c)
            for A,B in nonnegative_factors(P[shift:]):
                records.append({'deleted':[i,j],'shift':shift,'factor10':A,'factor11':B})
    return {'source_character':source,'deleted_pairs_checked':91,'nonnegative_cases':valid,
            'recursive_nodes':nodes,'large_leg_factorizations':records,
            'solutions':complete_profiles(records,source),
            'canonical_claim':'EXP-CYCLIC-CARTAN-FRONTIER-051',
            'scope':'Independent coefficient recursion for the already-merged standard torus character classification. No new classification, tensor maps or exponent improvement.'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report();args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Compatible profile triples:',len(result['solutions']),'nodes:',result['recursive_nodes'])
