"""Exact controls for two Hankel Segre-image bounds; not a theorem prover."""
import argparse
import json
from functools import reduce
from pathlib import Path
import sympy as sp


def positive_partitions(total,length,minimum=1):
    if length==0:
        if total==0:yield ()
        return
    for first in range(minimum,total//length+1):
        for rest in positive_partitions(total-first,length-1,first):
            yield (first,)+rest


def alpha(d,r,mu):
    k=d-r
    return sum(max(a+b-k-1,0) for i,a in enumerate(mu) for b in mu[i:])


def symbol_cap(a,b,r):
    """The written theorem requires both strict inequalities."""
    if not (1<=r<min(a,b) and 5*r<2*(a+b)):
        return None
    t=3*r-(a+b-1);k=max(1,(t+3)//2)
    return max(r,k*k)


def general_splitting_controls():
    checked=nonzero=0;parameters=[]
    for r in range(2,21):
        for t in range(1,r):
            total=3*r+1-t;a=total//2;b=total-a
            if not (r<min(a,b) and 5*r<2*(a+b)):continue
            d=total-2;k=max(1,(t+3)//2);maximum=0
            for c in range(r):
                for p in range(2,r-c+2):
                    for mu in positive_partitions(r-c,p-1):
                        value=alpha(d,r,mu);checked+=1
                        if value:
                            nonzero+=1;ell=p+c
                            assert 2<=ell<=k
                            assert value<=t-2*ell+4
                            assert c+p*value<=k*k
                            maximum=max(maximum,c+p*value)
            parameters.append({'r':r,'t':t,'a':a,'b':b,'k':k,
                               'nonconstant_ruling_image_cap':maximum,
                               'segre_image_cap':symbol_cap(a,b,r)})
    return {'rank_range':[2,20],'splitting_cases_checked':checked,
            'positive_assignment_cases':nonzero,'parameters':parameters,
            'coverage':'All positive splitting partitions for every stated finite parameter case; the all-size claim rests on the written proof.'}


def splitting_controls():
    records=[];nonzero=[]
    for n,r in [(8,6),(9,7)]:
        d=2*n-2
        for c in range(r):
            for p in range(2,r-c+2):
                for mu in positive_partitions(r-c,p-1):
                    value=alpha(d,r,mu)
                    item={'n':n,'r':r,'d':d,'p':p,'c':c,'mu':list(mu),
                          'assignment_dimension':value,'image_dimension_upper':c+p*value}
                    records.append(item)
                    if value:
                        assert p+c<=3
                        nonzero.append(item)
    return {'all_splittings':records,'nonzero_splittings':nonzero,
            'counts':[len(records),len(nonzero)]}


def hankel(h,n):
    return sp.Matrix(n,n,lambda i,j:h[i+j])


def nonzero_minor(matrix,size):
    _,columns=matrix.rref();columns=list(columns[:size])
    if len(columns)!=size:raise ArithmeticError('rank too small')
    _,rows=matrix[:,columns].T.rref();rows=list(rows[:size])
    determinant=matrix.extract(rows,columns).det(method='domain-ge')
    if not determinant:raise ArithmeticError('zero advertised minor')
    return {'rows':rows,'columns':columns,'determinant':int(determinant)}


def annihilation(h,q):
    r=len(q)-1;d=len(h)-1
    residual=[sp.expand(sum(q[j]*h[j+k] for j in range(r+1))) for k in range(d-r+1)]
    if any(residual):raise ArithmeticError('annihilator identity failed')
    return len(residual)


def moving_three_space():
    n=8;r=6;d=14;u=sp.symbols('u0:3')
    h=[sp.Integer(0)]*(d+1);h[5]=u[2];h[10]=-u[1];h[11]=-u[0]
    q=[sp.Integer(0)]*(r+1);q[0]=u[0];q[1]=u[1];q[6]=u[2]
    equations=annihilation(h,q)
    evaluated=hankel(h,n).subs(dict(zip(u,[2,3,5])))
    assert evaluated.rank()==r
    coefficients=sp.Matrix([[sp.expand(x).coeff(v) for v in u] for x in h])
    assert coefficients.rank()==3
    # Two full-rank points have distinct, coprime minimal annihilators.
    z=sp.symbols('z');points=[[2,3,5],[3,5,7]];polys=[];minors=[]
    for point in points:
        values=dict(zip(u,point));polys.append(sum(q[k]*z**k for k in range(r+1)).subs(values))
        minors.append(nonzero_minor(hankel(h,n).subs(values),r))
    assert sp.degree(sp.gcd(*polys),z)==0
    return {'n':n,'r':r,'space_dimension':3,'moments':{str(i):str(x) for i,x in enumerate(h) if x},
            'annihilator':{str(i):str(x) for i,x in enumerate(q) if x},
            'annihilation_identities':equations,'sample_points':points,'rank_minors':minors,
            'endpoint_annihilator_gcd_degree':0,'all_parameter_rank_upper_bound':r}


def segre_control(n,r):
    d=2*n-2;k=d-r;low=range(k-r+1,r)
    u=sp.symbols('u0:2');v=sp.symbols('v0:'+str(len(low)))
    h=[sp.Integer(0)]*(d+1)
    for j,w in zip(low,v):h[j]=u[1]*w;h[j+r]=-u[0]*w
    q=[sp.Integer(0)]*(r+1);q[0]=u[0];q[r]=u[1]
    equations=annihilation(h,q)
    monomials=[x*y for x in u for y in v]
    coefficient_matrix=sp.Matrix([[sp.expand(x).coeff(m) for m in monomials] for x in h])
    dimension=coefficient_matrix.rank();assert dimension==2*len(v)
    values={**dict(zip(u,[2,3])),**dict(zip(v,range(5,5+len(v))))}
    evaluated=hankel(h,n).subs(values);assert evaluated.rank()==r
    return {'n':n,'r':r,'input_dimensions':[2,len(v)],'image_dimension':dimension,
            'moments':{str(i):str(x) for i,x in enumerate(h) if x},
            'annihilator':{str(i):str(x) for i,x in enumerate(q) if x},
            'annihilation_identities':equations,'sample_parameters':{str(a):int(b) for a,b in values.items()},
            'rank_minor':nonzero_minor(evaluated,r),'all_rank_one_inputs_have_rank_at_most':r,
            'refutes_image_dimension_at_most_r':dimension>r}


def quadratic_pencil():
    t=sp.symbols('t');h=[sp.Integer(0)]*15;h[5]=1;h[8]=t
    q=[sp.Integer(0)]*8;q[0]=t**2;q[3]=-t;q[6]=1
    equations=annihilation(h,q)
    assert reduce(sp.gcd,q)==1
    matrix=hankel(h,8);evaluated=matrix.subs(t,2);assert evaluated.rank()==7
    degrees=[sp.degree(x,t) for x in q if x];assert max(degrees)==2
    assert matrix*sp.Matrix(q)==sp.zeros(8,1)
    return {'n':8,'generic_rank':7,'moment_support':{'5':'1','8':'t'},
            'primitive_annihilator':{str(i):str(x) for i,x in enumerate(q) if x},
            'annihilator_parameter_degree':2,'annihilation_identities':equations,
            'rank_minor_at_t_two':nonzero_minor(evaluated,7),
            'index_sum_contribution':2*(8-7)*2,'index_sum_rank_upper':7,
            'refutes_unrestricted_linear_annihilator_claim':True}


def report():
    splits=splitting_controls();three=moving_three_space()
    segre=[segre_control(8,6),segre_control(9,7)];outside=quadratic_pencil()
    return {'scope':'Exact arithmetic controls for a written, unreviewed proof; not a finite proof of the general theorem.',
            'splittings':splits,'general_splitting_controls':general_splitting_controls(),'moving_three_space':three,'segre_controls':segre,
            'outside_hypothesis_quadratic_pencil':outside,'example_segre_dimension_upper':9,
            'example_formats':[[8,6],[9,7]],'independent_review':False,'improves_omega':False}


def write_json(path,data):
    """Keep complete witnesses on one line, retaining all exact data."""
    compact={'records','dimension_frontier','all_splittings','parameters'}
    def render(value,level=0,key=None):
        pad='  '*level
        if isinstance(value,dict):
            return '{\n'+',\n'.join(pad+'  '+json.dumps(k)+': '+render(v,level+1,k) for k,v in value.items())+'\n'+pad+'}'
        if isinstance(value,list):
            if key in compact:return '[\n'+',\n'.join(pad+'  '+json.dumps(v,separators=(',',':')) for v in value)+'\n'+pad+']'
            if all(not isinstance(v,(list,dict)) for v in value):return json.dumps(value)
            return '[\n'+',\n'.join(pad+'  '+render(v,level+1) for v in value)+'\n'+pad+']'
        return json.dumps(value)
    path.write_text(render(data)+'\n')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
    result=report();write_json(args.output,result)
    print('Exact splitting, moving-family, Segre and quadratic-pencil controls passed.')
