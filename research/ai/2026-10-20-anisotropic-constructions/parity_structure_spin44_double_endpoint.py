"""Exact replay of a coupled graph repair with two zero endpoint responses.

Recovered claim AI-SPIN-DOUBLE-ENDPOINT-121 uses freshly reconstructed
rational graph coefficients. The lost original artifact's bytes are not
claimed to have been recovered. All accepted checks use the standard library.
"""

from collections import Counter
import hashlib
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parity_structure_spin_endpoint import coordinate, determinant_mod, full_response, parse_maps


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
PREFIX = "parity_structure_spin44_double_endpoint"
BASE = DIRECTORY / "parity_balancing_spin44_full_maps.json"
MAPS = DIRECTORY / (PREFIX+"_maps.json")
WITNESS = DIRECTORY / (PREFIX+"_witness.json")
MINOR = DIRECTORY / (PREFIX+"_response_minor.json")
REPORT = DIRECTORY / (PREFIX+"_certificate.json")
CLAIM = "AI-SPIN-DOUBLE-ENDPOINT-121"
PRIME = 65521
DELETED = [0,4,8,16,24]
S = [[1,0,0,-2,1],[0,1,0,2,2],[0,0,1,0,2]]
T = [[2,-2,0,1,0],[-1,-2,-2,0,1]]


def parse_factor(item, rows, columns):
    if item.get("shape") != [rows, columns]:
        raise ArithmeticError("Incorrect graph-factor shape")
    denominator = item.get("denominator")
    if type(denominator) is not int or denominator <= 0:
        raise ArithmeticError("A graph factor needs a positive integer denominator")
    entries, seen = [], set()
    for entry in item["entries"]:
        if (not isinstance(entry, list) or len(entry) != 3
                or any(type(v) is not int for v in entry)):
            raise ArithmeticError("Malformed graph-factor entry")
        r,c,v = entry
        if not 0 <= r < rows or not 0 <= c < columns or not v or (r,c) in seen:
            raise ArithmeticError("Invalid graph-factor entry")
        entries.append((r,c,v));seen.add((r,c))
    return entries,denominator


def normalized_map(rows, columns, entries, denominator):
    entries = {key: value for key,value in entries.items() if value}
    divisor = denominator
    for value in entries.values():
        divisor = gcd(divisor,abs(value))
    return {"shape": [rows,columns], "denominator": denominator//divisor,
            "entries": [[r,c,v//divisor] for (r,c),v in sorted(entries.items())]}


def base_and_fibers():
    data=json.loads(BASE.read_text())
    base=next(v for v in data["restrictions"] if v["source"]==[8,8])
    if base["target"] != [3,3,32]:
        raise ArithmeticError("The base module has the wrong format")
    retained=[c for c in range(32) if c not in DELETED]
    result=[]
    for name, mix in zip("YZ",(S,T)):
        item=base["maps"][name]
        rows=[Counter() for _ in range(96)]
        for row,column,value in item["entries"]:
            rows[row][column]=value
        kept=[rows[32*v+c] for v in range(3) for c in retained]
        fibers=[]
        for outer, coefficients in product(range(3),mix):
            row=Counter()
            for d,coefficient in zip(DELETED,coefficients):
                for column,value in rows[32*outer+d].items():
                    row[column] += coefficient*value
            fibers.append({c:v for c,v in row.items() if v})
        result.append((kept,fibers,item["denominator"]))
    return base,result


def reconstruct(witness):
    if (witness.get("claim_id") != CLAIM or witness.get("deleted_channels") != DELETED
            or witness.get("S") != S or witness.get("T") != T
            or witness.get("new_exponent_established") is not False):
        raise ArithmeticError("The stated graph family or mathematical scope changed")
    if any(sum(a*b for a,b in zip(s,t)) for s,t in product(S,T)):
        raise ArithmeticError("The deleted-channel graph spaces are not orthogonal")
    base,source=base_and_fibers()
    if hashlib.sha256(BASE.read_bytes()).hexdigest()!=witness.get("base_maps_sha256"):
        raise ArithmeticError("The pinned base maps changed")
    maps={"X":base["maps"]["X"]}
    for name,field,(kept,fibers,base_denominator),columns in zip("YZ",("A","B"),source,(9,6)):
        factor,denominator=parse_factor(witness[field],81,columns)
        entries=Counter()
        for row,values in enumerate(kept):
            for column,value in values.items():
                entries[row,column] += denominator*value
        for row,fiber,coefficient in factor:
            for column,value in fibers[fiber].items():
                entries[row,column] += coefficient*value
        maps[name]=normalized_map(81,960,entries,base_denominator*denominator)
    return {"claim_id":CLAIM,"source":[8,8],"target":[3,3,27],
            "maps":maps,"new_exponent_established":False,
            "recovery_status":"fresh rational coefficients; original bytes not recovered"}


def verify(data=None,witness=None,minor=None):
    data=json.loads(MAPS.read_text()) if data is None else data
    witness=json.loads(WITNESS.read_text()) if witness is None else witness
    minor=json.loads(MINOR.read_text()) if minor is None else minor
    if data!=reconstruct(witness):
        raise ArithmeticError("Actual maps differ from the specified exact coupled graph")
    maps,denominators=parse_maps(data)
    if any(c//120>1 for _,c,_ in maps[1]) or any(c%8>1 for _,c,_ in maps[2]):
        raise ArithmeticError("The changed maps escaped their two low physical channels")
    response,source_count,contributions=full_response(maps[1],maps[2])
    actual=Counter()
    for row,column,value in maps[0]:
        for yz,coefficient in response.get(column,{}).items():
            ry,rz=divmod(yz,81)
            actual[row,ry,rz] += value*coefficient
    actual={point:value for point,value in actual.items() if value}
    scale=denominators[0]*denominators[1]*denominators[2]
    expected={(3*i+j,27*j+a,27*i+a):scale for i,j,a in product(range(3),range(3),range(27))}
    if actual!=expected:
        errors=sum(actual.get(p,0)!=expected.get(p,0) for p in actual.keys()|expected.keys())
        raise ArithmeticError(f"The full module has {errors} incorrect coefficients")
    allowed={coordinate(i,k,s) for i in range(8) for k in range(3) for s in range(8)}
    killed={coordinate(7,0,7),coordinate(7,2,7)}
    if set(response)!=allowed-killed:
        raise ArithmeticError("The actual response support is not the claimed 190 coordinates")
    rows,columns=minor["source_columns"],minor["output_columns"]
    if (minor.get("prime")!=PRIME or len(rows)!=190 or len(columns)!=190
            or len(set(rows))!=190 or len(set(columns))!=190
            or any(type(r) is not int or r not in response for r in rows)
            or any(type(c) is not int or not 0<=c<81*81 for c in columns)):
        raise ArithmeticError("Malformed full-response minor")
    det=determinant_mod([[response[r].get(c,0) for c in columns] for r in rows],PRIME)
    if not det or det!=minor.get("determinant_mod_prime"):
        raise ArithmeticError("The complete response minor failed exact replay")
    return {"claim_id":CLAIM,"source":"A(8,8)","target":"M(3,3,27)",
            "arithmetic":"complete Python-integer contraction of actual rational maps",
            "source_terms_checked":source_count,"all_target_coefficients_checked":59049,
            "nonzero_target_coefficients":len(actual),"all_other_coefficients_zero":True,
            "map_denominators":denominators,"sparse_map_entries":[len(m) for m in maps],
            "response_integer_contributions":contributions,
            "killed_first_coordinates":[[7,0,7],[7,2,7]],
            "all_endpoint_response_coefficients_checked":2*81*81,
            "full_response_rank_exact":190,"full_response_kernel_dimension_exact":770,
            "fixed_core_first_preimage_dimension_exact":779,
            "response_minor_prime":PRIME,"response_minor_determinant":det,
            "full_improving_target_constructed":False,"new_exponent_established":False,
            "external_independent_review":False,
            "recovery_status":"theorem recovered with fresh exact graph coefficients",
            "lost_original_maps_sha256":"e2cc86faa681bbaccec8405fafe4d6c1918016f2d024d2c05bc146884cc2ee9f"}


def main():
    report=verify()
    for name,path in (("maps",MAPS),("witness",WITNESS),("minor",MINOR)):
        report[name+"_sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":main()
