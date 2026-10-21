"""Apply the written Hankel theorem to the existing exact ordinary screens."""
import argparse
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


controls=load('research/ai/2026-10-21-hankel-pencil-degree/verify.py','pencil_degree_controls')
rectangular=load('research/ai/2026-10-21-rectangular-ordinary-frontier/verify.py','prior_rectangular_frontier')
squares=load('research/ai/2026-10-20-anisotropic-constructions/square_sum_frontier.py','prior_square_frontier')


def witness(a,shape):
    N=a*a*(2*a-1)
    for x,y,z in [shape,shape[1:]+shape[:1],shape[2:]+shape[:2]]:
        lift=z+2*N-z*(x+y)
        for r in range(1,a):
            cap=controls.symbol_cap(a,a,r)
            if cap is not None and x*y>cap*a*a and lift<(r+1)*a*a:
                return {'gate':'hankel_linear_annihilator','symbol_rank':r,
                        'matrix_parameter_dimensions':[x,y],'slice_rank':z,
                        'block_parameter_dimension':x*y,'lift_rank_upper_bound':lift,
                        'required_rank':(r+1)*a*a,'symbol_image_cap':cap,
                        'dimension_cap':cap*a*a,'strict_pencil_condition':[5*r,4*a]}
    return None


def rectangular_report():
    sources=[];new=0
    for a in range(2,13):
        source=rectangular.source(a);old_excluded=source['excluded_shapes'];added=[]
        for row in source['records']:
            if row['excluded']:continue
            certificate=witness(a,row['shape'])
            if certificate is not None:
                row['excluded']=True;row['witness']=certificate;added.append(row['shape'])
        source['excluded_by_previous_gates']=old_excluded
        source['additional_excluded_shapes']=added
        source['excluded_shapes']=sum(x['excluded'] for x in source['records'])
        source['survivors']=[x['shape'] for x in source['records'] if not x['excluded']]
        sources.append(source);new+=len(added)
    first=next(x for x in sources if x['survivors'])
    assert new==453 and first['a']==10 and len(first['survivors'])==53
    return {'source_range':[2,12],'ordinary_single_rectangular_blocks_only':True,
            'complete_improving_sorted_shapes':sum(s['improving_shapes'] for s in sources),
            'complete_excluded_shapes':sum(s['excluded_shapes'] for s in sources),
            'additional_exclusions':new,'sources':sources,
            'first_source_with_necessary_test_survivors':10,
            'ordinary_survivors_are_constructions':False,
            'singular_degenerations_excluded':False,'independent_review':False,'improves_omega':False}


old_allowed_blocks=squares.allowed_blocks


def extended_allowed_blocks(a,b,dimension):
    allowed,scalar,repeated=old_allowed_blocks(a,b,dimension)
    N=a*b*(a+b-1);loss=N-dimension
    def survives(n):
        for r in range(1,min(a,b)):
            cap=controls.symbol_cap(a,b,r)
            if cap is not None and n*n>cap*a*b and n+2*loss<(r+1)*a*b:return False
        return True
    return [n for n in allowed if survives(n)],scalar,repeated


def square_report():
    # Reuse the credited exact integer recurrence, changing only its allowed-block
    # filter in this independently loaded module; its source file is unchanged.
    squares.allowed_blocks=extended_allowed_blocks
    records=[squares.source_frontier(a,a,retain_dimensions=True) for a in [8,9]]
    for record in records:
        shape=record['maximum']['maximizing_relaxed_partition']
        record['maximum']['lower_score_numerator_of_saved_partition']=sum(squares.score_interval(n)[0] for n in shape)
    return {'scope':'All square partitions of every target dimension in the two stated balanced sources; ordinary maps only.',
            'sources':records,'recurrence_credit':'Existing square_sum_frontier.py',
            'singular_degenerations_excluded':False,'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rectangular-output',type=Path,required=True)
    parser.add_argument('--square-output',type=Path,required=True)
    args=parser.parse_args()
    for output in [args.rectangular_output,args.square_output]:output.parent.mkdir(parents=True,exist_ok=True)
    controls.write_json(args.rectangular_output,rectangular_report())
    controls.write_json(args.square_output,square_report())
    print('Updated rectangular and balanced A8/A9 square-partition screens completed exactly.')
