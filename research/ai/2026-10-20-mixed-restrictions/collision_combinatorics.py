"""Necessary output-capacity conditions, independent of the SMT solver."""
from collections import Counter
from itertools import permutations


def repetition_defect(indices):
    """Minimum excess-output lower bound from repeated difference windows."""
    m = len(indices)
    difference = tuple(b-a for a, b in zip(indices, indices[1:]))
    return sum(m-length-max(Counter(difference[start:start+length]
                                   for start in range(m-length)).values())
               for length in range(1, m))


def normalized_permutations(m, capacity):
    """Finite enumeration only; normalization uses reflection of both inputs."""
    return [list(x) for x in permutations(range(m)) if x[0] < x[-1]
            and repetition_defect(x) <= capacity]


def end_exception_word(word):
    return (len(set(word)) == 1 or
            len(set(word[1:])) == 1 or len(set(word[:-1])) == 1)


def word_defect(word):
    n = len(word)
    return sum(n-length+1-max(Counter(tuple(word[start:start+length])
                                     for start in range(n-length+1)).values())
               for length in range(1, n+1))


def endpoint_candidates(m):
    """The written word-gap proof implies this list when m>=6 and B=N."""
    if m < 6:
        raise ValueError("all-size word-gap classification starts at m=6")
    candidates = [list(range(m)), list(range(m-1, -1, -1)),
                  [0] + list(range(m-1, 0, -1)),
                  list(range(m-2, -1, -1)) + [m-1],
                  [m-1] + list(range(m-1)), list(range(1, m)) + [0]]
    return [x for x in candidates if x[0] < x[-1]]
