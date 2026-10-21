"""Independent exact checks of literal formulas in arXiv:2610.13971v1."""
from fractions import Fraction as F
from collections import Counter
import json

def linear(images,x):
    out=0
    for i,a in enumerate(images):
        if x>>i&1:out^=a
    return out

def sign(x):return -1 if x.bit_count()%2 else 1
Theta={'A1':3,'A2':0,'A3':0,'B1':5,'B2':9,'B3':0,'C1':6,'C2':9,'C3':0,'P':10,'Q':12,'R':15}
B=((9,4,8,6),(8,6,4,9))
def mask(layer,chi):
    if layer==0:return ['C1'] if chi in (6,7,10,11) else []
    if chi in (6,10):return ['A1','B1','B2','C1','P','Q','R']
    if chi in (7,11):return ['A1','A2','B1','C1','P','Q','R']
    return ['A1','A3','B1','B2','C1','P','Q','R']

def scalar(support,corrected):
    if corrected:return F(1,128)
    return F(1) if support.startswith(('B','C')) else F(1,128)

def dense_audit(corrected):
    mismatches=[]
    for rho in range(16):
        for beta in range(16):
            value=sum(scalar(s,corrected)*sign((chi & (rho^linear(B[layer],beta)))^(Theta[s]&beta))
                      for layer in range(2) for chi in range(16) for s in mask(layer,chi))
            expected=int(linear(B[0],beta)==linear(B[1],beta) and rho==linear(B[0],beta))
            if value!=expected:mismatches.append({'rho':rho,'beta':beta,'actual':str(value),'expected':expected})
    return {'corrected_uniform_X_scaling':corrected,'checked':256,'mismatch_count':len(mismatches),'mismatches':mismatches}

