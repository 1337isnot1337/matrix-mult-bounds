; benchmark generated from python API
(set-info :status unknown)
(declare-fun xp_0 () Int)
(declare-fun xp_1 () Int)
(declare-fun xp_2 () Int)
(declare-fun xp_3 () Int)
(declare-fun xp_4 () Int)
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
(declare-fun yp_10 () Int)
(declare-fun yp_11 () Int)
(declare-fun yp_12 () Int)
(declare-fun yp_13 () Int)
(declare-fun yp_14 () Int)
(declare-fun eta_0 () Real)
(declare-fun eta_4 () Real)
(declare-fun eta_1 () Real)
(declare-fun eta_2 () Real)
(declare-fun eta_3 () Real)
(assert
 (let (($x31 (>= xp_0 0)))
 (and $x31 (< xp_0 5))))
(assert
 (let (($x35 (>= xp_1 0)))
 (and $x35 (< xp_1 5))))
(assert
 (let (($x38 (>= xp_2 0)))
 (and $x38 (< xp_2 5))))
(assert
 (let (($x41 (>= xp_3 0)))
 (and $x41 (< xp_3 5))))
(assert
 (let (($x44 (>= xp_4 0)))
 (and $x44 (< xp_4 5))))
(assert
 (and (distinct xp_0 xp_1 xp_2 xp_3 xp_4) true))
(assert
 (let (($x84 (>= yp_0 0)))
 (and $x84 (< yp_0 15))))
(assert
 (let (($x89 (>= yp_1 0)))
 (and $x89 (< yp_1 15))))
(assert
 (let (($x92 (>= yp_2 0)))
 (and $x92 (< yp_2 15))))
(assert
 (let (($x95 (>= yp_3 0)))
 (and $x95 (< yp_3 15))))
(assert
 (let (($x98 (>= yp_4 0)))
 (and $x98 (< yp_4 15))))
(assert
 (let (($x101 (>= yp_5 0)))
 (and $x101 (< yp_5 15))))
(assert
 (let (($x104 (>= yp_6 0)))
 (and $x104 (< yp_6 15))))
(assert
 (let (($x107 (>= yp_7 0)))
 (and $x107 (< yp_7 15))))
(assert
 (let (($x110 (>= yp_8 0)))
 (and $x110 (< yp_8 15))))
(assert
 (let (($x113 (>= yp_9 0)))
 (and $x113 (< yp_9 15))))
(assert
 (let (($x116 (>= yp_10 0)))
 (and $x116 (< yp_10 15))))
(assert
 (let (($x119 (>= yp_11 0)))
 (and $x119 (< yp_11 15))))
(assert
 (let (($x122 (>= yp_12 0)))
 (and $x122 (< yp_12 15))))
(assert
 (let (($x125 (>= yp_13 0)))
 (and $x125 (< yp_13 15))))
(assert
 (let (($x128 (>= yp_14 0)))
 (and $x128 (< yp_14 15))))
(assert
 (and (distinct yp_0 yp_1 yp_2 yp_3 yp_4 yp_5 yp_6 yp_7 yp_8 yp_9 yp_10 yp_11 yp_12 yp_13 yp_14) true))
(assert
 (= eta_0 0.0))
(assert
 (< xp_0 xp_4))
(assert
 (let ((?x207 (+ yp_6 xp_0)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x207) true))))
(assert
 (let ((?x208 (+ yp_7 xp_1)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x208) true))))
(assert
 (let ((?x209 (+ yp_8 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x209) true))))
(assert
 (let ((?x210 (+ yp_9 xp_3)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x210) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x202 (+ yp_10 xp_0)))
 (and (distinct ?x202 ?x236) true))))
(assert
 (let ((?x207 (+ yp_6 xp_0)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x207) true))))
(assert
 (let ((?x208 (+ yp_7 xp_1)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x208) true))))
(assert
 (let ((?x209 (+ yp_8 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x209) true))))
(assert
 (let ((?x210 (+ yp_9 xp_3)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x210) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x203 (+ yp_11 xp_1)))
 (and (distinct ?x203 ?x236) true))))
(assert
 (let ((?x207 (+ yp_6 xp_0)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x207) true))))
(assert
 (let ((?x208 (+ yp_7 xp_1)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x208) true))))
(assert
 (let ((?x209 (+ yp_8 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x209) true))))
(assert
 (let ((?x210 (+ yp_9 xp_3)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x210) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x204 (+ yp_12 xp_2)))
 (and (distinct ?x204 ?x236) true))))
(assert
 (let ((?x207 (+ yp_6 xp_0)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x207) true))))
(assert
 (let ((?x208 (+ yp_7 xp_1)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x208) true))))
(assert
 (let ((?x209 (+ yp_8 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x209) true))))
(assert
 (let ((?x210 (+ yp_9 xp_3)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x210) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x205 (+ yp_13 xp_3)))
 (and (distinct ?x205 ?x236) true))))
(assert
 (let ((?x207 (+ yp_6 xp_0)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x207) true))))
(assert
 (let ((?x208 (+ yp_7 xp_1)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x208) true))))
(assert
 (let ((?x209 (+ yp_8 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x209) true))))
(assert
 (let ((?x210 (+ yp_9 xp_3)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x210) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x206 (+ yp_14 xp_4)))
 (and (distinct ?x206 ?x236) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x207 (+ yp_6 xp_0)))
 (and (distinct ?x207 ?x236) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x208 (+ yp_7 xp_1)))
 (and (distinct ?x208 ?x236) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x209 (+ yp_8 xp_2)))
 (and (distinct ?x209 ?x236) true))))
(assert
 (let ((?x211 (+ yp_6 xp_1)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x211) true))))
(assert
 (let ((?x212 (+ yp_7 xp_2)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x212) true))))
(assert
 (let ((?x213 (+ yp_8 xp_3)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x213) true))))
(assert
 (let ((?x214 (+ yp_9 xp_4)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x214) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x210 (+ yp_9 xp_3)))
 (and (distinct ?x210 ?x236) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x211 (+ yp_6 xp_1)))
 (and (distinct ?x211 ?x236) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x212 (+ yp_7 xp_2)))
 (and (distinct ?x212 ?x236) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x213 (+ yp_8 xp_3)))
 (and (distinct ?x213 ?x236) true))))
(assert
 (let ((?x215 (+ yp_3 xp_0)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x215) true))))
(assert
 (let ((?x216 (+ yp_4 xp_1)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x216) true))))
(assert
 (let ((?x217 (+ yp_5 xp_2)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x217) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x214 (+ yp_9 xp_4)))
 (and (distinct ?x214 ?x236) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x215 (+ yp_3 xp_0)))
 (and (distinct ?x215 ?x236) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x216 (+ yp_4 xp_1)))
 (and (distinct ?x216 ?x236) true))))
(assert
 (let ((?x218 (+ yp_3 xp_1)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x218) true))))
(assert
 (let ((?x219 (+ yp_4 xp_2)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x219) true))))
(assert
 (let ((?x220 (+ yp_5 xp_3)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x220) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x217 (+ yp_5 xp_2)))
 (and (distinct ?x217 ?x236) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x218 (+ yp_3 xp_1)))
 (and (distinct ?x218 ?x236) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x219 (+ yp_4 xp_2)))
 (and (distinct ?x219 ?x236) true))))
(assert
 (let ((?x221 (+ yp_3 xp_2)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x221) true))))
(assert
 (let ((?x222 (+ yp_4 xp_3)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x222) true))))
(assert
 (let ((?x223 (+ yp_5 xp_4)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x223) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x220 (+ yp_5 xp_3)))
 (and (distinct ?x220 ?x236) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x221 (+ yp_3 xp_2)))
 (and (distinct ?x221 ?x236) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x222 (+ yp_4 xp_3)))
 (and (distinct ?x222 ?x236) true))))
(assert
 (let ((?x224 (+ yp_1 xp_0)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x224) true))))
(assert
 (let ((?x225 (+ yp_2 xp_1)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x225) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x223 (+ yp_5 xp_4)))
 (and (distinct ?x223 ?x236) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x224 (+ yp_1 xp_0)))
 (and (distinct ?x224 ?x236) true))))
(assert
 (let ((?x226 (+ yp_1 xp_1)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x226) true))))
(assert
 (let ((?x227 (+ yp_2 xp_2)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x227) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x225 (+ yp_2 xp_1)))
 (and (distinct ?x225 ?x236) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x226 (+ yp_1 xp_1)))
 (and (distinct ?x226 ?x236) true))))
(assert
 (let ((?x228 (+ yp_1 xp_2)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x228) true))))
(assert
 (let ((?x229 (+ yp_2 xp_3)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x229) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x227 (+ yp_2 xp_2)))
 (and (distinct ?x227 ?x236) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x228 (+ yp_1 xp_2)))
 (and (distinct ?x228 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x228 (+ yp_1 xp_2)))
 (and (distinct ?x228 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x228 (+ yp_1 xp_2)))
 (and (distinct ?x228 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x228 (+ yp_1 xp_2)))
 (and (distinct ?x228 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x228 (+ yp_1 xp_2)))
 (and (distinct ?x228 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x228 (+ yp_1 xp_2)))
 (and (distinct ?x228 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x228 (+ yp_1 xp_2)))
 (and (distinct ?x228 ?x236) true))))
(assert
 (let ((?x230 (+ yp_1 xp_3)))
 (let ((?x229 (+ yp_2 xp_3)))
 (and (distinct ?x229 ?x230) true))))
(assert
 (let ((?x231 (+ yp_2 xp_4)))
 (let ((?x229 (+ yp_2 xp_3)))
 (and (distinct ?x229 ?x231) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x229 (+ yp_2 xp_3)))
 (and (distinct ?x229 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x229 (+ yp_2 xp_3)))
 (and (distinct ?x229 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x229 (+ yp_2 xp_3)))
 (and (distinct ?x229 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x229 (+ yp_2 xp_3)))
 (and (distinct ?x229 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x229 (+ yp_2 xp_3)))
 (and (distinct ?x229 ?x236) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x230 (+ yp_1 xp_3)))
 (and (distinct ?x230 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x230 (+ yp_1 xp_3)))
 (and (distinct ?x230 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x230 (+ yp_1 xp_3)))
 (and (distinct ?x230 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x230 (+ yp_1 xp_3)))
 (and (distinct ?x230 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x230 (+ yp_1 xp_3)))
 (and (distinct ?x230 ?x236) true))))
(assert
 (let ((?x232 (+ yp_0 xp_0)))
 (let ((?x231 (+ yp_2 xp_4)))
 (and (distinct ?x231 ?x232) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x231 (+ yp_2 xp_4)))
 (and (distinct ?x231 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x231 (+ yp_2 xp_4)))
 (and (distinct ?x231 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x231 (+ yp_2 xp_4)))
 (and (distinct ?x231 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x231 (+ yp_2 xp_4)))
 (and (distinct ?x231 ?x236) true))))
(assert
 (let ((?x233 (+ yp_0 xp_1)))
 (let ((?x232 (+ yp_0 xp_0)))
 (and (distinct ?x232 ?x233) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x232 (+ yp_0 xp_0)))
 (and (distinct ?x232 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x232 (+ yp_0 xp_0)))
 (and (distinct ?x232 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x232 (+ yp_0 xp_0)))
 (and (distinct ?x232 ?x236) true))))
(assert
 (let ((?x234 (+ yp_0 xp_2)))
 (let ((?x233 (+ yp_0 xp_1)))
 (and (distinct ?x233 ?x234) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x233 (+ yp_0 xp_1)))
 (and (distinct ?x233 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x233 (+ yp_0 xp_1)))
 (and (distinct ?x233 ?x236) true))))
(assert
 (let ((?x235 (+ yp_0 xp_3)))
 (let ((?x234 (+ yp_0 xp_2)))
 (and (distinct ?x234 ?x235) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x234 (+ yp_0 xp_2)))
 (and (distinct ?x234 ?x236) true))))
(assert
 (let ((?x236 (+ yp_0 xp_4)))
 (let ((?x235 (+ yp_0 xp_3)))
 (and (distinct ?x235 ?x236) true))))
(assert
 (let (($x3456 (= xp_4 4)))
 (let (($x3464 (= xp_2 1)))
 (let (($x3458 (= xp_1 2)))
 (let (($x3461 (= xp_4 3)))
 (let (($x3465 (= xp_3 4)))
 (let (($x3476 (= xp_2 0)))
 (let (($x3450 (= xp_1 1)))
 (let (($x3478 (= xp_0 2)))
 (let (($x3466 (= xp_4 2)))
 (let (($x3454 (= xp_3 3)))
 (let (($x3459 (= xp_2 4)))
 (let (($x3474 (= xp_1 0)))
 (let (($x3473 (= xp_0 1)))
 (let (($x3470 (= xp_3 2)))
 (let (($x3469 (= xp_2 3)))
 (let (($x3448 (= xp_0 0)))
 (or (and $x3448 $x3450 (= xp_2 2) $x3454 $x3456) (and $x3448 $x3458 $x3459 (= xp_3 1) $x3461) (and $x3448 (= xp_1 3) $x3464 $x3465 $x3466) (and $x3448 (= xp_1 4) $x3469 $x3470 (= xp_4 1)) (and $x3473 $x3474 $x3459 $x3454 $x3466) (and $x3473 (= xp_1 3) $x3476 $x3470 $x3456) (and $x3478 $x3474 $x3469 (= xp_3 1) $x3456) (and $x3478 $x3450 $x3476 $x3465 $x3461) (and (= xp_0 3) $x3458 $x3464 (= xp_3 0) $x3456)))))))))))))))))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x3486 (- ?x3485 eta_4)))
 (let (($x3488 (> ?x3486 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_0)) $x3488)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x3498 (- ?x3497 eta_4)))
 (let (($x3500 (> ?x3498 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_1)) $x3500)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x3511 (- ?x3510 eta_4)))
 (let (($x3513 (> ?x3511 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_2)) $x3513)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x3525 (- ?x3524 eta_4)))
 (let (($x3527 (> ?x3525 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_3)) $x3527)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x3539 (- ?x3538 eta_4)))
 (let (($x3541 (> ?x3539 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_4)) $x3541)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_0)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_1)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_2)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_3)) $x3587)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x3597 (- ?x3596 eta_4)))
 (let (($x3600 (> ?x3597 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_4)) $x3600)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x3613 (- ?x3612 eta_4)))
 (let (($x3616 (> ?x3613 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_0)) $x3616)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_1)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_2)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_3)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_4)) $x3587)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_0)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_1)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_2)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_3)) $x3677)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x3690 (- ?x3689 eta_4)))
 (let (($x3693 (> ?x3690 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_4)) $x3693)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_0)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_1)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_2)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_3)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_4)) $x3677)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x3738 (- ?x3737 eta_4)))
 (let (($x3741 (> ?x3738 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_0)) $x3741)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_1)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_2)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_3)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_4)) $x3664)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_0)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_1)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_2)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_3)) $x3810)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x3823 (- ?x3822 eta_4)))
 (let (($x3826 (> ?x3823 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_4)) $x3826)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_0)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_1)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_2)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_3)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_4)) $x3810)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_0)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_1)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_2)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_3)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_4)) $x3794)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x3911 (- ?x3910 eta_4)))
 (let (($x3914 (> ?x3911 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_0)) $x3914)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_1)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_2)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_3)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_4)) $x3781)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_1)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_2)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_3)) $x3968)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x3974 (- ?x3973 eta_4)))
 (let (($x3977 (> ?x3974 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_4)) $x3977)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_0)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_2)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_3)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_4)) $x3968)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_0)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_1)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_3)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_4)) $x3959)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_0)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_1)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_2)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_4)) $x3950)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x4056 (- ?x4055 eta_4)))
 (let (($x4058 (> ?x4056 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_0)) $x4058)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_1)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_2)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_3)) $x3986)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x3486 (- ?x3485 eta_4)))
 (let (($x3488 (> ?x3486 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_0)) $x3488)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x3498 (- ?x3497 eta_4)))
 (let (($x3500 (> ?x3498 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_1)) $x3500)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x3511 (- ?x3510 eta_4)))
 (let (($x3513 (> ?x3511 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_2)) $x3513)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x3525 (- ?x3524 eta_4)))
 (let (($x3527 (> ?x3525 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_3)) $x3527)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x3539 (- ?x3538 eta_4)))
 (let (($x3541 (> ?x3539 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_4)) $x3541)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_0)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_1)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_2)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_3)) $x3587)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x3597 (- ?x3596 eta_4)))
 (let (($x3600 (> ?x3597 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_4)) $x3600)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x3613 (- ?x3612 eta_4)))
 (let (($x3616 (> ?x3613 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_0)) $x3616)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_1)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_2)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_3)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_4)) $x3587)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_0)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_1)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_2)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_3)) $x3677)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x3690 (- ?x3689 eta_4)))
 (let (($x3693 (> ?x3690 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_4)) $x3693)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_0)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_1)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_2)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_3)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_4)) $x3677)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x3738 (- ?x3737 eta_4)))
 (let (($x3741 (> ?x3738 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_0)) $x3741)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_1)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_2)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_3)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_4)) $x3664)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_0)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_1)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_2)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_3)) $x3810)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x3823 (- ?x3822 eta_4)))
 (let (($x3826 (> ?x3823 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_4)) $x3826)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_0)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_1)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_2)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_3)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_4)) $x3810)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_0)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_1)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_2)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_3)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_4)) $x3794)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x3911 (- ?x3910 eta_4)))
 (let (($x3914 (> ?x3911 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_0)) $x3914)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_1)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_2)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_3)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_4)) $x3781)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_1)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_2)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_3)) $x3968)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x3974 (- ?x3973 eta_4)))
 (let (($x3977 (> ?x3974 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_4)) $x3977)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_0)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_2)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_3)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_4)) $x3968)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_0)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_1)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_3)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_4)) $x3959)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_0)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_1)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_2)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_4)) $x3950)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x4056 (- ?x4055 eta_4)))
 (let (($x4058 (> ?x4056 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_0)) $x4058)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_1)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_2)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_3)) $x3986)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x3486 (- ?x3485 eta_4)))
 (let (($x3488 (> ?x3486 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_0)) $x3488)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x3498 (- ?x3497 eta_4)))
 (let (($x3500 (> ?x3498 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_1)) $x3500)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x3511 (- ?x3510 eta_4)))
 (let (($x3513 (> ?x3511 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_2)) $x3513)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x3525 (- ?x3524 eta_4)))
 (let (($x3527 (> ?x3525 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_3)) $x3527)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x3539 (- ?x3538 eta_4)))
 (let (($x3541 (> ?x3539 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_4)) $x3541)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_0)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_1)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_2)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_3)) $x3587)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x3597 (- ?x3596 eta_4)))
 (let (($x3600 (> ?x3597 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_4)) $x3600)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x3613 (- ?x3612 eta_4)))
 (let (($x3616 (> ?x3613 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_0)) $x3616)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_1)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_2)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_3)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_4)) $x3587)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_0)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_1)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_2)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_3)) $x3677)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x3690 (- ?x3689 eta_4)))
 (let (($x3693 (> ?x3690 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_4)) $x3693)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_0)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_1)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_2)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_3)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_4)) $x3677)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x3738 (- ?x3737 eta_4)))
 (let (($x3741 (> ?x3738 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_0)) $x3741)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_1)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_2)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_3)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_4)) $x3664)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_0)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_1)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_2)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_3)) $x3810)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x3823 (- ?x3822 eta_4)))
 (let (($x3826 (> ?x3823 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_4)) $x3826)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_0)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_1)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_2)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_3)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_4)) $x3810)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_0)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_1)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_2)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_3)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_4)) $x3794)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x3911 (- ?x3910 eta_4)))
 (let (($x3914 (> ?x3911 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_0)) $x3914)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_1)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_2)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_3)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_4)) $x3781)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_1)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_2)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_3)) $x3968)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x3974 (- ?x3973 eta_4)))
 (let (($x3977 (> ?x3974 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_4)) $x3977)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_0)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_2)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_3)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_4)) $x3968)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_0)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_1)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_3)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_4)) $x3959)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_0)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_1)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_2)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_4)) $x3950)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x4056 (- ?x4055 eta_4)))
 (let (($x4058 (> ?x4056 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_0)) $x4058)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_1)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_2)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_3)) $x3986)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x3486 (- ?x3485 eta_4)))
 (let (($x3488 (> ?x3486 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_0)) $x3488)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x3498 (- ?x3497 eta_4)))
 (let (($x3500 (> ?x3498 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_1)) $x3500)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x3511 (- ?x3510 eta_4)))
 (let (($x3513 (> ?x3511 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_2)) $x3513)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x3525 (- ?x3524 eta_4)))
 (let (($x3527 (> ?x3525 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_3)) $x3527)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x3539 (- ?x3538 eta_4)))
 (let (($x3541 (> ?x3539 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_4)) $x3541)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_0)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_1)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_2)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_3)) $x3587)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x3597 (- ?x3596 eta_4)))
 (let (($x3600 (> ?x3597 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_4)) $x3600)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x3613 (- ?x3612 eta_4)))
 (let (($x3616 (> ?x3613 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_0)) $x3616)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_1)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_2)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_3)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_4)) $x3587)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_0)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_1)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_2)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_3)) $x3677)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x3690 (- ?x3689 eta_4)))
 (let (($x3693 (> ?x3690 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_4)) $x3693)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_0)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_1)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_2)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_3)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_4)) $x3677)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x3738 (- ?x3737 eta_4)))
 (let (($x3741 (> ?x3738 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_0)) $x3741)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_1)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_2)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_3)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_4)) $x3664)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_0)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_1)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_2)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_3)) $x3810)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x3823 (- ?x3822 eta_4)))
 (let (($x3826 (> ?x3823 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_4)) $x3826)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_0)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_1)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_2)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_3)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_4)) $x3810)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_0)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_1)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_2)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_3)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_4)) $x3794)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x3911 (- ?x3910 eta_4)))
 (let (($x3914 (> ?x3911 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_0)) $x3914)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_1)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_2)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_3)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_4)) $x3781)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_1)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_2)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_3)) $x3968)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x3974 (- ?x3973 eta_4)))
 (let (($x3977 (> ?x3974 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_4)) $x3977)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_0)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_2)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_3)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_4)) $x3968)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_0)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_1)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_3)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_4)) $x3959)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_0)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_1)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_2)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_4)) $x3950)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x4056 (- ?x4055 eta_4)))
 (let (($x4058 (> ?x4056 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_0)) $x4058)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_1)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_2)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_3)) $x3986)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x3486 (- ?x3485 eta_4)))
 (let (($x3488 (> ?x3486 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_0)) $x3488)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x3498 (- ?x3497 eta_4)))
 (let (($x3500 (> ?x3498 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_1)) $x3500)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x3511 (- ?x3510 eta_4)))
 (let (($x3513 (> ?x3511 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_2)) $x3513)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x3525 (- ?x3524 eta_4)))
 (let (($x3527 (> ?x3525 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_3)) $x3527)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x3539 (- ?x3538 eta_4)))
 (let (($x3541 (> ?x3539 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_4)) $x3541)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_0)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_1)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_2)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_3)) $x3587)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x3597 (- ?x3596 eta_4)))
 (let (($x3600 (> ?x3597 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_4)) $x3600)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x3613 (- ?x3612 eta_4)))
 (let (($x3616 (> ?x3613 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_0)) $x3616)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x3552 (- ?x3551 eta_4)))
 (let (($x3554 (> ?x3552 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_1)) $x3554)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x3561 (- ?x3560 eta_4)))
 (let (($x3563 (> ?x3561 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_2)) $x3563)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x3573 (- ?x3572 eta_4)))
 (let (($x3575 (> ?x3573 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_3)) $x3575)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x3585 (- ?x3584 eta_4)))
 (let (($x3587 (> ?x3585 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_4)) $x3587)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_0)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_1)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_2)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_3)) $x3677)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x3690 (- ?x3689 eta_4)))
 (let (($x3693 (> ?x3690 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_4)) $x3693)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_0)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_1)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_2)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_3)) $x3664)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x3674 (- ?x3673 eta_4)))
 (let (($x3677 (> ?x3674 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_4)) $x3677)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x3738 (- ?x3737 eta_4)))
 (let (($x3741 (> ?x3738 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_0)) $x3741)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x3706 (- ?x3705 eta_4)))
 (let (($x3709 (> ?x3706 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_1)) $x3709)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x3641 (- ?x3640 eta_4)))
 (let (($x3643 (> ?x3641 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_2)) $x3643)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x3650 (- ?x3649 eta_4)))
 (let (($x3652 (> ?x3650 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_3)) $x3652)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x3662 (- ?x3661 eta_4)))
 (let (($x3664 (> ?x3662 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_4)) $x3664)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_0)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_1)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_2)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_3)) $x3810)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x3823 (- ?x3822 eta_4)))
 (let (($x3826 (> ?x3823 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_4)) $x3826)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_0)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_1)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_2)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_3)) $x3794)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x3807 (- ?x3806 eta_4)))
 (let (($x3810 (> ?x3807 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_4)) $x3810)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_0)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_1)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_2)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_3)) $x3781)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x3791 (- ?x3790 eta_4)))
 (let (($x3794 (> ?x3791 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_4)) $x3794)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x3911 (- ?x3910 eta_4)))
 (let (($x3914 (> ?x3911 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_0)) $x3914)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x3875 (- ?x3874 eta_4)))
 (let (($x3878 (> ?x3875 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_1)) $x3878)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x3839 (- ?x3838 eta_4)))
 (let (($x3842 (> ?x3839 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_2)) $x3842)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x3770 (- ?x3769 eta_4)))
 (let (($x3772 (> ?x3770 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_3)) $x3772)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x3779 (- ?x3778 eta_4)))
 (let (($x3781 (> ?x3779 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_4)) $x3781)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_1)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_2)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_3)) $x3968)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x3974 (- ?x3973 eta_4)))
 (let (($x3977 (> ?x3974 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_4)) $x3977)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_0)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_2)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_3)) $x3959)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x3965 (- ?x3964 eta_4)))
 (let (($x3968 (> ?x3965 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_4)) $x3968)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_0)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_1)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_3)) $x3950)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x3956 (- ?x3955 eta_4)))
 (let (($x3959 (> ?x3956 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_4)) $x3959)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_0)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_1)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_2)) $x3986)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x3947 (- ?x3946 eta_4)))
 (let (($x3950 (> ?x3947 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_4)) $x3950)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x4056 (- ?x4055 eta_4)))
 (let (($x4058 (> ?x4056 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_0)) $x4058)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x4029 (- ?x4028 eta_4)))
 (let (($x4031 (> ?x4029 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_1)) $x4031)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x4005 (- ?x4004 eta_4)))
 (let (($x4007 (> ?x4005 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_2)) $x4007)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x3983 (- ?x3982 eta_4)))
 (let (($x3986 (> ?x3983 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_3)) $x3986)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_0)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_1)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_2)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_3)) $x5247)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x5256 (- ?x3538 eta_3)))
 (let (($x5258 (> ?x5256 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_4)) $x5258)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_0)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_1)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_2)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_3)) $x5299)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x5308 (- ?x3596 eta_3)))
 (let (($x5310 (> ?x5308 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_4)) $x5310)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_4)) $x5299)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_0)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_1)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_2)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_3)) $x5377)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x5389 (- ?x3689 eta_3)))
 (let (($x5391 (> ?x5389 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_4)) $x5391)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_4)) $x5366)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_1)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_2)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_3)) $x5470)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x5473 (- ?x3822 eta_3)))
 (let (($x5475 (> ?x5473 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_4)) $x5475)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_4)) $x5460)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_0)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_1)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_2)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_3)) $x5568)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x5580 (- ?x3973 eta_3)))
 (let (($x5582 (> ?x5580 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_4)) $x5582)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_4)) $x5529)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_0)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_1)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_2)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_3)) $x5247)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x5256 (- ?x3538 eta_3)))
 (let (($x5258 (> ?x5256 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_4)) $x5258)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_0)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_1)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_2)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_3)) $x5299)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x5308 (- ?x3596 eta_3)))
 (let (($x5310 (> ?x5308 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_4)) $x5310)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_4)) $x5299)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_0)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_1)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_2)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_3)) $x5377)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x5389 (- ?x3689 eta_3)))
 (let (($x5391 (> ?x5389 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_4)) $x5391)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_4)) $x5366)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_1)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_2)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_3)) $x5470)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x5473 (- ?x3822 eta_3)))
 (let (($x5475 (> ?x5473 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_4)) $x5475)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_4)) $x5460)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_0)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_1)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_2)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_3)) $x5568)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x5580 (- ?x3973 eta_3)))
 (let (($x5582 (> ?x5580 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_4)) $x5582)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_4)) $x5529)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_0)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_1)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_2)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_3)) $x5247)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x5256 (- ?x3538 eta_3)))
 (let (($x5258 (> ?x5256 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_4)) $x5258)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_0)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_1)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_2)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_3)) $x5299)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x5308 (- ?x3596 eta_3)))
 (let (($x5310 (> ?x5308 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_4)) $x5310)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_4)) $x5299)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_0)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_1)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_2)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_3)) $x5377)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x5389 (- ?x3689 eta_3)))
 (let (($x5391 (> ?x5389 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_4)) $x5391)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_4)) $x5366)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_1)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_2)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_3)) $x5470)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x5473 (- ?x3822 eta_3)))
 (let (($x5475 (> ?x5473 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_4)) $x5475)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_4)) $x5460)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_0)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_1)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_2)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_3)) $x5568)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x5580 (- ?x3973 eta_3)))
 (let (($x5582 (> ?x5580 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_4)) $x5582)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_4)) $x5529)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_0)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_1)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_2)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_3)) $x5247)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x5256 (- ?x3538 eta_3)))
 (let (($x5258 (> ?x5256 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_4)) $x5258)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_0)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_1)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_2)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_3)) $x5299)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x5308 (- ?x3596 eta_3)))
 (let (($x5310 (> ?x5308 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_4)) $x5310)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_4)) $x5299)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_0)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_1)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_2)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_3)) $x5377)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x5389 (- ?x3689 eta_3)))
 (let (($x5391 (> ?x5389 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_4)) $x5391)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_4)) $x5366)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_1)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_2)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_3)) $x5470)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x5473 (- ?x3822 eta_3)))
 (let (($x5475 (> ?x5473 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_4)) $x5475)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_4)) $x5460)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_0)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_1)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_2)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_3)) $x5568)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x5580 (- ?x3973 eta_3)))
 (let (($x5582 (> ?x5580 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_4)) $x5582)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_4)) $x5529)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x6557 (- ?x6556 eta_3)))
 (let (($x6559 (> ?x6557 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_0)) $x6559)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_1)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_2)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_3)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_4)) $x5247)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_4)) $x5299)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x6597 (- ?x6596 eta_3)))
 (let (($x6599 (> ?x6597 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_0)) $x6599)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_1)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_2)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_3)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_4)) $x5288)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_4)) $x5366)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x6663 (- ?x6662 eta_3)))
 (let (($x6665 (> ?x6663 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_0)) $x6665)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_1)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_2)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_3)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_4)) $x5355)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_4)) $x5460)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x6719 (- ?x6718 eta_3)))
 (let (($x6721 (> ?x6719 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_0)) $x6721)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_1)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_2)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_3)) $x5480)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_4)) $x5529)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x6833 (- ?x6832 eta_3)))
 (let (($x6835 (> ?x6833 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_0)) $x6835)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_1)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_2)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_3)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_4)) $x5596)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x6557 (- ?x6556 eta_3)))
 (let (($x6559 (> ?x6557 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_0)) $x6559)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_1)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_2)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_3)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_4)) $x5247)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_4)) $x5299)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x6597 (- ?x6596 eta_3)))
 (let (($x6599 (> ?x6597 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_0)) $x6599)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_1)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_2)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_3)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_4)) $x5288)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_4)) $x5366)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x6663 (- ?x6662 eta_3)))
 (let (($x6665 (> ?x6663 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_0)) $x6665)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_1)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_2)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_3)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_4)) $x5355)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_4)) $x5460)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x6719 (- ?x6718 eta_3)))
 (let (($x6721 (> ?x6719 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_0)) $x6721)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_1)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_2)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_3)) $x5480)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_4)) $x5529)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x6833 (- ?x6832 eta_3)))
 (let (($x6835 (> ?x6833 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_0)) $x6835)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_1)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_2)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_3)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_4)) $x5596)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x6557 (- ?x6556 eta_3)))
 (let (($x6559 (> ?x6557 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_0)) $x6559)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_1)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_2)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_3)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_4)) $x5247)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_4)) $x5299)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x6597 (- ?x6596 eta_3)))
 (let (($x6599 (> ?x6597 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_0)) $x6599)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_1)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_2)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_3)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_4)) $x5288)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_4)) $x5366)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x6663 (- ?x6662 eta_3)))
 (let (($x6665 (> ?x6663 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_0)) $x6665)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_1)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_2)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_3)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_4)) $x5355)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_4)) $x5460)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x6719 (- ?x6718 eta_3)))
 (let (($x6721 (> ?x6719 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_0)) $x6721)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_1)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_2)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_3)) $x5480)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_4)) $x5529)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x6833 (- ?x6832 eta_3)))
 (let (($x6835 (> ?x6833 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_0)) $x6835)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_1)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_2)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_3)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_4)) $x5596)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x6557 (- ?x6556 eta_3)))
 (let (($x6559 (> ?x6557 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_0)) $x6559)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x5214 (- ?x3485 eta_3)))
 (let (($x5216 (> ?x5214 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_1)) $x5216)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x5223 (- ?x3497 eta_3)))
 (let (($x5225 (> ?x5223 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_2)) $x5225)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x5234 (- ?x3510 eta_3)))
 (let (($x5236 (> ?x5234 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_3)) $x5236)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x5245 (- ?x3524 eta_3)))
 (let (($x5247 (> ?x5245 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_4)) $x5247)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_0)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_1)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_2)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_3)) $x5288)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x5297 (- ?x3584 eta_3)))
 (let (($x5299 (> ?x5297 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_4)) $x5299)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x6597 (- ?x6596 eta_3)))
 (let (($x6599 (> ?x6597 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_0)) $x6599)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x5322 (- ?x3612 eta_3)))
 (let (($x5324 (> ?x5322 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_1)) $x5324)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x5267 (- ?x3551 eta_3)))
 (let (($x5269 (> ?x5267 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_2)) $x5269)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x5275 (- ?x3560 eta_3)))
 (let (($x5277 (> ?x5275 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_3)) $x5277)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x5286 (- ?x3572 eta_3)))
 (let (($x5288 (> ?x5286 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_4)) $x5288)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_0)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_1)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_2)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_3)) $x5366)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x5375 (- ?x3673 eta_3)))
 (let (($x5377 (> ?x5375 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_4)) $x5377)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_0)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_1)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_2)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_3)) $x5355)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x5364 (- ?x3661 eta_3)))
 (let (($x5366 (> ?x5364 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_4)) $x5366)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x6663 (- ?x6662 eta_3)))
 (let (($x6665 (> ?x6663 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_0)) $x6665)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x5429 (- ?x3737 eta_3)))
 (let (($x5431 (> ?x5429 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_1)) $x5431)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x5403 (- ?x3705 eta_3)))
 (let (($x5405 (> ?x5403 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_2)) $x5405)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x5345 (- ?x3640 eta_3)))
 (let (($x5347 (> ?x5345 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_3)) $x5347)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x5353 (- ?x3649 eta_3)))
 (let (($x5355 (> ?x5353 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_4)) $x5355)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_0)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_2)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_3)) $x5465)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x5468 (- ?x3806 eta_3)))
 (let (($x5470 (> ?x5468 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_4)) $x5470)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_0)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_1)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_3)) $x5460)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x5463 (- ?x3790 eta_3)))
 (let (($x5465 (> ?x5463 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_4)) $x5465)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_0)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_1)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_2)) $x5480)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x5458 (- ?x3778 eta_3)))
 (let (($x5460 (> ?x5458 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_4)) $x5460)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x6719 (- ?x6718 eta_3)))
 (let (($x6721 (> ?x6719 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_0)) $x6721)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x5506 (- ?x3910 eta_3)))
 (let (($x5508 (> ?x5506 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_1)) $x5508)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x5489 (- ?x3874 eta_3)))
 (let (($x5491 (> ?x5489 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_2)) $x5491)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x5478 (- ?x3838 eta_3)))
 (let (($x5480 (> ?x5478 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_3)) $x5480)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_0)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_1)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_2)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_3)) $x5554)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x5566 (- ?x3964 eta_3)))
 (let (($x5568 (> ?x5566 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_4)) $x5568)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_0)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_1)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_2)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_3)) $x5540)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x5552 (- ?x3955 eta_3)))
 (let (($x5554 (> ?x5552 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_4)) $x5554)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_0)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_1)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_2)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_3)) $x5529)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x5538 (- ?x3946 eta_3)))
 (let (($x5540 (> ?x5538 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_4)) $x5540)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_0)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_1)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_2)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_3)) $x5596)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x5527 (- ?x5526 eta_3)))
 (let (($x5529 (> ?x5527 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_4)) $x5529)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x6833 (- ?x6832 eta_3)))
 (let (($x6835 (> ?x6833 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_0)) $x6835)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x5690 (- ?x4055 eta_3)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_1)) $x5692)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x5658 (- ?x4028 eta_3)))
 (let (($x5660 (> ?x5658 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_2)) $x5660)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x5626 (- ?x4004 eta_3)))
 (let (($x5628 (> ?x5626 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_3)) $x5628)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x5594 (- ?x3982 eta_3)))
 (let (($x5596 (> ?x5594 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_4)) $x5596)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_0)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_1)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_2)) $x7682)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x7691 (- ?x3524 eta_2)))
 (let (($x7693 (> ?x7691 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_3)) $x7693)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x7702 (- ?x3538 eta_2)))
 (let (($x7704 (> ?x7702 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_4)) $x7704)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_0)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_1)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_2)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_3)) $x7745)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x7754 (- ?x3596 eta_2)))
 (let (($x7756 (> ?x7754 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_4)) $x7756)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_0)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_1)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_2)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_3)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_4)) $x7745)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_1)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_2)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_3)) $x7803)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x7806 (- ?x3689 eta_2)))
 (let (($x7808 (> ?x7806 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_4)) $x7808)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_0)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_2)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_3)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_4)) $x7803)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_4)) $x7798)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_0)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_1)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_2)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_3)) $x7874)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x7886 (- ?x3822 eta_2)))
 (let (($x7888 (> ?x7886 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_4)) $x7888)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_0)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_1)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_2)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_3)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_4)) $x7874)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_4)) $x7849)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_0)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_1)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_2)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_3)) $x8028)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x8040 (- ?x3973 eta_2)))
 (let (($x8042 (> ?x8040 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_4)) $x8042)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_0)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_1)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_2)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_3)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_4)) $x8028)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_4)) $x7989)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_0)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_1)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_2)) $x7682)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x7691 (- ?x3524 eta_2)))
 (let (($x7693 (> ?x7691 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_3)) $x7693)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x7702 (- ?x3538 eta_2)))
 (let (($x7704 (> ?x7702 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_4)) $x7704)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_0)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_1)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_2)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_3)) $x7745)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x7754 (- ?x3596 eta_2)))
 (let (($x7756 (> ?x7754 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_4)) $x7756)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_0)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_1)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_2)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_3)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_4)) $x7745)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_1)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_2)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_3)) $x7803)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x7806 (- ?x3689 eta_2)))
 (let (($x7808 (> ?x7806 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_4)) $x7808)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_0)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_2)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_3)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_4)) $x7803)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_4)) $x7798)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_0)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_1)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_2)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_3)) $x7874)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x7886 (- ?x3822 eta_2)))
 (let (($x7888 (> ?x7886 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_4)) $x7888)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_0)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_1)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_2)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_3)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_4)) $x7874)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_4)) $x7849)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_0)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_1)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_2)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_3)) $x8028)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x8040 (- ?x3973 eta_2)))
 (let (($x8042 (> ?x8040 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_4)) $x8042)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_0)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_1)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_2)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_3)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_4)) $x8028)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_4)) $x7989)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_0)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_1)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_2)) $x7682)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x7691 (- ?x3524 eta_2)))
 (let (($x7693 (> ?x7691 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_3)) $x7693)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x7702 (- ?x3538 eta_2)))
 (let (($x7704 (> ?x7702 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_4)) $x7704)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_0)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_1)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_2)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_3)) $x7745)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x7754 (- ?x3596 eta_2)))
 (let (($x7756 (> ?x7754 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_4)) $x7756)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_0)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_1)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_2)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_3)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_4)) $x7745)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_1)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_2)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_3)) $x7803)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x7806 (- ?x3689 eta_2)))
 (let (($x7808 (> ?x7806 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_4)) $x7808)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_0)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_2)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_3)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_4)) $x7803)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_4)) $x7798)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_0)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_1)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_2)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_3)) $x7874)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x7886 (- ?x3822 eta_2)))
 (let (($x7888 (> ?x7886 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_4)) $x7888)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_0)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_1)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_2)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_3)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_4)) $x7874)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_4)) $x7849)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_0)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_1)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_2)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_3)) $x8028)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x8040 (- ?x3973 eta_2)))
 (let (($x8042 (> ?x8040 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_4)) $x8042)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_0)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_1)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_2)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_3)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_4)) $x8028)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_4)) $x7989)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x8764 (- ?x6556 eta_2)))
 (let (($x8766 (> ?x8764 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_0)) $x8766)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_1)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_2)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_3)) $x7682)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x7691 (- ?x3524 eta_2)))
 (let (($x7693 (> ?x7691 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_4)) $x7693)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_0)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_1)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_2)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_3)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_4)) $x7745)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_0)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_1)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_2)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_3)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_4)) $x7734)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_0)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_2)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_3)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_4)) $x7803)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_4)) $x7798)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_0)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_1)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_2)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_4)) $x7793)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_0)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_1)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_2)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_3)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_4)) $x7874)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_4)) $x7849)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_0)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_1)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_2)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_3)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_4)) $x7838)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_0)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_1)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_2)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_3)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_4)) $x8028)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_4)) $x7989)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_0)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_1)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_2)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_3)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_4)) $x8056)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x8764 (- ?x6556 eta_2)))
 (let (($x8766 (> ?x8764 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_0)) $x8766)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_1)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_2)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_3)) $x7682)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x7691 (- ?x3524 eta_2)))
 (let (($x7693 (> ?x7691 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_4)) $x7693)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_0)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_1)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_2)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_3)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_4)) $x7745)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_0)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_1)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_2)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_3)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_4)) $x7734)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_0)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_2)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_3)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_4)) $x7803)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_4)) $x7798)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_0)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_1)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_2)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_4)) $x7793)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_0)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_1)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_2)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_3)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_4)) $x7874)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_4)) $x7849)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_0)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_1)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_2)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_3)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_4)) $x7838)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_0)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_1)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_2)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_3)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_4)) $x8028)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_4)) $x7989)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_0)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_1)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_2)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_3)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_4)) $x8056)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x8764 (- ?x6556 eta_2)))
 (let (($x8766 (> ?x8764 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_0)) $x8766)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_1)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_2)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_3)) $x7682)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x7691 (- ?x3524 eta_2)))
 (let (($x7693 (> ?x7691 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_4)) $x7693)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_0)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_1)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_2)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_3)) $x7734)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x7743 (- ?x3584 eta_2)))
 (let (($x7745 (> ?x7743 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_4)) $x7745)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_0)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_1)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_2)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_3)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_4)) $x7734)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_0)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_2)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_3)) $x7798)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x7801 (- ?x3673 eta_2)))
 (let (($x7803 (> ?x7801 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_4)) $x7803)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_4)) $x7798)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_0)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_1)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_2)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_4)) $x7793)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_0)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_1)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_2)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_3)) $x7860)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x7872 (- ?x3806 eta_2)))
 (let (($x7874 (> ?x7872 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_4)) $x7874)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_4)) $x7849)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_0)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_1)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_2)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_3)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_4)) $x7838)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_0)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_1)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_2)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_3)) $x8014)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x8026 (- ?x3964 eta_2)))
 (let (($x8028 (> ?x8026 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_4)) $x8028)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_4)) $x7989)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_0)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_1)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_2)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_3)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_4)) $x8056)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x9643 (- ?x9642 eta_2)))
 (let (($x9645 (> ?x9643 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_0)) $x9645)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x8764 (- ?x6556 eta_2)))
 (let (($x8766 (> ?x8764 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_1)) $x8766)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_2)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_3)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_4)) $x7682)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_0)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_1)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_2)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_3)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_4)) $x7734)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x9683 (- ?x9682 eta_2)))
 (let (($x9685 (> ?x9683 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_0)) $x9685)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_1)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_2)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_3)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_4)) $x7723)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_4)) $x7798)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_0)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_1)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_2)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_4)) $x7793)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x9728 (- ?x9727 eta_2)))
 (let (($x9730 (> ?x9728 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_0)) $x9730)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_1)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_2)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_3)) $x7813)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_4)) $x7849)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_0)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_1)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_2)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_3)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_4)) $x7838)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x9812 (- ?x9811 eta_2)))
 (let (($x9814 (> ?x9812 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_0)) $x9814)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_1)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_2)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_3)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_4)) $x7902)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_4)) $x7989)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_0)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_1)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_2)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_3)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_4)) $x8056)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x9937 (- ?x9936 eta_2)))
 (let (($x9939 (> ?x9937 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_0)) $x9939)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_1)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_2)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_3)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_4)) $x8088)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x9643 (- ?x9642 eta_2)))
 (let (($x9645 (> ?x9643 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_0)) $x9645)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x8764 (- ?x6556 eta_2)))
 (let (($x8766 (> ?x8764 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_1)) $x8766)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_2)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_3)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_4)) $x7682)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_0)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_1)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_2)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_3)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_4)) $x7734)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x9683 (- ?x9682 eta_2)))
 (let (($x9685 (> ?x9683 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_0)) $x9685)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_1)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_2)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_3)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_4)) $x7723)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_4)) $x7798)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_0)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_1)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_2)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_4)) $x7793)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x9728 (- ?x9727 eta_2)))
 (let (($x9730 (> ?x9728 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_0)) $x9730)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_1)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_2)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_3)) $x7813)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_4)) $x7849)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_0)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_1)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_2)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_3)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_4)) $x7838)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x9812 (- ?x9811 eta_2)))
 (let (($x9814 (> ?x9812 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_0)) $x9814)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_1)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_2)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_3)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_4)) $x7902)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_4)) $x7989)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_0)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_1)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_2)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_3)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_4)) $x8056)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x9937 (- ?x9936 eta_2)))
 (let (($x9939 (> ?x9937 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_0)) $x9939)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_1)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_2)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_3)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_4)) $x8088)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x9643 (- ?x9642 eta_2)))
 (let (($x9645 (> ?x9643 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_0)) $x9645)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x8764 (- ?x6556 eta_2)))
 (let (($x8766 (> ?x8764 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_1)) $x8766)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x7660 (- ?x3485 eta_2)))
 (let (($x7662 (> ?x7660 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_2)) $x7662)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x7669 (- ?x3497 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_3)) $x7671)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x7680 (- ?x3510 eta_2)))
 (let (($x7682 (> ?x7680 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_4)) $x7682)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_0)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_1)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_2)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_3)) $x7723)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x7732 (- ?x3572 eta_2)))
 (let (($x7734 (> ?x7732 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_4)) $x7734)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x9683 (- ?x9682 eta_2)))
 (let (($x9685 (> ?x9683 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_0)) $x9685)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x8803 (- ?x6596 eta_2)))
 (let (($x8805 (> ?x8803 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_1)) $x8805)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x7768 (- ?x3612 eta_2)))
 (let (($x7770 (> ?x7768 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_2)) $x7770)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x7713 (- ?x3551 eta_2)))
 (let (($x7715 (> ?x7713 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_3)) $x7715)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x7721 (- ?x3560 eta_2)))
 (let (($x7723 (> ?x7721 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_4)) $x7723)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_0)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_1)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_3)) $x7793)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x7796 (- ?x3661 eta_2)))
 (let (($x7798 (> ?x7796 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_4)) $x7798)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_0)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_1)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_2)) $x7813)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x7791 (- ?x3649 eta_2)))
 (let (($x7793 (> ?x7791 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_4)) $x7793)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x9728 (- ?x9727 eta_2)))
 (let (($x9730 (> ?x9728 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_0)) $x9730)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x8847 (- ?x6662 eta_2)))
 (let (($x8849 (> ?x8847 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_1)) $x8849)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x7822 (- ?x3737 eta_2)))
 (let (($x7824 (> ?x7822 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_2)) $x7824)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x7811 (- ?x3705 eta_2)))
 (let (($x7813 (> ?x7811 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_3)) $x7813)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_0)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_1)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_2)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_3)) $x7849)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x7858 (- ?x3790 eta_2)))
 (let (($x7860 (> ?x7858 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_4)) $x7860)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_0)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_1)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_2)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_3)) $x7838)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x7847 (- ?x3778 eta_2)))
 (let (($x7849 (> ?x7847 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_4)) $x7849)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_0)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_1)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_2)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_3)) $x7902)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x7836 (- ?x3769 eta_2)))
 (let (($x7838 (> ?x7836 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_4)) $x7838)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x9812 (- ?x9811 eta_2)))
 (let (($x9814 (> ?x9812 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_0)) $x9814)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x8927 (- ?x6718 eta_2)))
 (let (($x8929 (> ?x8927 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_1)) $x8929)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x7958 (- ?x3910 eta_2)))
 (let (($x7960 (> ?x7958 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_2)) $x7960)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x7929 (- ?x3874 eta_2)))
 (let (($x7931 (> ?x7929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_3)) $x7931)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x7900 (- ?x3838 eta_2)))
 (let (($x7902 (> ?x7900 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_4)) $x7902)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_0)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_1)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_2)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_3)) $x8000)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x8012 (- ?x3955 eta_2)))
 (let (($x8014 (> ?x8012 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_4)) $x8014)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_0)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_1)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_2)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_3)) $x7989)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x7998 (- ?x3946 eta_2)))
 (let (($x8000 (> ?x7998 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_4)) $x8000)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_0)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_1)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_2)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_3)) $x8056)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x7987 (- ?x5526 eta_2)))
 (let (($x7989 (> ?x7987 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_4)) $x7989)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_0)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_1)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_2)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_3)) $x8088)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x8054 (- ?x3982 eta_2)))
 (let (($x8056 (> ?x8054 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_4)) $x8056)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x9937 (- ?x9936 eta_2)))
 (let (($x9939 (> ?x9937 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_0)) $x9939)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x9050 (- ?x6832 eta_2)))
 (let (($x9052 (> ?x9050 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_1)) $x9052)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x8150 (- ?x4055 eta_2)))
 (let (($x8152 (> ?x8150 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_2)) $x8152)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x8118 (- ?x4028 eta_2)))
 (let (($x8120 (> ?x8118 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_3)) $x8120)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x8086 (- ?x4004 eta_2)))
 (let (($x8088 (> ?x8086 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_4)) $x8088)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_0)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_1)) $x10535)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x10544 (- ?x3510 eta_1)))
 (let (($x10546 (> ?x10544 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_2)) $x10546)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x10555 (- ?x3524 eta_1)))
 (let (($x10557 (> ?x10555 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_3)) $x10557)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x10566 (- ?x3538 eta_1)))
 (let (($x10568 (> ?x10566 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_4)) $x10568)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_1)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_2)) $x10584)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x10587 (- ?x3584 eta_1)))
 (let (($x10589 (> ?x10587 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_3)) $x10589)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x10592 (- ?x3596 eta_1)))
 (let (($x10594 (> ?x10592 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_4)) $x10594)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_0)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_2)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_3)) $x10584)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x10587 (- ?x3584 eta_1)))
 (let (($x10589 (> ?x10587 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_4)) $x10589)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_0)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_1)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_2)) $x10632)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x10641 (- ?x3673 eta_1)))
 (let (($x10643 (> ?x10641 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_3)) $x10643)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x10655 (- ?x3689 eta_1)))
 (let (($x10657 (> ?x10655 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_4)) $x10657)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_0)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_1)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_2)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_3)) $x10632)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x10641 (- ?x3673 eta_1)))
 (let (($x10643 (> ?x10641 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_4)) $x10643)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_0)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_1)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_2)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_3)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_4)) $x10632)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_0)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_1)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_2)) $x10745)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x10757 (- ?x3806 eta_1)))
 (let (($x10759 (> ?x10757 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_3)) $x10759)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x10771 (- ?x3822 eta_1)))
 (let (($x10773 (> ?x10771 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_4)) $x10773)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_0)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_1)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_2)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_3)) $x10745)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x10757 (- ?x3806 eta_1)))
 (let (($x10759 (> ?x10757 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_4)) $x10759)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_0)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_1)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_2)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_3)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_4)) $x10745)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_4)) $x10734)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_0)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_1)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_2)) $x10899)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x10911 (- ?x3964 eta_1)))
 (let (($x10913 (> ?x10911 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_3)) $x10913)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x10925 (- ?x3973 eta_1)))
 (let (($x10927 (> ?x10925 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_4)) $x10927)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_0)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_1)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_2)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_3)) $x10899)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x10911 (- ?x3964 eta_1)))
 (let (($x10913 (> ?x10911 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_4)) $x10913)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_0)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_1)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_2)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_3)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_4)) $x10899)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_4)) $x10874)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_0)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_1)) $x10535)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x10544 (- ?x3510 eta_1)))
 (let (($x10546 (> ?x10544 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_2)) $x10546)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x10555 (- ?x3524 eta_1)))
 (let (($x10557 (> ?x10555 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_3)) $x10557)))))
(assert
 (let ((?x3538 (+ 4.0 eta_0)))
 (let ((?x10566 (- ?x3538 eta_1)))
 (let (($x10568 (> ?x10566 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_4)) $x10568)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_1)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_2)) $x10584)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x10587 (- ?x3584 eta_1)))
 (let (($x10589 (> ?x10587 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_3)) $x10589)))))
(assert
 (let ((?x3596 (+ 4.0 eta_1)))
 (let ((?x10592 (- ?x3596 eta_1)))
 (let (($x10594 (> ?x10592 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_4)) $x10594)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_0)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_2)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_3)) $x10584)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x10587 (- ?x3584 eta_1)))
 (let (($x10589 (> ?x10587 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_4)) $x10589)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_0)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_1)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_2)) $x10632)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x10641 (- ?x3673 eta_1)))
 (let (($x10643 (> ?x10641 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_3)) $x10643)))))
(assert
 (let ((?x3689 (+ 4.0 eta_2)))
 (let ((?x10655 (- ?x3689 eta_1)))
 (let (($x10657 (> ?x10655 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_4)) $x10657)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_0)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_1)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_2)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_3)) $x10632)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x10641 (- ?x3673 eta_1)))
 (let (($x10643 (> ?x10641 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_4)) $x10643)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_0)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_1)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_2)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_3)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_4)) $x10632)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_0)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_1)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_2)) $x10745)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x10757 (- ?x3806 eta_1)))
 (let (($x10759 (> ?x10757 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_3)) $x10759)))))
(assert
 (let ((?x3822 (+ 4.0 eta_3)))
 (let ((?x10771 (- ?x3822 eta_1)))
 (let (($x10773 (> ?x10771 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_4)) $x10773)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_0)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_1)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_2)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_3)) $x10745)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x10757 (- ?x3806 eta_1)))
 (let (($x10759 (> ?x10757 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_4)) $x10759)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_0)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_1)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_2)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_3)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_4)) $x10745)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_4)) $x10734)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_0)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_1)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_2)) $x10899)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x10911 (- ?x3964 eta_1)))
 (let (($x10913 (> ?x10911 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_3)) $x10913)))))
(assert
 (let ((?x3973 (+ 4.0 eta_4)))
 (let ((?x10925 (- ?x3973 eta_1)))
 (let (($x10927 (> ?x10925 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_4)) $x10927)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_0)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_1)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_2)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_3)) $x10899)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x10911 (- ?x3964 eta_1)))
 (let (($x10913 (> ?x10911 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_4)) $x10913)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_0)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_1)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_2)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_3)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_4)) $x10899)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_4)) $x10874)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x11371 (- ?x6556 eta_1)))
 (let (($x11373 (> ?x11371 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_0)) $x11373)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_1)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_2)) $x10535)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x10544 (- ?x3510 eta_1)))
 (let (($x10546 (> ?x10544 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_3)) $x10546)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x10555 (- ?x3524 eta_1)))
 (let (($x10557 (> ?x10555 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_4)) $x10557)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_0)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_2)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_3)) $x10584)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x10587 (- ?x3584 eta_1)))
 (let (($x10589 (> ?x10587 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_4)) $x10589)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_0)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_1)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_3)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_4)) $x10584)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_0)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_1)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_2)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_3)) $x10632)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x10641 (- ?x3673 eta_1)))
 (let (($x10643 (> ?x10641 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_4)) $x10643)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_0)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_1)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_2)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_3)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_4)) $x10632)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_0)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_1)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_2)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_3)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_4)) $x10621)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_0)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_1)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_2)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_3)) $x10745)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x10757 (- ?x3806 eta_1)))
 (let (($x10759 (> ?x10757 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_4)) $x10759)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_0)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_1)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_2)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_3)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_4)) $x10745)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_4)) $x10734)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_0)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_1)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_2)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_3)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_4)) $x10723)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_0)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_1)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_2)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_3)) $x10899)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x10911 (- ?x3964 eta_1)))
 (let (($x10913 (> ?x10911 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_4)) $x10913)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_0)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_1)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_2)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_3)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_4)) $x10899)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_4)) $x10874)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_0)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_1)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_2)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_3)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_4)) $x10941)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x11371 (- ?x6556 eta_1)))
 (let (($x11373 (> ?x11371 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_0)) $x11373)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_1)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_2)) $x10535)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x10544 (- ?x3510 eta_1)))
 (let (($x10546 (> ?x10544 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_3)) $x10546)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x10555 (- ?x3524 eta_1)))
 (let (($x10557 (> ?x10555 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_4)) $x10557)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_0)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_2)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_3)) $x10584)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x10587 (- ?x3584 eta_1)))
 (let (($x10589 (> ?x10587 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_4)) $x10589)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_0)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_1)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_3)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_4)) $x10584)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_0)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_1)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_2)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_3)) $x10632)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x10641 (- ?x3673 eta_1)))
 (let (($x10643 (> ?x10641 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_4)) $x10643)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_0)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_1)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_2)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_3)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_4)) $x10632)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_0)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_1)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_2)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_3)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_4)) $x10621)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_0)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_1)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_2)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_3)) $x10745)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x10757 (- ?x3806 eta_1)))
 (let (($x10759 (> ?x10757 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_4)) $x10759)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_0)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_1)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_2)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_3)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_4)) $x10745)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_4)) $x10734)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_0)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_1)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_2)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_3)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_4)) $x10723)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_0)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_1)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_2)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_3)) $x10899)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x10911 (- ?x3964 eta_1)))
 (let (($x10913 (> ?x10911 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_4)) $x10913)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_0)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_1)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_2)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_3)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_4)) $x10899)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_4)) $x10874)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_0)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_1)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_2)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_3)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_4)) $x10941)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x11994 (- ?x9642 eta_1)))
 (let (($x11996 (> ?x11994 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_0)) $x11996)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x11371 (- ?x6556 eta_1)))
 (let (($x11373 (> ?x11371 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_1)) $x11373)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_2)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_3)) $x10535)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x10544 (- ?x3510 eta_1)))
 (let (($x10546 (> ?x10544 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_4)) $x10546)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_0)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_1)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_3)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_4)) $x10584)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x12024 (- ?x9682 eta_1)))
 (let (($x12026 (> ?x12024 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_0)) $x12026)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_1)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_2)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_4)) $x10579)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_0)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_1)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_2)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_3)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_4)) $x10632)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_0)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_1)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_2)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_3)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_4)) $x10621)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x12078 (- ?x9727 eta_1)))
 (let (($x12080 (> ?x12078 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_0)) $x12080)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_1)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_2)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_3)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_4)) $x10610)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_0)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_1)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_2)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_3)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_4)) $x10745)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_4)) $x10734)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_0)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_1)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_2)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_3)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_4)) $x10723)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x12172 (- ?x9811 eta_1)))
 (let (($x12174 (> ?x12172 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_0)) $x12174)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_1)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_2)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_3)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_4)) $x10787)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_0)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_1)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_2)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_3)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_4)) $x10899)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_4)) $x10874)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_0)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_1)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_2)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_3)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_4)) $x10941)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x12295 (- ?x9936 eta_1)))
 (let (($x12297 (> ?x12295 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_0)) $x12297)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_1)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_2)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_3)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_4)) $x10973)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x11994 (- ?x9642 eta_1)))
 (let (($x11996 (> ?x11994 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_0)) $x11996)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x11371 (- ?x6556 eta_1)))
 (let (($x11373 (> ?x11371 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_1)) $x11373)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_2)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_3)) $x10535)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x10544 (- ?x3510 eta_1)))
 (let (($x10546 (> ?x10544 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_4)) $x10546)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_0)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_1)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_3)) $x10579)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x10582 (- ?x3572 eta_1)))
 (let (($x10584 (> ?x10582 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_4)) $x10584)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x12024 (- ?x9682 eta_1)))
 (let (($x12026 (> ?x12024 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_0)) $x12026)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_1)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_2)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_4)) $x10579)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_0)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_1)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_2)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_3)) $x10621)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x10630 (- ?x3661 eta_1)))
 (let (($x10632 (> ?x10630 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_4)) $x10632)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_0)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_1)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_2)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_3)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_4)) $x10621)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x12078 (- ?x9727 eta_1)))
 (let (($x12080 (> ?x12078 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_0)) $x12080)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_1)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_2)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_3)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_4)) $x10610)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_0)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_1)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_2)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_3)) $x10734)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x10743 (- ?x3790 eta_1)))
 (let (($x10745 (> ?x10743 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_4)) $x10745)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_4)) $x10734)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_0)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_1)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_2)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_3)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_4)) $x10723)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x12172 (- ?x9811 eta_1)))
 (let (($x12174 (> ?x12172 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_0)) $x12174)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_1)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_2)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_3)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_4)) $x10787)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_0)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_1)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_2)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_3)) $x10885)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x10897 (- ?x3955 eta_1)))
 (let (($x10899 (> ?x10897 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_4)) $x10899)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_4)) $x10874)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_0)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_1)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_2)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_3)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_4)) $x10941)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x12295 (- ?x9936 eta_1)))
 (let (($x12297 (> ?x12295 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_0)) $x12297)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_1)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_2)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_3)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_4)) $x10973)))))
(assert
 (let ((?x12617 (+ (- 3.0) eta_0)))
 (let ((?x12618 (- ?x12617 eta_1)))
 (let (($x12620 (> ?x12618 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_0)) $x12620)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x11994 (- ?x9642 eta_1)))
 (let (($x11996 (> ?x11994 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_1)) $x11996)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x11371 (- ?x6556 eta_1)))
 (let (($x11373 (> ?x11371 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_2)) $x11373)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_3)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_4)) $x10535)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x12024 (- ?x9682 eta_1)))
 (let (($x12026 (> ?x12024 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_0)) $x12026)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_1)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_2)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_4)) $x10579)))))
(assert
 (let ((?x12648 (+ (- 4.0) eta_1)))
 (let ((?x12649 (- ?x12648 eta_1)))
 (let (($x12651 (> ?x12649 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_0)) $x12651)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x12024 (- ?x9682 eta_1)))
 (let (($x12026 (> ?x12024 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_1)) $x12026)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_2)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_3)) $x10599)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_0)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_1)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_2)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_3)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_4)) $x10621)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x12078 (- ?x9727 eta_1)))
 (let (($x12080 (> ?x12078 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_0)) $x12080)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_1)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_2)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_3)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_4)) $x10610)))))
(assert
 (let ((?x12700 (+ (- 5.0) eta_2)))
 (let ((?x12701 (- ?x12700 eta_1)))
 (let (($x12703 (> ?x12701 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_0)) $x12703)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x12078 (- ?x9727 eta_1)))
 (let (($x12080 (> ?x12078 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_1)) $x12080)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_2)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_3)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_4)) $x10671)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_4)) $x10734)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_0)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_1)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_2)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_3)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_4)) $x10723)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x12172 (- ?x9811 eta_1)))
 (let (($x12174 (> ?x12172 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_0)) $x12174)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_1)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_2)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_3)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_4)) $x10787)))))
(assert
 (let ((?x12792 (+ (- 6.0) eta_3)))
 (let ((?x12793 (- ?x12792 eta_1)))
 (let (($x12795 (> ?x12793 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_0)) $x12795)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x12172 (- ?x9811 eta_1)))
 (let (($x12174 (> ?x12172 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_1)) $x12174)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_2)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_3)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_4)) $x10816)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_4)) $x10874)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_0)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_1)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_2)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_3)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_4)) $x10941)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x12295 (- ?x9936 eta_1)))
 (let (($x12297 (> ?x12295 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_0)) $x12297)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_1)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_2)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_3)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_4)) $x10973)))))
(assert
 (let ((?x12920 (+ (- 7.0) eta_4)))
 (let ((?x12921 (- ?x12920 eta_1)))
 (let (($x12923 (> ?x12921 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_0)) $x12923)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x12295 (- ?x9936 eta_1)))
 (let (($x12297 (> ?x12295 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_1)) $x12297)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_2)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_3)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_4)) $x11005)))))
(assert
 (let ((?x12617 (+ (- 3.0) eta_0)))
 (let ((?x12618 (- ?x12617 eta_1)))
 (let (($x12620 (> ?x12618 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_0)) $x12620)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x11994 (- ?x9642 eta_1)))
 (let (($x11996 (> ?x11994 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_1)) $x11996)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x11371 (- ?x6556 eta_1)))
 (let (($x11373 (> ?x11371 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_2)) $x11373)))))
(assert
 (let ((?x3485 (+ 0.0 eta_0)))
 (let ((?x10524 (- ?x3485 eta_1)))
 (let (($x10526 (> ?x10524 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_3)) $x10526)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x10533 (- ?x3497 eta_1)))
 (let (($x10535 (> ?x10533 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_4)) $x10535)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x12024 (- ?x9682 eta_1)))
 (let (($x12026 (> ?x12024 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_0)) $x12026)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_1)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_2)) $x10599)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x10577 (- ?x3560 eta_1)))
 (let (($x10579 (> ?x10577 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_4)) $x10579)))))
(assert
 (let ((?x12648 (+ (- 4.0) eta_1)))
 (let ((?x12649 (- ?x12648 eta_1)))
 (let (($x12651 (> ?x12649 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_0)) $x12651)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x12024 (- ?x9682 eta_1)))
 (let (($x12026 (> ?x12024 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_1)) $x12026)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x11401 (- ?x6596 eta_1)))
 (let (($x11403 (> ?x11401 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_2)) $x11403)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x10597 (- ?x3612 eta_1)))
 (let (($x10599 (> ?x10597 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_3)) $x10599)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_0)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_1)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_2)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_3)) $x10610)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x10619 (- ?x3649 eta_1)))
 (let (($x10621 (> ?x10619 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_4)) $x10621)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x12078 (- ?x9727 eta_1)))
 (let (($x12080 (> ?x12078 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_0)) $x12080)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_1)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_2)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_3)) $x10671)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x10608 (- ?x3640 eta_1)))
 (let (($x10610 (> ?x10608 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_4)) $x10610)))))
(assert
 (let ((?x12700 (+ (- 5.0) eta_2)))
 (let ((?x12701 (- ?x12700 eta_1)))
 (let (($x12703 (> ?x12701 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_0)) $x12703)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x12078 (- ?x9727 eta_1)))
 (let (($x12080 (> ?x12078 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_1)) $x12080)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x11455 (- ?x6662 eta_1)))
 (let (($x11457 (> ?x11455 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_2)) $x11457)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x10695 (- ?x3737 eta_1)))
 (let (($x10697 (> ?x10695 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_3)) $x10697)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x10669 (- ?x3705 eta_1)))
 (let (($x10671 (> ?x10669 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_4)) $x10671)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_0)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_1)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_2)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_3)) $x10723)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x10732 (- ?x3778 eta_1)))
 (let (($x10734 (> ?x10732 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_4)) $x10734)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_0)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_1)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_2)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_3)) $x10787)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x10721 (- ?x3769 eta_1)))
 (let (($x10723 (> ?x10721 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_4)) $x10723)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x12172 (- ?x9811 eta_1)))
 (let (($x12174 (> ?x12172 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_0)) $x12174)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_1)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_2)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_3)) $x10816)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x10785 (- ?x3838 eta_1)))
 (let (($x10787 (> ?x10785 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_4)) $x10787)))))
(assert
 (let ((?x12792 (+ (- 6.0) eta_3)))
 (let ((?x12793 (- ?x12792 eta_1)))
 (let (($x12795 (> ?x12793 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_0)) $x12795)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x12172 (- ?x9811 eta_1)))
 (let (($x12174 (> ?x12172 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_1)) $x12174)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x11546 (- ?x6718 eta_1)))
 (let (($x11548 (> ?x11546 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_2)) $x11548)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x10843 (- ?x3910 eta_1)))
 (let (($x10845 (> ?x10843 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_3)) $x10845)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x10814 (- ?x3874 eta_1)))
 (let (($x10816 (> ?x10814 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_4)) $x10816)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_0)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_1)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_2)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_3)) $x10874)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x10883 (- ?x3946 eta_1)))
 (let (($x10885 (> ?x10883 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_4)) $x10885)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_0)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_1)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_2)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_3)) $x10941)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x10872 (- ?x5526 eta_1)))
 (let (($x10874 (> ?x10872 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_4)) $x10874)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_0)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_1)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_2)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_3)) $x10973)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x10939 (- ?x3982 eta_1)))
 (let (($x10941 (> ?x10939 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_4)) $x10941)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x12295 (- ?x9936 eta_1)))
 (let (($x12297 (> ?x12295 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_0)) $x12297)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_1)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_2)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_3)) $x11005)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x10971 (- ?x4004 eta_1)))
 (let (($x10973 (> ?x10971 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_4)) $x10973)))))
(assert
 (let ((?x12920 (+ (- 7.0) eta_4)))
 (let ((?x12921 (- ?x12920 eta_1)))
 (let (($x12923 (> ?x12921 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_0)) $x12923)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x12295 (- ?x9936 eta_1)))
 (let (($x12297 (> ?x12295 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_1)) $x12297)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x11669 (- ?x6832 eta_1)))
 (let (($x11671 (> ?x11669 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_2)) $x11671)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x11035 (- ?x4055 eta_1)))
 (let (($x11037 (> ?x11035 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_3)) $x11037)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x11003 (- ?x4028 eta_1)))
 (let (($x11005 (> ?x11003 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_4)) $x11005)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x13238 (- ?x3497 eta_0)))
 (let (($x13240 (> ?x13238 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_1)) $x13240)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x13244 (- ?x3510 eta_0)))
 (let (($x13246 (> ?x13244 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_2)) $x13246)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x13249 (- ?x3524 eta_0)))
 (let (($x13251 (> ?x13249 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_3)) $x13251)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_4)) (> (- (+ 4.0 eta_0) eta_0) 0.0)))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_0)) $x13261)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x13270 (- ?x3560 eta_0)))
 (let (($x13272 (> ?x13270 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_1)) $x13272)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x13281 (- ?x3572 eta_0)))
 (let (($x13283 (> ?x13281 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_2)) $x13283)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x13292 (- ?x3584 eta_0)))
 (let (($x13294 (> ?x13292 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_3)) $x13294)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_4)) (> (- (+ 4.0 eta_1) eta_0) 0.0)))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_0)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_1)) $x13261)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x13270 (- ?x3560 eta_0)))
 (let (($x13272 (> ?x13270 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_2)) $x13272)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x13281 (- ?x3572 eta_0)))
 (let (($x13283 (> ?x13281 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_3)) $x13283)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x13292 (- ?x3584 eta_0)))
 (let (($x13294 (> ?x13292 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_4)) $x13294)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_0)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_1)) $x13353)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x13362 (- ?x3661 eta_0)))
 (let (($x13364 (> ?x13362 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_2)) $x13364)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x13373 (- ?x3673 eta_0)))
 (let (($x13375 (> ?x13373 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_3)) $x13375)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_4)) (> (- (+ 4.0 eta_2) eta_0) 0.0)))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_0)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_1)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_2)) $x13353)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x13362 (- ?x3661 eta_0)))
 (let (($x13364 (> ?x13362 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_3)) $x13364)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x13373 (- ?x3673 eta_0)))
 (let (($x13375 (> ?x13373 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_4)) $x13375)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_0)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_1)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_2)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_3)) $x13353)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x13362 (- ?x3661 eta_0)))
 (let (($x13364 (> ?x13362 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_4)) $x13364)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_0)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_1)) $x13466)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x13475 (- ?x3790 eta_0)))
 (let (($x13477 (> ?x13475 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_2)) $x13477)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x13489 (- ?x3806 eta_0)))
 (let (($x13491 (> ?x13489 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_3)) $x13491)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_4)) (> (- (+ 4.0 eta_3) eta_0) 0.0)))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_0)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_1)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_2)) $x13466)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x13475 (- ?x3790 eta_0)))
 (let (($x13477 (> ?x13475 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_3)) $x13477)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x13489 (- ?x3806 eta_0)))
 (let (($x13491 (> ?x13489 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_4)) $x13491)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_0)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_1)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_2)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_3)) $x13466)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x13475 (- ?x3790 eta_0)))
 (let (($x13477 (> ?x13475 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_4)) $x13477)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_0)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_1)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_2)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_3)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_4)) $x13466)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_0)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_1)) $x13617)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x13629 (- ?x3955 eta_0)))
 (let (($x13631 (> ?x13629 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_2)) $x13631)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x13643 (- ?x3964 eta_0)))
 (let (($x13645 (> ?x13643 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_3)) $x13645)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_4)) (> (- (+ 4.0 eta_4) eta_0) 0.0)))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_0)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_1)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_2)) $x13617)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x13629 (- ?x3955 eta_0)))
 (let (($x13631 (> ?x13629 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_3)) $x13631)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x13643 (- ?x3964 eta_0)))
 (let (($x13645 (> ?x13643 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_4)) $x13645)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_0)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_1)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_2)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_3)) $x13617)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x13629 (- ?x3955 eta_0)))
 (let (($x13631 (> ?x13629 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_4)) $x13631)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_0)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_1)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_2)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_3)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_4)) $x13617)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_0)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_1)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_2)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_3)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_4)) $x13606)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x13799 (- ?x6556 eta_0)))
 (let (($x13801 (> ?x13799 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_0)) $x13801)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x13238 (- ?x3497 eta_0)))
 (let (($x13240 (> ?x13238 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_2)) $x13240)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x13244 (- ?x3510 eta_0)))
 (let (($x13246 (> ?x13244 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_3)) $x13246)))))
(assert
 (let ((?x3524 (+ 3.0 eta_0)))
 (let ((?x13249 (- ?x3524 eta_0)))
 (let (($x13251 (> ?x13249 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_4)) $x13251)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_0)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_1)) $x13261)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x13270 (- ?x3560 eta_0)))
 (let (($x13272 (> ?x13270 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_2)) $x13272)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x13281 (- ?x3572 eta_0)))
 (let (($x13283 (> ?x13281 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_3)) $x13283)))))
(assert
 (let ((?x3584 (+ 3.0 eta_1)))
 (let ((?x13292 (- ?x3584 eta_0)))
 (let (($x13294 (> ?x13292 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_4)) $x13294)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x13827 (- ?x6596 eta_0)))
 (let (($x13829 (> ?x13827 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_0)) $x13829)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_1)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_2)) $x13261)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x13270 (- ?x3560 eta_0)))
 (let (($x13272 (> ?x13270 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_3)) $x13272)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x13281 (- ?x3572 eta_0)))
 (let (($x13283 (> ?x13281 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_4)) $x13283)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_0)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_1)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_2)) $x13353)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x13362 (- ?x3661 eta_0)))
 (let (($x13364 (> ?x13362 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_3)) $x13364)))))
(assert
 (let ((?x3673 (+ 3.0 eta_2)))
 (let ((?x13373 (- ?x3673 eta_0)))
 (let (($x13375 (> ?x13373 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_4)) $x13375)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_0)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_1)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_2)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_3)) $x13353)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x13362 (- ?x3661 eta_0)))
 (let (($x13364 (> ?x13362 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_4)) $x13364)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_0)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_1)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_2)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_3)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_4)) $x13353)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_0)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_1)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_2)) $x13466)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x13475 (- ?x3790 eta_0)))
 (let (($x13477 (> ?x13475 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_3)) $x13477)))))
(assert
 (let ((?x3806 (+ 3.0 eta_3)))
 (let ((?x13489 (- ?x3806 eta_0)))
 (let (($x13491 (> ?x13489 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_4)) $x13491)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_0)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_1)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_2)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_3)) $x13466)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x13475 (- ?x3790 eta_0)))
 (let (($x13477 (> ?x13475 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_4)) $x13477)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_0)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_1)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_2)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_3)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_4)) $x13466)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_0)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_1)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_2)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_3)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_4)) $x13455)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_0)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_1)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_2)) $x13617)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x13629 (- ?x3955 eta_0)))
 (let (($x13631 (> ?x13629 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_3)) $x13631)))))
(assert
 (let ((?x3964 (+ 3.0 eta_4)))
 (let ((?x13643 (- ?x3964 eta_0)))
 (let (($x13645 (> ?x13643 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_4)) $x13645)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_0)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_1)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_2)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_3)) $x13617)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x13629 (- ?x3955 eta_0)))
 (let (($x13631 (> ?x13629 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_4)) $x13631)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_0)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_1)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_2)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_3)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_4)) $x13617)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_0)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_1)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_2)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_3)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_4)) $x13606)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_0)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_1)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_2)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_3)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_4)) $x13673)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x14137 (- ?x9642 eta_0)))
 (let (($x14139 (> ?x14137 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_0)) $x14139)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x13799 (- ?x6556 eta_0)))
 (let (($x13801 (> ?x13799 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_1)) $x13801)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x13238 (- ?x3497 eta_0)))
 (let (($x13240 (> ?x13238 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_3)) $x13240)))))
(assert
 (let ((?x3510 (+ 2.0 eta_0)))
 (let ((?x13244 (- ?x3510 eta_0)))
 (let (($x13246 (> ?x13244 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_4)) $x13246)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x13827 (- ?x6596 eta_0)))
 (let (($x13829 (> ?x13827 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_0)) $x13829)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_1)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_2)) $x13261)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x13270 (- ?x3560 eta_0)))
 (let (($x13272 (> ?x13270 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_3)) $x13272)))))
(assert
 (let ((?x3572 (+ 2.0 eta_1)))
 (let ((?x13281 (- ?x3572 eta_0)))
 (let (($x13283 (> ?x13281 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_4)) $x13283)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x14165 (- ?x9682 eta_0)))
 (let (($x14167 (> ?x14165 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_0)) $x14167)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x13827 (- ?x6596 eta_0)))
 (let (($x13829 (> ?x13827 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_1)) $x13829)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_2)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_3)) $x13261)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x13270 (- ?x3560 eta_0)))
 (let (($x13272 (> ?x13270 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_4)) $x13272)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_0)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_1)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_2)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_3)) $x13353)))))
(assert
 (let ((?x3661 (+ 2.0 eta_2)))
 (let ((?x13362 (- ?x3661 eta_0)))
 (let (($x13364 (> ?x13362 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_4)) $x13364)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_0)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_1)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_2)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_3)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_4)) $x13353)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x14230 (- ?x9727 eta_0)))
 (let (($x14232 (> ?x14230 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_0)) $x14232)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_1)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_2)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_3)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_4)) $x13342)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_0)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_1)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_2)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_3)) $x13466)))))
(assert
 (let ((?x3790 (+ 2.0 eta_3)))
 (let ((?x13475 (- ?x3790 eta_0)))
 (let (($x13477 (> ?x13475 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_4)) $x13477)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_0)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_1)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_2)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_3)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_4)) $x13466)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_0)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_1)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_2)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_3)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_4)) $x13455)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x14324 (- ?x9811 eta_0)))
 (let (($x14326 (> ?x14324 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_0)) $x14326)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_1)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_2)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_3)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_4)) $x13519)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_0)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_1)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_2)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_3)) $x13617)))))
(assert
 (let ((?x3955 (+ 2.0 eta_4)))
 (let ((?x13629 (- ?x3955 eta_0)))
 (let (($x13631 (> ?x13629 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_4)) $x13631)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_0)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_1)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_2)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_3)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_4)) $x13617)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_0)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_1)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_2)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_3)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_4)) $x13606)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_0)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_1)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_2)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_3)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_4)) $x13673)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x14447 (- ?x9936 eta_0)))
 (let (($x14449 (> ?x14447 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_0)) $x14449)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_1)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_2)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_3)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_4)) $x13705)))))
(assert
 (let ((?x12617 (+ (- 3.0) eta_0)))
 (let ((?x14478 (- ?x12617 eta_0)))
 (let (($x14480 (> ?x14478 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_0)) $x14480)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x14137 (- ?x9642 eta_0)))
 (let (($x14139 (> ?x14137 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_1)) $x14139)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x13799 (- ?x6556 eta_0)))
 (let (($x13801 (> ?x13799 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_2)) $x13801)))))
(assert
 (let ((?x3497 (+ 1.0 eta_0)))
 (let ((?x13238 (- ?x3497 eta_0)))
 (let (($x13240 (> ?x13238 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_4)) $x13240)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x14165 (- ?x9682 eta_0)))
 (let (($x14167 (> ?x14165 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_0)) $x14167)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x13827 (- ?x6596 eta_0)))
 (let (($x13829 (> ?x13827 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_1)) $x13829)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_2)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_3)) $x13261)))))
(assert
 (let ((?x3560 (+ 1.0 eta_1)))
 (let ((?x13270 (- ?x3560 eta_0)))
 (let (($x13272 (> ?x13270 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_4)) $x13272)))))
(assert
 (let ((?x12648 (+ (- 4.0) eta_1)))
 (let ((?x14506 (- ?x12648 eta_0)))
 (let (($x14508 (> ?x14506 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_0)) $x14508)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x14165 (- ?x9682 eta_0)))
 (let (($x14167 (> ?x14165 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_1)) $x14167)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x13827 (- ?x6596 eta_0)))
 (let (($x13829 (> ?x13827 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_2)) $x13829)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_3)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_4)) $x13261)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_0)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_1)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_2)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_3)) $x13342)))))
(assert
 (let ((?x3649 (+ 1.0 eta_2)))
 (let ((?x13351 (- ?x3649 eta_0)))
 (let (($x13353 (> ?x13351 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_4)) $x13353)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x14230 (- ?x9727 eta_0)))
 (let (($x14232 (> ?x14230 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_0)) $x14232)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_1)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_2)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_3)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_4)) $x13342)))))
(assert
 (let ((?x12700 (+ (- 5.0) eta_2)))
 (let ((?x14568 (- ?x12700 eta_0)))
 (let (($x14570 (> ?x14568 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_0)) $x14570)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x14230 (- ?x9727 eta_0)))
 (let (($x14232 (> ?x14230 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_1)) $x14232)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_2)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_3)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_4)) $x13403)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_0)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_1)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_2)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_3)) $x13455)))))
(assert
 (let ((?x3778 (+ 1.0 eta_3)))
 (let ((?x13464 (- ?x3778 eta_0)))
 (let (($x13466 (> ?x13464 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_4)) $x13466)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_0)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_1)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_2)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_3)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_4)) $x13455)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x14324 (- ?x9811 eta_0)))
 (let (($x14326 (> ?x14324 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_0)) $x14326)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_1)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_2)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_3)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_4)) $x13519)))))
(assert
 (let ((?x12792 (+ (- 6.0) eta_3)))
 (let ((?x14659 (- ?x12792 eta_0)))
 (let (($x14661 (> ?x14659 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_0)) $x14661)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x14324 (- ?x9811 eta_0)))
 (let (($x14326 (> ?x14324 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_1)) $x14326)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_2)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_3)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_4)) $x13548)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_0)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_1)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_2)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_3)) $x13606)))))
(assert
 (let ((?x3946 (+ 1.0 eta_4)))
 (let ((?x13615 (- ?x3946 eta_0)))
 (let (($x13617 (> ?x13615 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_4)) $x13617)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_0)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_1)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_2)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_3)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_4)) $x13606)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_0)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_1)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_2)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_3)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_4)) $x13673)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x14447 (- ?x9936 eta_0)))
 (let (($x14449 (> ?x14447 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_0)) $x14449)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_1)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_2)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_3)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_4)) $x13705)))))
(assert
 (let ((?x12920 (+ (- 7.0) eta_4)))
 (let ((?x14785 (- ?x12920 eta_0)))
 (let (($x14787 (> ?x14785 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_0)) $x14787)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x14447 (- ?x9936 eta_0)))
 (let (($x14449 (> ?x14447 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_1)) $x14449)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_2)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_3)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_4)) $x13737)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_0)) (> (- (+ (- 4.0) eta_0) eta_0) 0.0)))
(assert
 (let ((?x12617 (+ (- 3.0) eta_0)))
 (let ((?x14478 (- ?x12617 eta_0)))
 (let (($x14480 (> ?x14478 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_1)) $x14480)))))
(assert
 (let ((?x9642 (+ (- 2.0) eta_0)))
 (let ((?x14137 (- ?x9642 eta_0)))
 (let (($x14139 (> ?x14137 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_2)) $x14139)))))
(assert
 (let ((?x6556 (+ (- 1.0) eta_0)))
 (let ((?x13799 (- ?x6556 eta_0)))
 (let (($x13801 (> ?x13799 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_3)) $x13801)))))
(assert
 (let ((?x12648 (+ (- 4.0) eta_1)))
 (let ((?x14506 (- ?x12648 eta_0)))
 (let (($x14508 (> ?x14506 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_0)) $x14508)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x14165 (- ?x9682 eta_0)))
 (let (($x14167 (> ?x14165 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_1)) $x14167)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x13827 (- ?x6596 eta_0)))
 (let (($x13829 (> ?x13827 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_2)) $x13829)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_3)) $x13319)))))
(assert
 (let ((?x3551 (+ 0.0 eta_1)))
 (let ((?x13259 (- ?x3551 eta_0)))
 (let (($x13261 (> ?x13259 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_4)) $x13261)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_0)) (> (- (+ (- 5.0) eta_1) eta_0) 0.0)))
(assert
 (let ((?x12648 (+ (- 4.0) eta_1)))
 (let ((?x14506 (- ?x12648 eta_0)))
 (let (($x14508 (> ?x14506 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_1)) $x14508)))))
(assert
 (let ((?x9682 (+ (- 3.0) eta_1)))
 (let ((?x14165 (- ?x9682 eta_0)))
 (let (($x14167 (> ?x14165 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_2)) $x14167)))))
(assert
 (let ((?x6596 (+ (- 2.0) eta_1)))
 (let ((?x13827 (- ?x6596 eta_0)))
 (let (($x13829 (> ?x13827 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_3)) $x13829)))))
(assert
 (let ((?x3612 (+ (- 1.0) eta_1)))
 (let ((?x13317 (- ?x3612 eta_0)))
 (let (($x13319 (> ?x13317 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_4)) $x13319)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x14230 (- ?x9727 eta_0)))
 (let (($x14232 (> ?x14230 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_0)) $x14232)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_1)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_2)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_3)) $x13403)))))
(assert
 (let ((?x3640 (+ 0.0 eta_2)))
 (let ((?x13340 (- ?x3640 eta_0)))
 (let (($x13342 (> ?x13340 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_4)) $x13342)))))
(assert
 (let ((?x12700 (+ (- 5.0) eta_2)))
 (let ((?x14568 (- ?x12700 eta_0)))
 (let (($x14570 (> ?x14568 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_0)) $x14570)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x14230 (- ?x9727 eta_0)))
 (let (($x14232 (> ?x14230 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_1)) $x14232)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_2)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_3)) $x13429)))))
(assert
 (let ((?x3705 (+ (- 1.0) eta_2)))
 (let ((?x13401 (- ?x3705 eta_0)))
 (let (($x13403 (> ?x13401 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_4)) $x13403)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_0)) (> (- (+ (- 6.0) eta_2) eta_0) 0.0)))
(assert
 (let ((?x12700 (+ (- 5.0) eta_2)))
 (let ((?x14568 (- ?x12700 eta_0)))
 (let (($x14570 (> ?x14568 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_1)) $x14570)))))
(assert
 (let ((?x9727 (+ (- 4.0) eta_2)))
 (let ((?x14230 (- ?x9727 eta_0)))
 (let (($x14232 (> ?x14230 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_2)) $x14232)))))
(assert
 (let ((?x6662 (+ (- 3.0) eta_2)))
 (let ((?x13892 (- ?x6662 eta_0)))
 (let (($x13894 (> ?x13892 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_3)) $x13894)))))
(assert
 (let ((?x3737 (+ (- 2.0) eta_2)))
 (let ((?x13427 (- ?x3737 eta_0)))
 (let (($x13429 (> ?x13427 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_4)) $x13429)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_0)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_1)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_2)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_3)) $x13519)))))
(assert
 (let ((?x3769 (+ 0.0 eta_3)))
 (let ((?x13453 (- ?x3769 eta_0)))
 (let (($x13455 (> ?x13453 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_4)) $x13455)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x14324 (- ?x9811 eta_0)))
 (let (($x14326 (> ?x14324 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_0)) $x14326)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_1)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_2)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_3)) $x13548)))))
(assert
 (let ((?x3838 (+ (- 1.0) eta_3)))
 (let ((?x13517 (- ?x3838 eta_0)))
 (let (($x13519 (> ?x13517 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_4)) $x13519)))))
(assert
 (let ((?x12792 (+ (- 6.0) eta_3)))
 (let ((?x14659 (- ?x12792 eta_0)))
 (let (($x14661 (> ?x14659 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_0)) $x14661)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x14324 (- ?x9811 eta_0)))
 (let (($x14326 (> ?x14324 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_1)) $x14326)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_2)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_3)) $x13577)))))
(assert
 (let ((?x3874 (+ (- 2.0) eta_3)))
 (let ((?x13546 (- ?x3874 eta_0)))
 (let (($x13548 (> ?x13546 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_4)) $x13548)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_0)) (> (- (+ (- 7.0) eta_3) eta_0) 0.0)))
(assert
 (let ((?x12792 (+ (- 6.0) eta_3)))
 (let ((?x14659 (- ?x12792 eta_0)))
 (let (($x14661 (> ?x14659 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_1)) $x14661)))))
(assert
 (let ((?x9811 (+ (- 5.0) eta_3)))
 (let ((?x14324 (- ?x9811 eta_0)))
 (let (($x14326 (> ?x14324 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_2)) $x14326)))))
(assert
 (let ((?x6718 (+ (- 4.0) eta_3)))
 (let ((?x13983 (- ?x6718 eta_0)))
 (let (($x13985 (> ?x13983 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_3)) $x13985)))))
(assert
 (let ((?x3910 (+ (- 3.0) eta_3)))
 (let ((?x13575 (- ?x3910 eta_0)))
 (let (($x13577 (> ?x13575 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_4)) $x13577)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_0)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_1)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_2)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_3)) $x13673)))))
(assert
 (let ((?x5526 (+ 0.0 eta_4)))
 (let ((?x13604 (- ?x5526 eta_0)))
 (let (($x13606 (> ?x13604 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_4)) $x13606)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_0)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_1)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_2)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_3)) $x13705)))))
(assert
 (let ((?x3982 (+ (- 1.0) eta_4)))
 (let ((?x13671 (- ?x3982 eta_0)))
 (let (($x13673 (> ?x13671 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_4)) $x13673)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x14447 (- ?x9936 eta_0)))
 (let (($x14449 (> ?x14447 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_0)) $x14449)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_1)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_2)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_3)) $x13737)))))
(assert
 (let ((?x4004 (+ (- 2.0) eta_4)))
 (let ((?x13703 (- ?x4004 eta_0)))
 (let (($x13705 (> ?x13703 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_4)) $x13705)))))
(assert
 (let ((?x12920 (+ (- 7.0) eta_4)))
 (let ((?x14785 (- ?x12920 eta_0)))
 (let (($x14787 (> ?x14785 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_0)) $x14787)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x14447 (- ?x9936 eta_0)))
 (let (($x14449 (> ?x14447 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_1)) $x14449)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_2)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
 (let ((?x13767 (- ?x4055 eta_0)))
 (let (($x13769 (> ?x13767 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_3)) $x13769)))))
(assert
 (let ((?x4028 (+ (- 3.0) eta_4)))
 (let ((?x13735 (- ?x4028 eta_0)))
 (let (($x13737 (> ?x13735 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_4)) $x13737)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_0)) (> (- (+ (- 8.0) eta_4) eta_0) 0.0)))
(assert
 (let ((?x12920 (+ (- 7.0) eta_4)))
 (let ((?x14785 (- ?x12920 eta_0)))
 (let (($x14787 (> ?x14785 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_1)) $x14787)))))
(assert
 (let ((?x9936 (+ (- 6.0) eta_4)))
 (let ((?x14447 (- ?x9936 eta_0)))
 (let (($x14449 (> ?x14447 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_2)) $x14449)))))
(assert
 (let ((?x6832 (+ (- 5.0) eta_4)))
 (let ((?x14106 (- ?x6832 eta_0)))
 (let (($x14108 (> ?x14106 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_3)) $x14108)))))
(assert
 (let ((?x4055 (+ (- 4.0) eta_4)))
(let ((?x13767 (- ?x4055 eta_0)))
(let (($x13769 (> ?x13767 0.0)))
(=> (= (+ yp_0 xp_4) (+ yp_14 xp_4)) $x13769)))))
(check-sat)
