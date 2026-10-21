"""Full-coefficient ALS with dense mixing inside exact torus weight spaces.

Optional numerical discovery uses NumPy. It never reports a numerical
residual as a tensor certificate. The maintained integer verifier is separate.
"""
from itertools import product
import json
from pathlib import Path
import time

import numpy as np


def source_coordinates(a,b):
    m=a+b-1
    coords=[list(product(range(a),range(m),range(b))),
            list(product(range(b),range(a),range(m))),
            list(product(range(m),range(b),range(a)))]
    weights=[[k-i-s for i,k,s in coords[0]],
             [L-j-p for j,p,L in coords[1]],
             [H-q-r for H,q,r in coords[2]]]
    return coords,weights


def index_groups(weights):
    return {w:[i for i,x in enumerate(weights) if x==w] for w in sorted(set(weights))}


def vertex_weights(counts):
    return [w for w,c in enumerate(counts) for _ in range(c)]


class Problem:
    def __init__(self,a,b,vertices):
        self.a,self.b=a,b
        self.vertices=vertices
        self.shape=tuple(map(len,vertices))
        l,h,n=self.shape
        self.target_dims=(l*h,h*n,n*l)
        self.source_dims=(a*b*(a+b-1),)*3
        coords,sw=source_coordinates(a,b)
        u,v,w=vertices
        tw=[[x-y for x in u for y in v],
            [y-z for y in v for z in w],
            [z-x for z in w for x in u]]
        self.source_groups=list(map(index_groups,sw))
        self.target_groups=list(map(index_groups,tw))
        for axis in range(3):
            for weight,rows in self.target_groups[axis].items():
                if len(rows)>len(self.source_groups[axis].get(weight,[])):
                    raise ValueError("Target weight space exceeds source weight space")
        source_pos=[{j:(weight,i) for weight,rows in g.items() for i,j in enumerate(rows)}
                    for g in self.source_groups]
        target_pos=[{j:(weight,i) for weight,rows in g.items() for i,j in enumerate(rows)}
                    for g in self.target_groups]
        self.source={};self.target={}
        for x in self.target_groups[0]:
            for y in self.target_groups[1]:
                z=-x-y
                if z not in self.target_groups[2]:
                    continue
                weights=(x,y,z)
                self.source[weights]=np.zeros(tuple(len(self.source_groups[i][q]) for i,q in enumerate(weights)))
                self.target[weights]=np.zeros(tuple(len(self.target_groups[i][q]) for i,q in enumerate(weights)))
        m=a+b-1
        for i,j,p,q,r,s in product(range(a),range(b),range(a),range(b),range(a),range(b)):
            point=((i*m+p+q)*b+s,(j*a+p)*m+r+s,((i+j)*b+q)*a+r)
            entries=[source_pos[axis][index] for axis,index in enumerate(point)]
            weights=tuple(x[0] for x in entries)
            if weights in self.source:
                self.source[weights][tuple(x[1] for x in entries)]=1
        for i,j,k in product(range(l),range(h),range(n)):
            point=(i*h+j,j*n+k,k*l+i)
            entries=[target_pos[axis][index] for axis,index in enumerate(point)]
            weights=tuple(x[0] for x in entries)
            if sum(weights):
                raise ArithmeticError("Target does not conserve the chosen weight")
            self.target[weights][tuple(x[1] for x in entries)]=1
        self.by_axis=[{w:[key for key in self.source if key[axis]==w]
                       for w in self.target_groups[axis]} for axis in range(3)]

    def random_maps(self,seed,complex_maps=False):
        rng=np.random.default_rng(seed)
        result=[]
        for axis in range(3):
            blocks={}
            for w,rows in self.target_groups[axis].items():
                dims=(len(rows),len(self.source_groups[axis][w]))
                values=rng.normal(size=dims)
                if complex_maps:
                    values=(values+1j*rng.normal(size=dims))/np.sqrt(2)
                blocks[w]=values/np.sqrt(max(dims))
            result.append(blocks)
        return result

    def from_dense(self,matrices):
        result=[]
        for axis,matrix in enumerate(matrices):
            blocks={}
            reconstructed=np.zeros_like(matrix)
            for weight,rows in self.target_groups[axis].items():
                cols=self.source_groups[axis][weight]
                blocks[weight]=matrix[np.ix_(rows,cols)].copy()
                reconstructed[np.ix_(rows,cols)]=blocks[weight]
            if not np.array_equal(matrix,reconstructed):
                raise ArithmeticError("A supplied map mixes distinct torus weights")
            result.append(blocks)
        return result

    def dense(self,maps):
        dtype=np.result_type(*[v for blocks in maps for v in blocks.values()])
        result=[np.zeros((td,sd),dtype=dtype) for td,sd in zip(self.target_dims,self.source_dims)]
        for axis,blocks in enumerate(maps):
            for weight,block in blocks.items():
                result[axis][np.ix_(self.target_groups[axis][weight],self.source_groups[axis][weight])]=block
        return result

    def residual(self,maps):
        squared=0.0
        for key,tensor in self.source.items():
            actual=np.einsum('abc,ia,jb,kc->ijk',tensor,*[maps[i][w] for i,w in enumerate(key)],optimize=True)
            squared+=float(np.linalg.norm(actual-self.target[key])**2)
        return np.sqrt(squared/np.prod(self.shape))

    def update(self,maps,axis):
        others=[j for j in range(3) if j!=axis]
        for weight,keys in self.by_axis[axis].items():
            matrices=[];targets=[]
            for key in keys:
                tensor=np.moveaxis(self.source[key],axis,0)
                contraction=np.einsum('abc,ib,jc->aij',tensor,maps[others[0]][key[others[0]]],maps[others[1]][key[others[1]]],optimize=True)
                matrices.append(contraction.reshape(tensor.shape[0],-1))
                targets.append(np.moveaxis(self.target[key],axis,0).reshape(len(self.target_groups[axis][weight]),-1))
            matrix=np.concatenate(matrices,axis=1)
            target=np.concatenate(targets,axis=1)
            maps[axis][weight]=np.linalg.lstsq(matrix.T,target.T,rcond=1e-12)[0].T

    def normalize(self,maps):
        norms=[np.sqrt(sum(float(np.linalg.norm(v)**2) for v in axis.values())) for axis in maps]
        if min(norms)==0:
            raise ArithmeticError("An iterate lost an entire tensor leg")
        common=np.exp(np.mean(np.log(norms)))
        for axis,norm in zip(maps,norms):
            for w in axis:
                axis[w]*=common/norm

    def summary(self):
        return {"source_lengths":[self.a,self.b],"target_shape":list(self.shape),
            "source_dimensions":list(self.source_dims),"target_dimensions":list(self.target_dims),
            "vertex_weights":self.vertices,
            "source_weight_counts":[{str(k):len(v) for k,v in g.items()} for g in self.source_groups],
            "target_weight_counts":[{str(k):len(v) for k,v in g.items()} for g in self.target_groups],
            "free_map_entries":sum(len(self.target_groups[i][w])*len(self.source_groups[i][w]) for i in range(3) for w in self.target_groups[i]),
            "conserving_weight_blocks":len(self.source),
            "explicit_coefficient_count":sum(v.size for v in self.target.values()),
            "full_coefficient_count":int(np.prod(self.target_dims))}


def known_control():
    root=Path(__file__).resolve().parents[3]
    data=json.loads((root/'results/cyclic-mixed-map-2026-10-20/witness.json').read_text())
    problem=Problem(2,2,[[2,0],[1,2,0],[1,1,0,2]])
    dense=[]
    for axis,name in enumerate('ABC'):
        matrix=np.zeros((problem.target_dims[axis],12))
        for i,j,c in data['maps'][name]:
            matrix[i,j]=int(c)
        dense.append(matrix)
    maps=problem.from_dense(dense)
    if problem.residual(maps)!=0:
        raise ArithmeticError("Known integer control did not replay exactly")
    for old,new in zip(dense,problem.dense(maps)):
        if not np.array_equal(old,new):
            raise ArithmeticError("Block/dense map round trip failed")
    return problem.summary()


def natural_control(a,b):
    c=max(a,b)
    # This direct formula fixes all three a-length short coordinates to zero.
    if c!=b:
        raise ValueError("Use a<=b for this coordinate control")
    problem=Problem(a,b,[list(range(c))]*3)
    m=a+b-1;source_dimension=a*b*m
    dense=[np.zeros((c*c,source_dimension)) for _ in range(3)]
    for i,j in product(range(c),repeat=2):
        dense[0][i*c+j,i*b+j]=1
        dense[1][i*c+j,(j*a)*m+i]=1
        dense[2][i*c+j,(i*b+j)*a]=1
    maps=problem.from_dense(dense)
    if problem.residual(maps)!=0:
        raise ArithmeticError("Unequal-length coordinate control failed")
    return problem.summary()


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--starts',type=int,default=4)
    parser.add_argument('--iterations',type=int,default=200)
    parser.add_argument('--output',type=Path,default=Path('results/local/anisotropic-torus'))
    parser.add_argument('--seed',type=int,default=2026102200)
    parser.add_argument('--complex',action='store_true')
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    controls=[known_control(),natural_control(2,3)]
    vertices=[vertex_weights(x) for x in ((1,1,2,2,2,2,1,1),(1,1,2,2,2,2,1,1),(1,2,2,1,2,2,2,1))]
    problem=Problem(4,5,vertices)
    print(json.dumps(problem.summary()),flush=True)
    best=float('inf');records=[];started=time.monotonic()
    for trial in range(args.starts):
        seed=args.seed+trial
        maps=problem.random_maps(seed,args.complex)
        trajectory=[]
        for iteration in range(args.iterations):
            for axis in range(3):
                problem.update(maps,axis)
            problem.normalize(maps)
            if iteration%10==0 or iteration+1==args.iterations:
                error=problem.residual(maps)
                trajectory.append([iteration+1,float(error)])
                if error<best:
                    best=error
                    matrices=problem.dense(maps)
                    np.savez_compressed(args.output/'best.npz',A=matrices[0],B=matrices[1],C=matrices[2],error=error,seed=seed,iteration=iteration+1)
                print('trial',trial,'iteration',iteration+1,'full_relative_error',float(error),'best',float(best),'seconds',time.monotonic()-started,flush=True)
                if error<1e-11:
                    break
        records.append({'seed':seed,'iterations':iteration+1,'full_relative_error':float(error),
                        'trajectory':trajectory,'map_norms':[float(np.linalg.norm(x)) for x in problem.dense(maps)]})
        report={**problem.summary(),'controls':controls,'starts_completed':len(records),
                'maximum_iterations':args.iterations,'complex_maps':args.complex,
                'best_full_relative_error':float(best),'records':records,
                'exact_witness_found':False,'exclusion_proved':False,'new_exponent_established':False}
        (args.output/'report.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
