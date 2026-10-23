"""Exact finite acceptance for independent coordinate compressions of A4.

The source reconstruction is imported from the pinned parent verifier.
The reduced outer space is rebuilt directly, without importing the block
discovery or census discovery code. Modular ranks are complex lower bounds;
the two upper-rank witnesses are checked by exact integer zero identities.
"""
from collections import Counter
import hashlib
import importlib.util
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / 'research/ai/2026-10-23-a4-coordinate-compressions'
PARENT = ROOT / 'research/ai/2026-10-23-conjugation-limit'
RESULTS = ROOT / 'results/a4-coordinate-compressions-2026-10-23'
PRIME = 1009
SIZE = 28
DIMENSION = 46


def source_verifier():
    spec = importlib.util.spec_from_file_location('a4_coordinate_source', PARENT / 'verify.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def outer_space():
    source = source_verifier()
    slices, _ = source.build_source()
    outer = [{SIZE * (position // 112) + position % 112: value
              for position, value in slices[48 + index].items()
              if position // 112 < SIZE and position % 112 < SIZE}
             for index in range(16)]
    fixed = outer[0]
    commutators = []
    sandwiches = []
    for index, matrix in enumerate(outer):
        right = source.matrix_product(matrix, fixed, SIZE)
        left = source.matrix_product(fixed, matrix, SIZE)
        if index not in (0, 3):
            commutator = dict(right)
            source.add_multiple(commutator, left, -1)
            commutators.append(commutator)
        sandwiches.append(source.matrix_product(fixed, right, SIZE))
    return outer + commutators + sandwiches


def modular_dimension(matrices):
    pivots = {}
    for entries in matrices:
        row = {position: value % PRIME for position, value in entries.items()
               if value % PRIME}
        while row:
            pivot = max(row)
            if pivot not in pivots:
                inverse = pow(row[pivot], -1, PRIME)
                pivots[pivot] = {position: value * inverse % PRIME
                                 for position, value in row.items()}
                break
            coefficient = row[pivot]
            for position, value in pivots[pivot].items():
                entry = (row.get(position, 0) - coefficient * value) % PRIME
                if entry:
                    row[position] = entry
                else:
                    row.pop(position, None)
    return len(pivots)


def projected(matrix, rows, columns):
    return {position: value for position, value in matrix.items()
            if position // SIZE not in rows and position % SIZE not in columns}


def census(matrices):
    pairs = list(combinations(range(SIZE), 2))
    histogram = Counter()
    for rows in pairs:
        row_restricted = [{position: value for position, value in matrix.items()
                           if position // SIZE not in rows} for matrix in matrices]
        for columns in pairs:
            rank = modular_dimension(
                {position: value for position, value in matrix.items()
                 if position % SIZE not in columns} for matrix in row_restricted)
            histogram[rank] += 1
    return {str(rank): count for rank, count in sorted(histogram.items())}


def verify_sharpness(witnesses, matrices):
    if len(witnesses) != 2:
        raise ValueError('the two sharpness witnesses are required')
    seen = set()
    for witness in witnesses:
        rows, columns = witness['deleted_rows'], witness['deleted_columns']
        if (rows != sorted(set(rows)) or columns != sorted(set(columns))
                or len(rows) != 2 or len(columns) != 2
                or any(type(index) is not int or not 0 <= index < SIZE
                       for index in rows + columns)):
            raise ValueError('invalid coordinate pair')
        pair = tuple(rows), tuple(columns)
        if pair in seen:
            raise ValueError('repeated sharpness pair')
        seen.add(pair)
        coefficient_rows = []
        for coefficients in witness['kernel_coefficients']:
            row = {}
            combination = {}
            for index, coefficient in coefficients:
                if (type(index) is not int or type(coefficient) is not int
                        or not 0 <= index < DIMENSION or not coefficient or index in row):
                    raise ValueError('invalid kernel coefficient')
                row[index] = coefficient
                for position, value in matrices[index].items():
                    combination[position] = combination.get(position, 0) + coefficient * value
            remaining = projected({p: x for p, x in combination.items() if x}, rows, columns)
            if remaining:
                raise ValueError('a claimed exact kernel identity is false')
            coefficient_rows.append(row)
        if len(coefficient_rows) != 6 or modular_dimension(coefficient_rows) != 6:
            raise ValueError('six independent exact kernel directions are required')
        if modular_dimension(projected(matrix, rows, columns) for matrix in matrices) != 40:
            raise ValueError('a sharpness witness has the wrong modular dimension')
    return 2


def verify_sources():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for entry in sources['local_dependencies']:
        if hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest() != entry['sha256']:
            raise ValueError('a pinned dependency changed')


def verify(certificate):
    if (certificate.get('schema') != 'a4-independent-coordinate-compressions-v1'
            or certificate.get('prime') != PRIME
            or certificate.get('coordinate_size') != SIZE
            or certificate.get('space_dimension') != DIMENSION
            or certificate.get('cases') != 142884):
        raise ValueError('wrong finite-census scope')
    verify_sources()
    matrices = outer_space()
    if len(matrices) != DIMENSION or modular_dimension(matrices) != DIMENSION:
        raise ValueError('the reduced source dimension is wrong')
    checked = verify_sharpness(certificate['sharpness_witnesses'], matrices)
    histogram = census(matrices)
    if histogram != certificate['modular_rank_histogram']:
        raise ValueError('the complete coordinate census differs')
    minimum = min(map(int, histogram))
    if minimum != 40 or sum(histogram.values()) != 142884:
        raise ValueError('the claimed finite minimum or coverage is false')
    return {'cases_checked': 142884, 'modular_rank_histogram': histogram,
            'minimum_complex_image_dimension': 40,
            'exact_sharpness_witnesses_checked': checked,
            'maximum_coordinate_compression_kernel_dimension': 6,
            'full_source_independent_coordinate_compressions_excluded': True,
            'arbitrary_constant_compressions_excluded': False,
            'full_target_constructed': False}


if __name__ == '__main__':
    certificate = json.loads((RESULTS / 'certificate.json').read_text())
    report = verify(certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
