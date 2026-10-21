"""Use the uniform cap with credited higher-input-rank necessary tests."""
import argparse
from functools import lru_cache
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]


def load(relative,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/relative)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


prior=load('research/ai/2026-10-21-hankel-pencil-degree/application.py','wronskian_prior_application')
geometry=load('research/ai/2026-10-21-hankel-wronskian-cap/geometry.py','wronskian_geometry')


@lru_cache(maxsize=None)
def image_cap(r,k):
    """Credited strict saturation/k-ruling bound plus the local Hankel equality case."""
    if not (r>=1 and k>=2):raise ValueError('Need r>=1,k>=2')
    if 2*r<k*(k+2):return r,'projection_saturation'
    if 2*r==k*(k+2):return r,'hankel_boundary_saturation'
    maximum=0
    for p in range(1,r+1):
        for q in range(1,r+1):
            if p<=k or q<=k:bound=r
            else:
                bound=min(p*q,r+(q-k)*((r-p)//(k-1)),r+(p-k)*((r-q)//(k-1)))
            maximum=max(maximum,bound)
    return maximum,'generic_k_ruling'


def additional_witness(a,b,x,y,z,loss):
    G=a*b
    for r in range(1,min(a,b)):
        for k in range(2,min(r,x,y)+1):
            R=k*z+loss
            if R>=(r+1)*G:continue
            cap,method=image_cap(r,k)
            if x*y>cap*G:
                return {'gate':'uniform_hankel_higher_input','method':method,
                        'parameter_dimensions':[x,y],'matrix_input_rank':k,
                        'target_slice_rank_at_input_rank':k*z,'symbol_rank':r,
                        'source_lift_rank_upper':R,'strict_rank_threshold':(r+1)*G,
                        'linear_hankel_space_cap':r,'scalar_image_dimension_cap':cap,
                        'block_dimension':x*y,'full_dimension_cap':cap*G,
                        'closed_hankel_cone_dimension_upper':2*r}
    # Concurrent PR76 supplies the quantitative crossed-rank inequality and
    # the all-rank crossed-Hankel locus dimension bound. The lower-symbol
    # prerequisite is proved here using the uniform cap and image_cap.
    full=min(a,b)
    for k in range(2,min(full,x,y)+1):
        lower_cap,lower_method=image_cap(full-1,k)
        if x*y<=lower_cap*G:continue
        R=k*z+loss
        crossed=R-(G-1)*full
        if crossed<full:continue  # Already covered by the preceding rank gate.
        locus,unsectioned,proper=geometry.crossed_dimension_cap(a,b,crossed,x*y)
        parameter_dimension=k*(x+y-k)
        if parameter_dimension>locus:
            return {'gate':'full_symbol_crossed_locus','parameter_dimensions':[x,y],
                    'matrix_input_rank':k,'full_symbol_rank':full,
                    'lower_symbol_rank':full-1,'lower_symbol_image_cap':lower_cap,
                    'lower_cap_method':lower_method,'block_dimension':x*y,
                    'lower_full_dimension_cap':lower_cap*G,
                    'source_lift_rank_upper':R,'crossed_rank_upper':crossed,
                    'crossed_locus_dimension_upper':locus,
                    'unsectioned_crossed_dimension_upper':unsectioned,
                    'proper_source_parameter_subspace':proper,
                    'rank_parameter_variety_dimension':parameter_dimension}
    return None


def rectangular_report():
    previous=prior.rectangular_report();new=0
    for source in previous['sources']:
        a=source['a'];N=source['source_leg_dimension'];added=[]
        source['excluded_at_pencil_checkpoint']=source['excluded_shapes']
        for row in source['records']:
            if row['excluded']:continue
            shape=row['shape'];certificate=None
            for x,y,z in [shape,shape[1:]+shape[:1],shape[2:]+shape[:2]]:
                certificate=additional_witness(a,a,x,y,z,2*N-z*(x+y))
                if certificate is not None:break
            if certificate is not None:
                row['excluded']=True;row['witness']=certificate;added.append(row['shape'])
        source['additional_higher_input_exclusions']=added
        source['excluded_shapes']=sum(row['excluded'] for row in source['records'])
        source['survivors']=[row['shape'] for row in source['records'] if not row['excluded']]
        new+=len(added)
    assert new>=235
    return {'comparison_base':'Preserved main-PR75 balanced rectangular report, not the full concurrent PR76 frontier.',
            'source_range':[2,12],'complete_improving_sorted_shapes':5139,
            'excluded_at_comparison_base':4645,'additional_higher_input_exclusions':new,
            'complete_excluded_shapes':sum(s['excluded_shapes'] for s in previous['sources']),
            'remaining_necessary_test_survivors':sum(len(s['survivors']) for s in previous['sources']),
            'sources':previous['sources'],'ordinary_single_balanced_targets_only':True,
            'no_new_coordinate_cap_certificates_required':True,
            'concurrent_bilinear_proof_commit':'6db658954fe976e3d433991ebf606d1d5d31a9e9',
            'candidate_constructed':False,'singular_degenerations_excluded':False,
            'independent_review':False,'improves_omega':False}


old_allowed=prior.extended_allowed_blocks


def allowed_blocks(a,b,D):
    ns,scalar,repeated=old_allowed(a,b,D);N=a*b*(a+b-1)
    return [n for n in ns if additional_witness(a,b,n,n,n,2*(N-D)) is None],scalar,repeated


def square_report():
    # Reuse the maintained exact recurrence. Pure score memoization changes no
    # intervals or accepted comparison; no prior source file is modified.
    prior.squares.allowed_blocks=allowed_blocks
    if not hasattr(prior.squares.score_interval,'cache_info'):
        prior.squares.score_interval=lru_cache(maxsize=None)(prior.squares.score_interval)
    sources=[prior.squares.source_frontier(a,a,retain_dimensions=True) for a in range(8,13)]
    for source in sources:
        shape=source['maximum']['maximizing_relaxed_partition']
        source['maximum']['lower_score_numerator_of_saved_partition']=sum(prior.squares.score_interval(n)[0] for n in shape)
    return {'scope':'Every square partition at every target leg dimension in the five balanced sources A8..A12; necessary conditions only.',
            'sources':sources,'recurrence_credit':'Existing square_sum_frontier.py',
            'higher_input_proof_credit':'Concurrent PR76 saturation.md, two_ruling_cap.md, quantitative_crossed_rank.md and bundle_hankel_dimension.md at pinned commit6db6589',
            'local_refinements':['Uniform Wronskian linear-space cap','Hankel-specific equality saturation','Proper crossed-rank linear-section bound'],
            'new_linear_space_cap':'Uniform characteristic-zero Wronskian proof',
            'candidate_constructed':False,'singular_degenerations_excluded':False,
            'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--rectangular-output',type=Path,required=True)
    p.add_argument('--square-output',type=Path,required=True)
    args=p.parse_args()
    for path in [args.rectangular_output,args.square_output]:path.parent.mkdir(parents=True,exist_ok=True)
    formatter=load('research/ai/2026-10-21-hankel-wronskian-cap/verify.py','wronskian_formatter')
    formatter.write_json(args.rectangular_output,rectangular_report())
    formatter.write_json(args.square_output,square_report())
    print('Uniform-cap higher-input applications replayed exactly.')
