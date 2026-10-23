# Research field

Initial snapshot: October 20, 2026. The operational-barrier entry was added on October 23. This map is selective. Each source record states the inspection scope.

## Main lines of work

The classical approach starts with bilinear algorithms and tensor rank. Border rank and interpolation permit degenerations before exact asymptotic conversion. Strassen's laser method and the asymptotic sum inequality extract independent matrix products from powers of auxiliary tensors. The Coppersmith-Winograd tensor supplies a long sequence of such analyses. [STR69, BINI80, SCH81, STR87, CW90]

Higher-power analyses and optimization improved these bounds incrementally. The recent sequence includes refined laser extraction, asymmetric hashing, combination-loss analysis, and numerical optimization with certification. [STO10, VW12, LG14, AW21, DWZ23, VXXZ24, AD25, DUP26]

The asymptotic spectrum instead describes tensor comparisons using monotone semiring characters. The 9/4 argument combines this viewpoint with explicit shared-leg and convolution constructions. It is not merely another parameter setting in the older Coppersmith-Winograd optimization. [STR88, CVZ23, OAI26]

The group-theoretic approach embeds multiplication into group algebras. Finite algorithm search seeks explicit small bilinear identities. Both remain relevant research directions, but their certificates and obstructions differ. [CU03, BCGPU23, ALPHATENSOR22]

Blaser's survey provides an entry point for the older framework. It does not describe the 2026 results. [BLASER13]

## Selected exponent milestones

These are selected upper bounds, not a complete priority history. A strict inequality and a non-strict inequality are retained as reported.

| Source and publication context | Square exponent statement |
| --- | --- |
| Strassen, 1969 | $\omega\le\log_2 7$ |
| Le Gall, 2014 | $\omega<2.3728639$ |
| Alman and Vassilevska Williams, SODA 2021 | $\omega<2.37286$ |
| Duan, Wu, and Zhou, FOCS 2023 | $\omega<2.371866$ |
| Vassilevska Williams, Xu, Xu, and Zhou, SODA 2024 | $\omega\le2.371552$ |
| Alman et al., SODA 2025 / arXiv v2 | $\omega<2.371339$ |
| Dupont et al., August 17, 2026 | $\omega<2.371177$ |
| OpenAI, paper dated October 2, 2026 | $\omega\le9/4$ |

The August 2026 revision of *More Asymmetry* incorporates the numerical improvement credited to Dupont et al. Its earlier 2.371339 statement uses arXiv v2. Reading only the current abstract can obscure this attribution. [AD25, DUP26]

The leaderboard lists 2.25 on the snapshot date. Its verification label belongs to its own checking process. This repository did not rerun that process. [BIGO26]

## The 2026 shared-leg branch

Uznański extends the method to rectangular products. With $k\ge0$, the reported upper curve is

$$
f(k)=\begin{cases}2,&0\le k\le1/2,\\1+k+1/(4k),&k>1/2.\end{cases}
$$

It gives the dual-exponent bound $\alpha\ge1/2$, but $f(1)=9/4$. The author discloses the use of GPT-6.1 through Codex and his review of the argument. [UZ26]

Lü improves the finite separation overhead from $5M$ to $2M-1$ when the auxiliary dimension is $M$. The paper retains the 9/4 exponent. A better finite copy count alone does not establish a smaller asymptotic exponent. [LU26]

Navot's project extends the result to every field. The Hugin-Hilbert project extends the rectangular bound to associative rings. Filmus's repository develops a block-identities route and distinguishes formal polynomial correctness from functional correctness over finite fields. Their READMEs identify external proof dependencies and report formal verification. None was rebuilt during this initialization. [NAVOT26, RINGS26, FILMUS26]

## Barriers and their scope

A method barrier is not an unrestricted lower bound on $\omega$. Ambainis, Filmus, and Le Gall constrain specified laser-method analyses. Alman constrains the universal method on Coppersmith-Winograd tensors. The cap-set work constrains specified group-theoretic routes. These statements have different hypotheses. [AFL15, ALMAN19, BCCGNU17]

Amanov, van den Berg and Zuiddam prove an operational barrier for the polynomial-degeneration method. Their formal preorder includes specified degeneration ingredients, restrictions, isomorphisms and combination rules. Its square and rectangular exponent bounds cannot improve through those operations alone. The functions that prove this barrier need not be invariants of actual tensors. Arbitrary new degenerations remain outside this conclusion. [ABZ26]

The local matching-profile result is narrower still: it concerns the explicitly listed scalar axioms. It does not represent all tensor inequalities. See [the local status](../STATUS.md).

## References and inspection record

The JSON source registry is authoritative for versions and inspection scope. The BibTeX export is a convenience, not evidence of a full-paper review.

[Source registry](../references/sources.json) | [BibTeX](../references/references.bib)

### ABZ26

[Multiplying matrices via polynomials: exposition and barriers](https://arxiv.org/html/2610.30054v1). Alimzhan Amanov; Maxim van den Berg; Jeroen Zuiddam. Submitted October 21, 2026.

The paper presents the square and rectangular bounds over every field. Section 5 proves an operational barrier for the stated formal calculus. Definition 5.5 gives asymmetric monotones, and Proposition 5.9 proves their monotonicity. The local [paired-repair deduction](../research/ai/2026-10-23-operational-repair-barrier/README.md) applies those functions to the existing paired source.

Inspection: Primary v1 HTML, Theorems 1.1, 1.2 and 5.4, Definitions 5.1–5.5, and Propositions 5.7–5.9. The external monotonicity proof is imported, with its scope retained. No local formalization is claimed.

### STR69

[Gaussian elimination is not optimal](https://doi.org/10.1007/BF02165411). Volker Strassen. 1969.

The seven-product construction starts the subcubic recursion approach. This is a finite algorithm, unlike an existence-only exponent statement.

Inspection: Publisher metadata; cited by OAI26.

### BINI80

[Relations between exact and approximate bilinear algorithms. Applications](https://doi.org/10.1007/BF02575865). Dario Bini. 1980.

Interpolation connects approximate bilinear constructions to exact asymptotic algorithms. The original article was not reviewed in full during initialization.

Inspection: Bibliographic entry and use in OAI26.

### SCH81

[Partial and total matrix multiplication](https://doi.org/10.1137/0210032). Arnold Schonhage. 1981.

The asymptotic sum inequality connects simultaneous independent matrix products to exponent bounds.

Inspection: Bibliographic entry and use in OAI26.

### STR87

[Relative bilinear complexity and matrix multiplication](https://doi.org/10.1515/crll.1987.375-376.406). Volker Strassen. 1987.

A foundational source for the tensor-power and laser-method framework.

Inspection: Bibliographic entry and use in OAI26.

### STR88

[The asymptotic spectrum of tensors](https://doi.org/10.1515/crll.1988.384.102). Volker Strassen. 1988.

Spectral points encode asymptotic tensor comparisons through additive, multiplicative, monotone numerical invariants.

Inspection: Bibliographic entry and use in OAI26.

### CW90

[Matrix multiplication via arithmetic progressions](https://doi.org/10.1016/S0747-7171(08)80013-2). Don Coppersmith; Shmuel Winograd. 1990.

Auxiliary tensors and progression-free sets underpin the later Coppersmith-Winograd tensor analyses.

Inspection: Bibliographic entry and use in OAI26.

### STO10

[On the complexity of matrix multiplication](https://hdl.handle.net/1842/4734). Andrew James Stothers. 2010.

A doctoral thesis on higher-power analysis. The thesis itself was not reviewed in full during initialization.

Inspection: Bibliographic entry in OAI26.

### VW12

[Multiplying matrices faster than Coppersmith-Winograd](https://doi.org/10.1145/2213977.2214056). Virginia Vassilevska Williams. 2012.

A higher-power analysis in the classical exponent-improvement sequence.

Inspection: Bibliographic entry and historical discussion in OAI26.

OAI26 also cites the expanded corrected author version, dated July 1, 2014.

### BLASER13

[Fast Matrix Multiplication](https://theoryofcomputing.org/articles/gs005/). Markus Blaser. 2013.

A self-contained entry point for bilinear algorithms, tensors, and historical methods. It predates the later records.

Inspection: Publisher page and abstract.

Theory of Computing Graduate Surveys 5; DOI 10.4086/toc.gs.2013.005.

### LG14

[Powers of Tensors and Fast Matrix Multiplication](https://arxiv.org/abs/1401.7714). Francois Le Gall. 2014.

Convex optimization of tensor-power analysis gives omega < 2.3728639.

Inspection: Primary abstract and OAI26 bibliography.

### AW21

[A Refined Laser Method and Faster Matrix Multiplication](https://arxiv.org/abs/2010.05846). Josh Alman; Virginia Vassilevska Williams. 2021.

A refined component-extraction analysis gives omega < 2.37286.

Inspection: Primary abstract and publisher metadata.

Preprint 2020; SODA 2021; TheoretiCS journal version 2024, DOI 10.46298/theoretics.24.21.

### DWZ23

[Faster Matrix Multiplication via Asymmetric Hashing](https://arxiv.org/abs/2210.10173v5). Ran Duan; Hongxun Wu; Renfei Zhou. 2023.

Combination-loss analysis and asymmetric hashing give omega < 2.371866.

Inspection: Primary abstract and version history.

Preprint 2022; v5 November 28, 2023; FOCS 2023.

### VXXZ24

[New Bounds for Matrix Multiplication: from Alpha to Omega](https://arxiv.org/abs/2307.07970). Virginia Vassilevska Williams; Yinzhan Xu; Zixuan Xu; Renfei Zhou. 2024.

Further analysis gives omega <= 2.371552 and improvements for rectangular products.

Inspection: Primary abstract.

Preprint July 2023; SODA 2024.

### AD25

[More Asymmetry Yields Faster Matrix Multiplication](https://arxiv.org/abs/2404.16349v2). Josh Alman; Ran Duan; Virginia Vassilevska Williams; Yinzhan Xu; Zixuan Xu; Renfei Zhou. 2025.

The pre-Dupont analysis gives omega < 2.371339. Later numerical improvements must be credited separately.

Inspection: Primary abstracts, version history, and publisher metadata.

v2 October 20, 2024; SODA 2025. v3 August 19, 2026 incorporates the 2.371177 bound credited to DUP26.

### DUP26

[Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884). Emilien Dupont; Marvin Eisenberger; Borislav Kozlovskii; Abbas Mehrabian; Francisco J. R. Ruiz; Abigail See; Renfei Zhou; Josh Alman; Virginia Vassilevska Williams; Matej Balog. 2026.

Optimization within the combination-loss framework yields omega < 2.371177. The paper includes rigorous certification of the numerical bound.

Inspection: Primary manuscript text and abstract.

Submitted August 17, 2026. This is the pre-9/4 comparison bound, not the current listed record.

### OAI26

[An Upper Bound of 9/4 for the Matrix Multiplication Exponent](https://github.com/openai/math/blob/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/build/paper.tex). OpenAI. 2026.

The complex-field 9/4 theorem uses shared-leg separation, convolution inequalities, and a discrete-growth argument. This is external work.

Inspection: Primary TeX inspected; matching PDF pages visually inspected.

Paper dated October 2, 2026. Inspected TeX Git blob: 4492e66c707b9329f763c46e7cc113ff21d2edc0. Main-branch links can change.

### UZ26

[Rectangular matrix multiplication from polynomial products](https://arxiv.org/abs/2610.10494v2). Przemyslaw Uznanski. 2026.

The rectangular curve gives alpha >= 1/2 and returns 9/4 at the square shape. It does not lower the square exponent.

Inspection: Primary manuscript and version history.

v1 October 7, 2026 had the title Rectangular matrix multiplication from shared-leg entropy. v2 October 11. Author discloses GPT-6.1/Codex derivation and his review/responsibility.

### LU26

[Polynomial Separation of a Shared Tensor Leg and Matrix Multiplication in Arbitrary Characteristic](https://arxiv.org/abs/2610.18914). Houxi Lu. 2026.

Polynomial separation uses M+n-1 source copies; n=M gives 2M-1 rather than 5M. It retains the 9/4 exponent.

Inspection: Primary manuscript text.

Manuscript dated October 9, 2026; submitted October 12. Enough distinct field elements are required before extension to an algebraic closure.

### CVZ23

[Universal points in the asymptotic spectrum of tensors](https://arxiv.org/abs/1709.07851). Matthias Christandl; Peter Vrana; Jeroen Zuiddam. 2023.

Constructs universal spectral points and relates tensor asymptotics to quantum functionals.

Inspection: Primary abstract and OAI26 bibliography.

Preprint 2017; JAMS 36 (2023), 31-79; DOI 10.1090/jams/996.

### CU03

[A group-theoretic approach to fast matrix multiplication](https://arxiv.org/abs/math/0307321). Henry Cohn; Christopher Umans. 2003.

Embeds matrix multiplication into group algebras. This is an alternative construction framework, not a proof that omega equals two.

Inspection: Primary abstract.

### AFL15

[Fast Matrix Multiplication: Limitations of the Laser Method](https://arxiv.org/abs/1411.5414). Andris Ambainis; Yuval Filmus; Francois Le Gall. 2015.

Proves limitations for specified laser-method analyses. Such limitations are not lower bounds on unrestricted matrix multiplication.

Inspection: Primary manuscript and abstract.

Preprint November 2014; conference publication 2015.

### ALMAN19

[Limits on the Universal Method for Matrix Multiplication](https://arxiv.org/abs/1812.08731). Josh Alman. 2019.

The universal method on Coppersmith-Winograd tensors cannot yield an exponent below 2.16805. The tensor and method restrictions are essential.

Inspection: Primary abstract and proceedings metadata.

Preprint 2018; CCC 2019, DOI 10.4230/LIPIcs.CCC.2019.12.

### BCCGNU17

[On cap sets and the group-theoretic approach to matrix multiplication](https://arxiv.org/abs/1605.06702). Jonah Blasiak; Thomas Church; Henry Cohn; Joshua A. Grochow; Eric Naslund; William F. Sawin; Chris Umans. 2017.

Cap-set and slice-rank methods obstruct the omega=2 route through abelian groups of bounded exponent in the specified framework.

Inspection: Primary abstract and author archive metadata.

Preprint 2016; publication 2017.

### BCGPU23

[Matrix multiplication via matrix groups](https://arxiv.org/abs/2204.03826). Jonah Blasiak; Henry Cohn; Joshua A. Grochow; Kevin Pratt; Chris Umans. 2023.

Investigates matrix-group constructions and limitations, including continuous analogues.

Inspection: Primary abstract and proceedings metadata.

Preprint 2022; ITCS 2023, DOI 10.4230/LIPIcs.ITCS.2023.19.

### ALPHATENSOR22

[Discovering faster matrix multiplication algorithms with reinforcement learning](https://www.nature.com/articles/s41586-022-05172-4). Alhussein Fawzi; others. 2022.

AlphaTensor searches for finite bilinear algorithms. A small-tensor improvement or hardware benchmark is not automatically an asymptotic exponent record.

Inspection: Primary article.

Nature 610, 47-53. Full author list is available at the source; the bibliography uses et al.

### NAVOT26

[Matrix multiplication over arbitrary fields](https://github.com/selanavot/matrix-multiplication-all-fields). Sela Navot (project direction); GPT-6 Astra and GPT-6.1 Sol (disclosed proof generation). 2026.

Extends the OpenAI theorem to every field using characteristic-sensitive separation and fixed-overhead descent. External authors report Lean verification.

Inspection: Repository README and disclosed verification record.

Upstream baseline adc7f1241b42e322a6451854ab7e4b4c146bf78a. Archived release DOI 10.5281/zenodo.23219128. No local rebuild here.

### RINGS26

[Rectangular matrix multiplication over arbitrary rings: exponent 9/4](https://github.com/Hugin-Hilbert/rectangular-matmul-rings). Hugin-Hilbert repository maintainers. 2026.

Extends the rectangular curve to associative rings, including noncommutative and nonunital rings. It explicitly credits UZ26 for the curve.

Inspection: Repository README.

Inspected README blob f9fc18814ac14dc41cfb5785b439b30f9a910d21. Reported publication check October 14, 2026. No local Lean rebuild.

### FILMUS26

[Matrix multiplication from block identities](https://github.com/YuvalFilmus/matrix-multiplication-block-identities). Yuval Filmus repository; consult source for contribution details. 2026.

Gives a block-identities route with square and rectangular formalizations over every field. It reuses identified Navot/OpenAI APIs and credits UZ26.

Inspection: Repository README and theorem table.

Inspected README blob 06cab6441f44afd899d7e7586f3134abdf20ff71. Formal polynomial and finite-field functional correctness are distinguished. No local Lean rebuild.

### BIGO26

[Big O Speedrun: Matrix Multiplication](https://bigospeedrun.com/matrix-multiplication). Big O Speedrun. 2026.

Lists OpenAI at 2.25 with a Lean Verified label. This is a status source, not an independent proof by this repository.

Inspection: Leaderboard and exact problem description.

Data updated October 20, 2026 at 9:17 AM PT; site says its proof check was October 10 at 10:45 PM PT.

### RA26

[Matrix multiplication: a barrier for symmetrized sector inequalities](https://github.com/rohanarun/matrix-multiplication-sector-barrier/blob/0b09d3616da31d8750366747d7821d70ae6d1b90/proof.tex). Rohan Arun repository; disclosed AI-generated draft. 2026.

Inspection and scope: [source comparison](external_followups.md). Version: Main 0b09d3616da31d8750366747d7821d70ae6d1b90; least-profile commit 5a759558440672e69641547743bde3cf6d6ae50f, October 10. External tests not run.

### SDW26

[Strassen's support functionals coincide with the quantum functionals](https://arxiv.org/html/2601.21553v1). Keiya Sakabe; M. Levent Dogan; Michael Walter. 2026.

Inspection and scope: [source comparison](external_followups.md). Version: arXiv:2601.21553v1.

### ALP26

[The edge of the asymptotic spectrum of tensors](https://arxiv.org/html/2604.01386v2). Josh Alman; Baitian Li; Kevin Pratt. 2026.

Inspection and scope: [source comparison](external_followups.md). Version: v2, September 27, 2026. The compression theorem assumes an infinite field; the edge classification applies over arbitrary fields.
