"""SL(2,7) adapter for the pinned concurrent SAT/Farkas implementation."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).with_name('imported')))
import group_exact
import search as upstream
from pysat.card import CardEnc, EncType
from central_involution import forced_center_pair_exclusions
from subgroup_normalization import octahedral_certificate, verify_certificate


def borel_certificate(G):
    p = 7
    index = {x: i for i, x in enumerate(G['matrices'])}
    members = [i for i, x in enumerate(G['matrices']) if x[2] == 0]
    conjugators = [(a, b, 0, d) for a in range(1, p)
                   for d in range(1, p) for b in range(p)]

    def mm(x, y):
        a, b, c, d = x
        e, f, g, h = y
        return ((a*e+b*g)%p, (a*f+b*h)%p,
                (c*e+d*g)%p, (c*f+d*h)%p)

    def image(q, P):
        a, b, c, d = P
        iv = pow((a*d-b*c)%p, -1, p)
        inverse = (d*iv%p, -b*iv%p, -c*iv%p, a*iv%p)
        return index[mm(mm(P, G['matrices'][q]), inverse)]

    remaining, anchors, witnesses = set(members)-{0}, [], []
    while remaining:
        representative = min(remaining)
        orbit = {image(q, P) for q in (representative, G['inv'][representative])
                 for P in conjugators}
        anchor = min(orbit)
        anchors.append(anchor)
        for q in sorted(orbit):
            found = None
            for reverse in (False, True):
                actual = G['inv'][q] if reverse else q
                for P in conjugators:
                    if image(actual, P) == anchor:
                        found = {'quotient': q, 'reverse_pair': reverse,
                                 'conjugator': P, 'anchor': anchor}
                        break
                if found:
                    break
            if found is None:
                raise ArithmeticError('missing quotient normalization')
            witnesses.append(found)
        remaining -= orbit
    if len(members) != 42 or len(witnesses) != 41:
        raise ArithmeticError('incorrect Borel coverage')
    return {'order': 42, 'index': 8, 'members': members,
            'anchors': anchors, 'witnesses': witnesses}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--seed', type=int, default=20261320)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--normalization', choices=['borel', 'octahedral'], default='borel')
    args = parser.parse_args()
    G = group_exact.group(7)
    cert = (borel_certificate(G) if args.normalization == 'borel'
            else octahedral_certificate(G))
    if args.normalization == 'octahedral' and not verify_certificate(G, cert):
        raise ArithmeticError('subgroup normalization certificate failed')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_name(args.normalization+'-certificate.json').write_text(
        json.dumps(cert, indent=2)+'\n')
    original_build = upstream.build_solver

    def build(group, shape, seed, engine):
        solver, members, metadata = original_build(group, shape, seed, engine)
        top = metadata['variables']
        for f, size in enumerate(shape):
            card = CardEnc.atleast([members[f][g] for g in cert['members']],
                (size+cert['index']-1)//cert['index'], top_id=top, encoding=EncType.seqcounter)
            solver.append_formula(card.clauses)
            top = card.nv
        solver.add_clause([members[0][g] for g in cert['anchors']])
        metadata['variables_after_subgroup'] = top
        metadata['SL2_7_subgroup_normalization'] = {
            'type': args.normalization, 'order': cert['order'], 'index': cert['index'],
            'identity_fiber_lower': [(size+cert['index']-1)//cert['index'] for size in shape],
            'anchors': cert['anchors']}
        exclusions = forced_center_pair_exclusions(group, shape)
        for item in exclusions:
            f = item['set']
            for g, h in item['pairs']:
                solver.add_clause([-members[f][g], -members[f][h]])
        metadata['central_involution_exclusions'] = [
            {k: v for k, v in item.items() if k != 'pairs'}
            for item in exclusions]
        metadata['central_involution_binary_clauses'] = sum(
            len(item['pairs']) for item in exclusions)
        return solver, members, metadata

    # The pinned run routine chooses group(5); this adapter replaces that
    # supplier only. The group implementation and exact checker are unchanged.
    upstream.group = lambda _p=5: G
    upstream.build_solver = build
    upstream.run([16, 16, 17], args.seconds, args.seed, args.output,
                 max_models=1000, engine='cadical195')


if __name__ == '__main__':
    main()
