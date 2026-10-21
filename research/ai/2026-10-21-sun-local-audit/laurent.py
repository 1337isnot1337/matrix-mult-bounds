"""Exact sparse coefficient expansion for local source maps in arXiv2610.13971v1."""
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import product
import json

def lin(name,degree=0,coefficient=1):return [(degree,name,F(coefficient))] if coefficient else []
def addprod(out,A,B,C,scale=1):
 for (pa,a,x),(pb,b,y),(pc,c,z) in product(A,B,C):out[pa+pb+pc,a,b,c]+=F(scale)*x*y*z

def cw(out,X,Y,Z,q=3):
 for i in range(1,q+1):
  for a,b,c in [(0,i,i),(i,0,i),(i,i,0)]:addprod(out,X[a],Y[b],Z[c])
 for a,b,c in [(0,0,'inf'),(0,'inf',0),('inf',0,0)]:addprod(out,X[a],Y[b],Z[c])

def clean(T):return {key:value for key,value in T.items() if value}
def report(T,expected):
 T=clean(T);actual={(a,b,c):v for (p,a,b,c),v in T.items() if p==0}
 negatives=[{'power':p,'coordinates':[a,b,c],'coefficient':str(v)} for (p,a,b,c),v in T.items() if p<0]
 mismatches=[{'coordinates':list(key),'actual':str(actual.get(key,0)),'expected':str(expected.get(key,0))} for key in sorted(actual.keys()|expected.keys()) if actual.get(key,0)!=expected.get(key,0)]
 return {'nonzero_coefficients_by_power':dict(sorted(Counter(p for p,*_ in T).items())), 'negative_coefficients':negatives,'constant_coefficient_count':len(actual),'constant_mismatches':mismatches}

def active_d4():
 T=defaultdict(F)
 addprod(T,lin('x1',1,-1)+lin('x2'),lin('y1',-1,-1),lin('z0'))
 addprod(T,lin('x2'),lin('y1',-1)+lin('y2'),lin('z0')+lin('z1',1))
 addprod(T,lin('x3'),lin('y3'),lin('z0'))
 addprod(T,lin('x4'),lin('y4'),lin('z0')+lin('z2'))
 expected={(f'x{i}',f'y{i}','z0'):F(1) for i in range(1,5)}
 expected['x2','y1','z1']=F(1);expected['x4','y4','z2']=F(1)
 result=report(T,expected)
 result['full_remainder_matches']=clean(T)=={(0,*key):v for key,v in expected.items()}|{(1,'x2','y2','z1'):F(1)}
 return result

def active_lift():
 T=defaultdict(F)
 addprod(T,lin('b',-1)+lin('a'),lin('u')+lin('v',1),lin('z')+lin('s',1))
 addprod(T,lin('b',-1,-1),lin('u'),lin('z'))
 addprod(T,lin('c'),lin('w'),lin('r'))
 addprod(T,lin('eX'),lin('eY'),lin('eZ'))
 expected={key:F(1) for key in [('a','u','z'),('b','v','z'),('b','u','s'),('c','w','r'),('eX','eY','eZ')]}
 return report(T,expected)

def singular_c3():
 T=defaultdict(F)
 A={1:lin('X0')+lin('X1')+lin('X2')+lin('X3'),2:lin('X0')+lin('X1'),3:lin('X0')}
 def shift(items,n):return [(p+n,a,v) for p,a,v in items]
 X={0:lin('XE',2),1:shift(A[1],3),2:A[2],3:A[3],'inf':shift(A[1],2)}
 Y={0:lin('Y0',-1),1:lin('barY',-1),2:lin('Y1',1),3:lin('Y2',1),'inf':[]}
 Z={0:lin('Z0',-1),1:lin('ZE',-1),2:[],3:lin('Z1',1),'inf':[]}
 cw(T,X,Y,Z)
 expected={key:F(1) for key in [('X0','Y0','Z0'),('X0','Y1','Z0'),('X0','Y2','Z0'),('X1','Y0','Z0'),('X1','Y1','Z0'),('X2','Y0','Z0'),('X3','Y0','Z0'),('X0','Y0','Z1'),('XE','barY','ZE')]}
 return report(T,expected)

def five_empty():
 B=[[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[2,0,0,0,0,-1,1,0,0,0],[2,0,0,0,0,-1,0,1,0,0],[2,0,0,0,0,-1,0,0,1,0],[2,0,0,0,0,-1,0,0,0,1]]
 D=[[0,0,0,0,0,0,1,0,0,-1],[0,0,0,0,0,0,0,1,0,-1],[0,0,0,0,0,0,0,0,1,-1],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[-F(1,2),-1,-1,-1,0,F(1,4),0,0,0,-F(1,4)]]
 c=[1,0,0,0,0,F(1,2),0,0,0,-F(1,2)]
 T=defaultdict(F)
 for j in range(5):
  X={0:lin('barX',-2)+sum((lin(f'P{a}',1,B[a][j]) for a in range(7)),[]),'inf':sum((lin(f'P{a}',1,B[a][j+5]) for a in range(7)),[])}
  Y={0:lin('barY',-2)+lin('U',1,c[j])+sum((lin(f'Q{a}',1,D[a][j]) for a in range(7)),[]),'inf':lin('U',1,c[j+5])+sum((lin(f'Q{a}',1,D[a][j+5]) for a in range(7)),[])}
  Z={0:lin('barZ',-2)+lin('V',1,c[j]),'inf':lin('V',1,c[j+5])+lin('barZ',4,int(j==0))}
  for i in range(1,4):X[i]=lin(f'Xsh{3*j+i}',1);Y[i]=lin(f'Ysh{3*j+i}',1);Z[i]=lin(f'Zsh{3*j+i}',1)
  cw(T,X,Y,Z)
 expected={}
 for i in range(1,16):
  for key in [('barX',f'Ysh{i}',f'Zsh{i}'),(f'Xsh{i}','barY',f'Zsh{i}'),(f'Xsh{i}',f'Ysh{i}','barZ')]:expected[key]=F(1)
 expected['barX','U','V']=F(1);expected['barX','barY','barZ']=F(1)
 for a in range(7):expected[f'P{a}',f'Q{a}','barZ']=F(1)
 return report(T,expected)

