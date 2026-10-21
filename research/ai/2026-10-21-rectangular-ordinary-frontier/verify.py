"""Apply the existing ordinary-source theorems to balanced rectangular targets."""
import argparse
import json
from math import isqrt
from pathlib import Path


def write_json(path,data):
    """Keep each complete format or corner witness on one reviewable line."""
    def render(value,level=0,key=None):
        pad='  '*level
        if isinstance(value,dict):
            return '{\n'+',\n'.join(pad+'  '+json.dumps(k)+': '+render(v,level+1,k) for k,v in value.items())+'\n'+pad+'}'
        if isinstance(value,list):
            if key in ['records','cases']:
                return '[\n'+',\n'.join(pad+'  '+json.dumps(v,separators=(',',':')) for v in value)+'\n'+pad+']'
            if all(not isinstance(v,(list,dict)) for v in value):return json.dumps(value)
            return '[\n'+',\n'.join(pad+'  '+render(v,level+1) for v in value)+'\n'+pad+']'
        return json.dumps(value)
    path.write_text(render(data)+'\n')


def exclusion(a,l,h,n):
    N=a*a*(2*a-1);m=2*a-1
    for u,v,w in [(l,h,n),(h,n,l),(n,l,h)]:
        pair=u*v;lift=w+(N-v*w)+(N-w*u)
        common={'matrix_parameter_dimensions':[u,v],'slice_rank':w,
                'lift_rank_upper_bound':lift,'block_parameter_dimension':pair}
        if lift<a*a:return {'gate':'minimum_slice_rank','required_rank':a*a,**common}
        if lift<2*a*a and pair>a*a:
            return {'gate':'polynomial_rank_locus','required_rank':2*a*a,'dimension_cap':a*a,**common}
        for r in range(2,a):
            if 3*r<=m and lift<(r+1)*a*a and pair>r*a*a:
                return {'gate':'hankel_symbol','symbol_rank':r,'required_rank':(r+1)*a*a,
                        'dimension_cap':r*a*a,**common}
            if m==3*r-1 and lift<(r+1)*a*a and pair>max(r,4)*a*a:
                return {'gate':'first_hankel_boundary','symbol_rank':r,'required_rank':(r+1)*a*a,
                        'dimension_cap':max(r,4)*a*a,**common}
    return None


def source(a):
    N=a*a*(2*a-1);records=[];threshold=(6*a-2)**4
    for l in range(1,isqrt(N)+1):
        for h in range(l,isqrt(N)+1):
            for n in range(h,N//h+1):
                volume=l*h*n
                if 216*volume<=threshold:continue
                witness=exclusion(a,l,h,n)
                records.append({'shape':[l,h,n],'leg_dimensions':[l*h,h*n,n*l],
                                'volume':volume,'excluded':witness is not None,'witness':witness})
    return {'a':a,'source_leg_dimension':N,'source_lengths':[a,a],
            'critical_volume_comparison':{'scale':216,'strict_threshold':threshold},
            'improving_shapes':len(records),'excluded_shapes':sum(r['excluded'] for r in records),
            'survivors':[r['shape'] for r in records if not r['excluded']],'records':records}


def report():
    sources=[source(a) for a in range(2,13)]
    first_source=next(s for s in sources if s['survivors'])
    if first_source['a']!=8 or first_source['survivors']!=[[27,28,28]]:
        raise ArithmeticError('first balanced rectangular survivor changed')
    volume=27*28*28;value=216*volume
    if not value**191>46**765 or not 4*191<9*85:
        raise ArithmeticError('conditional integer exponent certificate failed')
    return {'source_range':[2,12],'ordinary_single_rectangular_blocks_only':True,
            'complete_improving_sorted_shapes':sum(s['improving_shapes'] for s in sources),
            'complete_excluded_shapes':sum(s['excluded_shapes'] for s in sources),
            'sources':sources,
            'first_balanced_survivor':{'a':8,'source_leg_dimensions':[960,960,960],
                'target_shape':[27,28,28],'target_leg_dimensions':[756,784,756],
                'volume':volume,'constructed':False,'general_degeneration_excluded':False},
            'conditional_exponent':{'numerator':191,'denominator':85,
                'premise':'An ordinary restriction, or a degeneration, from A8 to M(27,28,28) over C.',
                'integer_certificate':{'left_base':value,'left_power':191,'right_base':46,'right_power':765},
                'comparison_passes':True,'less_than_nine_fourths':True,'premise_proved':False},
            'scope':'Finite application of existing credited polynomial and Hankel theorems. Survivors are not constructions. Unbalanced sources, direct sums, tensor powers and singular degenerations are outside this exclusion scan.',
            'new_mathematical_theorem_claimed':False,'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
    write_json(args.output,report())
    print('All balanced rectangular targets checked for a2..12; first survivor A8 to M(27,28,28) is unconstructed.')
