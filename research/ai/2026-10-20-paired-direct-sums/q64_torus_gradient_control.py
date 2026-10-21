"""Optional numerical controls for the physical diagonal norm normalization."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import numpy as np
from q64_torus_gauge import normalize,pullback,Q
from q64_parabolic_gauge import gauge as parabolic_gauge
from q64_parabolic_exact_control import control_maps,powers
from q64_experiment_replay import contraction,degrees


def controls(checkpoint):
    raw=checkpoint.read_bytes();p=json.loads(raw)
    maps=[np.array(r)+1j*np.array(i) for r,i in zip(p['maps_real'],p['maps_imag'])]
    normalized,data=normalize(maps)
    rng=np.random.default_rng(202610447)
    target=[(rng.normal(size=m.shape)+1j*rng.normal(size=m.shape))/np.sqrt(2) for m in maps]
    gradient=pullback([m-t for m,t in zip(normalized,target)],data)
    def objective(ms):
        ns,_=normalize(ms)
        return float(sum(np.linalg.norm(n-t)**2 for n,t in zip(ns,target)))
    checks=[]
    for _ in range(3):
        direction=[rng.normal(size=m.shape)+1j*rng.normal(size=m.shape) for m in maps]
        norm=np.sqrt(sum(np.linalg.norm(v)**2 for v in direction))
        direction=[v/norm for v in direction]
        analytic=float(2*sum(np.vdot(g,v).real for g,v in zip(gradient,direction)))
        step=1e-5
        numeric=(objective([m+step*v for m,v in zip(maps,direction)])-objective([m-step*v for m,v in zip(maps,direction)]))/(2*step)
        discrepancy=abs(analytic-numeric)/max(1,abs(analytic),abs(numeric))
        checks.append({'analytic_directional_derivative':analytic,'central_difference':numeric,'relative_discrepancy':discrepancy})
        assert discrepancy<2e-5
    r=np.concatenate(maps);g=np.concatenate(gradient)
    gauge_derivatives=[float(2*np.vdot(g,Q[:,j,None]*r).real) for j in range(13)]
    assert max(map(abs,gauge_derivatives))<1e-7
    perturbation=rng.normal(size=13)*0.025
    scaled=r*np.exp(Q@perturbation)[:,None]
    again,_=normalize([scaled[:25],scaled[25:45],scaled[45:]])
    equivariance=max(float(np.max(abs(a-b))) for a,b in zip(again,normalized))
    assert equivariance<1e-9
    positive,_=normalize([np.array(m,dtype=complex) for m in control_maps()])
    actual,target_coefficients=contraction([m.tolist() for m in positive],103)
    exponents=degrees(powers())
    error=max(abs(a-t) for a,t,d in zip(actual,target_coefficients,exponents) if d<=0)
    assert error<1e-12
    parabolic=parabolic_gauge([np.array(m,dtype=complex) for m in control_maps()])
    actual,_=contraction([m.tolist() for m in parabolic],103)
    parabolic_error=max(abs(a-t) for a,t,d in zip(actual,target_coefficients,exponents) if d<=0)
    assert parabolic_error<1e-12
    return {'checkpoint':checkpoint.name,'checkpoint_sha256':sha256(raw).hexdigest(),
            'gradient_checks':checks,'gradient_control_passes':True,
            'maximum_gauge_tangent_derivative':max(map(abs,gauge_derivatives)),
            'gauge_orbit_representative_maximum_difference':equivariance,
            'stationarity_relative':data['relative_stationarity'],
            'positive_coefficient_control_source':'Q(6,4) direct sum D_103; Q columns zero',
            'positive_control_scalar_cost':103,'all_control_positions_checked':10000,
            'positive_control_maximum_required_error':float(error),
            'parabolic_positive_control_maximum_required_error':float(parabolic_error),
            'controls_are_numerical':True,'exact_coefficient_certificate':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoint',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();result=controls(args.checkpoint)
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
