"""Complete finite screen of ordinary common torus profiles for A88 -> M27 + M7.

The all-profile reduction uses the written zero-grade minimum-rank proof.
Terminal classifications invoke the written boundary-profile and extreme-pair
proofs. Integer enumeration is evidence for their finite hypotheses, not a
replacement for those proofs. No third-party package is required.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPORT = HERE / "parity_structure_common_profiles.json"
A = 8
WIDTH = 14
UPPER_BLOCKS = ((13, -13), (12, -12))


def normalise(profile):
    """Translate the nonempty support to start at zero and trim trailing zeros."""
    nonzero = [i for i, value in enumerate(profile) if value]
    if not nonzero:
        raise ValueError("A vertex profile must be nonempty")
    return tuple(profile[nonzero[0]:nonzero[-1] + 1])


def reflection_representative(profile):
    profile = normalise(profile)
    return min(profile, profile[::-1])


@lru_cache(maxsize=None)
def correlation(profile):
    return tuple(sum(profile[i] * profile[i + w]
                     for i in range(max(0, len(profile) - w)))
                 for w in range(WIDTH + 1))


@lru_cache(maxsize=None)
def target_block_rank(profile, wx, wy):
    """Exact third flattening rank at ordered input weights (wx, wy)."""
    return sum(profile[j + wx] * profile[j - wy]
               for j, multiplicity in enumerate(profile)
               if multiplicity and 0 <= j + wx < len(profile)
               and 0 <= j - wy < len(profile))


def source_tables():
    dimensions = Counter(i + s - k
                         for i in range(A)
                         for k in range(2 * A - 1)
                         for s in range(A))
    if any(dimensions[w] != dimensions[-w] for w in range(WIDTH + 1)):
        raise ArithmeticError("The source weight counts are not symmetric")
    columns = defaultdict(set)
    terms = 0
    for i, j, p, q, r, s in product(range(A), repeat=6):
        wx = i + s - p - q
        wy = j + p - r - s
        z = ((i + j) * A + q) * A + r
        columns[wx, wy].add(z)
        terms += 1
    ranks = {pair: len(value) for pair, value in columns.items()}
    valid_pairs = {(x, y) for x in range(-WIDTH, WIDTH + 1)
                   for y in range(-WIDTH, WIDTH + 1)
                   if abs(x + y) <= WIDTH}
    if set(ranks) != valid_pairs:
        raise ArithmeticError("The source block table misses a valid weight pair")
    return tuple(dimensions[w] for w in range(WIDTH + 1)), ranks, terms


def large_profiles():
    """All normalised 27-vertex profiles with squared multiplicities <= 53.

    Pad to fifteen bins and put x_j=m_j-2. Then sum x=-3 and sum x^2<=5.
    The only three possible patterns are generated explicitly below.
    """
    profiles = set()
    for ones in combinations(range(15), 3):
        profile = [2] * 15
        for i in ones:
            profile[i] = 1
        profiles.add(reflection_representative(profile))
    for zero in range(1, 15):
        for one in range(15):
            if zero == one:
                continue
            profile = [2] * 15
            profile[zero] = 0
            profile[one] = 1
            profiles.add(reflection_representative(profile))
    for ones in combinations(range(15), 4):
        for three in range(15):
            if three in ones:
                continue
            profile = [2] * 15
            for i in ones:
                profile[i] = 1
            profile[three] = 3
            profiles.add(reflection_representative(profile))
    for profile in profiles:
        if sum(profile) != 27 or sum(value * value for value in profile) not in (51, 53):
            raise ArithmeticError("A generated large profile has the wrong size")
    return tuple(sorted(profiles))


def small_profiles(zero_count):
    if zero_count == 7:
        for rest in combinations(range(1, 15), 6):
            profile = [0] * (rest[-1] + 1)
            for i in (0,) + rest:
                profile[i] = 1
            yield tuple(profile)
    elif zero_count == 9:
        for rest in combinations(range(1, 15), 5):
            support = (0,) + rest
            for doubled in support:
                profile = [0] * (rest[-1] + 1)
                for i in support:
                    profile[i] = 1 + (i == doubled)
                yield tuple(profile)
    else:
        raise ValueError("Only zero counts 7 and 9 survive the all-profile reduction")


def total_counts(large, small):
    return tuple(x + y for x, y in zip(correlation(large), correlation(small)))


def total_block_rank(large, small, wx, wy):
    return target_block_rank(large, wx, wy) + target_block_rank(small, wx, wy)


def saturated_violation(large, small, counts, dimensions, ranks):
    saturated = [w for w in range(-WIDTH, WIDTH + 1)
                 if counts[abs(w)] == dimensions[abs(w)]]
    for wx in saturated:
        for wy in saturated:
            wz = -wx - wy
            if abs(wz) > WIDTH:
                continue
            loss = dimensions[abs(wz)] - counts[abs(wz)]
            target_rank = total_block_rank(large, small, wx, wy)
            if ranks[wx, wy] - loss > target_rank:
                return {"weights": [wx, wy, wz],
                        "source_rank": ranks[wx, wy],
                        "third_leg_loss": loss, "target_rank": target_rank}
    return None


def upper_violation(large, small, ranks):
    for wx, wy in UPPER_BLOCKS:
        target_rank = total_block_rank(large, small, wx, wy)
        if target_rank > ranks[wx, wy]:
            return {"weights": [wx, wy, -wx - wy],
                    "source_rank": ranks[wx, wy], "target_rank": target_rank}
    return None


def terminal_proof_class(large, small, counts):
    """Check every finite hypothesis used by the two terminal written proofs."""
    boundary = (len(large) == 15
                and all(large[i] == 1 for i in (0, 1, 13, 14))
                and large[2] >= 2 and large[12] >= 2)
    if not boundary or any(value not in (0, 1) for value in small):
        return None
    if len(small) <= 13:
        return "boundary_profile_without_auxiliary_extreme_coordinates"
    if (len(small) == 14 and counts[13] == 3 and counts[14] == 1
            and total_block_rank(large, small, -13, 13) >= 1):
        # At the LARGE charge-zero diagonal, the target (-13,+13) slice
        # has rank m_large(13)=1. The auxiliary summand contributes zero.
        # Both full degree-13 maps have dimension three and are isomorphisms.
        return "saturated_degree13_with_auxiliary_scalar_channel"
    return None


def zero_grade_controls():
    path = HERE / "parity_structure_zero_grade_rank.py"
    spec = importlib.util.spec_from_file_location("common_profiles_zero_grade", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    report = module.verify(A)
    if report["maximum_ordinary_graded_target_zero_dimension_with_scalar_slice"] != 60:
        raise ArithmeticError("The zero-grade proof no longer gives the required bound")
    return report


def enumerate_profiles():
    dimensions, ranks, source_terms = source_tables()
    zero_report = zero_grade_controls()
    raw_large = large_profiles()
    large = tuple(profile for profile in raw_large
                  if all(t <= s for t, s in zip(correlation(profile), dimensions)))
    small = {7: tuple(small_profiles(7)), 9: tuple(small_profiles(9))}
    counts = Counter()
    lower_rejections = Counter()
    upper_rejections = Counter()
    terminal_counts = Counter()
    final_profiles = defaultdict(Counter)
    final_hash = sha256()
    examples = {}
    for big in large:
        small_counts = (7, 9) if correlation(big)[0] == 51 else (7,)
        for small_zero in small_counts:
            for little in small[small_zero]:
                # Only simultaneous reflection of both profiles is removed.
                # For asymmetric big, BOTH orientations of little are kept.
                if big == big[::-1] and little > little[::-1]:
                    continue
                counts["canonical_pairs_considered"] += 1
                target = total_counts(big, little)
                if any(t > s for t, s in zip(target, dimensions)):
                    continue
                counts["pass_weight_capacity"] += 1
                violation = saturated_violation(big, little, target, dimensions, ranks)
                if violation is not None:
                    lower_rejections[tuple(violation["weights"])] += 1
                    continue
                counts["pass_saturated_input_lower_rank"] += 1
                violation = upper_violation(big, little, ranks)
                if violation is not None:
                    upper_rejections[tuple(violation["weights"])] += 1
                    continue
                counts["pass_selected_upper_rank"] += 1
                proof_class = terminal_proof_class(big, little, target)
                if proof_class is None:
                    raise ArithmeticError("An unclassified ordinary common profile remains")
                terminal_counts[proof_class] += 1
                final_profiles[big][proof_class] += 1
                record = {"large": list(big), "small": list(little),
                          "weight_counts": list(target), "proof_class": proof_class}
                final_hash.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode())
                final_hash.update(b"\n")
                examples.setdefault(proof_class, record)
    if sum(terminal_counts.values()) != counts["pass_selected_upper_rank"]:
        raise ArithmeticError("The terminal classes do not partition the survivors")
    return {
        "format": "common-integer-torus-profiles-v1",
        "source": "A(8,8)", "target": "M27 direct_sum M7",
        "scope": "ordinary grading-preserving complex restrictions with a common vertex charge list within each square block",
        "source_weight_convention": "F(i,k,s) has weight i+s-k; each target matrix unit has row charge minus column charge",
        "normalisations": ["independent translation of the two block profiles",
                           "simultaneous reflection of both profiles"],
        "zero_grade_controls": zero_report,
        "allowed_zero_count_pairs": [[51, 7], [53, 7], [51, 9]],
        "source_abs_weight_dimensions": list(dimensions),
        "source_terms_examined": source_terms,
        "ordered_source_rank_blocks": len(ranks),
        "large_reflection_representatives_before_individual_capacity": len(raw_large),
        "large_reflection_representatives_after_individual_capacity": len(large),
        "large_profiles_by_zero_count": {str(k): v for k, v in sorted(Counter(correlation(p)[0] for p in large).items())},
        "small_normalised_profiles_by_zero_count": {str(k): len(v) for k, v in sorted(small.items())},
        "counts": dict(counts),
        "saturated_lower_rejections": [{"weights": list(k), "count": v} for k, v in sorted(lower_rejections.items())],
        "selected_upper_blocks": [list(pair) for pair in UPPER_BLOCKS],
        "selected_upper_rejections": [{"weights": list(k), "count": v} for k, v in sorted(upper_rejections.items())],
        "terminal_written_proof_classes": dict(sorted(terminal_counts.items())),
        "terminal_large_profiles": [{"profile": list(k), "counts": dict(sorted(v.items()))}
                                    for k, v in sorted(final_profiles.items())],
        "terminal_examples": dict(sorted(examples.items())),
        "terminal_profile_stream_sha256": final_hash.hexdigest(),
        "unclassified_profiles": 0,
        "standard_library_only": True,
        "unequal_vertex_profiles_excluded": False,
        "ungraded_restrictions_excluded": False,
        "arbitrary_singular_degenerations_excluded": False,
        "new_exponent_established": False,
    }


def verify(certificate=None):
    actual = enumerate_profiles()
    if certificate is None:
        certificate = json.loads(REPORT.read_text())
    if certificate != actual:
        raise ArithmeticError("The saved common-profile certificate does not match the complete exact enumeration")
    return actual


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the recomputed report")
    args = parser.parse_args()
    if args.write:
        data = enumerate_profiles()
        REPORT.write_text(json.dumps(data, indent=2) + "\n")
    else:
        data = verify()
    print(json.dumps({"counts": data["counts"],
                      "terminal_classes": data["terminal_written_proof_classes"],
                      "unclassified_profiles": data["unclassified_profiles"]}, indent=2))
