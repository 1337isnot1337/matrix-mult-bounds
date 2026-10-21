"""Complete integer A(2,3)->M4 positive control for the quotient ansatz."""

import argparse
from itertools import product
import json
from pathlib import Path

from parity_balancing_spin1_verify import source_points


def build():
    maps={name:[[0]*24 for _ in range(16)] for name in 'ABC'}
    common=[[0]*24 for _ in range(16)]
    for i,t,p,u in product(range(2),repeat=4):
        row=(2*i+t)*4+2*p+u
        middle=p+2*t
        common[row][(i*4+middle)*3+2*u]=1
        maps['A'][row][(i*4+middle)*3+2*u]=1
        maps['B'][row][(2*u*2+i)*4+middle]=1
        maps['C'][row][(middle*3+2*u)*2+i]=1
    return {'source':'full A(2,3)','target':'M4','source_format':[24]*3,
            'target_format':[16]*3,'common_map_denominator':1,
            'map_numerators':maps,'common_source_map':common,
            'quotient_physical_coordinates':[0,2,3,5],
            'kernel_physical_coordinates':[1,4],
            'kernel_maps_identically_zero':True,'extra_correction_source':False,
            'new_exponent_established':False}


def verify(certificate):
    if certificate.get('source')!='full A(2,3)' or certificate.get('target')!='M4':
        raise ValueError('The certificate must declare the full A23 source and M4 target')
    if certificate.get('extra_correction_source') is not False:
        raise ValueError('This positive control uses no extra source')
    maps=[certificate['map_numerators'][name] for name in 'ABC']
    if any(len(matrix)!=16 or any(len(row)!=24 for row in matrix) for matrix in maps):
        raise ValueError('The complete maps must be16 by24')
    if any(type(v) is not int for matrix in maps for row in matrix for v in row):
        raise ValueError('Integer map entries are required')
    columns=[[[ (row,matrix[row][col]) for row in range(16) if matrix[row][col]]
              for col in range(24)] for matrix in maps]
    actual=[0]*4096
    points=source_points(2,3)
    for x,y,z in points:
        for (i,a),(j,b),(k,c) in product(columns[0][x],columns[1][y],columns[2][z]):
            actual[(i*16+j)*16+k]+=a*b*c
    expected=[0]*4096
    for i,j,k in product(range(4),repeat=3):
        expected[((4*i+j)*16+4*j+k)*16+4*k+i]=1
    if actual!=expected:
        raise ArithmeticError('The complete full-source coefficient identity failed')
    common=certificate['common_source_map']
    selected=certificate['quotient_physical_coordinates']
    kernel=certificate['kernel_physical_coordinates']
    for index,coordinates in enumerate(common):
        matrix=[[coordinates[(row//3*4+row%3+col//3)*3+col%3]
                 for col in range(6)] for row in range(6)]
        for i,row in enumerate(selected):
            for col in range(6):
                expected_entry=int(i==index//4 and col==selected[index%4])
                if matrix[row][col]!=expected_entry:
                    raise ArithmeticError('The quotient-action identity failed')
        if any(matrix[row][col] for row in range(6) for col in kernel):
            raise ArithmeticError('The claimed zero kernel action failed')
    return {'arithmetic':'Python integers','source_terms_checked':len(points),
            'target_coefficients_checked':4096,'nonzero_target_coefficients':64,
            'quotient_matrix_units_checked':16,'all_kernel_maps_zero':True,
            'ordinary_full_A23_to_M4':True,'new_exponent_established':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--certificate',type=Path)
    args=parser.parse_args()
    certificate=json.loads(args.certificate.read_text()) if args.certificate else build()
    certificate['verification']=verify(certificate)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps(certificate['verification'],indent=2))


if __name__=='__main__':
    main()
