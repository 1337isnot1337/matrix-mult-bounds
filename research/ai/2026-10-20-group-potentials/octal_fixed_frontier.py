"""Exact local frontier for constant normal directions in F8^2:C7.

Two 19-point families have five three-point fibers and two two-point fibers,
at multipliers 6 and 7. Their direction planes are constant. Within each
family the two short fibers share a direction. GL(2,F8) normalizes the first
plane and its distinguished direction to one of four templates. Every second
plane transverse over F2 and each of its three short directions is tested.
This does not cover varying direction planes or all fiber-size patterns.
"""
from itertools import combinations
import argparse
import json
from pathlib import Path
import time

from octal_group import fm,inverse,scale
from mask_packing import exact_pack


def planes():
    return sorted({tuple(sorted((0,u,v,u^v))) for u,v in combinations(range(1,64),2)})


def options(A,B,u,v,q=1):
    rows=[]
    for a in range(1,8):
        b=fm(a,q)
        left=A if a<6 else [0,u];right=B if b<6 else [0,v]
        W={scale(inverse(a),x^y) for x in left for y in right}
        if len(W)!=len(left)*len(right):raise ArithmeticError('normal pair collision')
        rows.append(sorted({sum(1<<(h^w) for w in W) for h in range(64)}))
    return rows


def frontier():
    started=time.monotonic();all_planes=planes();cases=0;nodes=0;max_nodes=0;survivors=[]
    if len(all_planes)!=651:raise ArithmeticError('wrong Grassmannian size')
    for r in [2,4,6,8]:
        A=[0,1,r];Aplane={0,1,r,1^r}
        for Bplane in all_planes:
            if Aplane.intersection(Bplane)!={0}:continue
            for v in Bplane[1:]:
                w=min(x for x in Bplane[1:] if x!=v)
                B=[0,v,w];result=exact_pack(options(A,B,1,v))
                cases+=1;nodes+=result['search_counts']['nodes']
                max_nodes=max(max_nodes,result['search_counts']['nodes'])
                if result['satisfiable']:
                    survivors.append({'first_template_ratio':r,'second_plane':Bplane,
                                      'second_short_direction':v,
                                      'local_packing':result['selected_masks']})
    if cases!=6720:raise ArithmeticError('normalization case count mismatch')
    return {'group':'F8^2:C7','pair_target_sizes':[19,19],
            'normal_plane_count':651,'complete_normalized_cases':cases,
            'search_nodes':nodes,'max_nodes_per_case':max_nodes,
            'locally_packable_cases':len(survivors),'survivors':survivors,
            'elapsed_seconds':time.monotonic()-started,
            'scope':__doc__,'method':'Complete standard-library integer backtracking',
            'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=frontier()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='survivors'},indent=2))
