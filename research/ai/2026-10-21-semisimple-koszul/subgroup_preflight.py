"""Exact preflight for the already excluded full-D18 coordinate frame."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECTION = ROOT/'results/sl2-f8-ideals-2026-10-21/projections.json'
VERIFIER = ROOT/'research/ai/2026-10-21-sl2-f8-ideals/sl2_f8_ideal_certificate.py'


def projection_receipt(proof, shape, subgroup):
    if len(shape) != 3 or any(type(n) is not int or n < 1 for n in shape):
        raise ValueError('positive integer target dimensions required')
    if shape[0] != len(subgroup) or proof['subgroup'] != subgroup:
        raise ValueError('projection does not describe the fixed first-leg subgroup')
    spec = importlib.util.spec_from_file_location('f8_preflight_projection', VERIFIER)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    return verifier.verify_projection(
        proof['subgroup'], proof['central_projection'], proof['ideal_dimension_upper_bound'])


def verify_exclusion(proof, shape, subgroup):
    receipt = projection_receipt(proof, shape, subgroup)
    other_pair = shape[1]*shape[2]
    if other_pair <= receipt['ideal_dimension_upper_bound']:
        raise ValueError('the subgroup-ideal bound does not exclude this target')
    return {**receipt, 'other_pair_product': other_pair,
            'fixed_full_subgroup_frame_excluded': True,
            'general_complex_degenerations_excluded': False}


def exclusion_for(shape, subgroup):
    data = json.loads(PROJECTION.read_text())
    record = next(row for row in data['records'] if row['subgroup'] == subgroup)
    upper = record['verification']['ideal_dimension_upper_bound']
    proof = {'subgroup': subgroup, 'central_projection': record['central_projection'],
             'ideal_dimension_upper_bound': upper,
             'source': 'research/ai/2026-10-21-sl2-f8-ideals/proof.md'}
    # Acceptance uses the actual integer idempotent/containment identities,
    # including the trace rank, rather than the saved receipt alone.
    receipt = projection_receipt(proof, shape, subgroup)
    if shape[1]*shape[2] <= receipt['ideal_dimension_upper_bound']:
        return None
    proof['verification'] = {**receipt, 'other_pair_product': shape[1]*shape[2],
                             'fixed_full_subgroup_frame_excluded': True,
                             'general_complex_degenerations_excluded': False}
    return proof
