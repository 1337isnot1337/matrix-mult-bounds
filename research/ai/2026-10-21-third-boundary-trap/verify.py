"""Exact certificates for the third-order boundary normal lemma."""
from functools import lru_cache
import argparse
import importlib.util
import json
from pathlib import Path
import sympy as sp

folder=Path(__file__).resolve().parent

def load(name):
    spec=importlib.util.spec_from_file_location('third_boundary_'+name,folder/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

normal=load('normal');minors=load('minors');support=load('support')


@lru_cache(None)
def reports():
    report,block=normal.calculate()
    E=sp.MutableSparseMatrix(*block['shape'],{(i,j):sp.Rational(n,q) for i,j,n,q in block['entries']})
    return {'normal':report,'block':block,'minimum':minors.calculate(E,normal.minor_tools),
            'support_control':support.report()}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,report in reports().items():
        (args.output_dir/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
        print(name,'written',flush=True)
