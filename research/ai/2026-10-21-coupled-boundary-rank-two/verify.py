"""Complete coupled cubic-minor reduction of the boundary obstruction pair."""
import argparse
from collections import Counter, defaultdict
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]


def load(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode(matrix):
    return {'shape':list(matrix.shape),'entries':[
        [i,j,str(value)] for (i,j),value in sorted(matrix.todok().items()) if value]}


def decode(record):
    return sp.MutableSparseMatrix(*record['shape'],{
        (i,j):sp.Rational(value) for i,j,value in record['entries']})


def decode_old(record):
    return sp.MutableSparseMatrix(*record['shape'],{
        (i,j):sp.Rational(p,q) for i,j,p,q in record['entries']})


def rank(matrix):
    return len(matrix.to_DM().rref()[1])


@lru_cache(None)
def source():
    old = load(ROOT/'research/ai/2026-10-21-moving-boundary-flags/minimum_rank.py',
               'coupled_boundary_minors_source')
    data = old.normal.data()
    return old,data


def cubic_forms(matrix,old,side):
    table = [[0]*12 for _ in range(200)]
    byrow = defaultdict(dict)
    forms,indices,positions = [],{},defaultdict(list)
    for (i,j),value in matrix.todok().items():
        byrow[i][j] = value
    for flat,row in sorted(byrow.items()):
        form = old.primitive_form(row)
        if form not in indices:
            indices[form] = len(indices)+1
            forms.append(form)
        index = indices[form]
        column,row = divmod(flat,200)
        table[row][column] = index
        positions[index].append((row,column))
    found,records = [],[]
    for index,form in enumerate(forms,1):
        witness = old.triangular_witness(table,positions[index],size=3)
        if witness is None:
            continue
        scales = []
        for k,(row,column) in enumerate(witness):
            j,value = form[0]
            scale = matrix[200*column+row,j]/value
            expected = sp.Matrix(1,matrix.cols,lambda _,j:scale*dict(form).get(j,0))
            if not scale or matrix[200*column+row,:]!=expected:
                raise ArithmeticError('cubic diagonal is not the claimed repeated form')
            for _,future in witness[k+1:]:
                if matrix[200*future+row,:].todok():
                    raise ArithmeticError('cubic upper triangular entry is not zero')
            scales.append(scale)
        found.append(form)
        records.append({'side':side,'positions':[list(p) for p in witness],
                        'form':[list(p) for p in form],
                        'determinant_ratio':str(sp.prod(scales))})
    return found,records


@lru_cache(None)
def reports():
    old,data = source()
    original_b = data['left_obstruction'][:2400,:]
    original_c = data['right_obstruction'][:2400,:]
    b,c = original_b,original_c
    full = sp.eye(228)
    rounds = []
    while b.todok() or c.todok():
        left,left_records = cubic_forms(b,old,'B')
        right,right_records = cubic_forms(c,old,'C')
        forms = left+right
        if not forms:
            raise ArithmeticError('coupled cubic reduction stalled before closure')
        constraints = sp.MutableSparseMatrix(len(forms),b.cols,{
            (i,j):value for i,row in enumerate(forms) for j,value in row})
        kernel,_ = old.normal.sparse_nullspace(constraints)
        rounds.append({'parameter_dimension':b.cols,
                       'forced_linear_rank':b.cols-kernel.cols,
                       'kernel':encode(kernel),'minors':left_records+right_records})
        b,c,full = b*kernel,c*kernel,full*kernel
    if [(r['parameter_dimension'],r['forced_linear_rank'],len(r['minors'])) for r in rounds] != [
            (228,132,164),(96,40,40),(56,24,24),(32,4,4)]:
        raise ArithmeticError('complete cubic reduction coverage changed')
    prior = json.loads((ROOT/'results/third-boundary-trap-2026-10-21/normal.json').read_text())
    prior_basis = decode_old(prior['normal_basis'])
    actual = data['first_kernel']*full
    rows = list(prior_basis.T.to_DM().rref()[1])
    transform = prior_basis[rows,:].inv()*actual[rows,:]
    if prior_basis*transform!=actual or rank(transform)!=28:
        raise ArithmeticError('the final normal family differs from the prior complete boundary family')
    controls = {}
    histogram = Counter()
    low_pairs = []
    for j in range(228):
        mb = sp.Matrix(200,12,lambda row,column:original_b[200*column+row,j])
        mc = sp.Matrix(200,12,lambda row,column:original_c[200*column+row,j])
        rb,rc = rank(mb),rank(mc)
        histogram[rb,rc] += 1
        if max(rb,rc)<=2 and rb+rc:
            low_pairs.append(j)
        if (rb,rc)==(2,4):
            controls.setdefault('B_rank_two_C_rank_four',j)
        if (rb,rc)==(4,2):
            controls.setdefault('B_rank_four_C_rank_two',j)
    if len(controls)!=2:
        raise ArithmeticError('individual rank-two positive controls missing')
    return {'coordinate_pilot':{
                'scope':'All228 coordinate normal directions only; not an all-subspace argument.',
                'completed_candidates':228,
                'rank_pair_histogram':[[a,b,n] for (a,b),n in sorted(histogram.items())],
                'nonzero_pairs_with_both_ranks_at_most_two':low_pairs},
            'source':{'matrix_shape':[200,12],'normal_parameter_dimension':228,
                      'vectorization':'column',
                      'B':encode(original_b),'C':encode(original_c),
                      'normal_first_kernel':encode(data['first_kernel'])},
            'certificate':{'rounds':rounds,'final_parameter_dimension':28,
                           'both_complete_obstructions_zero':True,
                           'original_parameter_map':encode(full),
                           'actual_normal_basis':encode(actual),
                           'prior_basis_transform':encode(transform),
                           'individual_rank_two_controls':controls,
                           'cubic_identities':232,
                           'scope':'Complete algebraic rank implication over C; no higher-order lift or improved exponent.'}}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,report in reports().items():
        (args.output_dir/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
        print(name,'written',flush=True)
