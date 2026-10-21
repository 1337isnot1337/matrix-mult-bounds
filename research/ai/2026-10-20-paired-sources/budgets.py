"""Integer upper certificates for all one-copy size-four matrix-block scores."""
from fractions import Fraction
from math import isqrt


SCALE = 1<<32
FORMAT = (16,28,28)


def shapes():
    return [(l,b,r) for l in range(1,17) for r in range(1,17) if l*r<=16
            for b in range(1,28//max(l,r)+1) if (l,b,r)!=(4,7,4)]


def block_bound(shape):
    l,b,r = shape
    power = (l*b*r)**3*SCALE**4
    root = isqrt(isqrt(power))
    return root+(root**4<power)


def index(a,b,c): return (a*29+b)*29+c


def make_certificate():
    blocks = [(l*r,l*b,b*r,block_bound((l,b,r))) for l,b,r in shapes()]
    table = [0]*(17*29*29)
    for a in range(17):
        for b in range(29):
            for c in range(29):
                table[index(a,b,c)] = max([0]+[value+table[index(a-x,b-y,c-z)]
                                               for x,y,z,value in blocks if x<=a and y<=b and z<=c])
    return table


def verify_certificate(table):
    if len(table) != 17*29*29 or any(not isinstance(v,int) or v<0 for v in table):
        raise ValueError('invalid budget potential')
    checked = 0
    for shape in shapes():
        l,b,r = shape
        x,y,z = l*r,l*b,b*r
        value = block_bound(shape)
        # Every root ceiling is independently bounded by an integer fourth power.
        if value**4 < (l*b*r)**3*SCALE**4:
            raise ArithmeticError('incorrect block upper interval')
        for A in range(x,17):
            for B in range(y,29):
                for C in range(z,29):
                    if table[index(A,B,C)] < value+table[index(A-x,B-y,C-z)]:
                        raise ArithmeticError('invalid budget induction inequality')
                    checked += 1
    numerator = table[index(*FORMAT)]
    partition = [(1,1,1),(1,3,3),(4,6,3)]
    if sum(block_bound(shape) for shape in partition) != numerator:
        raise ArithmeticError('rounded attaining partition no longer matches the potential')
    if not (numerator**4 < 106**3*SCALE**4 and
            6**3*numerator**2 < 22**4*SCALE**2):
        raise ArithmeticError('finite method ceiling does not pass the claimed comparison')
    return {'format':list(FORMAT),'allowed_shapes':len(shapes()),'potential_entries':len(table),
            'integer_transitions_checked':checked,'scale':SCALE,'upper_numerator':numerator,
            'rounded_attaining_partition':[list(shape) for shape in partition],
            'exact_endpoint_score_upper':str(Fraction(numerator,SCALE)),
            'below_sqrt106_profile_threshold':True,'below_finite_profile_ceiling':True,
            'scope':'One-copy matrix direct sums per paired factor; endpoint method ceiling only.',
            'improves_omega':False}


if __name__ == '__main__':
    import argparse,gzip,hashlib,json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--table',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args();table = make_certificate()
    blob = (json.dumps(table,separators=(',',':'))+'\n').encode()
    args.table.write_bytes(gzip.compress(blob,mtime=0))
    report = verify_certificate(table)
    report['table_decompressed_sha256'] = hashlib.sha256(blob).hexdigest()
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
