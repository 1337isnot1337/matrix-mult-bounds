"""Replay exact local checks; this does not verify the global M32 construction."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load(name):
    spec = spec_from_file_location('sun_local_' + name,
                                   Path(__file__).with_name(name + '.py'))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify():
    dense, laurent, endpoint = load('dense'), load('laurent'), load('endpoint')
    return {
        'source_url': 'https://arxiv.org/html/2610.13971v1',
        'source_html_sha256': '9c811f797344442cabe78f3b793ed74e0d986274567ec77e3ef1e23f8565171b',
        'literal_dense_scalars': dense.dense_audit(False),
        'corrected_dense_scalars': dense.dense_audit(True),
        'active_rank_four': laurent.active_d4(),
        'active_source_resolved_lift': laurent.active_lift(),
        'singular_C3': laurent.singular_c3(),
        'five_empty_C3': laurent.five_empty(),
        'generic_exceptional_endpoints': endpoint.endpoint_audit(),
        'crossed_group_representation': endpoint.crossed_group_audit(),
        'full_M32_coefficient_witness_reconstructed': False,
        'improves_omega': False,
        'scope': ('Independent local rational/Laurent expansion audit; the '
                  'global source-resolved assembly remains unverified.')}


if __name__ == '__main__':
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(verify(), indent=2) + '\n')
    print('Exact local audit written; no M32 witness or exponent improvement is certified.')
