# Modular SL(2,F8) filtration question

Question selected October 21, 2026: can a characteristic-two block or
radical filtration exclude any currently open coordinate/potential target
for SL(2,F8), especially M(18,18,25), beyond the maintained complex tests?

Base: main 00d51337. Branch: research/sl2-f8-modular-20261021.
Worktree: /tmp/matrix-f8-modular.

This is separate from the existing torus-packet, semisimple-trade,
determinant-factor and singular-assembly work on PR84. The exact matrix
group and field model retain the semisimple-source package's credit.

Plan: construct natural and Frobenius-tensor modules over F8, together
with the projective-line augmentation module over F2. Check their algebra
image and kernel powers exactly. If the kernel is nilpotent, split useful
central blocks and apply the independently justified modular counting
method. A numerical entropy estimate is discovery only; any accepted
obstruction needs an exact witness and written implication.

Completed exact result: proof.md and the exported certificates give the
all-power coordinate bound 1035637/2304<450. It excludes the tensor powers
of the six-packet-plus-M7 target. All 16 single-matrix complex-test survivors
remain unexcluded. Four focused tests passed in 32.366 seconds, including
762,048 representation products, 254,016 group-action columns, 19,800
left-generator power products, routing controls and corruption checks.
No independent review or smaller exponent is claimed.

The S5 contribution merged through PR93 at b3e36fd4; its exact squash tree
matches its tested head. The full local S5 suite continues separately.
Use /tmp/matrix-entropy-venv/bin/python and avoid large generated files.
