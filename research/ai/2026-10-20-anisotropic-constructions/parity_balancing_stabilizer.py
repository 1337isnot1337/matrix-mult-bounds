"""Exact fixed-seed obstruction for target-stabilizer singular scaling.

The stored binary64 maps are interpreted as exact dyadic complex numbers.
Reduction modulo a prime with i^2=-1 certifies a nonzero polynomial
invariant. It excludes only scaling this fixed seed to the target;
changing the source maps remains outside the claim.
"""

import argparse
import hashlib
import io
from itertools import product
import json
from math import isqrt
from pathlib import Path

import numpy as np

from parity_balancing_spin1_verify import source_points


def scalar_mul(a,b,prime):
    return ((a[0]*b[0]-a[1]*b[1])%prime,(a[0]*b[1]+a[1]*b[0])%prime)


def modular_matrix(matrix,prime):
    real,imag=np.empty(matrix.shape,dtype=np.int64),np.empty(matrix.shape,dtype=np.int64)
    for index in np.ndindex(matrix.shape):
        z=complex(matrix[index])
        for component,out in [(z.real,real),(z.imag,imag)]:
            numerator,denominator=float(component).as_integer_ratio()
            out[index]=(numerator%prime)*pow(denominator,-1,prime)%prime
    return real,imag


def multiply(left,right,prime):
    ar,ai=left;br,bi=right
    if 2*ar.shape[-1]*(prime-1)**2>=2**63:
        raise ArithmeticError('The modular integer product would exceed int64 range')
    return ((ar@br-ai@bi)%prime,(ar@bi+ai@br)%prime)


def operator_modulo(a,b,n,maps,prime):
    dimension=a*b*(a+b-1)
    d=n*n
    if any(matrix.shape!=(d,dimension) for matrix in maps):
        raise ValueError('Unexpected map dimensions')
    matrices=[modular_matrix(matrix,prime) for matrix in maps]
    groups=[[] for _ in range(dimension)]
    points=source_points(a,b)
    for x,y,z in points:
        groups[x].append((y,z))
    contractions=[np.empty((dimension,d*d),dtype=np.int64) for _ in range(2)]
    for x,pairs in enumerate(groups):
        ys,zs=map(list,zip(*pairs))
        left=(matrices[1][0][:,ys],matrices[1][1][:,ys])
        right=(matrices[2][0][:,zs].T,matrices[2][1][:,zs].T)
        values=multiply(left,right,prime)
        for component in range(2):
            contractions[component][x]=values[component].ravel()
    actual=multiply(matrices[0],contractions,prime)
    return tuple(part.reshape((n,)*6).transpose(0,2,4,5,1,3).reshape(n**3,n**3)
                 for part in actual),len(points)


def invariant(operator,prime):
    real,imag=operator
    size=len(real)
    if 2*size*size*(prime-1)**2>=2**63:
        raise ArithmeticError('The modular trace would exceed int64 range')
    trace=(int(np.trace(real))%prime,int(np.trace(imag))%prime)
    trace_square=(int(np.sum(real*real.T-imag*imag.T))%prime,
                  int(np.sum(real*imag.T+imag*real.T))%prime)
    squared_trace=scalar_mul(trace,trace,prime)
    value=((size*trace_square[0]-squared_trace[0])%prime,
           (size*trace_square[1]-squared_trace[1])%prime)
    return {'operator_size':size,'trace_mod_prime':list(trace),
            'trace_square_mod_prime':list(trace_square),
            'N_trace_O_squared_minus_trace_O_squared':list(value),
            'nonzero':value!=(0,0)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a',type=int,default=3)
    parser.add_argument('--b',type=int,default=3)
    parser.add_argument('--size',type=int,default=5)
    parser.add_argument('--initial',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--export-coordinates',type=Path)
    parser.add_argument('--prime',type=int,default=65519)
    args=parser.parse_args()
    p=args.prime
    if p%4!=3 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise ValueError('Use a prime congruent to3 modulo4')
    content=args.initial.read_bytes()
    with np.load(io.BytesIO(content)) as file:
        maps=[file[name].copy() for name in 'ABC']
    operator,count=operator_modulo(args.a,args.b,args.size,maps,p)
    result=invariant(operator,p)
    if not result['nonzero']:
        raise ArithmeticError('This prime does not certify a nonzero invariant')
    # The entire exact quotient control has reshuffled operator equal to I.
    from parity_balancing_quotient_control import build,verify
    control=build();verify(control)
    control_maps=[np.asarray(control['map_numerators'][name],dtype=np.int64) for name in 'ABC']
    control_operator,_=operator_modulo(2,3,4,control_maps,p)
    if not np.array_equal(control_operator[0],np.eye(64,dtype=np.int64)) or np.any(control_operator[1]):
        raise ArithmeticError('The M4 control did not reshuffle to the identity')
    result.update({'input_file':str(args.initial),'input_sha256':hashlib.sha256(content).hexdigest(),
                   'source':[args.a,args.b],'target_square_size':args.size,
                   'source_terms_replayed':count,'prime':p,'field':'F_p[i], i²=-1',
                   'input_coefficients_interpreted_as':'exact binary64 dyadic real and imaginary parts',
                   'exact_M4_control_operator_is_identity':True,
                   'fixed_seed_plus_global_scaling_and_target_stabilizer_limit_excluded':True,
                   'deforming_source_maps_excluded':False,'general_source_degeneration_excluded':False,
                   'new_exponent_established':False})
    if args.export_coordinates:
        coordinates={name:[[[float(complex(z).real).hex(),float(complex(z).imag).hex()]
                            for z in row] for row in matrix]
                     for name,matrix in zip('ABC',maps)}
        payload=json.dumps(coordinates,sort_keys=True,separators=(',',':')).encode('ascii')
        exported={'format':'complex-dyadic-hex-v1','source':[args.a,args.b],
                  'target_square_size':args.size,'prime':p,
                  'input_npz_file':str(args.initial),
                  'input_npz_sha256':hashlib.sha256(content).hexdigest(),
                  'coordinate_payload_sha256':hashlib.sha256(payload).hexdigest(),
                  'map_coordinates':coordinates,'expected_invariant':invariant(operator,p),
                  'scope':'This one fixed dyadic seed, allowing an overall scalar and target stabilizer. Changing source maps is not excluded.',
                  'new_exponent_established':False}
        args.export_coordinates.parent.mkdir(parents=True,exist_ok=True)
        args.export_coordinates.write_text(json.dumps(exported,indent=2)+'\n')
        result['exact_coordinate_export']=str(args.export_coordinates)
        result['coordinate_payload_sha256']=exported['coordinate_payload_sha256']
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
