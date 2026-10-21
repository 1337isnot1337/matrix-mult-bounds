"""Exact nonmonic polynomial-flag equations for a specified weight chamber.

This extends the coefficient construction to other strict compatible orders.
It does not infer a degeneration from the number of equations.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

from torus_exact import ExactModel, discover, equations, incidence_data


class ChamberModel(ExactModel):
    def __init__(self, eta, beta=100):
        if len(eta) != 4 or beta <= 0:
            raise ValueError('four offsets and positive shared slope are required')
        s = SimpleNamespace(m=4, B=10, eta=list(eta), beta=beta)
        s.points = [(a,d-a) for d in range(4) for a in range(d+1)]
        wy = [eta[a+b]-beta*a for a,b in s.points]
        wz = [-eta[3-c-d]-beta*c for c,d in s.points]
        if len(set(wy)) != 10 or len(set(wz)) != 10:
            raise ValueError('the polynomial flags require distinct coordinate weights')
        ry = {v:j for j,v in enumerate(sorted(wy))}
        rz = {v:j for j,v in enumerate(sorted(wz))}
        s.degrees = [[3-p for p in range(4)], [9-ry[w] for w in wy], [12-rz[w] for w in wz]]
        s.keys, s.index, s.constant_values = [], {}, {}
        for leg,degrees in enumerate(s.degrees):
            for row,degree in enumerate(degrees):
                for drop in range(degree+1):
                    key = leg,row,drop
                    index = len(s.keys)
                    s.keys.append(key); s.index[key] = index
                    if drop == 0:
                        s.constant_values[index] = Fraction(1)
                    elif key == (0,2,1):
                        s.constant_values[index] = Fraction(0)
        s.constraints = defaultdict(list)
        self.forced_zero_entries = []
        self.weights = [list(beta*p for p in range(4)), wy, wz]
        for p in range(4):
            for y,(a,b) in enumerate(s.points):
                for z,(c,d) in enumerate(s.points):
                    weight = beta*p+wy[y]+wz[z]
                    wanted = int(p==a+c and a+b+c+d==3)
                    if wanted and weight:
                        raise ArithmeticError('target term does not have weight zero')
                    if weight > 0:
                        continue
                    delta = s.degrees[0][p]+s.degrees[1][y]-(12-s.degrees[2][z])
                    if delta < 0:
                        if wanted:
                            raise ValueError('a desired coefficient vanishes by degree')
                        self.forced_zero_entries.append((p,y,z))
                    elif delta == 0 and not wanted:
                        raise ValueError('forbidden coefficient is a product of nonzero pivots')
                    else:
                        s.constraints[delta].append((p,y,z,wanted))
        s.levels = [{'level':level,'constraints':rows} for level,rows in sorted(s.constraints.items())]
        self.system = s
        self.variables,self.equations = equations(s)
        self.all_triples = [(p,y,z) for level in s.levels for p,y,z,_ in level['constraints']]
        self.targets,self.incidence,self.columns,relations = incidence_data(s)
        self.relations = [[int(value) for value in relation] for relation in relations]
        self.target_indices = [self.all_triples.index(triple) for triple in self.targets]
        self.zero_indices = [i for i,(_,wanted) in enumerate(self.equations) if not wanted]
        self.rows = list(self.incidence[:,self.columns].T.rref()[1])
        self.minor = self.incidence.extract(self.rows,self.columns)
        self.inverse = self.minor.inv()
        if len(self.targets) != 20 or self.minor.det() != -1:
            raise ArithmeticError('the expected target orbit changed')

    def structure(self):
        result = super().structure()
        result.update({'eta':self.system.eta,'beta':self.system.beta,
                       'degrees':self.system.degrees,'weights':self.weights,
                       'identically_zero_nonpositive_entries':self.forced_zero_entries,
                       'total_nonpositive_entries':len(self.equations)+len(self.forced_zero_entries)})
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--eta',default='0,301,628,844')
    parser.add_argument('--beta',type=int,default=100)
    parser.add_argument('--order',type=int,choices=(3,4),default=4)
    parser.add_argument('--seed',type=int,default=20261021)
    parser.add_argument('--timeout-ms',type=int,default=120000)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--structure-only',action='store_true')
    args = parser.parse_args()
    model = ChamberModel(list(map(int,args.eta.split(','))),args.beta)
    report = {'structure':model.structure(),'characteristic_zero_certificate':False,'improves_omega':False,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if not args.structure_only:
        query_path = args.output.with_suffix('.smt2')
        result = discover(model,args.order,args.seed,args.timeout_ms,4,query_path)
        with gzip.GzipFile(filename=str(query_path)+'.gz',mode='wb',mtime=0) as stream:
            stream.write(query_path.read_bytes())
        query_path.unlink()
        report['discovery'] = result
        report['characteristic_zero_certificate'] = result['status']=='nonsingular-certificate'
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k!='structure'},flush=True)


if __name__ == '__main__':
    main()
