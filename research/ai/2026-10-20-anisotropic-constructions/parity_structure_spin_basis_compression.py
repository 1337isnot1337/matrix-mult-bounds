"""Discovery outside the fixed weighted spin/radix family.

Each local convolution factor receives its own SL2 change of basis before
two-digit radix compression. NumPy/SciPy are optional discovery dependencies.
No numerical residual is accepted as an exact matrix tensor identity.
"""

from itertools import product
import argparse
import json
from pathlib import Path
import sys
import time

import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from spin_fiber_compression import LOCAL


ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'results/anisotropic-constructions-2026-10-20'
PREFIX='parity_structure_spin_basis_compression'
J=np.array(LOCAL,dtype=float)/2
ROW=np.array([[9*(rl//3+3*(rh//3))+rl%3+3*(rh%3) for rh in range(9)] for rl in range(9)])
FIBER=np.zeros((12,12),dtype=int)
for lo,hi in product(range(12),repeat=2):
    i0,t=divmod(lo,6);m0,s0=divmod(t,2)
    i1,t=divmod(hi,6);m1,s1=divmod(t,2)
    FIBER[lo,hi]=((i0+2*i1)*7+m0+2*m1)*4+s0+2*s1
PHYSICAL=np.array([[(i*7+p+q)*4+s for p,s in product(range(4),repeat=2)]
                   for i,q in product(range(4),repeat=2)])
TARGET=np.zeros((81,81,81))
for i,j,k in product(range(9),repeat=3):TARGET[9*i+j,9*j+k,9*k+i]=1
LOCAL_PHYSICAL=np.zeros((12,4,4))
for c in range(12):
    for i,q,p,s in product(range(2),repeat=4):
        LOCAL_PHYSICAL[c,2*i+q,2*p+s]=int(c==(i*3+p+q)*2+s)
QUOTIENT_GAUGE=np.array([[1,0,0],[0,0,-.5],[0,1,0]])


def symmetric_square(g):
    a,b,c,d=g.ravel()
    return np.array([[a*a,a*b,b*b],[2*a*c,a*d+b*c,2*b*d],[c*c,c*d,d*d]])


def symmetric_derivative(g,h):
    a,b,c,d=g.ravel();aa,bb,cc,dd=h.ravel()
    return np.array([[2*a*aa,aa*b+a*bb,2*b*bb],
                     [2*(aa*c+a*cc),aa*d+a*dd+bb*c+b*cc,2*(bb*d+b*dd)],
                     [2*c*cc,cc*d+c*dd,2*d*dd]])


def gauss(parameters):
    u,v,t=parameters;e=np.exp(t);f=np.exp(-t)
    g=np.array([[e,e*u],[e*v,e*u*v+f]])
    derivatives=[np.array([[0,e],[0,e*v]]),np.array([[0,0],[e,e*u]]),
                 np.array([[e,e*u],[e*v,e*u*v-f]])]
    return g,derivatives


def transformed_local(matrices):
    dual=[np.linalg.inv(symmetric_square(g)).T for g in matrices]
    actions=[np.kron(np.kron(matrices[(leg+2)%3],dual[leg]),matrices[(leg+1)%3]) for leg in range(3)]
    return [J@action.T for action in actions]


def local_maps(parameters,derivatives=False):
    parameters=np.asarray(parameters).reshape(2,3,3)
    maps=[];jac=[]
    for bit in range(2):
        decomposed=[gauss(p) for p in parameters[bit]]
        g=[v[0] for v in decomposed]
        dg=[v[1] for v in decomposed]
        h=[np.linalg.inv(symmetric_square(v)).T for v in g]
        block=[];dblock=np.zeros((9,3,9,12))
        for leg in range(3):
            factors=[g[(leg+2)%3],h[leg],g[(leg+1)%3]]
            block.append(J@np.kron(np.kron(*factors[:2]),factors[2]).T)
            if derivatives:
                for edge,parameter in product(range(3),range(3)):
                    dh=-h[edge]@symmetric_derivative(g[edge],dg[edge][parameter]).T@h[edge]
                    altered=factors.copy()
                    if edge==(leg+2)%3:altered[0]=dg[edge][parameter]
                    elif edge==leg:altered[1]=dh
                    else:altered[2]=dg[edge][parameter]
                    dblock[3*edge+parameter,leg]=J@np.kron(np.kron(*altered[:2]),altered[2]).T
        maps.append(block);jac.append(dblock)
    return maps,jac


def quotient_maps(parameters,derivatives=False):
    """Move all three local quotient kernels; the local scalar defect may change."""
    parameters=np.asarray(parameters).reshape(2,3,3)
    result=[];jac=[]
    for bit in range(2):
        projections=[];changes=[]
        for x,y,t in parameters[bit]:
            delta=np.exp(t);z=x*y+delta
            p=QUOTIENT_GAUGE@np.array([[-x,1,0,0],[-y,0,1,0],[-z,0,0,1]])
            dp=[]
            for row in ([-1,0,-y],[0,-1,-x],[0,0,-delta]):
                d=np.zeros((3,4));d[:,0]=row;dp.append(QUOTIENT_GAUGE@d)
            projections.append(p);changes.append(dp)
        block=[];derivative=np.zeros((9,3,9,12))
        for leg in range(3):
            output,following=leg,(leg+1)%3
            system=np.einsum('ab,cbk->cak',projections[output],LOCAL_PHYSICAL).reshape(12,12).T
            inverse=np.linalg.inv(system)
            rhs=np.zeros((9,3,4))
            for i,j in product(range(3),repeat=2):rhs[3*i+j,i]=projections[following][j]
            matrix=rhs.reshape(9,12)@inverse.T
            block.append(matrix)
            if derivatives:
                for vertex,parameter in product(range(3),range(3)):
                    right=np.zeros((9,12))
                    if vertex==following:
                        dr=np.zeros((9,3,4))
                        for i,j in product(range(3),repeat=2):dr[3*i+j,i]=changes[vertex][parameter][j]
                        right+=dr.reshape(9,12)
                    if vertex==output:
                        ds=np.einsum('ab,cbk->cak',changes[vertex][parameter],LOCAL_PHYSICAL).reshape(12,12).T
                        right-=matrix@ds.T
                    derivative[3*vertex+parameter,leg]=right@inverse.T
        result.append(block);jac.append(derivative)
    return result,jac


def compress(local,weights=None):
    weights=np.ones((3,12,12)) if weights is None else weights
    maps=[]
    for leg in range(3):
        raw=np.einsum('ac,bd->abcd',local[0][leg],local[1][leg])*weights[leg][None,None,:,:]
        m=np.zeros((81,112),dtype=raw.dtype)
        np.add.at(m,(ROW[:,:,None,None],FIBER[None,None,:,:]),raw)
        maps.append(m)
    return maps


def physical_products(a,b):
    return np.einsum('aij,bjk->abik',a,b,optimize=True)


def coefficient(maps):
    w=[m[:,PHYSICAL] for m in maps]
    c=physical_products(w[0],w[1]).reshape(81*81,256)@w[2].transpose(0,2,1).reshape(81,256).T
    return c.reshape(81,81,81),w


def objective(parameters,gradient=True,raw_weights=False,fit_scale=False,quotient_kernels=False):
    factory=quotient_maps if quotient_kernels else local_maps
    local,jac=factory(parameters[:18],gradient)
    weights=np.asarray(parameters[18:]).reshape(3,12,12) if raw_weights else np.ones((3,12,12))
    maps=compress(local,weights)
    actual,w=coefficient(maps)
    gain=float(np.vdot(actual,TARGET).real/np.vdot(actual,actual).real) if fit_scale else 1.
    actual=gain*actual
    residual=actual-TARGET
    value=np.vdot(residual,residual).real/(2*729)
    if not gradient:return value,[gain*maps[0],maps[1],maps[2]],actual
    residual=gain*residual
    map_grad=[]
    for leg in range(3):
        cyclic=(leg,(leg+1)%3,(leg+2)%3)
        pair=physical_products(w[cyclic[1]],w[cyclic[2]])
        gw=(residual.transpose(cyclic).reshape(81,81*81)
            @pair.transpose(0,1,3,2).reshape(81*81,256)).reshape(81,16,16)/729
        gm=np.zeros((81,112))
        np.add.at(gm,(np.arange(81)[:,None],PHYSICAL.reshape(1,256)),gw.reshape(81,256))
        map_grad.append(gm)
    local_grad=np.zeros((2,3,9,12))
    weight_grad=np.zeros((3,12,12))
    for leg in range(3):
        raw=map_grad[leg][ROW[:,:,None,None],FIBER[None,None,:,:]]
        weight_grad[leg]=np.einsum('abcd,ac,bd->cd',raw,local[0][leg],local[1][leg])
        weighted=raw*weights[leg][None,None,:,:]
        local_grad[0,leg]=np.einsum('abcd,bd->ac',weighted,local[1][leg])
        local_grad[1,leg]=np.einsum('abcd,ac->bd',weighted,local[0][leg])
    answer=np.array([np.einsum('plrc,lrc->p',jac[bit],local_grad[bit]) for bit in range(2)]).ravel()
    if raw_weights:answer=np.concatenate([answer,weight_grad.ravel()])
    return value,answer


def local_control():
    matrices=[np.array([[1,1],[0,1]],dtype=float),np.array([[1,0],[-1,1]],dtype=float),np.array([[0,1],[-1,0]],dtype=float)]
    maps=transformed_local(matrices)
    numerators=[np.rint(2*m).astype(np.int64) for m in maps]
    if any(not np.array_equal(2*m,n) for m,n in zip(maps,numerators)):
        raise ArithmeticError('Integral local basis control was not integral')
    actual=np.zeros((9,9,9),dtype=np.int64)
    for i,p,r,j,q,s in product(range(2),repeat=6):
        x=(i*3+p+q)*2+s;y=(p*3+r+s)*2+j;z=(r*3+i+j)*2+q
        actual+=np.einsum('a,b,c->abc',numerators[0][:,x],numerators[1][:,y],numerators[2][:,z])
    expected=np.zeros_like(actual)
    for i,j,k in product(range(3),repeat=3):expected[3*i+j,3*j+k,3*k+i]+=8
    for i,j,k in product(range(3),repeat=3):expected[4*i,4*j,4*k]+=8
    if not np.array_equal(actual,expected):raise ArithmeticError('The local source automorphism failed')
    local=[maps,[J,J,J]]
    full=compress(local)
    num=[np.rint(4*m).astype(np.int64) for m in full]
    points=[(0,1,39),(30,31,39),(30,31,69)]
    coefficients=[]
    for point in points:
        total=0
        for i,p,r,j,q,s in product(range(4),repeat=6):
            x=(i*7+p+q)*4+s;y=(p*7+r+s)*4+j;z=(r*7+i+j)*4+q
            total+=int(num[0][point[0],x])*int(num[1][point[1],y])*int(num[2][point[2],z])
        coefficients.append(total)
    return {'local_source_terms':64,'local_coefficients_checked':729,
            'local_target':'M3 plus tr(X)tr(Y)tr(Z)','local_identity_exact':True,
            'two_digit_source_terms_per_selected_coefficient':4096,
            'closure124_selected_points':points,'selected_coefficient_numerators_over64':coefficients,
            'closure124_linear_combination_numerator':coefficients[0]-coefficients[1]+coefficients[2]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--steps',type=int,default=0)
    parser.add_argument('--seed',type=int,default=183)
    parser.add_argument('--raw-weights',action='store_true')
    parser.add_argument('--fit-scale',action='store_true')
    parser.add_argument('--quotient-kernels',action='store_true')
    args=parser.parse_args()
    control=local_control()
    rng=np.random.default_rng(args.seed)
    probe=.07*rng.normal(size=18)
    if args.raw_weights:probe=np.concatenate([probe,1+.01*rng.normal(size=432)])
    if args.quotient_kernels:
        base,_=quotient_maps(np.zeros(18))
        if max(np.max(np.abs(m-J)) for bit in base for m in bit)>1e-12:
            raise ArithmeticError('The moving quotient chart misses the saved exact spin map')
    evaluate=lambda x,gradient=True:objective(x,gradient,args.raw_weights,args.fit_scale,args.quotient_kernels)
    value,grad=evaluate(probe)
    indices=[0,4,8,13,17];checks=[]
    if args.raw_weights:indices += [18,198,449]
    for i in indices:
        d=np.zeros(len(probe));d[i]=1e-6
        fd=(evaluate(probe+d,False)[0]-evaluate(probe-d,False)[0])/(2e-6)
        checks.append({'index':i,'analytic':float(grad[i]),'finite_difference':float(fd),'error':float(abs(fd-grad[i]))})
    if max(v['error'] for v in checks)>2e-5*max(1.,np.linalg.norm(grad)):
        raise ArithmeticError('The parameter gradient control failed')
    report={'chart':('Two digits, three independent local quotient kernels per digit' if args.quotient_kernels
                     else 'Two digits, three independent SL2 source factors per digit, Gauss coordinates'),
            'source':'A(4,4)','target':'M9','parameters':len(probe),'seed':args.seed,
            'all_raw_column_weights':args.raw_weights,'optimal_overall_output_scalar':args.fit_scale,
            'control':control,'gradient_controls':checks,'initial_relative_residual':float((2*value)**.5),
            'new_exponent_established':False,'exact_M9_constructed':False,'trajectory':[]}
    print(json.dumps({k:v for k,v in report.items() if k!='trajectory'}),flush=True)
    best=(value,probe.copy());counter=0;start=time.monotonic()
    def fg(x):
        nonlocal best
        f,g=evaluate(x)
        if f<best[0]:best=(f,x.copy())
        return f,g
    def callback(x):
        nonlocal counter
        counter+=1
        if counter%5==0:
            f,maps,_=evaluate(x,False)
            row={'iteration':counter,'relative_residual':float((2*f)**.5),
                 'map_norms':[float(np.linalg.norm(m)) for m in maps],
                 'smallest_map_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],
                 'max_parameter':float(np.max(np.abs(x))),'elapsed_seconds':time.monotonic()-start}
            report['trajectory'].append(row);print(json.dumps(row),flush=True)
    if args.steps:
        from scipy.optimize import minimize
        bounds=[(-4,4),(-4,4),(-2,2)]*6
        if args.raw_weights:bounds += [(-4,4)]*432
        result=minimize(fg,probe,jac=True,method='L-BFGS-B',bounds=bounds,
                        options={'maxiter':args.steps,'ftol':1e-13,'gtol':1e-9,'maxls':20},callback=callback)
        report['optimizer_message']=str(result.message);report['completed_iterations']=int(result.nit)
    f,maps,actual=evaluate(best[1],False)
    report.update({'best_relative_residual':float((2*f)**.5),
                   'best_parameters':best[1].tolist(),'full_target_coefficients_evaluated':81**3,
                   'best_map_norms':[float(np.linalg.norm(m)) for m in maps],
                   'best_smallest_map_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps]})
    OUT.mkdir(parents=True,exist_ok=True)
    suffix=('_quotient' if args.quotient_kernels else '')+('_weighted' if args.raw_weights else '')+('_scaled' if args.fit_scale else '')+f'_seed{args.seed}'
    path=OUT/(PREFIX+suffix+'.json');path.write_text(json.dumps(report,indent=2)+'\n')
    np.savez(OUT/(PREFIX+suffix+'.npz'),parameters=best[1],X=maps[0],Y=maps[1],Z=maps[2])
    print(json.dumps({'best_relative_residual':report['best_relative_residual'],'report':str(path)}),flush=True)


if __name__=='__main__':main()
