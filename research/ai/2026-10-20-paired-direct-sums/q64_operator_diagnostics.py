"""Operator diagnostics for saved Q64 monomial-Laurent candidates.

These necessary conditions do not establish a tensor degeneration.
The prescribed three-level chart would give (T-I)^3=0 exactly.
"""
import argparse
import json
from pathlib import Path
from q64_experiment_replay import contraction


def as_operator(tensor):
    """Regroup a flat coefficient list, preserving exact integer entries."""
    if len(tensor) != 10000:
        raise ValueError('Expected all 10000 coefficients in native A,B,C order.')
    result=[[0]*100 for _ in range(100)]
    for ia in range(5):
        for ka in range(5):
            for ib in range(5):
                for jb in range(4):
                    for jc in range(4):
                        for kc in range(5):
                            index=((5*ia+ka)*20+4*ib+jb)*20+5*jc+kc
                            result[(4*ia+jb)*5+kc][(4*ib+jc)*5+ka]=tensor[index]
    return result


def diagnostics(path):
    import numpy as np
    point=json.loads(Path(path).read_text())
    maps=[[[complex(r,i) for r,i in zip(rr,ii)] for rr,ii in zip(real,imag)]
          for real,imag in zip(point['maps_real'],point['maps_imag'])]
    actual,target=contraction(maps,point.get('auxiliary_rank',0))
    identity=np.asarray(as_operator(target))
    if not np.array_equal(identity,np.eye(100,dtype=int)):
        raise ArithmeticError('The target did not regroup to the identity operator.')
    error=np.asarray(as_operator(actual))-identity
    square=error@error
    cube=square@error
    return {'artifact':Path(path).name,
            'operator_regrouping':'row(i_A,j_B,k_C), column(i_B,j_C,k_A)',
            'error_frobenius_norm':float(np.linalg.norm(error)),
            'error_cube_frobenius_norm':float(np.linalg.norm(cube)),
            'error_spectral_radius':float(np.max(np.abs(np.linalg.eigvals(error)))),
            'absolute_traces_powers_1_2_3':[float(abs(np.trace(x))) for x in [error,square,cube]],
            'diagnostics_are_numerical':True,'exact_nilpotence_claimed':False,
            'nilpotence_alone_would_not_prove_the_prescribed_chart':True,
            'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoints',type=Path,nargs='+')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report={'operator_diagnostics':[diagnostics(path) for path in args.checkpoints]}
    if args.output:
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
