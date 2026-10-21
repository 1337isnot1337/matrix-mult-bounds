# Packetwise lifting obstruction for the printed dense compiler

October 21, 2026. Written derivation and exact finite coefficient check, unreviewed.

The source is Section 5 of [Tensor Degenerations for Matrix Multiplication, version 1](https://arxiv.org/html/2610.13971v1). This note identifies a concrete obstruction to lifting the printed packet contributions individually. It does not prove the impossibility of a different global construction that mixes those contributions.

## 1. One printed generic packet already contains a matrix tensor

For any generic layer-one character chi outside {6,7,10,11}, the eight retained supports have twists

    A1:3, A3:0, B1:5, B2:9, C1:6, P:10, Q:12, R:15.

These are exactly the even-weight subspace E of F_2^4. Therefore

    sum_(theta in E) (-1)^(theta dot beta)
      = 8 * 1_{beta in {0,15}}.

The kernel of B0+B1 in the paper is exactly {0,15}. The literal contribution of this one packet to equation (5.1), after the scalar normalization repair from the earlier audit, is consequently

    (1/16) (-1)^(chi dot (rho+B1 beta))
      * 1_{beta in ker(B0+B1)}.

Equation (5.2) makes the indicator precisely the vanishing of the three central defect bits. On that set, rho+B1 beta equals the H4 defect q+r+s. This conclusion holds for either chart representative, so it does not depend on a choice of chart section.

Fix the three physical displacements to q=1, r=2, s=3. All are nonzero, so all four central coordinates on each side remain in the unbarred target. Their high defect is zero. The resulting 4-by-4-by-4 coefficient tensor of this single packet is thus

    (1/16) * 1_{b=a+epsilon,
                phi=epsilon+delta,
                c=a+epsilon+delta}.

Relabel the three central coordinates as matrix edges

    X_(epsilon,a) -> X_(a,a+epsilon),
    Y_(delta,b)   -> Y_(b,b+delta),
    Z_(phi,c)    -> Z_(c,c+phi).

The displayed tensor becomes exactly (1/16) M2. The program verifies all 1,536 values: 12 generic characters, 64 central triples, and both chart representatives.

This cannot be the individual image or leading coefficient of a C3 packet, whose recorded border-rank cost is five. For a tensor of border rank at most five in first ambient dimension five, its degree-two first Koszul map has rank at most

    5 * binomial(4,2) = 30.

The program independently constructs this Koszul map for M2 padded to ambient five and finds rank 32 over F_65521. An integer coefficient matrix with this rank modulo a prime has rank at least 32 over characteristic zero. Thus C3 cannot degenerate to the literal per-packet contribution. A D4 source cannot do so either. This numerical rank check is used only to establish the characteristic-zero conclusion; it is not presented as an all-characteristic rank proof.

The point of failure is the passage from a scalar support ledger to one triple of source-coordinate linear maps. The scalar identity can hold even though its individual packet summands cannot be produced by the corresponding source packets. The paper's local arrow tensor and endpoint identities do not themselves supply that missing lift.

## 2. Direct diagnostic for additive linear phase assignments

The obstruction can also be seen before summing the eight supports. Suppose beta is decomposed additively into side-local linear functions beta_X+beta_Y+beta_Z, and each printed support phase is to be supplied term by term.

The source coordinate x0 is shared by A1, A3, P, and Q, whose twists are 3, 0, 10, and 12. A single X-side linear form must therefore give the same beta_X phase to these occurrences. This forces beta_X to annihilate 3, 10, and 12. Their annihilator is {0,15}, so (B0+B1)beta_X=0.

But the X contribution to the central defect is

    (a+epsilon, epsilon, a+epsilon),

which has rank two. Applying Lambda, as equation (5.2) requires, does not annihilate it. For example a=1, epsilon=0 gives Lambda(1,0,1)=13. This is a contradiction. The complete shared-coordinate checks on Y and Z yield the same annihilator {0,15}.

This second argument has the narrower additive-linear-phase hypothesis. The first argument only assumes that each printed packet contribution is preserved as an individual tensor contribution.

## 3. A straightforward resource replacement does not repair the result

There are twelve generic layer-one packets. In the compressed 128-cost one-row source, their assigned dense modules are seven C3 packets and five D4 packets, with allocated cost

    7*5+5*4 = 55.

Replacing these by twelve independent exact M2 modules of cost seven gives cost 84 for this part. The program expands the seven Strassen products over the integers and checks every coefficient of M2. If every other source charge is retained, the resulting budget is

    16*(128-55+84) = 2512.

This exceeds 2435, the largest integer strictly below 32^(9/4). The exact comparisons are `2435^4 < 32^9 < 2436^4`. Starting from the uncompressed 2128-cost source gives the same arithmetic.

Even 2512 is only an optimistic bookkeeping comparison. Some replaced modules also provide completion endpoints, and a valid replacement must preserve those. The missing row and Weyl coupling must also be implemented by actual side maps. This calculation is not a valid global construction or an exponent bound.

Run the exact check with:

```sh
python research/ai/2026-10-21-sun-local-audit/packet_lift.py --output /tmp/packet-lift.json
```

The output explicitly records that no full-preprint impossibility or improvement claim is made.
