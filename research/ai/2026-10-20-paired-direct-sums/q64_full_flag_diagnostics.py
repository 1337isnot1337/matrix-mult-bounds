"""Optional full-coefficient, operator, and gauge diagnostics for Q64 flags."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import numpy as np
from q64_experiment_replay import contraction,degrees,replay
from q64_operator_diagnostics import as_operator
from q64_parabolic_gauge import gauge
from q64_torus_gauge import normalize


def evaluate(maps,powers):
    actual,target=contraction([m.tolist() for m in maps],0)
    exponent=np.array(degrees(powers))
    difference=np.array(actual)-np.array(target)
    e=np.array(as_operator(difference.tolist()))
    mask=np.array(as_operator((exponent<=0).tolist()))
    w=np.concatenate(powers)
    energy=np.sum(abs(np.concatenate(maps))**2,axis=1)
    moments=[];power=e.copy()
    for k in range(1,7):
        moments.append({'power':k,'absolute_trace':float(abs(np.trace(power))),
                        'forbidden_power_frobenius_norm':float(np.linalg.norm(power[mask]))})
        power=power@e
    return {'all_target_positions_accounted':10000,
            'relative_nonpositive_coefficient_error':float(np.linalg.norm(difference[exponent<=0])/10),
            'negative_coefficient_norm':float(np.linalg.norm(difference[exponent<0])),
            'constant_coefficient_error_norm':float(np.linalg.norm(difference[exponent==0])),
            'positive_coefficient_norm':float(np.linalg.norm(difference[exponent>0])),
            'map_norms':[float(np.linalg.norm(m)) for m in maps],
            'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],
            'grading_norm_derivative':float(2*w@energy),
            'grading_norm_derivative_relative':float((w@energy)/(abs(w)@energy)),
            'operator_moments':moments,
            'operator_error_spectral_radius':float(np.max(abs(np.linalg.eigvals(e)))),
            'spectral_radius_is_a_necessary_condition_diagnostic_not_a_distance':True}


def diagnostics(path,with_gauges=False):
    raw=path.read_bytes();point=json.loads(raw)
    maps=[np.array(r)+1j*np.array(i) for r,i in zip(point['maps_real'],point['maps_imag'])]
    result={'checkpoint':path.name,'checkpoint_sha256':sha256(raw).hexdigest(),
            'complete_standard_library_replay':replay(path),
            'raw_metrics':evaluate(maps,point['map_row_powers']),
            'exact_coefficient_certificate':False,'improves_omega':False}
    if with_gauges:
        normalized,data=normalize(maps)
        result['torus_normalized_metrics']=evaluate(normalized,point['map_row_powers'])
        result['torus_relative_stationarity']=data['relative_stationarity']
        result['torus_newton_iterations']=data['iterations']
        result['torus_log_parameters']=data['log_gauge_parameters'].tolist()
        for _ in range(30):
            normalized=gauge(normalized)
        normalized,data=normalize(normalized)
        result['after_30_parabolic_sweeps_and_torus_normalization']=evaluate(normalized,point['map_row_powers'])
        result['final_torus_relative_stationarity']=data['relative_stationarity']
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoints',type=Path,nargs='+')
    parser.add_argument('--gauges',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result={'diagnostics':[diagnostics(path,args.gauges) for path in args.checkpoints],
            'numerical_diagnostics_are_not_exact_certificates':True}
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
