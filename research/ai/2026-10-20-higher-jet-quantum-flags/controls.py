"""Exact controls with moving projections whose leading kernels meet the flags."""
from pathlib import Path
import importlib.util
import json

_spec=importlib.util.spec_from_file_location('quantum_block_controls',Path(__file__).with_name('blocks.py'))
blocks=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(blocks)
one=blocks.one;jets=blocks.jets


def moving_projection_maps(G):
    """Represent 110 output coordinates by the 112 rows except 70 and 71.

    L0 kills these two leading directions. L1 sends them to rows 0 and 1.
    The image of L(t)G saturates to rows 0,1,73,74, independent of t.
    """
    constant={key:value for key,value in G.items() if key[0] not in [70,71]}
    linear={(0 if i==70 else 1,j):value for (i,j),value in G.items() if i in [70,71]}
    return constant,linear


def projected_coefficient(left,right,side):
    _,G_B=one.root_map(4,*left);_,G_C=one.root_map(4,*right)
    P0,_=moving_projection_maps(G_B);Q0,_=moving_projection_maps(G_C)
    phase=left if side=='left' else right
    # This is quotient by Ehat after L0, rather than a masked tensor fit.
    derivative={key:value for key,value in jets.first_jet(4,*phase).items()
                if key[0] not in [0,1,70,71,73,74]}
    rows=one.projected_source(4,derivative if side=='left' else P0,
                            Q0 if side=='left' else derivative)
    sliced=[]
    for row in rows:
        output={}
        for col,value in row.items():
            active=col//112 if side=='left' else col%112
            inactive=col%112 if side=='left' else col//112
            if inactive in [73,74]:
                output[active]=(output.get(active,0)+(1 if inactive==73 else 2)*value)%one.PRIME
        sliced.append({j:value for j,value in output.items() if value})
    rr,cc=one.independent_minor(sliced)
    if len(rr)<22:raise ArithmeticError('moving-projection rank control below 22')
    rr,cc=rr[:22],cc[:22]
    return {'left_phase':list(left),'right_phase':list(right),'varying_leg':side,
            'rank_lower_bound':22,'minor_rows':rr,'minor_columns':cc,
            'minor_determinant_mod_prime':one.determinant_mod([[sliced[i].get(j,0) for j in cc] for i in rr])}


def report():
    phases=[(6,1),(3,1),(3,2),(6,5)]
    return {'prime':one.PRIME,'leading_kernel_coordinates':[70,71],
            'saturated_leading_image_coordinates':[0,1,73,74],
            'inactive_contraction':{'73':1,'74':2},
            'records':[projected_coefficient(left,right,side) for left in phases for right in phases
                       for side in ['left','right']],
            'scope':'Explicit moving-surjection controls. Universal coverage comes from the written higher-jet proof and prior uniform slice minors, not these examples.'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(report(),indent=2)+'\n')
