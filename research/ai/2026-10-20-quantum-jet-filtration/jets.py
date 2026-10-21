"""Exact first-jet minors for ungraded quantum-curve obstructions."""
from functools import lru_cache
import importlib.util,json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'2026-10-20-graded-quantum-flags/one_leg.py';s=importlib.util.spec_from_file_location('one',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

@lru_cache(None)
def first_jet(a,order,power=1):
 labels,entries=m.local_matrix(a);_,phi,minimum,_=m.leading_parts(a,order);prime=m.PRIME;root=pow(10,(prime-1)//order*power,prime);derphi=m.evaluate(phi.diff(m.qmod.q.numer),root);result={}
 for key,value in entries.items():
  valuation=0;parts=[]
  for sign,poly in [(1,value.numer),(-1,value.denom)]:
   while True:
    quo,rem=poly.div(phi)
    if rem:break
    valuation+=sign;poly=quo
   parts.append(poly)
  relative=valuation-minimum
  if relative>1:continue
  N,D=parts;num=m.evaluate(N,root);den=m.evaluate(D,root);assert den
  if relative==1:v=derphi*num*pow(den,-1,prime)%prime
  else:
   assert relative==0
   v=(m.evaluate(N.diff(m.qmod.q.numer),root)*den-num*m.evaluate(D.diff(m.qmod.q.numer),root))*pow(den,-2,prime)%prime
  if v:result[key]=v
 return result


def report():
    phases=[(6,1),(3,1),(3,2),(6,5)];records=[]
    for left in phases:
        left_meta,B0=m.root_map(4,*left);left_rows=set(left_meta['row_labels'])
        B1={key:value for key,value in first_jet(4,*left).items() if key[0] not in left_rows}
        for right in phases:
            right_meta,C0=m.root_map(4,*right);right_rows=set(right_meta['row_labels'])
            C1={key:value for key,value in first_jet(4,*right).items() if key[0] not in right_rows}
            for side in ['left','right']:
                B={**B0,**B1} if side=='left' else B0
                C={**C0,**C1} if side=='right' else C0
                rows=m.projected_source(4,B,C);row_ids,columns=m.independent_minor(rows)
                minor=[[rows[i].get(j,0) for j in columns] for i in row_ids]
                determinant=m.determinant_mod(minor)
                if not determinant:raise ArithmeticError('zero first-jet minor')
                rate_columns=sum((col//112 not in left_rows) if side=='left' else (col%112 not in right_rows) for col in columns)
                record={'left_phase':list(left),'right_phase':list(right),'varying_leg':side,
                        'partial_saturation_rank_lower_bound':len(row_ids),'minor_rows':row_ids,'minor_columns':columns,
                        'minor_determinant_mod_prime':determinant,'nonzero_rate_monomial_exponent':rate_columns,
                        'leading_row_support_upper_bounds':[len(left_rows),len(right_rows)],
                        'slice_rank_upper_bound':112-len(row_ids)+len(left_rows)+len(right_rows)}
                inactive=sorted(right_rows if side=='left' else left_rows)
                labels,_=m.local_matrix(4)
                slice_minors=[]
                for coordinate in inactive:
                    sliced=[{(col//112 if side=='left' else col%112):value
                             for col,value in row.items()
                             if (col%112 if side=='left' else col//112)==coordinate}
                            for row in rows]
                    rr,cc=m.independent_minor(sliced)
                    if len(rr)<28:raise ArithmeticError('insufficient inactive-slice rank')
                    rr,cc=rr[:28],cc[:28]
                    det=m.determinant_mod([[sliced[i].get(j,0) for j in cc] for i in rr])
                    if not det:raise ArithmeticError('zero inactive-slice minor')
                    outside=left_rows if side=='left' else right_rows
                    slice_minors.append({'inactive_coordinate':coordinate,'inactive_grade':sum(labels[coordinate]),
                                         'rank_lower_bound':28,'minor_rows':rr,'minor_columns':cc,
                                         'minor_determinant_mod_prime':det,
                                         'nonzero_rate_monomial_exponent':sum(j not in outside for j in cc)})
                record['inactive_slice_minors']=slice_minors
                record['uniform_nonzero_inactive_slice_rank_lower_bound']=28
                record['slice_ceiling_after_constant_output_codimensions_at_most_two']=94
                records.append(record)
                print(left,right,side,'rank lower',len(row_ids),'slice ceiling',record['slice_rank_upper_bound'],flush=True)
    leading=[]
    for phase in phases:
        meta,G=m.root_map(4,*phase);matrix=[{} for _ in range(112)]
        for (i,j),value in G.items():matrix[i][j]=value
        rr,cc=m.independent_minor(matrix)
        if len(rr)!=4:raise ArithmeticError('leading map rank is not four')
        leading.append({'phase':list(phase),'minor_rows':rr,'minor_columns':cc,
                        'minor_determinant_mod_prime':m.determinant_mod([[matrix[i].get(j,0) for j in cc] for i in rr]),
                        'rank_lower_bound':4,'row_support_upper_bound':meta['nonzero_rows_over_number_field']})
    return {'source':'A4','source_first_dimension':112,'prime':m.PRIME,'leading_rank_controls':leading,'records':records,
            'scope':'Specified root-curve first derivatives on one regular leg; arbitrary first/higher jets on the other, arbitrary higher jets after the specified derivative, and arbitrary Laurent first-leg maps. The monomial minor covers every nonzero scalar rate.',
            'proof_status':'Written and unreviewed; requires the partial-saturation argument. No exponent improvement.'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(report(),indent=2)+'\n')
