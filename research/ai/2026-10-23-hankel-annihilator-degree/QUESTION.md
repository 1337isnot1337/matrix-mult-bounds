# Primitive annihilator degrees and source-rank excess

Base: b9006da, the first exact checkpoint of PR115, October 23, 2026.

The current question is whether the degree of the homogeneous supporting
form in x and z determines the two inner polynomial coefficient-map
ranks. The proposed exact count is

    rho=ar+(b-r)min(epsilon_z,a),
    sigma=br+(a-r)min(epsilon_x,b).

The written unreviewed proof now widens the pointwise constant-scheme strip to
`min(a(a-r),b(b-r))` and provides quantitative restrictions on moving
support. The balanced moving-support family is a written sharpness
control for every 2<=r<min(a,b). No common scheme over a whole lifted
matrix family is assumed. The historical ordinary A9 square sums are
already excluded by the credited Wronskian application.

Next question: can the two primitive degree costs be added when both
degrees equal one? The declared forty-case pilot and exact r=n-1
boundary family are recorded in additive_question.md. The universal
additive inequality is unproved and is not used by either strip theorem.
