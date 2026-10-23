"""Apply the closed-target Ferrers cap using the preserved source-lift tests."""
import argparse
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]


def load(relative,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/relative)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


v=load('research/ai/2026-10-21-ferrers-ruling-cap/verify.py','ferrers_application_verify')
prior=load('research/ai/2026-10-21-hankel-wronskian-cap/application.py','ferrers_preserved_hankel_application')
# Only this privately loaded module changes. No prior source is edited.
prior.image_cap=v.closed_target_cap


def rectangular_report():
    base=json.loads((ROOT/'results/hankel-wronskian-cap-2026-10-21/rectangular.json').read_text())
    sources=base['sources'];new=0
    for source in sources:
        a=source['a'];N=source['source_leg_dimension'];added=[]
        source['excluded_at_wronskian_checkpoint']=source['excluded_shapes']
        for row in source['records']:
            if row['excluded']:continue
            shape=row['shape'];witness=None
            for x,y,z in [shape,shape[1:]+shape[:1],shape[2:]+shape[:2]]:
                witness=prior.additional_witness(a,a,x,y,z,2*N-z*(x+y))
                if witness is not None:break
            if witness is not None:
                row['excluded']=True;row['witness']=witness;added.append(shape)
        source['new_ferrers_exclusions']=added;new+=len(added)
        source['excluded_shapes']=sum(row['excluded'] for row in source['records'])
        source['survivors']=[row['shape'] for row in source['records'] if not row['excluded']]
    return {'scope':'Every improving sorted ordinary single rectangular shape from the preserved balanced a2..a12 scan.',
            'comparison_base':'PR83 Hankel package; this is not the full concurrent all-source frontier.',
            'complete_improving_sorted_shapes':5139,'excluded_at_comparison_base':4899,
            'additional_ferrers_exclusions':new,'complete_excluded_shapes':4899+new,
            'remaining_necessary_test_survivors':240-new,'sources':sources,
            'cap':'Closed-target dominance dichotomy with uniform scalar Hankel linear-space cap',
            'candidate_constructed':False,'singular_degenerations_excluded':False,
            'independent_review':False,'improves_omega':False}


def square_report():
    result=prior.square_report()
    result['scope']='Every square partition at every dimension in A8..A12, with the closed-target Ferrers cap; necessary tests only.'
    result['comparison_base']='PR83 saved square report; not the full concurrent all-source frontier.'
    result['new_ruling_proof']='The two local proofs in2026-10-21-ferrers-ruling-cap; Borel fixed-point input credited.'
    result['inherited_refinements']=result.pop('local_refinements')
    result['inherited_higher_input_credit']=result.pop('higher_input_proof_credit')
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--rectangular-output',type=Path,required=True)
    p.add_argument('--square-output',type=Path,required=True)
    args=p.parse_args()
    formatter=load('research/ai/2026-10-21-hankel-wronskian-cap/verify.py','ferrers_app_formatter')
    for path in [args.rectangular_output,args.square_output]:path.parent.mkdir(parents=True,exist_ok=True)
    formatter.write_json(args.rectangular_output,rectangular_report())
    formatter.write_json(args.square_output,square_report())
    print('Exact Ferrers applications replayed.')
