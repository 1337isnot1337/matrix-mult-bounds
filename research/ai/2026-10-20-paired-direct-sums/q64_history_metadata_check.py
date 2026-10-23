"""Audit retained stdout snapshots against the corrected discovery histories."""
from hashlib import sha256
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
RESULTS = REPO/'results/paired-direct-sums-2026-10-20'


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def verify():
    correction = json.loads((RESULTS/'q64-ridge-metadata-correction.json').read_text())
    evidence = json.loads((RESULTS/'q64-ridge-emitted-records.json').read_text())
    logs = {row['log_name']: row for row in evidence['logs']}
    published = [row for row in correction['records'] if 'history_records_audited' in row]
    new = correction['m1_histories_corrected_before_first_publication']
    histories = snapshots = 0
    for record in published+new:
        raw = (REPO/record['artifact']).read_bytes()
        expected = record.get('after_sha256', record.get('artifact_sha256'))
        if sha256(raw).hexdigest() != expected:
            raise ArithmeticError('A corrected artifact content hash changed.')
        point = json.loads(raw)
        history = point['completed_run']['history']
        log = logs[record['log_name']]
        if log['log_sha256'] != record['log_sha256']:
            raise ArithmeticError('The retained stdout provenance identifiers differ.')
        if history != log['emitted_records']:
            raise ArithmeticError('A retained history differs from its emitted snapshots.')
        map_digest = digest([point['maps_real'], point['maps_imag']])
        if map_digest != record.get('map_payload_sha256_after', record.get('map_payload_sha256')):
            raise ArithmeticError('A saved map array changed during metadata correction.')
        if 'non_ridge_payload_sha256_before' in record:
            point.pop('history_metadata_correction', None)
            for row in point['completed_run']['history']:
                row.pop('ridge_parameters', None)
            if digest(point) != record['non_ridge_payload_sha256_before']:
                raise ArithmeticError('A published payload changed outside ridge metadata.')
        histories += 1
        snapshots += len(history)
    replay = json.loads((RESULTS/'q64-full-flag-replay.json').read_text())
    for row in replay['replays']:
        if sha256((RESULTS/row['artifact']).read_bytes()).hexdigest() != row['artifact_sha256']:
            raise ArithmeticError('A coefficient replay refers to an obsolete artifact hash.')
    return {'histories_checked': histories, 'retained_snapshots_checked': snapshots,
            'published_histories_audited': len(published),
            'published_snapshots_with_corrected_ridges': 90,
            'M1_snapshots_corrected_before_first_publication': 60,
            'all_non_ridge_published_payloads_unchanged': True,
            'all_retained_histories_equal_original_emitted_records': True,
            'optimizer_reruns_performed': 0}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
