# A sharp rank-two first-slice gap for the paired source

October 23, 2026. Owner-directed AI-derived work. Written proof, unreviewed and not formalized. No improvement of the matrix multiplication exponent is claimed.

## Statement

For a field \(K\), integers \(n\ge2\), \(b\ge1\), take the maintained paired tensor
\[
Q(n,b)=\sum_{p,q<n}\sum_{y,v<b} A_{pq}\otimes B_{y,q+v}\otimes C_{p+y,v}.
\]
For a coefficient matrix \(Y\in K^{n\times n}\), its first contraction has rows \((y,z)\), columns \((w,v)\), and entries
\[
S_Y[(y,z),(w,v)]=Y_{w-y,z-v},\quad
0\le y,v<b,\quad0\le z,w<n+b-1,
\]
with out-of-range entries zero.

**Theorem (sharp all-field rank-two gap).** If \(\operatorname{rank}Y=2\), then
\[
\boxed{\operatorname{rank} S_Y\ge b(b+1).}
\]
Equality holds over every field for every \(n,b\), by \(Y=E_{00}+E_{11}\). At \(b=4\), a rank-two first parameter therefore has source-slice rank at least 20. The previously maintained general inequality \(\operatorname{rank}S_Y\ge b^2+\operatorname{rank}Y-1\) only gives 17 in this case.

More precisely, the source slice has an exact matrix-rank formula
\[
\boxed{\operatorname{rank}S_Y=b^2+\sum_{i,j}\min(e_i,d_j),\qquad
\sum_i e_i=\sum_j d_j=b,}
\]
where \(e_i,d_j\) are the right and left Kronecker minimal indices of two explicitly defined full-rank polynomial-multiplication pencils. Zero minimal indices are allowed. This classifies the rank conditional on those pencil invariants; it does not assert that every pair of partitions occurs for source polynomials with bounded degree.

## Proof: multiplication pencils

Since \(\operatorname{rank}Y=2\), write \(Y=f_0g_0^T+f_1g_1^T\), with the two \(f_i\) independent, and the two \(g_i\) independent. Regard all four as coefficients of degree-less-than-\(n\) univariate polynomials. Put \(N=n+b-1\), and define
\[
F_i[y,w]=(f_i)_{w-y}\in K^{b\times N},\qquad
G_i[z,v]=(g_i)_{z-v}\in K^{N\times b}.
\]
The literal coefficient identity is
\[
S_Y=F_0\otimes G_0+F_1\otimes G_1.
\]
For any field extension and \((s,t)\ne(0,0)\), the polynomial \(sf_0+tf_1\) is nonzero. Multiplication by it from polynomials of degree less than \(b\) into polynomials of degree less than \(N\) is injective. Thus the pencil \(sF_0+tF_1\) has full row rank \(b\) at every projective parameter, over the algebraic closure as well. The pencil \(sG_0+tG_1\) likewise has full column rank \(b\).

Apply the classical Kronecker canonical form for matrix pencils *under strict equivalence* over the algebraic closure. A homogeneous pencil of full row rank at **every** projective parameter has only right singular blocks: left blocks always have deficient row rank, while a positive-size regular square block has a homogeneous determinant of positive degree with a projective zero. Therefore there are fixed invertible row and column transformations, without changing the parameter pair \((s,t)\), putting the first pencil into a direct sum of
\[
R_e(s,t)=s[I_e\;\;0]+t[0\;\;I_e]\in K^{e\times(e+1)},\quad e\ge0.
\]
The second pencil is similarly a direct sum of \(R_d(s,t)^T\). The indices satisfy \(\sum e_i=\sum d_j=b\). The strict-equivalence operations on the two pencils induce invertible row and column transformations on \(S_Y\), whose resulting matrix is a direct sum, indexed by all pairs \(i,j\), of
\[
T_{e,d}=R_e(1,0)\otimes R_d(1,0)^T+
R_e(0,1)\otimes R_d(0,1)^T.
\]
This is an ordinary **matrix** direct sum, because both the source and target of the Kronecker tensor product split into the indexed pairs. No tensor-rank additivity assertion is used.

## Proof: exact rank of a block

For \(e,d\ge1\), \(T_{e,d}\) maps a tuple \((U_0,\ldots,U_e)\) of polynomials of degree less than \(d\) to
\[
V_i(z)=U_i(z)+zU_{i+1}(z),\quad i=0,\ldots,e-1,
\]
with \(\deg V_i\le d\). The kernel equations give
\(U_i=(-z)^{e-i}U_e\). If \(e\ge d\), this forces \(U_e=0\). If \(e<d\), \(U_e\) may be any polynomial of degree less than \(d-e\), giving kernel dimension \(d-e\). Rank-nullity yields
\[
\operatorname{rank}T_{e,d}=(e+1)d-\max(d-e,0)
=ed+\min(e,d).
\]
The same formula gives rank zero for \(e=0\) or \(d=0\). It holds in every characteristic. Summing over the matrix-direct-sum blocks proves the exact formula.

For each \(e_i>0\), since \(\sum_j d_j=b\ge e_i\), we have \(\sum_j\min(e_i,d_j)\ge e_i\): either one \(d_j\) is at least \(e_i\), or every term is smaller and the sum equals \(b\). Summing gives \(\sum_{i,j}\min(e_i,d_j)\ge b\), which proves the lower bound.

For equality, take the two coefficient polynomials \(f_0=g_0=1\), \(f_1=g_1=z\); this is \(Y=E_{00}+E_{11}\). The nonzero parts of the two multiplication pencils are respectively one \(R_b\) and one \(R_b^T\), with other blocks of index zero. Consequently \(\operatorname{rank}S_Y=\operatorname{rank}T_{b,b}=b(b+1)\).

The argument extends scalars only to use Kronecker form. Matrix rank is unchanged under field extension, so the result applies to every original field, including characteristic two.

## External dependency, validation, and scope

The Kronecker strict-equivalence theorem is classical; it is **imported**, not claimed as an AI-derived result. See F. De Terán, F. Dopico and J. M. Landsberg, *An explicit description of the irreducible components of the set of matrix pencils with bounded normal rank*, arXiv:1606.02574 (2016), and S. D. Karathanasi and N. P. Karampetakis, *On the Kronecker canonical form of a full row rank matrix pencil and applications*, DOI:10.1093/imamci/dnz031 (published 2019). The original source contraction and its older bound are credited to the pre-existing repository proof, byte-pinned in sources.json.

The standalone standard-library verifier reconstructs the full source contraction from original coordinates, checks the separate Toeplitz-factor expression, tests 128 Kronecker-block ranks over two prime fields, tests 16 sharpness instances, and exhausts rank-two coefficient matrices over \(\mathbb F_2\) in seven small formats (including 7,350 rank-two matrices at \(n=4,b=2\)). These are finite controls; the proof above is the basis of the universal claim. Same-session checks are not independent mathematical review.

Run:
\`\`\`sh
python -S research/ai/2026-10-23-paired-rank-two-gap/verify.py --check-certificate results/paired-rank-two-gap-2026-10-23/certificate.json
python -m unittest discover -s tests -p test_paired_rank_two_gap.py -v
\`\`\`

This is a rank-two **ordinary source-slice theorem**, not a degeneration or a new actual source-to-target map. It does not constrain arbitrary mixed first maps without an additional rank-two-image hypothesis, and it does not prove any new auxiliary border-rank or asymptotic bound. The known exponent baseline remains \(\omega\le9/4\).