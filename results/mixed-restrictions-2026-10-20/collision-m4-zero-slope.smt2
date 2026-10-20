; benchmark generated from python API
(set-info :status unknown)
(declare-fun xp_0 () Int)
(declare-fun xp_1 () Int)
(declare-fun xp_2 () Int)
(declare-fun xp_3 () Int)
(declare-fun yp_0 () Int)
(declare-fun yp_1 () Int)
(declare-fun yp_2 () Int)
(declare-fun yp_3 () Int)
(declare-fun yp_4 () Int)
(declare-fun yp_5 () Int)
(declare-fun yp_6 () Int)
(declare-fun yp_7 () Int)
(declare-fun yp_8 () Int)
(declare-fun yp_9 () Int)
(declare-fun eta_0 () Real)
(declare-fun eta_3 () Real)
(declare-fun eta_1 () Real)
(declare-fun eta_2 () Real)
(assert
 (let (($x24 (>= xp_0 0)))
 (and $x24 (< xp_0 4))))
(assert
 (let (($x28 (>= xp_1 0)))
 (and $x28 (< xp_1 4))))
(assert
 (let (($x31 (>= xp_2 0)))
 (and $x31 (< xp_2 4))))
(assert
 (let (($x34 (>= xp_3 0)))
 (and $x34 (< xp_3 4))))
(assert
 (and (distinct xp_0 xp_1 xp_2 xp_3) true))
(assert
 (let (($x70 (>= yp_0 0)))
 (and $x70 (< yp_0 10))))
(assert
 (let (($x75 (>= yp_1 0)))
 (and $x75 (< yp_1 10))))
(assert
 (let (($x78 (>= yp_2 0)))
 (and $x78 (< yp_2 10))))
(assert
 (let (($x81 (>= yp_3 0)))
 (and $x81 (< yp_3 10))))
(assert
 (let (($x84 (>= yp_4 0)))
 (and $x84 (< yp_4 10))))
(assert
 (let (($x87 (>= yp_5 0)))
 (and $x87 (< yp_5 10))))
(assert
 (let (($x90 (>= yp_6 0)))
 (and $x90 (< yp_6 10))))
(assert
 (let (($x93 (>= yp_7 0)))
 (and $x93 (< yp_7 10))))
(assert
 (let (($x96 (>= yp_8 0)))
 (and $x96 (< yp_8 10))))
(assert
 (let (($x99 (>= yp_9 0)))
 (and $x99 (< yp_9 10))))
(assert
 (and (distinct yp_0 yp_1 yp_2 yp_3 yp_4 yp_5 yp_6 yp_7 yp_8 yp_9) true))
(assert
 (= eta_0 0.0))
(assert
 (< xp_0 xp_3))
(assert
 (let ((?x157 (+ yp_3 xp_0)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x157) true))))
(assert
 (let ((?x158 (+ yp_4 xp_1)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x158) true))))
(assert
 (let ((?x159 (+ yp_5 xp_2)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x159) true))))
(assert
 (let ((?x160 (+ yp_3 xp_1)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x160) true))))
(assert
 (let ((?x161 (+ yp_4 xp_2)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x161) true))))
(assert
 (let ((?x162 (+ yp_5 xp_3)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x162) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x153 (+ yp_6 xp_0)))
 (and (distinct ?x153 ?x172) true))))
(assert
 (let ((?x157 (+ yp_3 xp_0)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x157) true))))
(assert
 (let ((?x158 (+ yp_4 xp_1)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x158) true))))
(assert
 (let ((?x159 (+ yp_5 xp_2)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x159) true))))
(assert
 (let ((?x160 (+ yp_3 xp_1)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x160) true))))
(assert
 (let ((?x161 (+ yp_4 xp_2)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x161) true))))
(assert
 (let ((?x162 (+ yp_5 xp_3)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x162) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x154 (+ yp_7 xp_1)))
 (and (distinct ?x154 ?x172) true))))
(assert
 (let ((?x157 (+ yp_3 xp_0)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x157) true))))
(assert
 (let ((?x158 (+ yp_4 xp_1)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x158) true))))
(assert
 (let ((?x159 (+ yp_5 xp_2)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x159) true))))
(assert
 (let ((?x160 (+ yp_3 xp_1)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x160) true))))
(assert
 (let ((?x161 (+ yp_4 xp_2)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x161) true))))
(assert
 (let ((?x162 (+ yp_5 xp_3)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x162) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x155 (+ yp_8 xp_2)))
 (and (distinct ?x155 ?x172) true))))
(assert
 (let ((?x157 (+ yp_3 xp_0)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x157) true))))
(assert
 (let ((?x158 (+ yp_4 xp_1)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x158) true))))
(assert
 (let ((?x159 (+ yp_5 xp_2)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x159) true))))
(assert
 (let ((?x160 (+ yp_3 xp_1)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x160) true))))
(assert
 (let ((?x161 (+ yp_4 xp_2)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x161) true))))
(assert
 (let ((?x162 (+ yp_5 xp_3)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x162) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x156 (+ yp_9 xp_3)))
 (and (distinct ?x156 ?x172) true))))
(assert
 (let ((?x160 (+ yp_3 xp_1)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x160) true))))
(assert
 (let ((?x161 (+ yp_4 xp_2)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x161) true))))
(assert
 (let ((?x162 (+ yp_5 xp_3)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x162) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x157 (+ yp_3 xp_0)))
 (and (distinct ?x157 ?x172) true))))
(assert
 (let ((?x160 (+ yp_3 xp_1)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x160) true))))
(assert
 (let ((?x161 (+ yp_4 xp_2)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x161) true))))
(assert
 (let ((?x162 (+ yp_5 xp_3)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x162) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x158 (+ yp_4 xp_1)))
 (and (distinct ?x158 ?x172) true))))
(assert
 (let ((?x160 (+ yp_3 xp_1)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x160) true))))
(assert
 (let ((?x161 (+ yp_4 xp_2)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x161) true))))
(assert
 (let ((?x162 (+ yp_5 xp_3)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x162) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x159 (+ yp_5 xp_2)))
 (and (distinct ?x159 ?x172) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x160 (+ yp_3 xp_1)))
 (and (distinct ?x160 ?x172) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x161 (+ yp_4 xp_2)))
 (and (distinct ?x161 ?x172) true))))
(assert
 (let ((?x163 (+ yp_1 xp_0)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x163) true))))
(assert
 (let ((?x164 (+ yp_2 xp_1)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x164) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x162 (+ yp_5 xp_3)))
 (and (distinct ?x162 ?x172) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x163 (+ yp_1 xp_0)))
 (and (distinct ?x163 ?x172) true))))
(assert
 (let ((?x165 (+ yp_1 xp_1)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x165) true))))
(assert
 (let ((?x166 (+ yp_2 xp_2)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x166) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x164 (+ yp_2 xp_1)))
 (and (distinct ?x164 ?x172) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x165 (+ yp_1 xp_1)))
 (and (distinct ?x165 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x165 (+ yp_1 xp_1)))
 (and (distinct ?x165 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x165 (+ yp_1 xp_1)))
 (and (distinct ?x165 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x165 (+ yp_1 xp_1)))
 (and (distinct ?x165 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x165 (+ yp_1 xp_1)))
 (and (distinct ?x165 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x165 (+ yp_1 xp_1)))
 (and (distinct ?x165 ?x172) true))))
(assert
 (let ((?x167 (+ yp_1 xp_2)))
 (let ((?x166 (+ yp_2 xp_2)))
 (and (distinct ?x166 ?x167) true))))
(assert
 (let ((?x168 (+ yp_2 xp_3)))
 (let ((?x166 (+ yp_2 xp_2)))
 (and (distinct ?x166 ?x168) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x166 (+ yp_2 xp_2)))
 (and (distinct ?x166 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x166 (+ yp_2 xp_2)))
 (and (distinct ?x166 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x166 (+ yp_2 xp_2)))
 (and (distinct ?x166 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x166 (+ yp_2 xp_2)))
 (and (distinct ?x166 ?x172) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x167 (+ yp_1 xp_2)))
 (and (distinct ?x167 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x167 (+ yp_1 xp_2)))
 (and (distinct ?x167 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x167 (+ yp_1 xp_2)))
 (and (distinct ?x167 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x167 (+ yp_1 xp_2)))
 (and (distinct ?x167 ?x172) true))))
(assert
 (let ((?x169 (+ yp_0 xp_0)))
 (let ((?x168 (+ yp_2 xp_3)))
 (and (distinct ?x168 ?x169) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x168 (+ yp_2 xp_3)))
 (and (distinct ?x168 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x168 (+ yp_2 xp_3)))
 (and (distinct ?x168 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x168 (+ yp_2 xp_3)))
 (and (distinct ?x168 ?x172) true))))
(assert
 (let ((?x170 (+ yp_0 xp_1)))
 (let ((?x169 (+ yp_0 xp_0)))
 (and (distinct ?x169 ?x170) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x169 (+ yp_0 xp_0)))
 (and (distinct ?x169 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x169 (+ yp_0 xp_0)))
 (and (distinct ?x169 ?x172) true))))
(assert
 (let ((?x171 (+ yp_0 xp_2)))
 (let ((?x170 (+ yp_0 xp_1)))
 (and (distinct ?x170 ?x171) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x170 (+ yp_0 xp_1)))
 (and (distinct ?x170 ?x172) true))))
(assert
 (let ((?x172 (+ yp_0 xp_3)))
 (let ((?x171 (+ yp_0 xp_2)))
 (and (distinct ?x171 ?x172) true))))
(assert
 (let (($x1197 (= xp_3 3)))
 (let (($x1214 (= xp_2 0)))
 (let (($x1193 (= xp_1 1)))
 (let (($x1217 (= xp_0 2)))
 (let (($x1200 (= xp_3 2)))
 (let (($x1199 (= xp_2 3)))
 (let (($x1211 (= xp_1 0)))
 (let (($x1210 (= xp_0 1)))
 (let (($x1205 (= xp_3 1)))
 (let (($x1195 (= xp_2 2)))
 (let (($x1207 (= xp_1 3)))
 (let (($x1191 (= xp_0 0)))
 (or (and $x1191 $x1193 $x1195 $x1197) (and $x1191 $x1193 $x1199 $x1200) (and $x1191 (= xp_1 2) (= xp_2 1) $x1197) (and $x1191 (= xp_1 2) $x1199 $x1205) (and $x1191 $x1207 (= xp_2 1) $x1200) (and $x1191 $x1207 $x1195 $x1205) (and $x1210 $x1211 $x1195 $x1197) (and $x1210 $x1211 $x1199 $x1200) (and $x1210 (= xp_1 2) $x1214 $x1197) (and $x1210 $x1207 $x1214 $x1200) (and $x1217 $x1211 (= xp_2 1) $x1197) (and $x1217 $x1193 $x1214 $x1197)))))))))))))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_0)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_1)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_2)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_3)) $x1224)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_3)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_3)) $x1244)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_3)) $x1282)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_2)) $x1349)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_0)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_1)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_2)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_3)) $x1224)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_3)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_3)) $x1244)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_3)) $x1282)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_2)) $x1349)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_0)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_1)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_2)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_3)) $x1224)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_3)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_3)) $x1244)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_3)) $x1282)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_2)) $x1349)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_0)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_1)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_2)) $x1224)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1222 (- ?x1221 eta_3)))
 (let (($x1224 (> ?x1222 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_3)) $x1224)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_3)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_0)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_1)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_2)) $x1244)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1242 (- ?x1241 eta_3)))
 (let (($x1244 (> ?x1242 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_3)) $x1244)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_3)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_0)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_1)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_2)) $x1282)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1280 (- ?x1279 eta_3)))
 (let (($x1282 (> ?x1280 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_3)) $x1282)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_2)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_3)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_0)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_1)) $x1349)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1346 (- ?x1345 eta_3)))
 (let (($x1349 (> ?x1346 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_2)) $x1349)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_0)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_1)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_2)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_3)) $x1859)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_3)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_3)) $x1877)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_3)) $x1909)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_3)) $x1939)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_0)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_1)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_2)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_3)) $x1859)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_3)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_3)) $x1877)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_3)) $x1909)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_3)) $x1939)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_0)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_1)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_2)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_3)) $x1859)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_3)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_3)) $x1877)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_3)) $x1909)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_3)) $x1939)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_0)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_1)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_2)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_3)) $x1859)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_3)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_3)) $x1877)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_2)) $x1909)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_3)) $x1939)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_0)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_1)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_2)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_3)) $x1859)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_3)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_3)) $x1877)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_2)) $x1909)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_3)) $x1939)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_0)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_1)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_2)) $x1859)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x1857 (- ?x1221 eta_2)))
 (let (($x1859 (> ?x1857 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_3)) $x1859)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_3)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_0)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_1)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_2)) $x1877)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x1875 (- ?x1241 eta_2)))
 (let (($x1877 (> ?x1875 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_3)) $x1877)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_2)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_3)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_0)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_1)) $x1909)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x1907 (- ?x1279 eta_2)))
 (let (($x1909 (> ?x1907 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_2)) $x1909)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_3)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_0)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_1)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_2)) $x1939)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x1937 (- ?x1345 eta_2)))
 (let (($x1939 (> ?x1937 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_3)) $x1939)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_0)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_1)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_2)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_3)) $x2715)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_2)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_3)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_2)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_3)) $x2733)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_3)) $x2748)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_3)) $x2804)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_0)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_1)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_2)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_3)) $x2715)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_2)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_3)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_2)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_3)) $x2733)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_3)) $x2748)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_3)) $x2804)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_0)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_1)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_2)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_3)) $x2715)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_2)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_3)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_3)) $x2733)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_3)) $x2748)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_3)) $x2804)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_0)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_1)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_2)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_3)) $x2715)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_2)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_3)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_3)) $x2733)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_3)) $x2748)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_3)) $x2804)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_0)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_1)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_2)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_3)) $x2715)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_3)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_2)) $x2733)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_3)) $x2748)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_3)) $x2804)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_0)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_1)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_2)) $x2715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x2713 (- ?x1221 eta_1)))
 (let (($x2715 (> ?x2713 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_3)) $x2715)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_3)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_0)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_1)) $x2733)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x2731 (- ?x1241 eta_1)))
 (let (($x2733 (> ?x2731 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_2)) $x2733)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_3)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_0)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_1)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_2)) $x2748)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x2746 (- ?x1279 eta_1)))
 (let (($x2748 (> ?x2746 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_3)) $x2748)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_3)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_0)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_1)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_2)) $x2804)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x2802 (- ?x1345 eta_1)))
 (let (($x2804 (> ?x2802 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_3)) $x2804)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_1)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_2)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_3)) $x3614)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_3)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_3)) $x3624)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_3)) $x3659)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_3)) $x3715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_0)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_2)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_3)) $x3614)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_3)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_3)) $x3624)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_3)) $x3659)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_3)) $x3715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_0)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_1)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_3)) $x3614)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_3)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_3)) $x3624)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_3)) $x3659)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_3)) $x3715)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_0)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_1)) $x3614)))))
(assert
 (let ((?x1221 (+ 0.0 eta_0)))
 (let ((?x3612 (- ?x1221 eta_0)))
 (let (($x3614 (> ?x3612 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_2)) $x3614)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_3)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_0)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_1)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_2)) $x3624)))))
(assert
 (let ((?x1241 (+ 0.0 eta_1)))
 (let ((?x3622 (- ?x1241 eta_0)))
 (let (($x3624 (> ?x3622 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_3)) $x3624)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_3)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_0)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_1)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_2)) $x3659)))))
(assert
 (let ((?x1279 (+ 0.0 eta_2)))
 (let ((?x3657 (- ?x1279 eta_0)))
 (let (($x3659 (> ?x3657 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_3)) $x3659)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_3)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_0)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_1)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
 (let ((?x3713 (- ?x1345 eta_0)))
 (let (($x3715 (> ?x3713 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_2)) $x3715)))))
(assert
 (let ((?x1345 (+ 0.0 eta_3)))
(let ((?x3713 (- ?x1345 eta_0)))
(let (($x3715 (> ?x3713 0.0)))
(=> (= (+ yp_0 xp_3) (+ yp_9 xp_3)) $x3715)))))
(check-sat)
