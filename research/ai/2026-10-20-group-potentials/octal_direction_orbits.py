"""Exact GL(2,F8) and family-permutation normalization of fixed directions."""
from itertools import permutations
import argparse
import hashlib
import json
from pathlib import Path

from octal_group import fm,inverse


def canonical(base):
    planes=[{0,base[2*f],base[2*f+1],base[2*f]^base[2*f+1]} for f in range(3)]
    short=[base[2*f] for f in range(3)];keys=[]
    for order in permutations(range(3)):
        u=short[order[0]]
        for v in sorted(planes[order[0]]-{0,u}):
            ux,uy=u&7,u>>3;vx,vy=v&7,v>>3
            det=fm(ux,vy)^fm(uy,vx)
            if not det:raise ValueError('first direction plane must span F8^2')
            invdet=inverse(det)
            def transform(w):
                x,y=w&7,w>>3
                return fm(invdet,fm(vy,x)^fm(vx,y))|(fm(invdet,fm(uy,x)^fm(ux,y))<<3)
            key=[]
            for f in order:
                P={transform(w) for w in planes[f]};uu=transform(short[f]);vv=min(P-{0,uu})
                key.extend([uu,vv])
            keys.append(tuple(key))
    return min(keys)


def classify(source):
    data=json.loads(source.read_text());all_bases={tuple(e['base_columns']) for e in data['surviving_direction_triples']}
    classes={}
    for i,entry in enumerate(data['surviving_direction_triples']):
        key=canonical(entry['base_columns'])
        if key not in all_bases:raise ArithmeticError('normalization leaves the stated frontier')
        classes.setdefault(key,[]).append(i)
    return {'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'source_triples':len(all_bases),'orbit_count':len(classes),
        'orbits':[{'base_columns':key,'member_indices':indices} for key,indices in sorted(classes.items())],
        'scope':'Exact normalization of constant-direction planes and distinguished short directions. '
                'Family permutation preserves coordinate potentials, with sign reversal for odd permutations. '
                'No global offsets or positive potential witness is implied.',
        'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=classify(args.source)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='orbits'},indent=2))
