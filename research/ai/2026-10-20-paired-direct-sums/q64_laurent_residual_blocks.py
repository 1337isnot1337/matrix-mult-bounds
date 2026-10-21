"""Optional numerical localization of complete Q64 Laurent coefficient errors."""
import argparse
from itertools import product
import json
from pathlib import Path
import numpy as np


def analyze(path):
    point = json.loads(path.read_text())
    maps = [np.array(r)+1j*np.array(i)
            for r, i in zip(point['maps_real'], point['maps_imag'])]
    a, b, c = maps
    aux = point.get('auxiliary_rank', 0)
    h = np.zeros((36+aux, 20, 20), dtype=complex)
    for p, q, y, v in product(range(6), range(6), range(4), range(4)):
        h[6*p+q] += np.outer(b[:, 9*y+q+v], c[:, 4*(p+y)+v])
    for j in range(aux):
        h[36+j] += np.outer(b[:, 36+j], c[:, 36+j])
    actual = (a @ h.reshape(36+aux, 400)).reshape(25, 20, 20)
    target = np.zeros_like(actual)
    for i,j,k in product(range(5), range(4), range(5)):
        target[5*i+k, 4*i+j, 5*j+k] = 1
    error = actual-target
    powers = [np.array(w) for w in point['map_row_powers']]
    degree = powers[0][:,None,None]+powers[1][None,:,None]+powers[2][None,None,:]
    groups = [
        {'old': [5*i+k for i in range(4) for k in range(4)],
         'i_edge': [20+k for k in range(4)],
         'k_edge': [5*i+4 for i in range(4)], 'corner': [24]},
        {'old': list(range(16)), 'edge': list(range(16,20))},
        {'old': [5*j+k for j in range(4) for k in range(4)],
         'edge': [5*j+4 for j in range(4)]}]
    blocks=[]
    for names in product(*groups):
        indices = np.ix_(*(groups[axis][name] for axis,name in enumerate(names)))
        err = error[indices]
        d = int(degree[indices].flat[0])
        blocks.append({'A':names[0], 'B':names[1], 'C':names[2], 'degree':d,
                       'coefficient_count':err.size,
                       'unit_target_count':int(np.count_nonzero(target[indices])),
                       'frobenius_error':float(np.linalg.norm(err)),
                       'maximum_error':float(np.max(np.abs(err)))})
    rows=[]
    for row in range(25):
        mask=degree[row]<=0
        rows.append({'A_row':[row//5,row%5],
                     'negative_error':float(np.linalg.norm(error[row][degree[row]<0])),
                     'constant_error':float(np.linalg.norm(error[row][degree[row]==0])),
                     'nonpositive_error':float(np.linalg.norm(error[row][mask]))})
    old_b=groups[1]['old']; old_c=groups[2]['old']
    leading=h[:,old_b,:][:,:,old_c].reshape(36+aux,256)
    sv=np.linalg.svd(leading,compute_uv=False)
    leading_algebra_target=target[np.ix_(groups[0]['old'],old_b,old_c)]
    leading_algebra_actual=actual[np.ix_(groups[0]['old'],old_b,old_c)]
    # The projected old M4 block has target norm 8; its exactness is required.
    result={'checkpoint':path.name,'auxiliary_rank':aux,
            'full_nonpositive_relative_error':float(np.linalg.norm(error[degree<=0])/10),
            'blocks':blocks,'rows_sorted_by_error':sorted(rows,key=lambda x:x['nonpositive_error'],reverse=True),
            'leading_pre_A_singular_values':sv.tolist(),
            'leading_pre_A_tail_after_27_norm':float(np.linalg.norm(sv[27:])),
            'leading_pre_A_tail_after_27_relative':float(np.linalg.norm(sv[27:])/np.linalg.norm(sv)),
            'leading_old_M4_relative_error':float(np.linalg.norm(leading_algebra_actual-leading_algebra_target)/8),
            'exact_coefficient_certificate':False}
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoints',type=Path,nargs='+')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=[analyze(path) for path in args.checkpoints]
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
