# Exact coefficients near the balanced grading

Owner: product-filtration worker, branch
research/balanced-polynomial-coefficients-20261020, based on main 0d2ccb2.
Goal remains active: no exponent below 9/4 is established.

Question: does C(4,10) admit a constant-matrix degeneration to T_4 at
beta=100, eta=(0,201,403,607)? The leading-pivot obstruction does not decide
this order. The first pilot fixes every flag pivot to one, as a restricted
ansatz, not as an asserted lossless normalization. It has 50 complex input
parameters and 75 complex output parameters solved linearly. Four fresh
OS-seeded starts, at most 600 least-squares evaluations each, are selected
before inspecting outcomes. Input real and imaginary components are bounded
by 20; output coefficients are solved by least squares. Exact coefficient
replay, rather than a floating residual, is the acceptance rule.

An independent symbolic investigation groups the monic coefficient equations
by their distance below the leading degree. Its first equations occur at
distance three, and their linear compatibility imposes a polynomial condition
on lower-distance coefficients. No solution or general obstruction is inferred
from that condition alone. The intended output is an exact witness or a
precisely scoped coefficient obstruction, with all unresolved premises retained.

The previous partial-residual calibration and normal-form proof are in
../2026-10-20-singular-flags/. An eventual finite witness still needs a complete
growth implication or an unbounded construction before it improves the exponent.

Follow-up experiments use the exact recurrence system: three polynomial
least-squares starts (the best earlier monic trial, then two fresh complex
starts), at most 800 evaluations each. Exact residue-field searches over
F2, F3, F5 and F4 each have a 120-second total solver limit and at most
16 models. Each found point is checked coefficient by coefficient and by
its formal Jacobian rank. These additional scopes were recorded during
the investigation, after selecting the methods; they are not claimed as
part of the first pilot's advance selection. No missing finite-field point
or rank-deficient point is treated as a complex nonexistence theorem.
