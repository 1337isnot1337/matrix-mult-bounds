# Independent relabelings of the matched long-leg windows

**Question.** Can independent permutations of each matched long-leg coordinate window make the `Q(n,4) -> M(n,4,n)` correction have border rank `O(n)`?

**Answer.** No. If each B window `s-y in [0,n-1]` and each C window `z-v in [0,n-1]` is relabeled by an arbitrary permutation, every first-leg map leaves correction flattening rank at least `(n-1)^2`.

A target slice coefficient in the matched `(0,0)` block has a unique source preimage. Except on one row and one column, that same coefficient appears uniquely in the absent `(0,1)` block and must vanish. Exact rational replay exhausts all permutation profiles at `n=1,2` and checks deterministic profiles through `n=5`.
