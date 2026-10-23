"""Exact controls for the graded-module generic-flatness argument."""
import importlib.util
import json
from math import comb
from pathlib import Path
import sympy as s
spec=importlib.util.spec_from_file_location('flat_gate',Path(__file__).with_name('flat_realization.py'))
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def coordinate_change(moments,t):
    D=len(moments)-1
    return [sum((comb(D-k,j)*t**j*moments[k+j] for j in range(D-k+1)),
                s.zeros(*moments[0].shape)) for k in range(D+1)]


def control():
    residues=[]
    for lam in range(9):
        u=s.Matrix([1,lam,lam*lam]+[0]*7)
        v=s.Matrix([[1,lam**3,lam**6]+[0]*5])
        residues.append(u*v)
    moments=[sum((lam**k*residues[lam] for lam in range(9)),s.zeros(10,8))
             for k in range(17)]
    reversed_moments=moments[::-1]
    before=f.realize(reversed_moments,8,10)
    after=f.realize(coordinate_change(reversed_moments,1),8,10)
    h=[len(f.pivots(f.hankel(moments,17-d,d+1))) for d in range(17)]
    assert h[0]==h[16]==3 and h[9]==9
    assert h[7:11]==[9]*4
    assert not before['flat'] and after['flat']
    assert after['state_dimension']==9
    return {'outer_ranks':[h[0],h[16]],'apolar_hilbert_function':h,
            'infinity_chart':before,'changed_chart':after}


def report():
    return {'status':'finite exact controls for written generic-flatness proof',
            'control':control(),'improves_omega':False,'independent_review':False}

if __name__=='__main__':print(json.dumps(report(),indent=2))
