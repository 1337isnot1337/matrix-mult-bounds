"""Source-pinned integer support and finite rank controls for loss seven."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
OMIT_ROWS = [3*28+r for r in (21,22,23)]
OMIT_COLUMNS = [3,7,11,15]


def predecessor():
    pins = json.loads((PACKAGE/'sources.json').read_text())
    for entry in pins['local_dependencies']:
        if hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest() != entry['sha256']:
            raise ValueError('source pin mismatch: '+entry['path'])
    spec = importlib.util.spec_from_file_location('locus',ROOT/'research/ai/2026-10-23-resolvent-rank-six/verify.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_basis(slices, high):
    """All 112 matrices of D W, middle-first, D=I4 tensor K."""
    labels = [('scalar',0,0)]
    for middle in (1,2):
        labels += [('shift',middle,i) for i in range(16)]
    labels += [('low',0,i) for i in range(16)]
    labels += [('high',0,i) for i in range(16) if i != 3]
    for block in (1,2,3):
        labels += [('high',block,i) for i in range(16)]
    unit = [[sum(slices[i][r][c] for i in (3,6,9,12)) for c in range(28)] for r in range(28)]
    for kind,block,index in labels:
        matrix = {}
        if kind == 'scalar':
            positions = [(i,i,unit) for i in range(4)]
        elif kind == 'shift':
            positions = [(i+block,i,slices[index]) for i in range(4-block)]
        else:
            positions = [(3,block,slices[index] if kind == 'low' else high[index])]
        for rowblock,colblock,outer in positions:
            for r,row in enumerate(outer):
                for c,value in enumerate(row):
                    if value:
                        matrix[(28*rowblock+r,28*colblock+c)] = value
        yield (kind,block,index),matrix


def rank_mod(matrices,prime):
    """Sparse elimination on vectorized coefficient matrices over F_prime."""
    pivots = {}
    for matrix in matrices:
        work = {key:value % prime for key,value in matrix.items() if value % prime}
        while work:
            pivot = min(work)
            if pivot not in pivots:
                scale = pow(work[pivot],-1,prime)
                pivots[pivot] = {key:value*scale % prime for key,value in work.items()}
                break
            scale = work[pivot]
            for key,value in pivots[pivot].items():
                updated = (work.get(key,0)-scale*value) % prime
                if updated:
                    work[key] = updated
                else:
                    work.pop(key,None)
    return len(pivots)


def check_witness(high,omit_rows=OMIT_ROWS,omit_columns=OMIT_COLUMNS):
    for index in (0,4):
        support = {(r,c):value for r,row in enumerate(high[index])
                   if r not in (21,22,23) for c,value in enumerate(row) if value}
        expected = {(7*j,4*(j+index//4)+3):1 for j in range(3)}
        if support != expected:
            raise ValueError('wrong projected sharpness support')
        if any(3*28+r not in omit_rows and c not in omit_columns
               for r,row in enumerate(high[index]) for c,value in enumerate(row) if value):
            raise ValueError('claimed factor does not kill both witness directions')
    if len(set(omit_rows)) != 3 or len(set(omit_columns)) != 4:
        raise ValueError('wrong rank budgets')
    return {'left_rank':109,'right_rank':108,'total_rank_loss':7,'independent_killed_directions':2}


def verify():
    prior = predecessor()
    prior_report = prior.verify()
    slices,high,inverse = prior.source()
    witness = check_witness(high)
    basis = list(source_basis(slices,high))
    if len(basis) != 112:
        raise ValueError('wrong full-space dimension')
    report = []
    for prime in (2,3):
        original = rank_mod((matrix for _,matrix in basis),prime)
        compressed = rank_mod(({(r,c):x for (r,c),x in matrix.items()
                                if r not in OMIT_ROWS and c not in OMIT_COLUMNS}
                               for _,matrix in basis),prime)
        if (original,compressed) != (112,110):
            raise ValueError('full-space witness rank mismatch')
        report.append({'prime':prime,'original_dimension':original,'compressed_dimension':compressed,'kernel_dimension':2})
    return {'schema':'resolvent-loss-seven-verification-v1','predecessor_locus_dimension':prior_report['full_low_rank_dimension'],
            'sharpness':witness,'full_source_controls':report,'universal_bound_field':'every field by scalar extension and descent',
            'universal_proof':'proof.md, importing Stacks tag 0B2R; finite rank controls are not the universal proof',
            'independent_review':False,'improves_omega':False}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=json.dumps(verify(),indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(result)
    else:
        print(result,end='')
