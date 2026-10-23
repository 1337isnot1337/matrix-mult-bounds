"""Discovery only: propose integer triangular-minor elimination certificates."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location('source', ROOT / 'research/ai/2026-10-23-resolvent-minrank/verify.py')
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)


def find_minor(basis, size):
    entries = [[tuple(matrix[r][c] for matrix in basis) for c in range(28)] for r in range(28)]
    groups = {}
    for r in range(28):
        for c in range(28):
            form = entries[r][c]
            first = next((x for x in form if x), 0)
            if first not in (-1, 1):
                continue
            form = tuple(first * x for x in form)
            groups.setdefault(form, []).append((r, c))
    for form, pairs in sorted(groups.items(), key=lambda item: -len(item[1])):
        if min(len({r for r,c in pairs}), len({c for r,c in pairs})) < size:
            continue
        after = []
        for r,c in pairs:
            after.append(sum(1 << j for j,(rr,cc) in enumerate(pairs)
                             if rr != r and cc != c and not any(entries[r][cc])))
        dead = set()
        def search(mask, need):
            if not need:
                return []
            if mask.bit_count() < need or (mask,need) in dead:
                return None
            choices = [j for j in range(len(pairs)) if mask >> j & 1]
            choices.sort(key=lambda j: -(mask & after[j]).bit_count())
            for j in choices:
                rest = mask & after[j]
                if rest.bit_count() < need-1:
                    continue
                tail = search(rest, need-1)
                if tail is not None:
                    return [pairs[j]] + tail
            dead.add((mask,need))
            return None
        minor = search((1 << len(pairs))-1, size)
        if minor is not None:
            return list(form), minor
    return None


def discover(size):
    basis, labels = source.mixed_basis()
    certificate = {'size':size, 'dimension':len(basis), 'labels':labels, 'stages':[]}
    while True:
        result = find_minor(basis,size)
        if result is None:
            break
        form, minor = result
        pivot = next(i for i,x in enumerate(form) if x in (-1,1))
        certificate['stages'].append({'form':form,'pivot':pivot,'minor':minor})
        chosen = basis[pivot]
        basis = [source.combine([matrix,chosen],[1,-form[j]//form[pivot]])
                 for j,matrix in enumerate(basis) if j != pivot]
        print('remaining',len(basis),flush=True)
    certificate['remaining_dimension'] = len(basis)
    return certificate,basis


if __name__ == '__main__':
    certificate,basis = discover(8)
    folder=ROOT/'results/local/resolvent-rank-six'
    folder.mkdir(parents=True,exist_ok=True)
    (folder/'eight-minors.json').write_text(json.dumps(certificate,indent=2)+'\n')
    (folder/'remaining.json').write_text(json.dumps(basis)+'\n')
    print('final',len(basis))
