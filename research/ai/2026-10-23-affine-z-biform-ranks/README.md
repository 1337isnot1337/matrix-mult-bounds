# Affine-in-z biform coefficient ranks

Written all-field proof, unreviewed; exact finite checks. No matrix-tensor degeneration or exponent gain.

For 2<=a<=b and nonzero f=u(x)+z*v(x), let d be the maximum degree of the coprime pair u/g,v/g; set d=0 if one coefficient is zero. Then the literal cyclic-source coefficient matrix has rank ab+min(b,a*d), over every field. All attainable ranks follow by taking f=1+x^d*z.

See proof.md for the all-field syzygy proof, sources.json for pinned provenance, QUESTION.md for the next construction question.

From repository root:
    python -I research/ai/2026-10-23-affine-z-biform-ranks/verify.py
    python -m unittest discover -s tests -p 'test_affine_z_biform_ranks.py' -v
