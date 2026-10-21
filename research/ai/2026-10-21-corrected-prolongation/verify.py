"""Reconstruct the corrected172-parameter family and exact second jets."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

folder=Path(__file__).resolve().parent

def load(name):
    spec=importlib.util.spec_from_file_location('corrected_'+name,folder/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

linear=load('linear');quadratic=load('quadratic');seed=load('seed')


@lru_cache(None)
def reports():
    report,basis=linear.calculate()
    return {'linear':report,'basis':basis,'quadratic':quadratic.calculate(linear.m,basis),
            'seed':seed.calculate(linear.m,basis,{24:1}),
            'mixed_seed':seed.calculate(linear.m,basis,{24:1,25:2,100:-1,164:1})}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,report in reports().items():
        (args.output_dir/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
        print(name,'written',flush=True)
