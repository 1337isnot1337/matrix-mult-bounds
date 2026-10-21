"""Minor certificates for a specified sixteen-by-sixteen quantum block family."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

_dependency=Path(__file__).resolve().parents[1]/'2026-10-20-quantum-jet-filtration/jets.py'
_spec=importlib.util.spec_from_file_location('previous_quantum_jets',_dependency)
jets=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(jets)
one=jets.m


@lru_cache(None)
def block_maps():
    """For each chosen block b use Phi^(1[c!=b]-nu_c) on block c."""
    labels,entries=one.local_matrix(4)
    phi=one.qmod.R.from_expr(one.cyclotomic_poly(6,one.Symbol('q')))
    prime=one.PRIME;root=pow(10,(prime-1)//6,prime)
    derivative_phi=one.evaluate(phi.diff(one.qmod.q.numer),root)
    parts={};minima={}
    for key,value in entries.items():
        valuation=0;units=[]
        for sign,poly in [(1,value.numer),(-1,value.denom)]:
            while True:
                quotient,remainder=poly.div(phi)
                if remainder:break
                valuation+=sign;poly=quotient
            units.append(poly)
        numerator,denominator=units
        n=one.evaluate(numerator,root);d=one.evaluate(denominator,root)
        if not d:raise ArithmeticError('nonunit residue denominator')
        u0=n*pow(d,-1,prime)%prime
        u1=(one.evaluate(numerator.diff(one.qmod.q.numer),root)*d
            -n*one.evaluate(denominator.diff(one.qmod.q.numer),root))*pow(d,-2,prime)%prime
        block=labels[key[0]][:2]
        minima[block]=min(minima.get(block,valuation),valuation)
        parts[key]=(block,valuation,u0,u1)
    result={}
    for selected in sorted(minima):
        G={};J={};support=set()
        for key,(block,valuation,u0,u1) in parts.items():
            relative=valuation-minima[block]+int(block!=selected)
            if relative==0:
                support.add(key[0])
                if u0:G[key]=u0
                if u1:J[key]=u1
            elif relative==1:
                value=derivative_phi*u0%prime
                if value:J[key]=value
        result[selected]={'leading':G,'derivative':J,'row_support':support}
    return minima,result


def certificate(rows,size):
    row_ids,columns=one.independent_minor(rows)
    if len(row_ids)<size:raise ArithmeticError('insufficient certified rank')
    row_ids,columns=row_ids[:size],columns[:size]
    determinant=one.determinant_mod([[rows[i].get(j,0) for j in columns] for i in row_ids])
    if not determinant:raise ArithmeticError('zero selected minor')
    return {'rank_lower_bound':size,'minor_rows':row_ids,'minor_columns':columns,
            'minor_determinant_mod_prime':determinant}


def report():
    minima,data=block_maps();records=[];counts={'leading':0,'first_jet':0}
    for left,B in data.items():
        for right,C in data.items():
            sB=len(B['row_support']);sC=len(C['row_support'])
            core=one.projected_source(4,B['leading'],C['leading'])
            rank=len(one.independent_minor(core)[0])
            if rank>=15+min(sB,sC):
                witness=certificate(core,15+min(sB,sC));method='leading'
            else:
                derivative={key:value for key,value in B['derivative'].items()
                            if key[0] not in B['row_support']}
                projected=one.projected_source(4,{**B['leading'],**derivative},C['leading'])
                witness=certificate(projected,15+sB+sC);method='first_jet'
                witness['nonzero_rate_monomial_exponent']=sum(col//112 not in B['row_support']
                                                            for col in witness['minor_columns'])
            counts[method]+=1
            records.append({'left_block':list(left),'right_block':list(right),
                            'leading_row_support_upper_bounds':[sB,sC],
                            'method':method,'witness':witness,'slice_rank_upper_bound':97})
        print('Completed leading block',left,flush=True)
    return {'prime':one.PRIME,'root_order':6,'root_mod_prime':pow(10,(one.PRIME-1)//6,one.PRIME),
            'block_valuations':[{'block':list(b),'minimum':v} for b,v in sorted(minima.items())],
            'counts':counts,'records':records,
            'scope':'One chosen leading block per regular leg; every other block enters at the next Phi order. Full regular tensor limits with arbitrary Laurent remaining-leg maps. Subsequent restrictions allowed. Pre-limit output projections and general block-weight hierarchies are not included.',
            'proof_status':'Written and unreviewed; no exponent improvement.'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(report(),indent=2)+'\n')
