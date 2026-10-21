"""A linear output identity closes the fixed weighted spin-fiber family."""
from collections import Counter
import importlib.util
import json
from pathlib import Path

spec=importlib.util.spec_from_file_location('ordinary_fiber',Path(__file__).with_name('spin_fiber_compression.py'))
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
OUTPUT=v.RESULTS/'spin-fiber-closure-certificate.json'
POINTS2=((0,1,39),(30,31,39),(30,31,69))
POLYS2=({(96,239,372):64},{(14,157,290):64,(96,239,372):64},{(14,157,290):64})
POINTS3=((18,487,111),(102,571,111),(102,571,195))
POLYS3=({(572,3151,3952):512},{(90,2669,3470):512,(572,3151,3952):512},{(90,2669,3470):512})


def output_polynomial(power,point):
    polynomial=v.selected_equation(power,point)
    polynomial.pop((),None)
    return polynomial


def report():
    controls=[]
    points=POINTS2;expected=POLYS2
    for power in (2,3,4,5):
        if power==3:points=POINTS3;expected=POLYS3
        actual=tuple(output_polynomial(power,point) for point in points)
        if actual!=expected:raise ArithmeticError('A selected full-source polynomial differs')
        combination=Counter()
        for sign,polynomial in zip((1,-1,1),actual):
            for monomial,coefficient in polynomial.items():
                combination[monomial]+=sign*coefficient
        if any(combination.values()):raise ArithmeticError('The output hyperplane identity fails')
        target=sum(sign*v.matrix_coefficient(power,p) for sign,p in zip((1,-1,1),points))
        if target!=-1:raise ArithmeticError('The matrix tensor no longer violates the identity')
        minima=[{'row':row,'minimum_middle':min(m for _,m,_ in v.row_image(power,0,row))}
                for row in sorted({p[0] for p in points})]
        if power>=3 and any(item['minimum_middle']<2**power-1 for item in minima):
            raise ArithmeticError('The induction minimum-middle hypothesis fails')
        controls.append({'power':power,'target_hyperplane_value':target,'source_hyperplane_value':0,
                         'first_row_minima':minima,'equations':[{'target_rows':list(p),
                         'output_polynomial':v.export_polynomial(q)} for p,q in zip(points,actual)]})
        if power>=3:
            points=tuple(v.lift_point(power,p) for p in points)
            expected=tuple(v.lift_polynomial(power,q) for q in actual)
    return {'claim':'AI-SPIN-FIBER-CLOSURE-124','field':'Every characteristic-zero field',
            'family':'The independent raw-column weighted fixed spin/radix family of118',
            'all_power_statement':'For every k>=2 the complete output lies in a fixed linear hyperplane violated by M_(3^k)',
            'finite_induction_controls':controls,'linear_combination':[1,-1,1],
            'ordinary_maps_excluded':True,'laurent_limiting_degenerations_excluded':True,
            'arbitrary_source_maps_excluded':False,'new_exponent_established':False}


def verify(saved=None):
    if saved is None:saved=json.loads(OUTPUT.read_text())
    actual=report()
    if actual!=saved:raise ArithmeticError('The saved hyperplane certificate differs')
    return actual


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true');args=parser.parse_args()
    if args.write:OUTPUT.write_text(json.dumps(report(),indent=2)+'\n')
    else:verify()
    print('The linear output obstruction and all saved induction controls pass.')
