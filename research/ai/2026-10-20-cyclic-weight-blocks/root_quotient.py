"""Exact root-of-unity realization of the candidate vertex character."""
import importlib.util
import json
from pathlib import Path
from sympy import Symbol, cyclotomic_poly
spec=importlib.util.spec_from_file_location('quantum',Path(__file__).resolve().parents[1]/'2026-10-20-quantum-recoupling/quantum.py')
qmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(qmod)
q=qmod.q;K=qmod.K

def vanishes(value,phi):
    if not value:return True
    assert value.denom.rem(phi), 'Undefined root specialization'
    return not value.numer.rem(phi)

def quotient_control(D):
    m=2*D-2;middle=D-1
    phi=qmod.R.from_expr(cyclotomic_poly(2*D,Symbol('q')))
    assert vanishes(qmod.qint(D),phi)
    assert vanishes(q**D+1,phi)
    assert not vanishes(qmod.qint(D-1),phi)
    assert all(not vanishes(q**(m-2*i)-1,phi) for i in range(m+1) if i!=middle)
    kept=[i for i in range(m+1) if i!=middle]
    divided_checks=0
    # E^(k) v_i=[m-i+k choose k] v_(i-k),
    # F^(k) v_i=[i+k choose k] v_(i+k).
    for k in range(1,D):
        assert vanishes(qmod.qchoose(D-1+k,k),phi)
        divided_checks+=2
    for i in kept:
        ef=qmod.qint(i+1)*qmod.qint(m-i) if i+1 in kept else K.zero
        fe=qmod.qint(m-i+1)*qmod.qint(i) if i-1 in kept else K.zero
        assert vanishes(ef-fe-(qmod.qint(m-2*i) if m>=2*i else -qmod.qint(2*i-m)),phi)
    # Two summands for the E,F,K algebra only; divided powers link them.
    for j in range(D-1):
        if j:
            assert vanishes(qmod.qint(2*D-1-j)+qmod.qint(D-1-j),phi)
            assert vanishes(qmod.qint(D-1-j)-qmod.qint(j+1),phi)
        if j<D-2:assert vanishes(qmod.qint(D+j+1)+qmod.qint(j+1),phi)
    # F^(D) sends v_0 to v_D with coefficient 1, so the low and high
    # intervals are not separate divided-power submodules.
    assert qmod.qchoose(D,D)==1 and D in kept
    w=[1]+[2]*(D-1)+[1]+[2]*(D-1)+[1]
    assert len(w)==2*D+1 and sum(w)==4*D-1
    return {'D':D,'a':D+1,'root_order':2*D,'cyclotomic_polynomial':str(phi.as_expr()),
            'weyl_module_dimension':2*D-1,'trivial_line_index':middle,
            'quotient_dimension':len(kept),'trivial_line_extension_nonsplit':True,'divided_power_line_checks':divided_checks,
            'quotient_commutator_checks':len(kept),'U_dimension':4*D-2,'W_dimension':4*D-1,
            'W_weight_multiplicities':w,'divided_power_cross_interval_coefficient':1,
            'tensor_maps_constructed':False}

if __name__=='__main__':
 print(json.dumps({'records':[quotient_control(D) for D in range(2,11)],'new_exponent_established':False},indent=2))
