"""Exact SL(2,F8) group and rational central-algebra source certificate.

Reuses the unchanged finite-group center derivation from the SL(2,7)
package through an isolated module instance with a different group-table
callback. No prime-field arithmetic from that group's constructor is used.
"""
from functools import lru_cache
import importlib.util
from itertools import product
import json
from fractions import Fraction
from pathlib import Path
import sys

PARENT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(PARENT/'2026-10-20-group-potentials'))
from octal_group import fm


@lru_cache(None)
def group():
    identity = (1,0,0,1)
    matrices = [identity]+[m for m in product(range(8),repeat=4)
        if (fm(m[0],m[3])^fm(m[1],m[2]))==1 and m!=identity]
    if len(matrices)!=504:
        raise ArithmeticError('incorrect group order')
    index = {m:i for i,m in enumerate(matrices)}
    def multiply(x,y):
        a,b,c,d = x
        w,z,u,v = y
        return (fm(a,w)^fm(b,u),fm(a,z)^fm(b,v),
                fm(c,w)^fm(d,u),fm(c,z)^fm(d,v))
    table = [[index[multiply(x,y)] for y in matrices] for x in matrices]
    inverse = [index[d,b,c,a] for a,b,c,d in matrices]
    if any(table[i][inverse[i]] or table[inverse[i]][i] for i in range(504)):
        raise ArithmeticError('incorrect matrix inverse')
    return {'name':'SL(2,F8)','matrices':matrices,'mul':table,'inv':inverse,'identity':0}


def center_engine():
    path = PARENT/'2026-10-20-sl2-seven/source_certificate.py'
    spec = importlib.util.spec_from_file_location('sl2_f8_isolated_center_engine',path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.group = lambda ignored_prime:group()
    return module


def derive():
    G = group()
    engine = center_engine()
    report = engine.derive()
    report['field_model'] = 'F2[t]/(t^3+t+1)'
    report['group_center_order'] = sum(all(G['mul'][x][g]==G['mul'][g][x] for g in range(504)) for x in range(504))
    report['derivation_engine'] = 'research/ai/2026-10-20-sl2-seven/source_certificate.py, unchanged central-algebra procedure'
    report['conditional_exponent_gate'] = engine.exponent_gate(report['complex_degrees'],(18,18,25),Fraction(449,200))
    report['limitation'] = 'Exact source and conditional comparison only; no improving tensor degeneration constructed.'
    report['improves_omega'] = False
    return report


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    report = derive()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'degrees':report['complex_degrees'],
                      'conditional_gate':report['conditional_exponent_gate']},indent=2))
