"""Discovery adapter adding exact saturated-fiber parity to the maintained driver."""
import json
from pathlib import Path
import sys
from itertools import product

from source_data import group, subgroup_certificate, central_projection
from pair_saturation import pair_data, saturated_reject, verify_saturated
import projected_lifts


def main():
    G = group()
    cert = subgroup_certificate(G)
    Q = central_projection(G, cert)
    data = pair_data(G, Q, cert['center'])
    learn = '--learn-saturated' in sys.argv
    if learn:
        sys.argv.remove('--learn-saturated')
        if '--native-binary' not in sys.argv:
            raise ValueError('learning saturated rows requires --native-binary')
    state = {'learned_rows': 0, 'keys': set()}
    original_build = projected_lifts.build_outer

    def build(*args):
        outer, members, bits = original_build(*args)
        state.update(outer=outer, members=members, bits=bits, top=outer.nof_vars())
        twist = []
        for f in range(3):
            row = []
            for p in range(60):
                state['top'] += 1
                row.append(state['top'])
            outer.add_clause([-row[0]])
            twist.append(row)
        state['twist'] = twist
        return outer, members, bits

    def reject(pairs, sets):
        record = saturated_reject(pairs, data, sets)
        if not learn or not record or not record.get('saturated_pair_equations'):
            return record
        verify_saturated(pairs, data, record)
        for row in record['rows']:
            labels = [label for i, label in enumerate(record['variables']) if row['mask'] >> i & 1]
            if any(label[0] == 'owner' for label in labels):
                continue  # Already encoded by the native binary necessary conditions.
            variables = sorted(state['bits' if kind == 'bit' else 'twist'][f][p]
                               for kind, f, p in labels)
            key = (tuple(variables), row['rhs'], tuple(row['support']))
            if key in state['keys']:
                continue
            state['keys'].add(key)
            outer = state['outer']
            guard = [-state['members'][f][p] for f, p in row['support']]
            if not variables:
                if row['rhs']:
                    outer.add_clause(guard)
            else:
                prefix = variables[0]
                for v in variables[1:]:
                    state['top'] += 1
                    result = state['top']
                    for values in product(range(2), repeat=3):
                        if sum(values) % 2:
                            outer.add_clause([x if not b else -x
                                              for x, b in zip((prefix, v, result), values)])
                    prefix = result
                outer.add_clause(guard+[prefix if row['rhs'] else -prefix])
            state['learned_rows'] += 1
        return record

    if learn:
        projected_lifts.build_outer = build
    projected_lifts.reject = reject
    projected_lifts.verify_rejection = lambda pairs, record: verify_saturated(pairs, data, record)
    if '--binary-filter' not in sys.argv:
        sys.argv.append('--binary-filter')
    projected_lifts.main()
    path = Path(sys.argv[sys.argv.index('--output')+1])
    report = json.loads(path.read_text())
    report['saturated_pair_filter'] = True
    report['saturated_rows_learned_in_outer_solver'] = state['learned_rows']
    path.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
