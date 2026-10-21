"""Optional bounded full-flag search with explicit operator moment penalties.

This discovery script never accepts numerical coefficients as a proof.
Each map is parameterized in the open Frobenius ball of the declared radius.
"""
import argparse
from itertools import product
import json
from pathlib import Path
import time
import numpy as np
from scipy.optimize import minimize


def operator(t):
    return t.reshape(5,5,5,4,4,5).transpose(0,3,5,2,4,1).reshape(100,100)


def tensor(e):
    return e.reshape(5,4,5,5,4,5).transpose(0,5,3,1,4,2).reshape(25,20,20)


class Objective:
    shapes=[(25,36),(20,36),(20,36)]
    sizes=[900,720,720]
    total=2340

    def __init__(self,powers,radius,moment_weights):
        self.radius=radius
        self.moment_weights=np.array(moment_weights)
        self.powers=[np.array(w) for w in powers]
        self.degree=self.powers[0][:,None,None]+self.powers[1][None,:,None]+self.powers[2][None,None,:]
        self.mask=self.degree<=0
        self.source=np.zeros((36,36,36))
        for p,q,y,v in product(range(6),range(6),range(4),range(4)):
            self.source[6*p+q,9*y+q+v,4*(p+y)+v]=1
        self.target=np.zeros((25,20,20))
        for i,j,k in product(range(5),range(4),range(5)):
            self.target[5*i+k,4*i+j,5*j+k]=1
        assert np.count_nonzero(self.mask)==5050
        assert not np.any(self.target[self.degree!=0])
        self.layouts=[(axis,[j for j in range(3) if j!=axis]) for axis in range(3)]
        self.calls=0
        self.cached_x=None

    def encode(self,maps):
        zs=[]
        for m in maps:
            norm2=float(np.vdot(m,m).real)
            if norm2>=self.radius**2:
                raise ValueError('The initial maps must lie strictly within the norm budget.')
            zs.append((m/np.sqrt(self.radius**2-norm2)).ravel())
        z=np.concatenate(zs)
        return np.concatenate([z.real,z.imag])

    def decode(self,x):
        z=x[:self.total]+1j*x[self.total:]
        zs=[]; maps=[]; scales=[];start=0
        for shape,size in zip(self.shapes,self.sizes):
            piece=z[start:start+size].reshape(shape)
            scale=np.sqrt(1+float(np.vdot(piece,piece).real))
            zs.append(piece);scales.append(scale)
            maps.append(self.radius*piece/scale)
            start+=size
        return maps,zs,scales

    def __call__(self,x):
        if self.cached_x is not None and np.array_equal(x,self.cached_x):
            return self.cached_f,self.cached_g
        self.calls+=1
        maps,zs,scales=self.decode(x)
        envs=[]
        for axis,other in self.layouts:
            env=np.einsum('jt,ku,stu->sjk',maps[other[0]],maps[other[1]],
                          np.transpose(self.source,(axis,*other)),optimize=True).reshape(36,-1)
            envs.append(env)
        actual=(maps[0]@envs[0]).reshape(25,20,20)
        error=actual-self.target
        required=np.where(self.mask,error,0)
        e=operator(error)
        e2=e@e
        moments=np.array([np.trace(e),np.trace(e2),np.trace(e2@e)])
        coefficient_objective=float(np.vdot(required,required).real)
        moment_objective=float(np.sum(self.moment_weights*np.abs(moments)**2))
        objective=coefficient_objective+moment_objective
        ge=(self.moment_weights[0]*moments[0]*np.eye(100)
            +2*self.moment_weights[1]*moments[1]*e.conj().T
            +3*self.moment_weights[2]*moments[2]*e2.conj().T)
        gt=required+tensor(ge)
        gradients=[]
        for (axis,other),env,z,scale in zip(self.layouts,envs,zs,scales):
            gm=np.transpose(gt,(axis,*other)).reshape(self.shapes[axis][0],-1)@env.conj().T
            radial=float(np.vdot(gm,z).real)
            gz=self.radius/scale*(gm-z*radial/scale**2)
            gradients.append(gz.ravel())
        g=np.concatenate(gradients)
        packed=2*np.concatenate([g.real,g.imag])
        self.cached_x=x.copy();self.cached_f=objective;self.cached_g=packed
        self.cached_data={'maps':maps,'error':error,'operator_error':e,'moments':moments,
                          'coefficient_objective':coefficient_objective,'moment_objective':moment_objective}
        return objective,packed

    def metrics(self,x,with_spectrum=False):
        objective,grad=self(x)
        data=self.cached_data;err=data['error'];maps=data['maps']
        result={'objective':objective,'coefficient_objective':data['coefficient_objective'],
                'moment_objective':data['moment_objective'],
                'relative_nonpositive_coefficient_error':float(np.sqrt(data['coefficient_objective'])/10),
                'negative_coefficient_norm':float(np.linalg.norm(err[self.degree<0])),
                'constant_coefficient_error_norm':float(np.linalg.norm(err[self.degree==0])),
                'maximum_nonpositive_error':float(np.max(np.abs(err[self.mask]))),
                'positive_coefficient_norm':float(np.linalg.norm(err[self.degree>0])),
                'absolute_traces_powers_1_2_3':np.abs(data['moments']).tolist(),
                'traces_real':data['moments'].real.tolist(),'traces_imag':data['moments'].imag.tolist(),
                'map_norms':[float(np.linalg.norm(m)) for m in maps],
                'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],
                'gradient_norm':float(np.linalg.norm(grad)),'objective_evaluations':self.calls}
        if with_spectrum:
            result['operator_error_spectral_radius']=float(np.max(abs(np.linalg.eigvals(data['operator_error']))))
        return result


def gradient_control(obj,x):
    rng=np.random.default_rng(202610446)
    f,g=obj(x)
    checks=[]
    for _ in range(3):
        v=rng.normal(size=x.shape);v/=np.linalg.norm(v)
        exact=float(g@v)
        step=1e-7
        numerical=(obj(x+step*v)[0]-obj(x-step*v)[0])/(2*step)
        discrepancy=abs(exact-numerical)/max(1,abs(exact),abs(numerical))
        checks.append({'analytic_directional_derivative':exact,'central_difference':numerical,
                       'relative_discrepancy':discrepancy,'step':step})
        if discrepancy>2e-4:
            raise ArithmeticError('The complete complex and ball-parameter gradient check failed.')
    obj(x)
    return {'checks':checks,'gradient_control_passes':True,'is_exact_mathematical_certificate':False}


def run(initial,radius,weights,iterations,evaluations,checkpoint,control_output):
    point=json.loads(initial.read_text())
    maps=[np.array(r)+1j*np.array(i) for r,i in zip(point['maps_real'],point['maps_imag'])]
    obj=Objective(point['map_row_powers'],radius,weights)
    start=obj.encode(maps)
    control=gradient_control(obj,start)
    control_output.write_text(json.dumps(control,indent=2)+'\n')
    obj.calls=0
    history=[]; best=float('inf'); accepted=0;started=time.monotonic()

    def record(x,force=False):
        nonlocal best
        row={'accepted_iteration':accepted,**obj.metrics(x,with_spectrum=True),'elapsed_seconds':time.monotonic()-started}
        if force or accepted%10==0:
            history.append(row);print(json.dumps(row),flush=True)
        if row['objective']<best:
            best=row['objective'];ms=obj.cached_data['maps']
            checkpoint.write_text(json.dumps({'n':6,'b':4,'target_outer':5,'auxiliary_rank':0,
                'method':'Full-flag coefficient and first three operator moments; analytic-gradient L-BFGS',
                'map_row_powers':point['map_row_powers'],'norm_budget':radius,
                'trace_penalty_weights':weights,'accepted_iteration':accepted,
                'maps_real':[m.real.tolist() for m in ms],'maps_imag':[m.imag.tolist() for m in ms],
                **row,'exact_coefficient_certificate':False},separators=(',',':'))+'\n')

    record(start,True)
    def callback(x):
        nonlocal accepted
        accepted+=1
        record(x)
    result=minimize(obj,start,method='L-BFGS-B',jac=True,callback=callback,
                    options={'maxiter':iterations,'maxfun':evaluations,'maxls':40,'maxcor':20,'ftol':1e-15,'gtol':1e-8})
    record(result.x,True)
    return {'source':'Q(6,4)','target':'M(5,4,5)','auxiliary_rank':0,'norm_budget':radius,
            'moment_weights':weights,'maximum_accepted_iterations':iterations,'maximum_function_evaluations':evaluations,
            'accepted_iterations_completed':int(result.nit),'function_evaluations':int(result.nfev),
            'optimizer_success':bool(result.success),'optimizer_status':int(result.status),'optimizer_message':str(result.message),
            'best_combined_objective':best,'history':history,'gradient_control':control,
            'exact_coefficient_certificate':False,'degeneration_proved':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--initial',type=Path,required=True)
    parser.add_argument('--norm-budget',type=float,default=40)
    parser.add_argument('--moment-weights',type=float,nargs=3,default=[1,0.1,0.01])
    parser.add_argument('--iterations',type=int,default=600)
    parser.add_argument('--evaluations',type=int,default=1500)
    parser.add_argument('--check-gradient-only',action='store_true')
    parser.add_argument('--checkpoint',type=Path)
    parser.add_argument('--control-output',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.check_gradient_only:
        point=json.loads(args.initial.read_text())
        maps=[np.array(r)+1j*np.array(i) for r,i in zip(point['maps_real'],point['maps_imag'])]
        objective=Objective(point['map_row_powers'],args.norm_budget,args.moment_weights)
        result=gradient_control(objective,objective.encode(maps))
        if args.control_output:args.control_output.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result,indent=2))
    else:
        if not all([args.checkpoint,args.control_output,args.output]):
            parser.error('A search requires --checkpoint, --control-output, and --output.')
        result=run(args.initial,args.norm_budget,args.moment_weights,args.iterations,args.evaluations,args.checkpoint,args.control_output)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({key:value for key,value in result.items() if key not in ['history','gradient_control']},indent=2))
