"""Dependency-free replay of the exact fixed-seed stabilizer certificate.

Input coordinates are exact binary64 dyadics encoded with float.hex.
All tensor contractions and invariant evaluations use Python integers in
F_p[i]. No NumPy, floating point multiplication, or numerical linear
algebra is used. The only excluded family consists of this fixed seed
under target stabilizers and an overall scalar.
"""

import argparse
import hashlib
import json
from math import isfinite, isqrt
from pathlib import Path

from parity_balancing_spin1_verify import source_points
from parity_balancing_quotient_control import build as build_control
from parity_balancing_quotient_control import verify as verify_control


DEFAULT_COORDINATES=Path(__file__).resolve().parents[3]/'results'/'anisotropic-constructions-2026-10-20'/'parity_balancing_stabilizer_a33_seed_coordinates.json'


def multiply(a,b,p):
    return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)


def payload_hash(coordinates):
    payload=json.dumps(coordinates,sort_keys=True,separators=(',',':')).encode('ascii')
    return hashlib.sha256(payload).hexdigest()


def from_hex(text,p):
    value=float.fromhex(text)
    if not isfinite(value):
        raise ValueError('A dyadic coordinate must be finite')
    numerator,denominator=value.as_integer_ratio()
    return numerator*pow(denominator,-1,p)%p


def field_operator(a,b,n,maps,p):
    """Contract the source and apply the stated six-index reshuffle."""
    dimension=a*b*(a+b-1);d=n*n
    if any(len(matrix)!=d or any(len(row)!=dimension for row in matrix)
           for matrix in maps):
        raise ValueError('Unexpected map dimensions')
    amap,bmap,cmap=maps
    points=source_points(a,b)
    # First contract Y and Z, grouping by the original source X coordinate.
    gr=[[0]*(d*d) for _ in range(dimension)]
    gi=[[0]*(d*d) for _ in range(dimension)]
    for x,y,z in points:
        rowr,rowi=gr[x],gi[x]
        for j in range(d):
            br,bi=bmap[j][y];offset=j*d
            if br==0 and bi==0:
                continue
            for k in range(d):
                cr,ci=cmap[k][z]
                rowr[offset+k]+=br*cr-bi*ci
                rowi[offset+k]+=br*ci+bi*cr
    for x in range(dimension):
        gr[x]=[v%p for v in gr[x]];gi[x]=[v%p for v in gi[x]]
    tensor=[]
    for row in amap:
        tr=[0]*(d*d);ti=[0]*(d*d)
        for x,(ar,ai) in enumerate(row):
            if ar==0 and ai==0:
                continue
            rowr,rowi=gr[x],gi[x]
            for index in range(d*d):
                tr[index]+=ar*rowr[index]-ai*rowi[index]
                ti[index]+=ar*rowi[index]+ai*rowr[index]
        tensor.extend((r%p,i%p) for r,i in zip(tr,ti))
    size=n**3;operator=[]
    for row in range(size):
        i,jprime,kprime=row//(n*n),(row//n)%n,row%n
        values=[]
        for col in range(size):
            iprime,j,k=col//(n*n),(col//n)%n,col%n
            x=i*n+j;y=jprime*n+k;z=kprime*n+iprime
            values.append(tensor[(x*d+y)*d+z])
        operator.append(values)
    return operator,len(points)


def invariant(operator,p):
    size=len(operator)
    trace=(sum(operator[i][i][0] for i in range(size))%p,
           sum(operator[i][i][1] for i in range(size))%p)
    real=imag=0
    for i in range(size):
        for j in range(size):
            ar,ai=operator[i][j];br,bi=operator[j][i]
            real+=ar*br-ai*bi;imag+=ar*bi+ai*br
    trace_square=(real%p,imag%p)
    square=multiply(trace,trace,p)
    value=((size*trace_square[0]-square[0])%p,
           (size*trace_square[1]-square[1])%p)
    return {'operator_size':size,'trace_mod_prime':list(trace),
            'trace_square_mod_prime':list(trace_square),
            'N_trace_O_squared_minus_trace_O_squared':list(value),
            'nonzero':value!=(0,0)}


def exact_control(p):
    control=build_control();verify_control(control)
    maps=[[[ (int(v)%p,0) for v in row] for row in control['map_numerators'][key]]
          for key in 'ABC']
    operator,count=field_operator(2,3,4,maps,p)
    if any(value!=(int(i==j),0) for i,row in enumerate(operator)
           for j,value in enumerate(row)):
        raise ArithmeticError('The complete M4 control is not the identity after reshuffling')
    if invariant(operator,p)['nonzero']:
        raise ArithmeticError('The identity control has a nonzero invariant')
    return {'source_terms_replayed':count,'operator_size':64,
            'all_4096_operator_entries_match_identity':True}


def verify(data,with_control=True):
    if data.get('format')!='complex-dyadic-hex-v1':
        raise ValueError('Unsupported exact coordinate format')
    p=data['prime']
    if p<3 or p%4!=3 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise ValueError('The field prime must be 3 modulo4')
    coordinates=data['map_coordinates']
    digest=payload_hash(coordinates)
    if digest!=data['coordinate_payload_sha256']:
        raise ArithmeticError('The exact coordinate payload hash has changed')
    maps=[[[tuple(from_hex(component,p) for component in z) for z in row]
           for row in coordinates[key]] for key in 'ABC']
    if any(len(z)!=2 for matrix in maps for row in matrix for z in row):
        raise ValueError('A complex coordinate needs exactly two dyadic components')
    a,b=data['source'];n=data['target_square_size']
    operator,count=field_operator(a,b,n,maps,p)
    result=invariant(operator,p)
    if result!=data['expected_invariant']:
        raise ArithmeticError('The replayed invariant differs from the stored certificate')
    if not result['nonzero']:
        raise ArithmeticError('This input does not certify a nonzero invariant')
    result.update({'source':[a,b],'target_square_size':n,'prime':p,
                   'source_terms_replayed':count,'coordinate_payload_sha256':digest,
                   'input_npz_sha256':data['input_npz_sha256'],
                   'dependency_free_exact_replay':True,
                   'fixed_seed_plus_global_scaling_and_target_stabilizer_limit_excluded':True,
                   'deforming_source_maps_excluded':False,
                   'general_source_degeneration_excluded':False,
                   'new_exponent_established':False})
    if with_control:
        result['exact_M4_control']=exact_control(p)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('coordinates',type=Path,nargs='?',default=DEFAULT_COORDINATES)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--npz',type=Path,help='Optionally check the original file hash without loading its arrays')
    args=parser.parse_args();data=json.loads(args.coordinates.read_text())
    if args.npz and hashlib.sha256(args.npz.read_bytes()).hexdigest()!=data['input_npz_sha256']:
        raise ArithmeticError('The original NPZ hash does not match this exported seed')
    result=verify(data)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
