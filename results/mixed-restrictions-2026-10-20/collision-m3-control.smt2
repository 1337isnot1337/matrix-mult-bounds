; benchmark generated from python API
(set-info :status unknown)
(declare-fun xp_0 () Int)
(declare-fun xp_1 () Int)
(declare-fun xp_2 () Int)
(declare-fun yp_0 () Int)
(declare-fun yp_1 () Int)
(declare-fun yp_2 () Int)
(declare-fun yp_3 () Int)
(declare-fun yp_4 () Int)
(declare-fun yp_5 () Int)
(declare-fun eta_0 () Real)
(declare-fun eta_2 () Real)
(declare-fun eta_1 () Real)
(assert
 (let (($x18 (>= xp_0 0)))
 (and $x18 (< xp_0 3))))
(assert
 (let (($x22 (>= xp_1 0)))
 (and $x22 (< xp_1 3))))
(assert
 (let (($x25 (>= xp_2 0)))
 (and $x25 (< xp_2 3))))
(assert
 (and (distinct xp_0 xp_1 xp_2) true))
(assert
 (let (($x57 (>= yp_0 0)))
 (and $x57 (< yp_0 6))))
(assert
 (let (($x62 (>= yp_1 0)))
 (and $x62 (< yp_1 6))))
(assert
 (let (($x65 (>= yp_2 0)))
 (and $x65 (< yp_2 6))))
(assert
 (let (($x68 (>= yp_3 0)))
 (and $x68 (< yp_3 6))))
(assert
 (let (($x71 (>= yp_4 0)))
 (and $x71 (< yp_4 6))))
(assert
 (let (($x74 (>= yp_5 0)))
 (and $x74 (< yp_5 6))))
(assert
 (and (distinct yp_0 yp_1 yp_2 yp_3 yp_4 yp_5) true))
(assert
 (= eta_0 0.0))
(assert
 (let ((?x105 (+ 0.0 eta_0)))
 (let ((?x106 (- ?x105 eta_2)))
 (let (($x109 (> ?x106 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_0)) $x109)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x125 (- ?x124 eta_2)))
 (let (($x128 (> ?x125 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_1)) $x128)))))
(assert
 (let ((?x143 (+ 2.0 eta_0)))
 (let ((?x144 (- ?x143 eta_2)))
 (let (($x147 (> ?x144 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_2)) $x147)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x162 (- ?x161 eta_2)))
 (let (($x165 (> ?x162 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_0)) $x165)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x175 (- ?x174 eta_2)))
 (let (($x178 (> ?x175 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_1)) $x178)))))
(assert
 (let ((?x191 (+ 2.0 eta_1)))
 (let ((?x192 (- ?x191 eta_2)))
 (let (($x195 (> ?x192 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_2)) $x195)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x208 (- ?x207 eta_2)))
 (let (($x211 (> ?x208 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_0)) $x211)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x162 (- ?x161 eta_2)))
 (let (($x165 (> ?x162 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_1)) $x165)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x175 (- ?x174 eta_2)))
 (let (($x178 (> ?x175 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_2)) $x178)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x239 (- ?x238 eta_2)))
 (let (($x242 (> ?x239 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_1)) $x242)))))
(assert
 (let ((?x245 (+ 2.0 eta_2)))
 (let ((?x246 (- ?x245 eta_2)))
 (let (($x251 (> ?x246 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_2)) $x251)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x255 (- ?x254 eta_2)))
 (let (($x260 (> ?x255 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_0)) $x260)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x239 (- ?x238 eta_2)))
 (let (($x242 (> ?x239 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_2)) $x242)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x274 (- ?x273 eta_2)))
 (let (($x276 (> ?x274 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_0)) $x276)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x255 (- ?x254 eta_2)))
 (let (($x260 (> ?x255 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_1)) $x260)))))
(assert
 (let ((?x105 (+ 0.0 eta_0)))
 (let ((?x106 (- ?x105 eta_2)))
 (let (($x109 (> ?x106 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_0)) $x109)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x125 (- ?x124 eta_2)))
 (let (($x128 (> ?x125 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_1)) $x128)))))
(assert
 (let ((?x143 (+ 2.0 eta_0)))
 (let ((?x144 (- ?x143 eta_2)))
 (let (($x147 (> ?x144 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_2)) $x147)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x162 (- ?x161 eta_2)))
 (let (($x165 (> ?x162 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_0)) $x165)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x175 (- ?x174 eta_2)))
 (let (($x178 (> ?x175 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_1)) $x178)))))
(assert
 (let ((?x191 (+ 2.0 eta_1)))
 (let ((?x192 (- ?x191 eta_2)))
 (let (($x195 (> ?x192 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_2)) $x195)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x208 (- ?x207 eta_2)))
 (let (($x211 (> ?x208 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_0)) $x211)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x162 (- ?x161 eta_2)))
 (let (($x165 (> ?x162 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_1)) $x165)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x175 (- ?x174 eta_2)))
 (let (($x178 (> ?x175 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_2)) $x178)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x239 (- ?x238 eta_2)))
 (let (($x242 (> ?x239 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_1)) $x242)))))
(assert
 (let ((?x245 (+ 2.0 eta_2)))
 (let ((?x246 (- ?x245 eta_2)))
 (let (($x251 (> ?x246 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_2)) $x251)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x255 (- ?x254 eta_2)))
 (let (($x260 (> ?x255 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_0)) $x260)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x239 (- ?x238 eta_2)))
 (let (($x242 (> ?x239 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_2)) $x242)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x274 (- ?x273 eta_2)))
 (let (($x276 (> ?x274 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_0)) $x276)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x255 (- ?x254 eta_2)))
 (let (($x260 (> ?x255 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_1)) $x260)))))
(assert
 (let ((?x105 (+ 0.0 eta_0)))
 (let ((?x106 (- ?x105 eta_2)))
 (let (($x109 (> ?x106 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_0)) $x109)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x125 (- ?x124 eta_2)))
 (let (($x128 (> ?x125 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_1)) $x128)))))
(assert
 (let ((?x143 (+ 2.0 eta_0)))
 (let ((?x144 (- ?x143 eta_2)))
 (let (($x147 (> ?x144 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_2)) $x147)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x162 (- ?x161 eta_2)))
 (let (($x165 (> ?x162 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_0)) $x165)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x175 (- ?x174 eta_2)))
 (let (($x178 (> ?x175 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_1)) $x178)))))
(assert
 (let ((?x191 (+ 2.0 eta_1)))
 (let ((?x192 (- ?x191 eta_2)))
 (let (($x195 (> ?x192 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_2)) $x195)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x208 (- ?x207 eta_2)))
 (let (($x211 (> ?x208 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_0)) $x211)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x162 (- ?x161 eta_2)))
 (let (($x165 (> ?x162 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_1)) $x165)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x175 (- ?x174 eta_2)))
 (let (($x178 (> ?x175 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_2)) $x178)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x239 (- ?x238 eta_2)))
 (let (($x242 (> ?x239 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_1)) $x242)))))
(assert
 (let ((?x245 (+ 2.0 eta_2)))
 (let ((?x246 (- ?x245 eta_2)))
 (let (($x251 (> ?x246 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_2)) $x251)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x255 (- ?x254 eta_2)))
 (let (($x260 (> ?x255 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_0)) $x260)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x239 (- ?x238 eta_2)))
 (let (($x242 (> ?x239 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_2)) $x242)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x274 (- ?x273 eta_2)))
 (let (($x276 (> ?x274 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_0)) $x276)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x255 (- ?x254 eta_2)))
 (let (($x260 (> ?x255 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_1)) $x260)))))
(assert
 (let ((?x105 (+ 0.0 eta_0)))
 (let ((?x460 (- ?x105 eta_1)))
 (let (($x462 (> ?x460 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_0)) $x462)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x472 (- ?x124 eta_1)))
 (let (($x474 (> ?x472 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_1)) $x474)))))
(assert
 (let ((?x143 (+ 2.0 eta_0)))
 (let ((?x486 (- ?x143 eta_1)))
 (let (($x488 (> ?x486 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_2)) $x488)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x500 (- ?x174 eta_1)))
 (let (($x502 (> ?x500 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_1)) $x502)))))
(assert
 (let ((?x191 (+ 2.0 eta_1)))
 (let ((?x505 (- ?x191 eta_1)))
 (let (($x507 (> ?x505 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_2)) $x507)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x510 (- ?x207 eta_1)))
 (let (($x512 (> ?x510 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_0)) $x512)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x500 (- ?x174 eta_1)))
 (let (($x502 (> ?x500 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_2)) $x502)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_0)) $x523)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x532 (- ?x238 eta_1)))
 (let (($x534 (> ?x532 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_1)) $x534)))))
(assert
 (let ((?x245 (+ 2.0 eta_2)))
 (let ((?x546 (- ?x245 eta_1)))
 (let (($x548 (> ?x546 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_2)) $x548)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_0)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_1)) $x523)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x532 (- ?x238 eta_1)))
 (let (($x534 (> ?x532 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_2)) $x534)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x580 (- ?x273 eta_1)))
 (let (($x582 (> ?x580 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_0)) $x582)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_1)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_2)) $x523)))))
(assert
 (let ((?x105 (+ 0.0 eta_0)))
 (let ((?x460 (- ?x105 eta_1)))
 (let (($x462 (> ?x460 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_0)) $x462)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x472 (- ?x124 eta_1)))
 (let (($x474 (> ?x472 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_1)) $x474)))))
(assert
 (let ((?x143 (+ 2.0 eta_0)))
 (let ((?x486 (- ?x143 eta_1)))
 (let (($x488 (> ?x486 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_2)) $x488)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x500 (- ?x174 eta_1)))
 (let (($x502 (> ?x500 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_1)) $x502)))))
(assert
 (let ((?x191 (+ 2.0 eta_1)))
 (let ((?x505 (- ?x191 eta_1)))
 (let (($x507 (> ?x505 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_2)) $x507)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x510 (- ?x207 eta_1)))
 (let (($x512 (> ?x510 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_0)) $x512)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x500 (- ?x174 eta_1)))
 (let (($x502 (> ?x500 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_2)) $x502)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_0)) $x523)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x532 (- ?x238 eta_1)))
 (let (($x534 (> ?x532 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_1)) $x534)))))
(assert
 (let ((?x245 (+ 2.0 eta_2)))
 (let ((?x546 (- ?x245 eta_1)))
 (let (($x548 (> ?x546 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_2)) $x548)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_0)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_1)) $x523)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x532 (- ?x238 eta_1)))
 (let (($x534 (> ?x532 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_2)) $x534)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x580 (- ?x273 eta_1)))
 (let (($x582 (> ?x580 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_0)) $x582)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_1)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_2)) $x523)))))
(assert
 (let ((?x665 (+ (- 1.0) eta_0)))
 (let ((?x666 (- ?x665 eta_1)))
 (let (($x668 (> ?x666 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_0)) $x668)))))
(assert
 (let ((?x105 (+ 0.0 eta_0)))
 (let ((?x460 (- ?x105 eta_1)))
 (let (($x462 (> ?x460 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_1)) $x462)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x472 (- ?x124 eta_1)))
 (let (($x474 (> ?x472 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_2)) $x474)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x510 (- ?x207 eta_1)))
 (let (($x512 (> ?x510 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_0)) $x512)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x500 (- ?x174 eta_1)))
 (let (($x502 (> ?x500 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_2)) $x502)))))
(assert
 (let ((?x692 (+ (- 2.0) eta_1)))
 (let ((?x693 (- ?x692 eta_1)))
 (let (($x695 (> ?x693 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_0)) $x695)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x510 (- ?x207 eta_1)))
 (let (($x512 (> ?x510 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_1)) $x512)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_0)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_1)) $x523)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x532 (- ?x238 eta_1)))
 (let (($x534 (> ?x532 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_2)) $x534)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x580 (- ?x273 eta_1)))
 (let (($x582 (> ?x580 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_0)) $x582)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_1)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_2)) $x523)))))
(assert
 (let ((?x729 (+ (- 3.0) eta_2)))
 (let ((?x730 (- ?x729 eta_1)))
 (let (($x732 (> ?x730 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_0)) $x732)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x580 (- ?x273 eta_1)))
 (let (($x582 (> ?x580 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_1)) $x582)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_2)) $x562)))))
(assert
 (let ((?x665 (+ (- 1.0) eta_0)))
 (let ((?x666 (- ?x665 eta_1)))
 (let (($x668 (> ?x666 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_0)) $x668)))))
(assert
 (let ((?x105 (+ 0.0 eta_0)))
 (let ((?x460 (- ?x105 eta_1)))
 (let (($x462 (> ?x460 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_1)) $x462)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x472 (- ?x124 eta_1)))
 (let (($x474 (> ?x472 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_2)) $x474)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x510 (- ?x207 eta_1)))
 (let (($x512 (> ?x510 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_0)) $x512)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x500 (- ?x174 eta_1)))
 (let (($x502 (> ?x500 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_2)) $x502)))))
(assert
 (let ((?x692 (+ (- 2.0) eta_1)))
 (let ((?x693 (- ?x692 eta_1)))
 (let (($x695 (> ?x693 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_0)) $x695)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x510 (- ?x207 eta_1)))
 (let (($x512 (> ?x510 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_1)) $x512)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_0)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_1)) $x523)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x532 (- ?x238 eta_1)))
 (let (($x534 (> ?x532 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_2)) $x534)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x580 (- ?x273 eta_1)))
 (let (($x582 (> ?x580 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_0)) $x582)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_1)) $x562)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x521 (- ?x520 eta_1)))
 (let (($x523 (> ?x521 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_2)) $x523)))))
(assert
 (let ((?x729 (+ (- 3.0) eta_2)))
 (let ((?x730 (- ?x729 eta_1)))
 (let (($x732 (> ?x730 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_0)) $x732)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x580 (- ?x273 eta_1)))
 (let (($x582 (> ?x580 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_1)) $x582)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x560 (- ?x254 eta_1)))
 (let (($x562 (> ?x560 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_2)) $x562)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x811 (- ?x124 eta_0)))
 (let (($x813 (> ?x811 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_1)) $x813)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_2)) (> (- (+ 2.0 eta_0) eta_0) 0.0)))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x822 (- ?x161 eta_0)))
 (let (($x824 (> ?x822 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_0)) $x824)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x833 (- ?x174 eta_0)))
 (let (($x835 (> ?x833 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_1)) $x835)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_2)) (> (- (+ 2.0 eta_1) eta_0) 0.0)))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x858 (- ?x207 eta_0)))
 (let (($x860 (> ?x858 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_0)) $x860)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x822 (- ?x161 eta_0)))
 (let (($x824 (> ?x822 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_1)) $x824)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x833 (- ?x174 eta_0)))
 (let (($x835 (> ?x833 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_2)) $x835)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x875 (- ?x520 eta_0)))
 (let (($x877 (> ?x875 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_0)) $x877)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x886 (- ?x238 eta_0)))
 (let (($x888 (> ?x886 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_1)) $x888)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_2)) (> (- (+ 2.0 eta_2) eta_0) 0.0)))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x914 (- ?x254 eta_0)))
 (let (($x916 (> ?x914 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_0)) $x916)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x875 (- ?x520 eta_0)))
 (let (($x877 (> ?x875 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_1)) $x877)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x886 (- ?x238 eta_0)))
 (let (($x888 (> ?x886 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_2)) $x888)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x934 (- ?x273 eta_0)))
 (let (($x936 (> ?x934 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_0)) $x936)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x914 (- ?x254 eta_0)))
 (let (($x916 (> ?x914 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_1)) $x916)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x875 (- ?x520 eta_0)))
 (let (($x877 (> ?x875 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_2)) $x877)))))
(assert
 (let ((?x665 (+ (- 1.0) eta_0)))
 (let ((?x954 (- ?x665 eta_0)))
 (let (($x956 (> ?x954 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_0)) $x956)))))
(assert
 (let ((?x124 (+ 1.0 eta_0)))
 (let ((?x811 (- ?x124 eta_0)))
 (let (($x813 (> ?x811 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_2)) $x813)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x858 (- ?x207 eta_0)))
 (let (($x860 (> ?x858 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_0)) $x860)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x822 (- ?x161 eta_0)))
 (let (($x824 (> ?x822 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_1)) $x824)))))
(assert
 (let ((?x174 (+ 1.0 eta_1)))
 (let ((?x833 (- ?x174 eta_0)))
 (let (($x835 (> ?x833 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_2)) $x835)))))
(assert
 (let ((?x692 (+ (- 2.0) eta_1)))
 (let ((?x972 (- ?x692 eta_0)))
 (let (($x974 (> ?x972 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_0)) $x974)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x858 (- ?x207 eta_0)))
 (let (($x860 (> ?x858 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_1)) $x860)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x822 (- ?x161 eta_0)))
 (let (($x824 (> ?x822 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_2)) $x824)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x914 (- ?x254 eta_0)))
 (let (($x916 (> ?x914 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_0)) $x916)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x875 (- ?x520 eta_0)))
 (let (($x877 (> ?x875 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_1)) $x877)))))
(assert
 (let ((?x238 (+ 1.0 eta_2)))
 (let ((?x886 (- ?x238 eta_0)))
 (let (($x888 (> ?x886 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_2)) $x888)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x934 (- ?x273 eta_0)))
 (let (($x936 (> ?x934 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_0)) $x936)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x914 (- ?x254 eta_0)))
 (let (($x916 (> ?x914 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_1)) $x916)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x875 (- ?x520 eta_0)))
 (let (($x877 (> ?x875 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_2)) $x877)))))
(assert
 (let ((?x729 (+ (- 3.0) eta_2)))
 (let ((?x1016 (- ?x729 eta_0)))
 (let (($x1018 (> ?x1016 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_0)) $x1018)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x934 (- ?x273 eta_0)))
 (let (($x936 (> ?x934 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_1)) $x936)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x914 (- ?x254 eta_0)))
 (let (($x916 (> ?x914 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_2)) $x916)))))
(assert
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_0)) (> (- (+ (- 2.0) eta_0) eta_0) 0.0)))
(assert
 (let ((?x665 (+ (- 1.0) eta_0)))
 (let ((?x954 (- ?x665 eta_0)))
 (let (($x956 (> ?x954 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_1)) $x956)))))
(assert
 (let ((?x692 (+ (- 2.0) eta_1)))
 (let ((?x972 (- ?x692 eta_0)))
 (let (($x974 (> ?x972 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_0)) $x974)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x858 (- ?x207 eta_0)))
 (let (($x860 (> ?x858 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_1)) $x860)))))
(assert
 (let ((?x161 (+ 0.0 eta_1)))
 (let ((?x822 (- ?x161 eta_0)))
 (let (($x824 (> ?x822 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_2)) $x824)))))
(assert
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_0)) (> (- (+ (- 3.0) eta_1) eta_0) 0.0)))
(assert
 (let ((?x692 (+ (- 2.0) eta_1)))
 (let ((?x972 (- ?x692 eta_0)))
 (let (($x974 (> ?x972 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_1)) $x974)))))
(assert
 (let ((?x207 (+ (- 1.0) eta_1)))
 (let ((?x858 (- ?x207 eta_0)))
 (let (($x860 (> ?x858 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_2)) $x860)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x934 (- ?x273 eta_0)))
 (let (($x936 (> ?x934 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_0)) $x936)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x914 (- ?x254 eta_0)))
 (let (($x916 (> ?x914 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_1)) $x916)))))
(assert
 (let ((?x520 (+ 0.0 eta_2)))
 (let ((?x875 (- ?x520 eta_0)))
 (let (($x877 (> ?x875 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_2)) $x877)))))
(assert
 (let ((?x729 (+ (- 3.0) eta_2)))
 (let ((?x1016 (- ?x729 eta_0)))
 (let (($x1018 (> ?x1016 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_0)) $x1018)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
 (let ((?x934 (- ?x273 eta_0)))
 (let (($x936 (> ?x934 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_1)) $x936)))))
(assert
 (let ((?x254 (+ (- 1.0) eta_2)))
 (let ((?x914 (- ?x254 eta_0)))
 (let (($x916 (> ?x914 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_2)) $x916)))))
(assert
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_0)) (> (- (+ (- 4.0) eta_2) eta_0) 0.0)))
(assert
 (let ((?x729 (+ (- 3.0) eta_2)))
 (let ((?x1016 (- ?x729 eta_0)))
 (let (($x1018 (> ?x1016 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_1)) $x1018)))))
(assert
 (let ((?x273 (+ (- 2.0) eta_2)))
(let ((?x934 (- ?x273 eta_0)))
(let (($x936 (> ?x934 0.0)))
(=> (= (+ yp_0 xp_2) (+ yp_5 xp_2)) $x936)))))
(check-sat)
