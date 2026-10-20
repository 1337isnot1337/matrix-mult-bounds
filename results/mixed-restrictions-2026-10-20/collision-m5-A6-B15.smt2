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
 (and $x31 (< xp_0 6))))
(assert
 (let (($x35 (>= xp_1 0)))
 (and $x35 (< xp_1 6))))
(assert
 (let (($x38 (>= xp_2 0)))
 (and $x38 (< xp_2 6))))
(assert
 (let (($x41 (>= xp_3 0)))
 (and $x41 (< xp_3 6))))
(assert
 (let (($x44 (>= xp_4 0)))
 (and $x44 (< xp_4 6))))
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
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x196 (- ?x195 eta_4)))
 (let (($x199 (> ?x196 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_0)) $x199)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x215 (- ?x214 eta_4)))
 (let (($x218 (> ?x215 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_1)) $x218)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x234 (- ?x233 eta_4)))
 (let (($x237 (> ?x234 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_2)) $x237)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x253 (- ?x252 eta_4)))
 (let (($x256 (> ?x253 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_3)) $x256)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x272 (- ?x271 eta_4)))
 (let (($x275 (> ?x272 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_0 xp_4)) $x275)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_0)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_1)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_2)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_3)) $x339)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x352 (- ?x351 eta_4)))
 (let (($x355 (> ?x352 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_1 xp_4)) $x355)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x368 (- ?x367 eta_4)))
 (let (($x371 (> ?x368 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_0)) $x371)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_1)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_2)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_3)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_2 xp_4)) $x339)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_0)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_1)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_2)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_3)) $x462)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x475 (- ?x474 eta_4)))
 (let (($x478 (> ?x475 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_3 xp_4)) $x478)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_0)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_1)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_2)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_3)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_4 xp_4)) $x462)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x536 (- ?x535 eta_4)))
 (let (($x539 (> ?x536 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_0)) $x539)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_1)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_2)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_3)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_5 xp_4)) $x446)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_0)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_1)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_2)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_3)) $x630)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x643 (- ?x642 eta_4)))
 (let (($x646 (> ?x643 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_6 xp_4)) $x646)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_0)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_1)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_2)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_3)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_7 xp_4)) $x630)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_0)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_1)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_2)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_3)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_8 xp_4)) $x614)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x749 (- ?x748 eta_4)))
 (let (($x752 (> ?x749 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_0)) $x752)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_1)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_2)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_3)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_9 xp_4)) $x597)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_1)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_2)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_3)) $x815)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x819 (- ?x818 eta_4)))
 (let (($x824 (> ?x819 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_10 xp_4)) $x824)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_0)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_2)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_3)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_11 xp_4)) $x815)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_0)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_1)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_3)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_12 xp_4)) $x806)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_0)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_1)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_2)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_13 xp_4)) $x797)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x906 (- ?x905 eta_4)))
 (let (($x908 (> ?x906 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_0)) $x908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_1)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_2)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_10 xp_0) (+ yp_14 xp_3)) $x833)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x196 (- ?x195 eta_4)))
 (let (($x199 (> ?x196 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_0)) $x199)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x215 (- ?x214 eta_4)))
 (let (($x218 (> ?x215 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_1)) $x218)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x234 (- ?x233 eta_4)))
 (let (($x237 (> ?x234 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_2)) $x237)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x253 (- ?x252 eta_4)))
 (let (($x256 (> ?x253 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_3)) $x256)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x272 (- ?x271 eta_4)))
 (let (($x275 (> ?x272 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_0 xp_4)) $x275)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_0)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_1)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_2)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_3)) $x339)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x352 (- ?x351 eta_4)))
 (let (($x355 (> ?x352 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_1 xp_4)) $x355)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x368 (- ?x367 eta_4)))
 (let (($x371 (> ?x368 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_0)) $x371)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_1)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_2)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_3)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_2 xp_4)) $x339)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_0)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_1)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_2)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_3)) $x462)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x475 (- ?x474 eta_4)))
 (let (($x478 (> ?x475 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_3 xp_4)) $x478)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_0)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_1)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_2)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_3)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_4 xp_4)) $x462)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x536 (- ?x535 eta_4)))
 (let (($x539 (> ?x536 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_0)) $x539)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_1)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_2)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_3)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_5 xp_4)) $x446)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_0)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_1)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_2)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_3)) $x630)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x643 (- ?x642 eta_4)))
 (let (($x646 (> ?x643 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_6 xp_4)) $x646)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_0)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_1)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_2)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_3)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_7 xp_4)) $x630)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_0)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_1)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_2)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_3)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_8 xp_4)) $x614)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x749 (- ?x748 eta_4)))
 (let (($x752 (> ?x749 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_0)) $x752)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_1)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_2)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_3)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_9 xp_4)) $x597)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_1)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_2)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_3)) $x815)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x819 (- ?x818 eta_4)))
 (let (($x824 (> ?x819 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_10 xp_4)) $x824)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_0)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_2)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_3)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_11 xp_4)) $x815)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_0)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_1)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_3)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_12 xp_4)) $x806)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_0)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_1)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_2)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_13 xp_4)) $x797)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x906 (- ?x905 eta_4)))
 (let (($x908 (> ?x906 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_0)) $x908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_1)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_2)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_11 xp_1) (+ yp_14 xp_3)) $x833)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x196 (- ?x195 eta_4)))
 (let (($x199 (> ?x196 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_0)) $x199)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x215 (- ?x214 eta_4)))
 (let (($x218 (> ?x215 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_1)) $x218)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x234 (- ?x233 eta_4)))
 (let (($x237 (> ?x234 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_2)) $x237)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x253 (- ?x252 eta_4)))
 (let (($x256 (> ?x253 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_3)) $x256)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x272 (- ?x271 eta_4)))
 (let (($x275 (> ?x272 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_0 xp_4)) $x275)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_0)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_1)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_2)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_3)) $x339)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x352 (- ?x351 eta_4)))
 (let (($x355 (> ?x352 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_1 xp_4)) $x355)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x368 (- ?x367 eta_4)))
 (let (($x371 (> ?x368 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_0)) $x371)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_1)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_2)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_3)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_2 xp_4)) $x339)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_0)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_1)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_2)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_3)) $x462)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x475 (- ?x474 eta_4)))
 (let (($x478 (> ?x475 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_3 xp_4)) $x478)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_0)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_1)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_2)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_3)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_4 xp_4)) $x462)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x536 (- ?x535 eta_4)))
 (let (($x539 (> ?x536 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_0)) $x539)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_1)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_2)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_3)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_5 xp_4)) $x446)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_0)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_1)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_2)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_3)) $x630)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x643 (- ?x642 eta_4)))
 (let (($x646 (> ?x643 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_6 xp_4)) $x646)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_0)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_1)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_2)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_3)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_7 xp_4)) $x630)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_0)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_1)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_2)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_3)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_8 xp_4)) $x614)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x749 (- ?x748 eta_4)))
 (let (($x752 (> ?x749 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_0)) $x752)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_1)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_2)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_3)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_9 xp_4)) $x597)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_1)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_2)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_3)) $x815)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x819 (- ?x818 eta_4)))
 (let (($x824 (> ?x819 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_10 xp_4)) $x824)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_0)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_2)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_3)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_11 xp_4)) $x815)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_0)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_1)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_3)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_12 xp_4)) $x806)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_0)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_1)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_2)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_13 xp_4)) $x797)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x906 (- ?x905 eta_4)))
 (let (($x908 (> ?x906 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_0)) $x908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_1)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_2)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_12 xp_2) (+ yp_14 xp_3)) $x833)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x196 (- ?x195 eta_4)))
 (let (($x199 (> ?x196 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_0)) $x199)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x215 (- ?x214 eta_4)))
 (let (($x218 (> ?x215 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_1)) $x218)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x234 (- ?x233 eta_4)))
 (let (($x237 (> ?x234 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_2)) $x237)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x253 (- ?x252 eta_4)))
 (let (($x256 (> ?x253 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_3)) $x256)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x272 (- ?x271 eta_4)))
 (let (($x275 (> ?x272 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_0 xp_4)) $x275)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_0)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_1)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_2)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_3)) $x339)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x352 (- ?x351 eta_4)))
 (let (($x355 (> ?x352 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_1 xp_4)) $x355)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x368 (- ?x367 eta_4)))
 (let (($x371 (> ?x368 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_0)) $x371)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_1)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_2)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_3)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_2 xp_4)) $x339)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_0)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_1)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_2)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_3)) $x462)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x475 (- ?x474 eta_4)))
 (let (($x478 (> ?x475 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_3 xp_4)) $x478)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_0)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_1)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_2)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_3)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_4 xp_4)) $x462)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x536 (- ?x535 eta_4)))
 (let (($x539 (> ?x536 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_0)) $x539)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_1)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_2)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_3)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_5 xp_4)) $x446)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_0)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_1)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_2)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_3)) $x630)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x643 (- ?x642 eta_4)))
 (let (($x646 (> ?x643 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_6 xp_4)) $x646)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_0)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_1)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_2)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_3)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_7 xp_4)) $x630)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_0)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_1)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_2)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_3)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_8 xp_4)) $x614)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x749 (- ?x748 eta_4)))
 (let (($x752 (> ?x749 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_0)) $x752)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_1)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_2)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_3)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_9 xp_4)) $x597)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_1)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_2)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_3)) $x815)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x819 (- ?x818 eta_4)))
 (let (($x824 (> ?x819 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_10 xp_4)) $x824)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_0)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_2)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_3)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_11 xp_4)) $x815)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_0)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_1)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_3)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_12 xp_4)) $x806)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_0)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_1)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_2)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_13 xp_4)) $x797)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x906 (- ?x905 eta_4)))
 (let (($x908 (> ?x906 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_0)) $x908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_1)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_2)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_13 xp_3) (+ yp_14 xp_3)) $x833)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x196 (- ?x195 eta_4)))
 (let (($x199 (> ?x196 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_0)) $x199)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x215 (- ?x214 eta_4)))
 (let (($x218 (> ?x215 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_1)) $x218)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x234 (- ?x233 eta_4)))
 (let (($x237 (> ?x234 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_2)) $x237)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x253 (- ?x252 eta_4)))
 (let (($x256 (> ?x253 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_3)) $x256)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x272 (- ?x271 eta_4)))
 (let (($x275 (> ?x272 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_0 xp_4)) $x275)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_0)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_1)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_2)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_3)) $x339)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x352 (- ?x351 eta_4)))
 (let (($x355 (> ?x352 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_1 xp_4)) $x355)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x368 (- ?x367 eta_4)))
 (let (($x371 (> ?x368 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_0)) $x371)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x290 (- ?x289 eta_4)))
 (let (($x293 (> ?x290 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_1)) $x293)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x303 (- ?x302 eta_4)))
 (let (($x306 (> ?x303 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_2)) $x306)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x320 (- ?x319 eta_4)))
 (let (($x323 (> ?x320 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_3)) $x323)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x336 (- ?x335 eta_4)))
 (let (($x339 (> ?x336 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_2 xp_4)) $x339)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_0)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_1)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_2)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_3)) $x462)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x475 (- ?x474 eta_4)))
 (let (($x478 (> ?x475 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_3 xp_4)) $x478)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_0)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_1)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_2)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_3)) $x446)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x459 (- ?x458 eta_4)))
 (let (($x462 (> ?x459 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_4 xp_4)) $x462)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x536 (- ?x535 eta_4)))
 (let (($x539 (> ?x536 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_0)) $x539)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x491 (- ?x490 eta_4)))
 (let (($x494 (> ?x491 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_1)) $x494)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x413 (- ?x412 eta_4)))
 (let (($x416 (> ?x413 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_2)) $x416)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x426 (- ?x425 eta_4)))
 (let (($x429 (> ?x426 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_3)) $x429)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x443 (- ?x442 eta_4)))
 (let (($x446 (> ?x443 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_5 xp_4)) $x446)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_0)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_1)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_2)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_3)) $x630)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x643 (- ?x642 eta_4)))
 (let (($x646 (> ?x643 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_6 xp_4)) $x646)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_0)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_1)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_2)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_3)) $x614)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x627 (- ?x626 eta_4)))
 (let (($x630 (> ?x627 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_7 xp_4)) $x630)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_0)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_1)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_2)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_3)) $x597)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x611 (- ?x610 eta_4)))
 (let (($x614 (> ?x611 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_8 xp_4)) $x614)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x749 (- ?x748 eta_4)))
 (let (($x752 (> ?x749 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_0)) $x752)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x704 (- ?x703 eta_4)))
 (let (($x707 (> ?x704 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_1)) $x707)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x659 (- ?x658 eta_4)))
 (let (($x662 (> ?x659 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_2)) $x662)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x581 (- ?x580 eta_4)))
 (let (($x584 (> ?x581 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_3)) $x584)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x594 (- ?x593 eta_4)))
 (let (($x597 (> ?x594 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_9 xp_4)) $x597)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_1)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_2)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_3)) $x815)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x819 (- ?x818 eta_4)))
 (let (($x824 (> ?x819 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_10 xp_4)) $x824)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_0)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_2)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_3)) $x806)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x810 (- ?x809 eta_4)))
 (let (($x815 (> ?x810 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_11 xp_4)) $x815)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_0)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_1)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_3)) $x797)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x801 (- ?x800 eta_4)))
 (let (($x806 (> ?x801 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_12 xp_4)) $x806)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_0)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_1)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_2)) $x833)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x794 (- ?x793 eta_4)))
 (let (($x797 (> ?x794 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_13 xp_4)) $x797)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x906 (- ?x905 eta_4)))
 (let (($x908 (> ?x906 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_0)) $x908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x878 (- ?x877 eta_4)))
 (let (($x880 (> ?x878 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_1)) $x880)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x853 (- ?x852 eta_4)))
 (let (($x855 (> ?x853 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_2)) $x855)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x828 (- ?x827 eta_4)))
 (let (($x833 (> ?x828 0.0)))
 (=> (= (+ yp_14 xp_4) (+ yp_14 xp_3)) $x833)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_0)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_1)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_2)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_3)) $x2535)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x2547 (- ?x271 eta_3)))
 (let (($x2549 (> ?x2547 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_0 xp_4)) $x2549)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_0)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_1)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_2)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_3)) $x2602)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x2614 (- ?x351 eta_3)))
 (let (($x2616 (> ?x2614 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_1 xp_4)) $x2616)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_2 xp_4)) $x2602)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_0)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_1)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_2)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_3)) $x2707)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x2719 (- ?x474 eta_3)))
 (let (($x2721 (> ?x2719 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_3 xp_4)) $x2721)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_4 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_5 xp_4)) $x2693)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_1)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_2)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_3)) $x2821)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x2824 (- ?x642 eta_3)))
 (let (($x2826 (> ?x2824 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_6 xp_4)) $x2826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_7 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_8 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_9 xp_4)) $x2811)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_0)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_1)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_2)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_3)) $x2922)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x2934 (- ?x818 eta_3)))
 (let (($x2936 (> ?x2934 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_10 xp_4)) $x2936)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_11 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_12 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_13 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_0) (+ yp_14 xp_4)) $x2883)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_0)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_1)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_2)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_3)) $x2535)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x2547 (- ?x271 eta_3)))
 (let (($x2549 (> ?x2547 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_0 xp_4)) $x2549)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_0)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_1)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_2)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_3)) $x2602)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x2614 (- ?x351 eta_3)))
 (let (($x2616 (> ?x2614 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_1 xp_4)) $x2616)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_2 xp_4)) $x2602)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_0)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_1)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_2)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_3)) $x2707)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x2719 (- ?x474 eta_3)))
 (let (($x2721 (> ?x2719 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_3 xp_4)) $x2721)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_4 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_5 xp_4)) $x2693)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_1)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_2)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_3)) $x2821)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x2824 (- ?x642 eta_3)))
 (let (($x2826 (> ?x2824 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_6 xp_4)) $x2826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_7 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_8 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_9 xp_4)) $x2811)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_0)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_1)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_2)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_3)) $x2922)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x2934 (- ?x818 eta_3)))
 (let (($x2936 (> ?x2934 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_10 xp_4)) $x2936)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_11 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_12 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_13 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_1) (+ yp_14 xp_4)) $x2883)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_0)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_1)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_2)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_3)) $x2535)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x2547 (- ?x271 eta_3)))
 (let (($x2549 (> ?x2547 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_0 xp_4)) $x2549)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_0)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_1)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_2)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_3)) $x2602)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x2614 (- ?x351 eta_3)))
 (let (($x2616 (> ?x2614 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_1 xp_4)) $x2616)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_2 xp_4)) $x2602)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_0)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_1)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_2)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_3)) $x2707)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x2719 (- ?x474 eta_3)))
 (let (($x2721 (> ?x2719 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_3 xp_4)) $x2721)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_4 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_5 xp_4)) $x2693)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_1)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_2)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_3)) $x2821)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x2824 (- ?x642 eta_3)))
 (let (($x2826 (> ?x2824 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_6 xp_4)) $x2826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_7 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_8 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_9 xp_4)) $x2811)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_0)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_1)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_2)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_3)) $x2922)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x2934 (- ?x818 eta_3)))
 (let (($x2936 (> ?x2934 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_10 xp_4)) $x2936)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_11 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_12 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_13 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_2) (+ yp_14 xp_4)) $x2883)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_0)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_1)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_2)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_3)) $x2535)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x2547 (- ?x271 eta_3)))
 (let (($x2549 (> ?x2547 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_0 xp_4)) $x2549)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_0)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_1)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_2)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_3)) $x2602)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x2614 (- ?x351 eta_3)))
 (let (($x2616 (> ?x2614 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_1 xp_4)) $x2616)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_2 xp_4)) $x2602)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_0)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_1)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_2)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_3)) $x2707)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x2719 (- ?x474 eta_3)))
 (let (($x2721 (> ?x2719 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_3 xp_4)) $x2721)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_4 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_5 xp_4)) $x2693)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_1)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_2)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_3)) $x2821)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x2824 (- ?x642 eta_3)))
 (let (($x2826 (> ?x2824 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_6 xp_4)) $x2826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_7 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_8 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_9 xp_4)) $x2811)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_0)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_1)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_2)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_3)) $x2922)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x2934 (- ?x818 eta_3)))
 (let (($x2936 (> ?x2934 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_10 xp_4)) $x2936)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_11 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_12 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_13 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_3) (+ yp_14 xp_4)) $x2883)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x4118 (- ?x4117 eta_3)))
 (let (($x4120 (> ?x4118 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_0)) $x4120)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_1)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_2)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_3)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_0 xp_4)) $x2535)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_1 xp_4)) $x2602)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x4179 (- ?x4178 eta_3)))
 (let (($x4181 (> ?x4179 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_0)) $x4181)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_1)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_2)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_3)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_2 xp_4)) $x2588)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_3 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_4 xp_4)) $x2693)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x4266 (- ?x4265 eta_3)))
 (let (($x4268 (> ?x4266 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_0)) $x4268)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_1)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_2)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_3)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_5 xp_4)) $x2679)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_6 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_7 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_8 xp_4)) $x2811)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x4334 (- ?x4333 eta_3)))
 (let (($x4336 (> ?x4334 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_0)) $x4336)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_1)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_2)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_9 xp_3)) $x2831)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_10 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_11 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_12 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_13 xp_4)) $x2883)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x4451 (- ?x4450 eta_3)))
 (let (($x4453 (> ?x4451 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_0)) $x4453)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_1)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_2)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_3)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_6 xp_1) (+ yp_14 xp_4)) $x2950)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x4118 (- ?x4117 eta_3)))
 (let (($x4120 (> ?x4118 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_0)) $x4120)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_1)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_2)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_3)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_0 xp_4)) $x2535)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_1 xp_4)) $x2602)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x4179 (- ?x4178 eta_3)))
 (let (($x4181 (> ?x4179 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_0)) $x4181)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_1)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_2)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_3)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_2 xp_4)) $x2588)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_3 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_4 xp_4)) $x2693)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x4266 (- ?x4265 eta_3)))
 (let (($x4268 (> ?x4266 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_0)) $x4268)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_1)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_2)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_3)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_5 xp_4)) $x2679)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_6 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_7 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_8 xp_4)) $x2811)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x4334 (- ?x4333 eta_3)))
 (let (($x4336 (> ?x4334 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_0)) $x4336)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_1)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_2)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_9 xp_3)) $x2831)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_10 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_11 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_12 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_13 xp_4)) $x2883)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x4451 (- ?x4450 eta_3)))
 (let (($x4453 (> ?x4451 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_0)) $x4453)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_1)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_2)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_3)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_7 xp_2) (+ yp_14 xp_4)) $x2950)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x4118 (- ?x4117 eta_3)))
 (let (($x4120 (> ?x4118 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_0)) $x4120)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_1)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_2)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_3)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_0 xp_4)) $x2535)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_1 xp_4)) $x2602)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x4179 (- ?x4178 eta_3)))
 (let (($x4181 (> ?x4179 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_0)) $x4181)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_1)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_2)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_3)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_2 xp_4)) $x2588)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_3 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_4 xp_4)) $x2693)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x4266 (- ?x4265 eta_3)))
 (let (($x4268 (> ?x4266 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_0)) $x4268)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_1)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_2)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_3)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_5 xp_4)) $x2679)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_6 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_7 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_8 xp_4)) $x2811)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x4334 (- ?x4333 eta_3)))
 (let (($x4336 (> ?x4334 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_0)) $x4336)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_1)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_2)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_9 xp_3)) $x2831)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_10 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_11 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_12 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_13 xp_4)) $x2883)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x4451 (- ?x4450 eta_3)))
 (let (($x4453 (> ?x4451 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_0)) $x4453)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_1)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_2)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_3)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_8 xp_3) (+ yp_14 xp_4)) $x2950)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x4118 (- ?x4117 eta_3)))
 (let (($x4120 (> ?x4118 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_0)) $x4120)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x2493 (- ?x195 eta_3)))
 (let (($x2495 (> ?x2493 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_1)) $x2495)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x2505 (- ?x214 eta_3)))
 (let (($x2507 (> ?x2505 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_2)) $x2507)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x2519 (- ?x233 eta_3)))
 (let (($x2521 (> ?x2519 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_3)) $x2521)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x2533 (- ?x252 eta_3)))
 (let (($x2535 (> ?x2533 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_0 xp_4)) $x2535)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_0)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_1)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_2)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_3)) $x2588)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x2600 (- ?x335 eta_3)))
 (let (($x2602 (> ?x2600 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_1 xp_4)) $x2602)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x4179 (- ?x4178 eta_3)))
 (let (($x4181 (> ?x4179 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_0)) $x4181)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x2628 (- ?x367 eta_3)))
 (let (($x2630 (> ?x2628 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_1)) $x2630)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x2561 (- ?x289 eta_3)))
 (let (($x2563 (> ?x2561 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_2)) $x2563)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x2572 (- ?x302 eta_3)))
 (let (($x2574 (> ?x2572 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_3)) $x2574)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x2586 (- ?x319 eta_3)))
 (let (($x2588 (> ?x2586 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_2 xp_4)) $x2588)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_0)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_1)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_2)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_3)) $x2693)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x2705 (- ?x458 eta_3)))
 (let (($x2707 (> ?x2705 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_3 xp_4)) $x2707)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_0)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_1)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_2)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_3)) $x2679)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x2691 (- ?x442 eta_3)))
 (let (($x2693 (> ?x2691 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_4 xp_4)) $x2693)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x4266 (- ?x4265 eta_3)))
 (let (($x4268 (> ?x4266 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_0)) $x4268)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x2771 (- ?x535 eta_3)))
 (let (($x2773 (> ?x2771 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_1)) $x2773)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x2733 (- ?x490 eta_3)))
 (let (($x2735 (> ?x2733 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_2)) $x2735)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x2666 (- ?x412 eta_3)))
 (let (($x2668 (> ?x2666 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_3)) $x2668)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x2677 (- ?x425 eta_3)))
 (let (($x2679 (> ?x2677 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_5 xp_4)) $x2679)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_0)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_2)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_3)) $x2816)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x2819 (- ?x626 eta_3)))
 (let (($x2821 (> ?x2819 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_6 xp_4)) $x2821)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_0)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_1)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_3)) $x2811)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x2814 (- ?x610 eta_3)))
 (let (($x2816 (> ?x2814 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_7 xp_4)) $x2816)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_0)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_1)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_2)) $x2831)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x2809 (- ?x593 eta_3)))
 (let (($x2811 (> ?x2809 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_8 xp_4)) $x2811)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x4334 (- ?x4333 eta_3)))
 (let (($x4336 (> ?x4334 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_0)) $x4336)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x2860 (- ?x748 eta_3)))
 (let (($x2862 (> ?x2860 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_1)) $x2862)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x2843 (- ?x703 eta_3)))
 (let (($x2845 (> ?x2843 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_2)) $x2845)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x2829 (- ?x658 eta_3)))
 (let (($x2831 (> ?x2829 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_9 xp_3)) $x2831)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_0)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_1)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_2)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_3)) $x2908)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x2920 (- ?x809 eta_3)))
 (let (($x2922 (> ?x2920 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_10 xp_4)) $x2922)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_0)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_1)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_2)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_3)) $x2894)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x2906 (- ?x800 eta_3)))
 (let (($x2908 (> ?x2906 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_11 xp_4)) $x2908)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_0)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_1)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_2)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_3)) $x2883)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x2892 (- ?x793 eta_3)))
 (let (($x2894 (> ?x2892 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_12 xp_4)) $x2894)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_0)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_1)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_2)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_3)) $x2950)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x2881 (- ?x2880 eta_3)))
 (let (($x2883 (> ?x2881 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_13 xp_4)) $x2883)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x4451 (- ?x4450 eta_3)))
 (let (($x4453 (> ?x4451 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_0)) $x4453)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x3044 (- ?x905 eta_3)))
 (let (($x3046 (> ?x3044 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_1)) $x3046)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x3012 (- ?x877 eta_3)))
 (let (($x3014 (> ?x3012 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_2)) $x3014)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x2980 (- ?x852 eta_3)))
 (let (($x2982 (> ?x2980 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_3)) $x2982)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x2948 (- ?x827 eta_3)))
 (let (($x2950 (> ?x2948 0.0)))
 (=> (= (+ yp_9 xp_4) (+ yp_14 xp_4)) $x2950)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_0)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_1)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_2)) $x5483)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x5495 (- ?x252 eta_2)))
 (let (($x5497 (> ?x5495 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_3)) $x5497)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x5509 (- ?x271 eta_2)))
 (let (($x5511 (> ?x5509 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_4)) $x5511)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_0)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_1)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_2)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_3)) $x5564)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x5576 (- ?x351 eta_2)))
 (let (($x5578 (> ?x5576 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_4)) $x5578)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_0)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_1)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_2)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_3)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_4)) $x5564)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_1)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_2)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_3)) $x5640)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x5643 (- ?x474 eta_2)))
 (let (($x5645 (> ?x5643 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_4)) $x5645)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_0)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_2)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_3)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_4)) $x5640)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_4)) $x5635)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_0)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_1)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_2)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_3)) $x5717)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x5729 (- ?x642 eta_2)))
 (let (($x5731 (> ?x5729 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_6 xp_4)) $x5731)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_0)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_1)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_2)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_3)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_7 xp_4)) $x5717)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_8 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_9 xp_4)) $x5692)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_0)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_1)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_2)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_3)) $x5871)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x5883 (- ?x818 eta_2)))
 (let (($x5885 (> ?x5883 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_10 xp_4)) $x5885)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_0)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_1)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_2)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_3)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_11 xp_4)) $x5871)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_12 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_13 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_14 xp_4)) $x5832)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_0)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_1)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_2)) $x5483)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x5495 (- ?x252 eta_2)))
 (let (($x5497 (> ?x5495 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_3)) $x5497)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x5509 (- ?x271 eta_2)))
 (let (($x5511 (> ?x5509 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_4)) $x5511)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_0)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_1)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_2)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_3)) $x5564)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x5576 (- ?x351 eta_2)))
 (let (($x5578 (> ?x5576 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_4)) $x5578)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_0)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_1)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_2)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_3)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_4)) $x5564)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_1)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_2)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_3)) $x5640)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x5643 (- ?x474 eta_2)))
 (let (($x5645 (> ?x5643 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_4)) $x5645)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_0)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_2)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_3)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_4)) $x5640)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_4)) $x5635)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_0)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_1)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_2)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_3)) $x5717)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x5729 (- ?x642 eta_2)))
 (let (($x5731 (> ?x5729 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_6 xp_4)) $x5731)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_0)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_1)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_2)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_3)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_7 xp_4)) $x5717)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_8 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_9 xp_4)) $x5692)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_0)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_1)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_2)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_3)) $x5871)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x5883 (- ?x818 eta_2)))
 (let (($x5885 (> ?x5883 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_10 xp_4)) $x5885)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_0)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_1)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_2)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_3)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_11 xp_4)) $x5871)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_12 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_13 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_14 xp_4)) $x5832)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_0)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_1)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_2)) $x5483)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x5495 (- ?x252 eta_2)))
 (let (($x5497 (> ?x5495 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_3)) $x5497)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x5509 (- ?x271 eta_2)))
 (let (($x5511 (> ?x5509 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_4)) $x5511)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_0)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_1)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_2)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_3)) $x5564)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x5576 (- ?x351 eta_2)))
 (let (($x5578 (> ?x5576 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_4)) $x5578)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_0)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_1)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_2)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_3)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_4)) $x5564)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_1)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_2)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_3)) $x5640)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x5643 (- ?x474 eta_2)))
 (let (($x5645 (> ?x5643 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_4)) $x5645)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_0)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_2)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_3)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_4)) $x5640)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_4)) $x5635)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_0)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_1)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_2)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_3)) $x5717)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x5729 (- ?x642 eta_2)))
 (let (($x5731 (> ?x5729 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_6 xp_4)) $x5731)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_0)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_1)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_2)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_3)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_7 xp_4)) $x5717)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_8 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_9 xp_4)) $x5692)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_0)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_1)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_2)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_3)) $x5871)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x5883 (- ?x818 eta_2)))
 (let (($x5885 (> ?x5883 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_10 xp_4)) $x5885)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_0)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_1)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_2)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_3)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_11 xp_4)) $x5871)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_12 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_13 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_14 xp_4)) $x5832)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x6688 (- ?x4117 eta_2)))
 (let (($x6690 (> ?x6688 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_0)) $x6690)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_1)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_2)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_3)) $x5483)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x5495 (- ?x252 eta_2)))
 (let (($x5497 (> ?x5495 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_0 xp_4)) $x5497)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_0)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_1)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_2)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_3)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_1 xp_4)) $x5564)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_0)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_1)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_2)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_3)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_2 xp_4)) $x5550)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_0)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_2)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_3)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_3 xp_4)) $x5640)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_4 xp_4)) $x5635)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_0)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_1)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_2)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_5 xp_4)) $x5630)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_0)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_1)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_2)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_3)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_6 xp_4)) $x5717)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_7 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_8 xp_4)) $x5692)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_0)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_1)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_2)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_3)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_9 xp_4)) $x5681)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_0)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_1)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_2)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_3)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_10 xp_4)) $x5871)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_11 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_12 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_13 xp_4)) $x5832)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_0)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_1)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_2)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_3)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_1) (+ yp_14 xp_4)) $x5899)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x6688 (- ?x4117 eta_2)))
 (let (($x6690 (> ?x6688 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_0)) $x6690)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_1)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_2)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_3)) $x5483)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x5495 (- ?x252 eta_2)))
 (let (($x5497 (> ?x5495 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_0 xp_4)) $x5497)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_0)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_1)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_2)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_3)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_1 xp_4)) $x5564)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_0)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_1)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_2)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_3)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_2 xp_4)) $x5550)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_0)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_2)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_3)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_3 xp_4)) $x5640)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_4 xp_4)) $x5635)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_0)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_1)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_2)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_5 xp_4)) $x5630)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_0)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_1)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_2)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_3)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_6 xp_4)) $x5717)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_7 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_8 xp_4)) $x5692)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_0)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_1)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_2)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_3)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_9 xp_4)) $x5681)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_0)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_1)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_2)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_3)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_10 xp_4)) $x5871)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_11 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_12 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_13 xp_4)) $x5832)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_0)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_1)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_2)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_3)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_2) (+ yp_14 xp_4)) $x5899)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x6688 (- ?x4117 eta_2)))
 (let (($x6690 (> ?x6688 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_0)) $x6690)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_1)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_2)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_3)) $x5483)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x5495 (- ?x252 eta_2)))
 (let (($x5497 (> ?x5495 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_0 xp_4)) $x5497)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_0)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_1)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_2)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_3)) $x5550)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x5562 (- ?x335 eta_2)))
 (let (($x5564 (> ?x5562 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_1 xp_4)) $x5564)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_0)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_1)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_2)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_3)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_2 xp_4)) $x5550)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_0)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_2)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_3)) $x5635)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x5638 (- ?x458 eta_2)))
 (let (($x5640 (> ?x5638 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_3 xp_4)) $x5640)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_4 xp_4)) $x5635)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_0)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_1)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_2)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_5 xp_4)) $x5630)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_0)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_1)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_2)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_3)) $x5703)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x5715 (- ?x626 eta_2)))
 (let (($x5717 (> ?x5715 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_6 xp_4)) $x5717)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_7 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_8 xp_4)) $x5692)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_0)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_1)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_2)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_3)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_9 xp_4)) $x5681)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_0)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_1)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_2)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_3)) $x5857)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x5869 (- ?x809 eta_2)))
 (let (($x5871 (> ?x5869 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_10 xp_4)) $x5871)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_11 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_12 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_13 xp_4)) $x5832)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_0)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_1)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_2)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_3)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_3) (+ yp_14 xp_4)) $x5899)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x7669 (- ?x7668 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_0)) $x7671)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x6688 (- ?x4117 eta_2)))
 (let (($x6690 (> ?x6688 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_1)) $x6690)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_2)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_3)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_0 xp_4)) $x5483)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_0)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_1)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_2)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_3)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_1 xp_4)) $x5550)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x7730 (- ?x7729 eta_2)))
 (let (($x7732 (> ?x7730 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_0)) $x7732)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_1)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_2)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_3)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_2 xp_4)) $x5536)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_3 xp_4)) $x5635)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_0)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_1)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_2)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_4 xp_4)) $x5630)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x7787 (- ?x7786 eta_2)))
 (let (($x7789 (> ?x7787 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_0)) $x7789)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_1)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_2)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_5 xp_3)) $x5650)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_6 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_7 xp_4)) $x5692)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_0)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_1)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_2)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_3)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_8 xp_4)) $x5681)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x7874 (- ?x7873 eta_2)))
 (let (($x7876 (> ?x7874 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_0)) $x7876)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_1)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_2)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_3)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_9 xp_4)) $x5745)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_10 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_11 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_12 xp_4)) $x5832)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_0)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_1)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_2)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_3)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_13 xp_4)) $x5899)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x7999 (- ?x7998 eta_2)))
 (let (($x8001 (> ?x7999 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_0)) $x8001)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_1)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_2)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_3)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_3 xp_2) (+ yp_14 xp_4)) $x5931)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x7669 (- ?x7668 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_0)) $x7671)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x6688 (- ?x4117 eta_2)))
 (let (($x6690 (> ?x6688 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_1)) $x6690)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_2)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_3)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_0 xp_4)) $x5483)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_0)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_1)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_2)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_3)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_1 xp_4)) $x5550)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x7730 (- ?x7729 eta_2)))
 (let (($x7732 (> ?x7730 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_0)) $x7732)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_1)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_2)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_3)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_2 xp_4)) $x5536)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_3 xp_4)) $x5635)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_0)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_1)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_2)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_4 xp_4)) $x5630)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x7787 (- ?x7786 eta_2)))
 (let (($x7789 (> ?x7787 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_0)) $x7789)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_1)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_2)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_5 xp_3)) $x5650)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_6 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_7 xp_4)) $x5692)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_0)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_1)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_2)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_3)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_8 xp_4)) $x5681)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x7874 (- ?x7873 eta_2)))
 (let (($x7876 (> ?x7874 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_0)) $x7876)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_1)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_2)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_3)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_9 xp_4)) $x5745)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_10 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_11 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_12 xp_4)) $x5832)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_0)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_1)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_2)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_3)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_13 xp_4)) $x5899)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x7999 (- ?x7998 eta_2)))
 (let (($x8001 (> ?x7999 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_0)) $x8001)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_1)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_2)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_3)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_4 xp_3) (+ yp_14 xp_4)) $x5931)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x7669 (- ?x7668 eta_2)))
 (let (($x7671 (> ?x7669 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_0)) $x7671)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x6688 (- ?x4117 eta_2)))
 (let (($x6690 (> ?x6688 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_1)) $x6690)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x5455 (- ?x195 eta_2)))
 (let (($x5457 (> ?x5455 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_2)) $x5457)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x5467 (- ?x214 eta_2)))
 (let (($x5469 (> ?x5467 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_3)) $x5469)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x5481 (- ?x233 eta_2)))
 (let (($x5483 (> ?x5481 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_0 xp_4)) $x5483)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_0)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_1)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_2)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_3)) $x5536)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x5548 (- ?x319 eta_2)))
 (let (($x5550 (> ?x5548 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_1 xp_4)) $x5550)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x7730 (- ?x7729 eta_2)))
 (let (($x7732 (> ?x7730 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_0)) $x7732)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x6748 (- ?x4178 eta_2)))
 (let (($x6750 (> ?x6748 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_1)) $x6750)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x5590 (- ?x367 eta_2)))
 (let (($x5592 (> ?x5590 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_2)) $x5592)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x5523 (- ?x289 eta_2)))
 (let (($x5525 (> ?x5523 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_3)) $x5525)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x5534 (- ?x302 eta_2)))
 (let (($x5536 (> ?x5534 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_2 xp_4)) $x5536)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_0)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_1)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_3)) $x5630)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x5633 (- ?x442 eta_2)))
 (let (($x5635 (> ?x5633 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_3 xp_4)) $x5635)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_0)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_1)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_2)) $x5650)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x5628 (- ?x425 eta_2)))
 (let (($x5630 (> ?x5628 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_4 xp_4)) $x5630)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x7787 (- ?x7786 eta_2)))
 (let (($x7789 (> ?x7787 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_0)) $x7789)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x6801 (- ?x4265 eta_2)))
 (let (($x6803 (> ?x6801 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_1)) $x6803)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x5662 (- ?x535 eta_2)))
 (let (($x5664 (> ?x5662 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_2)) $x5664)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x5648 (- ?x490 eta_2)))
 (let (($x5650 (> ?x5648 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_5 xp_3)) $x5650)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_0)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_1)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_2)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_3)) $x5692)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x5701 (- ?x610 eta_2)))
 (let (($x5703 (> ?x5701 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_6 xp_4)) $x5703)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_0)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_1)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_2)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_3)) $x5681)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x5690 (- ?x593 eta_2)))
 (let (($x5692 (> ?x5690 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_7 xp_4)) $x5692)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_0)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_1)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_2)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_3)) $x5745)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x5679 (- ?x580 eta_2)))
 (let (($x5681 (> ?x5679 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_8 xp_4)) $x5681)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x7874 (- ?x7873 eta_2)))
 (let (($x7876 (> ?x7874 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_0)) $x7876)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x6884 (- ?x4333 eta_2)))
 (let (($x6886 (> ?x6884 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_1)) $x6886)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x5801 (- ?x748 eta_2)))
 (let (($x5803 (> ?x5801 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_2)) $x5803)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x5772 (- ?x703 eta_2)))
 (let (($x5774 (> ?x5772 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_3)) $x5774)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x5743 (- ?x658 eta_2)))
 (let (($x5745 (> ?x5743 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_9 xp_4)) $x5745)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_0)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_1)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_2)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_3)) $x5843)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x5855 (- ?x800 eta_2)))
 (let (($x5857 (> ?x5855 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_10 xp_4)) $x5857)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_0)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_1)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_2)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_3)) $x5832)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x5841 (- ?x793 eta_2)))
 (let (($x5843 (> ?x5841 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_11 xp_4)) $x5843)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_0)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_1)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_2)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_3)) $x5899)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x5830 (- ?x2880 eta_2)))
 (let (($x5832 (> ?x5830 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_12 xp_4)) $x5832)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_0)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_1)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_2)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_3)) $x5931)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x5897 (- ?x827 eta_2)))
 (let (($x5899 (> ?x5897 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_13 xp_4)) $x5899)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x7999 (- ?x7998 eta_2)))
 (let (($x8001 (> ?x7999 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_0)) $x8001)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x7007 (- ?x4450 eta_2)))
 (let (($x7009 (> ?x7007 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_1)) $x7009)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x5993 (- ?x905 eta_2)))
 (let (($x5995 (> ?x5993 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_2)) $x5995)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x5961 (- ?x877 eta_2)))
 (let (($x5963 (> ?x5961 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_3)) $x5963)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x5929 (- ?x852 eta_2)))
 (let (($x5931 (> ?x5929 0.0)))
 (=> (= (+ yp_5 xp_4) (+ yp_14 xp_4)) $x5931)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_0)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_1)) $x8684)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x8696 (- ?x233 eta_1)))
 (let (($x8698 (> ?x8696 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_2)) $x8698)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x8710 (- ?x252 eta_1)))
 (let (($x8712 (> ?x8710 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_3)) $x8712)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x8724 (- ?x271 eta_1)))
 (let (($x8726 (> ?x8724 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_4)) $x8726)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_1)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_2)) $x8745)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x8748 (- ?x335 eta_1)))
 (let (($x8750 (> ?x8748 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_3)) $x8750)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x8753 (- ?x351 eta_1)))
 (let (($x8755 (> ?x8753 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_4)) $x8755)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_0)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_2)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_3)) $x8745)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x8748 (- ?x335 eta_1)))
 (let (($x8750 (> ?x8748 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_4)) $x8750)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_0)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_1)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_2)) $x8796)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x8805 (- ?x458 eta_1)))
 (let (($x8807 (> ?x8805 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_3)) $x8807)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x8819 (- ?x474 eta_1)))
 (let (($x8821 (> ?x8819 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_4)) $x8821)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_0)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_1)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_2)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_3)) $x8796)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x8805 (- ?x458 eta_1)))
 (let (($x8807 (> ?x8805 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_4)) $x8807)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_0)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_1)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_2)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_3)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_4)) $x8796)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_0)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_1)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_2)) $x8909)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x8921 (- ?x626 eta_1)))
 (let (($x8923 (> ?x8921 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_3)) $x8923)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x8935 (- ?x642 eta_1)))
 (let (($x8937 (> ?x8935 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_6 xp_4)) $x8937)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_0)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_1)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_2)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_3)) $x8909)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x8921 (- ?x626 eta_1)))
 (let (($x8923 (> ?x8921 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_7 xp_4)) $x8923)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_0)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_1)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_2)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_3)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_8 xp_4)) $x8909)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_9 xp_4)) $x8898)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_0)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_1)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_2)) $x9063)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x9075 (- ?x809 eta_1)))
 (let (($x9077 (> ?x9075 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_3)) $x9077)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x9089 (- ?x818 eta_1)))
 (let (($x9091 (> ?x9089 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_10 xp_4)) $x9091)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_0)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_1)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_2)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_3)) $x9063)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x9075 (- ?x809 eta_1)))
 (let (($x9077 (> ?x9075 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_11 xp_4)) $x9077)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_0)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_1)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_2)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_3)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_12 xp_4)) $x9063)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_13 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_14 xp_4)) $x9038)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_0)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_1)) $x8684)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x8696 (- ?x233 eta_1)))
 (let (($x8698 (> ?x8696 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_2)) $x8698)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x8710 (- ?x252 eta_1)))
 (let (($x8712 (> ?x8710 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_3)) $x8712)))))
(assert
 (let ((?x271 (+ 4.0 eta_0)))
 (let ((?x8724 (- ?x271 eta_1)))
 (let (($x8726 (> ?x8724 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_4)) $x8726)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_1)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_2)) $x8745)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x8748 (- ?x335 eta_1)))
 (let (($x8750 (> ?x8748 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_3)) $x8750)))))
(assert
 (let ((?x351 (+ 4.0 eta_1)))
 (let ((?x8753 (- ?x351 eta_1)))
 (let (($x8755 (> ?x8753 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_4)) $x8755)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_0)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_2)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_3)) $x8745)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x8748 (- ?x335 eta_1)))
 (let (($x8750 (> ?x8748 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_4)) $x8750)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_0)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_1)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_2)) $x8796)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x8805 (- ?x458 eta_1)))
 (let (($x8807 (> ?x8805 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_3)) $x8807)))))
(assert
 (let ((?x474 (+ 4.0 eta_2)))
 (let ((?x8819 (- ?x474 eta_1)))
 (let (($x8821 (> ?x8819 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_4)) $x8821)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_0)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_1)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_2)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_3)) $x8796)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x8805 (- ?x458 eta_1)))
 (let (($x8807 (> ?x8805 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_4)) $x8807)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_0)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_1)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_2)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_3)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_4)) $x8796)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_0)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_1)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_2)) $x8909)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x8921 (- ?x626 eta_1)))
 (let (($x8923 (> ?x8921 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_3)) $x8923)))))
(assert
 (let ((?x642 (+ 4.0 eta_3)))
 (let ((?x8935 (- ?x642 eta_1)))
 (let (($x8937 (> ?x8935 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_6 xp_4)) $x8937)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_0)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_1)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_2)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_3)) $x8909)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x8921 (- ?x626 eta_1)))
 (let (($x8923 (> ?x8921 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_7 xp_4)) $x8923)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_0)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_1)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_2)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_3)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_8 xp_4)) $x8909)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_9 xp_4)) $x8898)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_0)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_1)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_2)) $x9063)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x9075 (- ?x809 eta_1)))
 (let (($x9077 (> ?x9075 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_3)) $x9077)))))
(assert
 (let ((?x818 (+ 4.0 eta_4)))
 (let ((?x9089 (- ?x818 eta_1)))
 (let (($x9091 (> ?x9089 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_10 xp_4)) $x9091)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_0)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_1)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_2)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_3)) $x9063)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x9075 (- ?x809 eta_1)))
 (let (($x9077 (> ?x9075 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_11 xp_4)) $x9077)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_0)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_1)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_2)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_3)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_12 xp_4)) $x9063)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_13 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_14 xp_4)) $x9038)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x9550 (- ?x4117 eta_1)))
 (let (($x9552 (> ?x9550 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_0)) $x9552)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_1)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_2)) $x8684)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x8696 (- ?x233 eta_1)))
 (let (($x8698 (> ?x8696 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_3)) $x8698)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x8710 (- ?x252 eta_1)))
 (let (($x8712 (> ?x8710 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_4)) $x8712)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_0)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_2)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_3)) $x8745)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x8748 (- ?x335 eta_1)))
 (let (($x8750 (> ?x8748 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_4)) $x8750)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_0)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_1)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_3)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_4)) $x8745)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_0)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_1)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_2)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_3)) $x8796)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x8805 (- ?x458 eta_1)))
 (let (($x8807 (> ?x8805 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_4)) $x8807)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_0)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_1)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_2)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_3)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_4)) $x8796)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_0)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_1)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_2)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_3)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_4)) $x8785)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_0)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_1)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_2)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_3)) $x8909)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x8921 (- ?x626 eta_1)))
 (let (($x8923 (> ?x8921 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_6 xp_4)) $x8923)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_0)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_1)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_2)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_3)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_7 xp_4)) $x8909)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_8 xp_4)) $x8898)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_0)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_1)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_2)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_3)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_9 xp_4)) $x8887)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_0)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_1)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_2)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_3)) $x9063)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x9075 (- ?x809 eta_1)))
 (let (($x9077 (> ?x9075 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_10 xp_4)) $x9077)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_0)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_1)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_2)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_3)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_11 xp_4)) $x9063)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_12 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_13 xp_4)) $x9038)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_0)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_1)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_2)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_3)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_14 xp_4)) $x9105)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x9550 (- ?x4117 eta_1)))
 (let (($x9552 (> ?x9550 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_0)) $x9552)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_1)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_2)) $x8684)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x8696 (- ?x233 eta_1)))
 (let (($x8698 (> ?x8696 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_3)) $x8698)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x8710 (- ?x252 eta_1)))
 (let (($x8712 (> ?x8710 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_4)) $x8712)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_0)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_2)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_3)) $x8745)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x8748 (- ?x335 eta_1)))
 (let (($x8750 (> ?x8748 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_4)) $x8750)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_0)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_1)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_3)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_4)) $x8745)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_0)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_1)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_2)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_3)) $x8796)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x8805 (- ?x458 eta_1)))
 (let (($x8807 (> ?x8805 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_4)) $x8807)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_0)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_1)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_2)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_3)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_4)) $x8796)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_0)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_1)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_2)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_3)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_4)) $x8785)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_0)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_1)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_2)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_3)) $x8909)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x8921 (- ?x626 eta_1)))
 (let (($x8923 (> ?x8921 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_6 xp_4)) $x8923)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_0)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_1)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_2)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_3)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_7 xp_4)) $x8909)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_8 xp_4)) $x8898)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_0)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_1)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_2)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_3)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_9 xp_4)) $x8887)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_0)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_1)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_2)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_3)) $x9063)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x9075 (- ?x809 eta_1)))
 (let (($x9077 (> ?x9075 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_10 xp_4)) $x9077)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_0)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_1)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_2)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_3)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_11 xp_4)) $x9063)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_12 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_13 xp_4)) $x9038)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_0)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_1)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_2)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_3)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_14 xp_4)) $x9105)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x10200 (- ?x7668 eta_1)))
 (let (($x10202 (> ?x10200 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_0)) $x10202)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x9550 (- ?x4117 eta_1)))
 (let (($x9552 (> ?x9550 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_1)) $x9552)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_2)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_3)) $x8684)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x8696 (- ?x233 eta_1)))
 (let (($x8698 (> ?x8696 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_0 xp_4)) $x8698)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_0)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_1)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_3)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_1 xp_4)) $x8745)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x10242 (- ?x7729 eta_1)))
 (let (($x10244 (> ?x10242 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_0)) $x10244)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_1)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_2)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_2 xp_4)) $x8740)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_0)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_1)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_2)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_3)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_3 xp_4)) $x8796)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_0)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_1)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_2)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_3)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_4 xp_4)) $x8785)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x10299 (- ?x7786 eta_1)))
 (let (($x10301 (> ?x10299 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_0)) $x10301)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_1)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_2)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_3)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_5 xp_4)) $x8774)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_0)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_1)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_2)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_3)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_6 xp_4)) $x8909)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_7 xp_4)) $x8898)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_0)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_1)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_2)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_3)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_8 xp_4)) $x8887)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x10393 (- ?x7873 eta_1)))
 (let (($x10395 (> ?x10393 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_0)) $x10395)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_1)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_2)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_3)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_9 xp_4)) $x8951)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_0)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_1)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_2)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_3)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_10 xp_4)) $x9063)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_11 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_12 xp_4)) $x9038)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_0)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_1)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_2)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_3)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_13 xp_4)) $x9105)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x10516 (- ?x7998 eta_1)))
 (let (($x10518 (> ?x10516 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_0)) $x10518)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_1)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_2)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_3)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_2) (+ yp_14 xp_4)) $x9137)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x10200 (- ?x7668 eta_1)))
 (let (($x10202 (> ?x10200 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_0)) $x10202)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x9550 (- ?x4117 eta_1)))
 (let (($x9552 (> ?x9550 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_1)) $x9552)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_2)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_3)) $x8684)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x8696 (- ?x233 eta_1)))
 (let (($x8698 (> ?x8696 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_0 xp_4)) $x8698)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_0)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_1)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_3)) $x8740)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x8743 (- ?x319 eta_1)))
 (let (($x8745 (> ?x8743 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_1 xp_4)) $x8745)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x10242 (- ?x7729 eta_1)))
 (let (($x10244 (> ?x10242 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_0)) $x10244)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_1)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_2)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_2 xp_4)) $x8740)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_0)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_1)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_2)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_3)) $x8785)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x8794 (- ?x442 eta_1)))
 (let (($x8796 (> ?x8794 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_3 xp_4)) $x8796)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_0)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_1)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_2)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_3)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_4 xp_4)) $x8785)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x10299 (- ?x7786 eta_1)))
 (let (($x10301 (> ?x10299 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_0)) $x10301)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_1)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_2)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_3)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_5 xp_4)) $x8774)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_0)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_1)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_2)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_3)) $x8898)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x8907 (- ?x610 eta_1)))
 (let (($x8909 (> ?x8907 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_6 xp_4)) $x8909)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_7 xp_4)) $x8898)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_0)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_1)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_2)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_3)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_8 xp_4)) $x8887)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x10393 (- ?x7873 eta_1)))
 (let (($x10395 (> ?x10393 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_0)) $x10395)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_1)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_2)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_3)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_9 xp_4)) $x8951)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_0)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_1)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_2)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_3)) $x9049)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x9061 (- ?x800 eta_1)))
 (let (($x9063 (> ?x9061 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_10 xp_4)) $x9063)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_11 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_12 xp_4)) $x9038)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_0)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_1)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_2)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_3)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_13 xp_4)) $x9105)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x10516 (- ?x7998 eta_1)))
 (let (($x10518 (> ?x10516 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_0)) $x10518)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_1)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_2)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_3)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_3) (+ yp_14 xp_4)) $x9137)))))
(assert
 (let ((?x10856 (+ (- 3.0) eta_0)))
 (let ((?x10857 (- ?x10856 eta_1)))
 (let (($x10859 (> ?x10857 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_0)) $x10859)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x10200 (- ?x7668 eta_1)))
 (let (($x10202 (> ?x10200 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_1)) $x10202)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x9550 (- ?x4117 eta_1)))
 (let (($x9552 (> ?x9550 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_2)) $x9552)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_3)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_0 xp_4)) $x8684)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x10242 (- ?x7729 eta_1)))
 (let (($x10244 (> ?x10242 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_0)) $x10244)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_1)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_2)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_1 xp_4)) $x8740)))))
(assert
 (let ((?x10899 (+ (- 4.0) eta_1)))
 (let ((?x10900 (- ?x10899 eta_1)))
 (let (($x10902 (> ?x10900 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_0)) $x10902)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x10242 (- ?x7729 eta_1)))
 (let (($x10244 (> ?x10242 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_1)) $x10244)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_2)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_2 xp_3)) $x8760)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_0)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_1)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_2)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_3)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_3 xp_4)) $x8785)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x10299 (- ?x7786 eta_1)))
 (let (($x10301 (> ?x10299 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_0)) $x10301)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_1)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_2)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_3)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_4 xp_4)) $x8774)))))
(assert
 (let ((?x10957 (+ (- 5.0) eta_2)))
 (let ((?x10958 (- ?x10957 eta_1)))
 (let (($x10960 (> ?x10958 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_0)) $x10960)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x10299 (- ?x7786 eta_1)))
 (let (($x10301 (> ?x10299 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_1)) $x10301)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_2)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_3)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_5 xp_4)) $x8835)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_6 xp_4)) $x8898)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_0)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_1)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_2)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_3)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_7 xp_4)) $x8887)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x10393 (- ?x7873 eta_1)))
 (let (($x10395 (> ?x10393 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_0)) $x10395)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_1)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_2)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_3)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_8 xp_4)) $x8951)))))
(assert
 (let ((?x11049 (+ (- 6.0) eta_3)))
 (let ((?x11050 (- ?x11049 eta_1)))
 (let (($x11052 (> ?x11050 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_0)) $x11052)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x10393 (- ?x7873 eta_1)))
 (let (($x10395 (> ?x10393 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_1)) $x10395)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_2)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_3)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_9 xp_4)) $x8980)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_10 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_11 xp_4)) $x9038)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_0)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_1)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_2)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_3)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_12 xp_4)) $x9105)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x10516 (- ?x7998 eta_1)))
 (let (($x10518 (> ?x10516 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_0)) $x10518)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_1)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_2)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_3)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_13 xp_4)) $x9137)))))
(assert
 (let ((?x11177 (+ (- 7.0) eta_4)))
 (let ((?x11178 (- ?x11177 eta_1)))
 (let (($x11180 (> ?x11178 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_0)) $x11180)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x10516 (- ?x7998 eta_1)))
 (let (($x10518 (> ?x10516 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_1)) $x10518)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_2)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_3)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_1 xp_3) (+ yp_14 xp_4)) $x9169)))))
(assert
 (let ((?x10856 (+ (- 3.0) eta_0)))
 (let ((?x10857 (- ?x10856 eta_1)))
 (let (($x10859 (> ?x10857 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_0)) $x10859)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x10200 (- ?x7668 eta_1)))
 (let (($x10202 (> ?x10200 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_1)) $x10202)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x9550 (- ?x4117 eta_1)))
 (let (($x9552 (> ?x9550 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_2)) $x9552)))))
(assert
 (let ((?x195 (+ 0.0 eta_0)))
 (let ((?x8670 (- ?x195 eta_1)))
 (let (($x8672 (> ?x8670 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_3)) $x8672)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x8682 (- ?x214 eta_1)))
 (let (($x8684 (> ?x8682 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_0 xp_4)) $x8684)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x10242 (- ?x7729 eta_1)))
 (let (($x10244 (> ?x10242 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_0)) $x10244)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_1)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_2)) $x8760)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x8738 (- ?x302 eta_1)))
 (let (($x8740 (> ?x8738 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_1 xp_4)) $x8740)))))
(assert
 (let ((?x10899 (+ (- 4.0) eta_1)))
 (let ((?x10900 (- ?x10899 eta_1)))
 (let (($x10902 (> ?x10900 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_0)) $x10902)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x10242 (- ?x7729 eta_1)))
 (let (($x10244 (> ?x10242 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_1)) $x10244)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x9592 (- ?x4178 eta_1)))
 (let (($x9594 (> ?x9592 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_2)) $x9594)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x8758 (- ?x367 eta_1)))
 (let (($x8760 (> ?x8758 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_2 xp_3)) $x8760)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_0)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_1)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_2)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_3)) $x8774)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x8783 (- ?x425 eta_1)))
 (let (($x8785 (> ?x8783 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_3 xp_4)) $x8785)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x10299 (- ?x7786 eta_1)))
 (let (($x10301 (> ?x10299 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_0)) $x10301)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_1)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_2)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_3)) $x8835)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x8772 (- ?x412 eta_1)))
 (let (($x8774 (> ?x8772 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_4 xp_4)) $x8774)))))
(assert
 (let ((?x10957 (+ (- 5.0) eta_2)))
 (let ((?x10958 (- ?x10957 eta_1)))
 (let (($x10960 (> ?x10958 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_0)) $x10960)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x10299 (- ?x7786 eta_1)))
 (let (($x10301 (> ?x10299 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_1)) $x10301)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x9646 (- ?x4265 eta_1)))
 (let (($x9648 (> ?x9646 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_2)) $x9648)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x8859 (- ?x535 eta_1)))
 (let (($x8861 (> ?x8859 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_3)) $x8861)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x8833 (- ?x490 eta_1)))
 (let (($x8835 (> ?x8833 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_5 xp_4)) $x8835)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_0)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_1)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_2)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_3)) $x8887)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x8896 (- ?x593 eta_1)))
 (let (($x8898 (> ?x8896 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_6 xp_4)) $x8898)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_0)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_1)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_2)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_3)) $x8951)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x8885 (- ?x580 eta_1)))
 (let (($x8887 (> ?x8885 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_7 xp_4)) $x8887)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x10393 (- ?x7873 eta_1)))
 (let (($x10395 (> ?x10393 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_0)) $x10395)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_1)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_2)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_3)) $x8980)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x8949 (- ?x658 eta_1)))
 (let (($x8951 (> ?x8949 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_8 xp_4)) $x8951)))))
(assert
 (let ((?x11049 (+ (- 6.0) eta_3)))
 (let ((?x11050 (- ?x11049 eta_1)))
 (let (($x11052 (> ?x11050 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_0)) $x11052)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x10393 (- ?x7873 eta_1)))
 (let (($x10395 (> ?x10393 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_1)) $x10395)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x9737 (- ?x4333 eta_1)))
 (let (($x9739 (> ?x9737 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_2)) $x9739)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x9007 (- ?x748 eta_1)))
 (let (($x9009 (> ?x9007 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_3)) $x9009)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x8978 (- ?x703 eta_1)))
 (let (($x8980 (> ?x8978 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_9 xp_4)) $x8980)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_0)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_1)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_2)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_3)) $x9038)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x9047 (- ?x793 eta_1)))
 (let (($x9049 (> ?x9047 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_10 xp_4)) $x9049)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_0)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_1)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_2)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_3)) $x9105)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x9036 (- ?x2880 eta_1)))
 (let (($x9038 (> ?x9036 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_11 xp_4)) $x9038)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_0)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_1)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_2)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_3)) $x9137)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x9103 (- ?x827 eta_1)))
 (let (($x9105 (> ?x9103 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_12 xp_4)) $x9105)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x10516 (- ?x7998 eta_1)))
 (let (($x10518 (> ?x10516 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_0)) $x10518)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_1)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_2)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_3)) $x9169)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x9135 (- ?x852 eta_1)))
 (let (($x9137 (> ?x9135 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_13 xp_4)) $x9137)))))
(assert
 (let ((?x11177 (+ (- 7.0) eta_4)))
 (let ((?x11178 (- ?x11177 eta_1)))
 (let (($x11180 (> ?x11178 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_0)) $x11180)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x10516 (- ?x7998 eta_1)))
 (let (($x10518 (> ?x10516 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_1)) $x10518)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x9860 (- ?x4450 eta_1)))
 (let (($x9862 (> ?x9860 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_2)) $x9862)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x9199 (- ?x905 eta_1)))
 (let (($x9201 (> ?x9199 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_3)) $x9201)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x9167 (- ?x877 eta_1)))
 (let (($x9169 (> ?x9167 0.0)))
 (=> (= (+ yp_2 xp_4) (+ yp_14 xp_4)) $x9169)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x11516 (- ?x214 eta_0)))
 (let (($x11518 (> ?x11516 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_1)) $x11518)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x11522 (- ?x233 eta_0)))
 (let (($x11524 (> ?x11522 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_2)) $x11524)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x11527 (- ?x252 eta_0)))
 (let (($x11529 (> ?x11527 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_3)) $x11529)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_4)) (> (- (+ 4.0 eta_0) eta_0) 0.0)))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_0)) $x11539)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x11548 (- ?x302 eta_0)))
 (let (($x11550 (> ?x11548 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_1)) $x11550)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x11559 (- ?x319 eta_0)))
 (let (($x11561 (> ?x11559 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_2)) $x11561)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x11570 (- ?x335 eta_0)))
 (let (($x11572 (> ?x11570 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_3)) $x11572)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_4)) (> (- (+ 4.0 eta_1) eta_0) 0.0)))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_0)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_1)) $x11539)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x11548 (- ?x302 eta_0)))
 (let (($x11550 (> ?x11548 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_2)) $x11550)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x11559 (- ?x319 eta_0)))
 (let (($x11561 (> ?x11559 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_3)) $x11561)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x11570 (- ?x335 eta_0)))
 (let (($x11572 (> ?x11570 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_4)) $x11572)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_0)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_1)) $x11631)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x11640 (- ?x442 eta_0)))
 (let (($x11642 (> ?x11640 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_2)) $x11642)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x11651 (- ?x458 eta_0)))
 (let (($x11653 (> ?x11651 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_3)) $x11653)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_4)) (> (- (+ 4.0 eta_2) eta_0) 0.0)))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_0)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_1)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_2)) $x11631)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x11640 (- ?x442 eta_0)))
 (let (($x11642 (> ?x11640 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_3)) $x11642)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x11651 (- ?x458 eta_0)))
 (let (($x11653 (> ?x11651 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_4)) $x11653)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_0)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_1)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_2)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_3)) $x11631)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x11640 (- ?x442 eta_0)))
 (let (($x11642 (> ?x11640 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_4)) $x11642)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_0)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_1)) $x11744)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x11753 (- ?x610 eta_0)))
 (let (($x11755 (> ?x11753 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_2)) $x11755)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x11767 (- ?x626 eta_0)))
 (let (($x11769 (> ?x11767 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_3)) $x11769)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_6 xp_4)) (> (- (+ 4.0 eta_3) eta_0) 0.0)))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_0)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_1)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_2)) $x11744)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x11753 (- ?x610 eta_0)))
 (let (($x11755 (> ?x11753 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_3)) $x11755)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x11767 (- ?x626 eta_0)))
 (let (($x11769 (> ?x11767 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_7 xp_4)) $x11769)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_0)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_1)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_2)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_3)) $x11744)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x11753 (- ?x610 eta_0)))
 (let (($x11755 (> ?x11753 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_8 xp_4)) $x11755)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_0)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_1)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_2)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_3)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_9 xp_4)) $x11744)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_0)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_1)) $x11895)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x11907 (- ?x800 eta_0)))
 (let (($x11909 (> ?x11907 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_2)) $x11909)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x11921 (- ?x809 eta_0)))
 (let (($x11923 (> ?x11921 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_3)) $x11923)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_10 xp_4)) (> (- (+ 4.0 eta_4) eta_0) 0.0)))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_0)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_1)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_2)) $x11895)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x11907 (- ?x800 eta_0)))
 (let (($x11909 (> ?x11907 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_3)) $x11909)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x11921 (- ?x809 eta_0)))
 (let (($x11923 (> ?x11921 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_11 xp_4)) $x11923)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_0)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_1)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_2)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_3)) $x11895)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x11907 (- ?x800 eta_0)))
 (let (($x11909 (> ?x11907 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_12 xp_4)) $x11909)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_0)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_1)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_2)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_3)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_13 xp_4)) $x11895)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_0)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_1)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_2)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_3)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_14 xp_4)) $x11884)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x12077 (- ?x4117 eta_0)))
 (let (($x12079 (> ?x12077 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_0)) $x12079)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x11516 (- ?x214 eta_0)))
 (let (($x11518 (> ?x11516 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_2)) $x11518)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x11522 (- ?x233 eta_0)))
 (let (($x11524 (> ?x11522 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_3)) $x11524)))))
(assert
 (let ((?x252 (+ 3.0 eta_0)))
 (let ((?x11527 (- ?x252 eta_0)))
 (let (($x11529 (> ?x11527 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_4)) $x11529)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_0)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_1)) $x11539)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x11548 (- ?x302 eta_0)))
 (let (($x11550 (> ?x11548 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_2)) $x11550)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x11559 (- ?x319 eta_0)))
 (let (($x11561 (> ?x11559 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_3)) $x11561)))))
(assert
 (let ((?x335 (+ 3.0 eta_1)))
 (let ((?x11570 (- ?x335 eta_0)))
 (let (($x11572 (> ?x11570 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_4)) $x11572)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x12105 (- ?x4178 eta_0)))
 (let (($x12107 (> ?x12105 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_0)) $x12107)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_1)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_2)) $x11539)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x11548 (- ?x302 eta_0)))
 (let (($x11550 (> ?x11548 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_3)) $x11550)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x11559 (- ?x319 eta_0)))
 (let (($x11561 (> ?x11559 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_4)) $x11561)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_0)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_1)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_2)) $x11631)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x11640 (- ?x442 eta_0)))
 (let (($x11642 (> ?x11640 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_3)) $x11642)))))
(assert
 (let ((?x458 (+ 3.0 eta_2)))
 (let ((?x11651 (- ?x458 eta_0)))
 (let (($x11653 (> ?x11651 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_4)) $x11653)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_0)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_1)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_2)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_3)) $x11631)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x11640 (- ?x442 eta_0)))
 (let (($x11642 (> ?x11640 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_4)) $x11642)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_0)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_1)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_2)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_3)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_4)) $x11631)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_0)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_1)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_2)) $x11744)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x11753 (- ?x610 eta_0)))
 (let (($x11755 (> ?x11753 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_3)) $x11755)))))
(assert
 (let ((?x626 (+ 3.0 eta_3)))
 (let ((?x11767 (- ?x626 eta_0)))
 (let (($x11769 (> ?x11767 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_6 xp_4)) $x11769)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_0)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_1)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_2)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_3)) $x11744)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x11753 (- ?x610 eta_0)))
 (let (($x11755 (> ?x11753 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_7 xp_4)) $x11755)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_0)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_1)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_2)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_3)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_8 xp_4)) $x11744)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_0)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_1)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_2)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_3)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_9 xp_4)) $x11733)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_0)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_1)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_2)) $x11895)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x11907 (- ?x800 eta_0)))
 (let (($x11909 (> ?x11907 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_3)) $x11909)))))
(assert
 (let ((?x809 (+ 3.0 eta_4)))
 (let ((?x11921 (- ?x809 eta_0)))
 (let (($x11923 (> ?x11921 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_10 xp_4)) $x11923)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_0)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_1)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_2)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_3)) $x11895)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x11907 (- ?x800 eta_0)))
 (let (($x11909 (> ?x11907 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_11 xp_4)) $x11909)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_0)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_1)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_2)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_3)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_12 xp_4)) $x11895)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_0)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_1)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_2)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_3)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_13 xp_4)) $x11884)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_0)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_1)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_2)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_3)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_14 xp_4)) $x11951)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x12415 (- ?x7668 eta_0)))
 (let (($x12417 (> ?x12415 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_0)) $x12417)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x12077 (- ?x4117 eta_0)))
 (let (($x12079 (> ?x12077 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_1)) $x12079)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x11516 (- ?x214 eta_0)))
 (let (($x11518 (> ?x11516 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_3)) $x11518)))))
(assert
 (let ((?x233 (+ 2.0 eta_0)))
 (let ((?x11522 (- ?x233 eta_0)))
 (let (($x11524 (> ?x11522 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_4)) $x11524)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x12105 (- ?x4178 eta_0)))
 (let (($x12107 (> ?x12105 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_0)) $x12107)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_1)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_2)) $x11539)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x11548 (- ?x302 eta_0)))
 (let (($x11550 (> ?x11548 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_3)) $x11550)))))
(assert
 (let ((?x319 (+ 2.0 eta_1)))
 (let ((?x11559 (- ?x319 eta_0)))
 (let (($x11561 (> ?x11559 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_4)) $x11561)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x12443 (- ?x7729 eta_0)))
 (let (($x12445 (> ?x12443 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_0)) $x12445)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x12105 (- ?x4178 eta_0)))
 (let (($x12107 (> ?x12105 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_1)) $x12107)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_2)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_3)) $x11539)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x11548 (- ?x302 eta_0)))
 (let (($x11550 (> ?x11548 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_4)) $x11550)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_0)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_1)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_2)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_3)) $x11631)))))
(assert
 (let ((?x442 (+ 2.0 eta_2)))
 (let ((?x11640 (- ?x442 eta_0)))
 (let (($x11642 (> ?x11640 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_4)) $x11642)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_0)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_1)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_2)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_3)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_4)) $x11631)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x12508 (- ?x7786 eta_0)))
 (let (($x12510 (> ?x12508 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_0)) $x12510)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_1)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_2)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_3)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_4)) $x11620)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_0)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_1)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_2)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_3)) $x11744)))))
(assert
 (let ((?x610 (+ 2.0 eta_3)))
 (let ((?x11753 (- ?x610 eta_0)))
 (let (($x11755 (> ?x11753 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_6 xp_4)) $x11755)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_0)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_1)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_2)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_3)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_7 xp_4)) $x11744)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_0)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_1)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_2)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_3)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_8 xp_4)) $x11733)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x12602 (- ?x7873 eta_0)))
 (let (($x12604 (> ?x12602 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_0)) $x12604)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_1)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_2)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_3)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_9 xp_4)) $x11797)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_0)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_1)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_2)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_3)) $x11895)))))
(assert
 (let ((?x800 (+ 2.0 eta_4)))
 (let ((?x11907 (- ?x800 eta_0)))
 (let (($x11909 (> ?x11907 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_10 xp_4)) $x11909)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_0)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_1)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_2)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_3)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_11 xp_4)) $x11895)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_0)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_1)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_2)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_3)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_12 xp_4)) $x11884)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_0)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_1)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_2)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_3)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_13 xp_4)) $x11951)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x12725 (- ?x7998 eta_0)))
 (let (($x12727 (> ?x12725 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_0)) $x12727)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_1)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_2)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_3)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_14 xp_4)) $x11983)))))
(assert
 (let ((?x10856 (+ (- 3.0) eta_0)))
 (let ((?x12756 (- ?x10856 eta_0)))
 (let (($x12758 (> ?x12756 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_0)) $x12758)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x12415 (- ?x7668 eta_0)))
 (let (($x12417 (> ?x12415 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_1)) $x12417)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x12077 (- ?x4117 eta_0)))
 (let (($x12079 (> ?x12077 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_2)) $x12079)))))
(assert
 (let ((?x214 (+ 1.0 eta_0)))
 (let ((?x11516 (- ?x214 eta_0)))
 (let (($x11518 (> ?x11516 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_0 xp_4)) $x11518)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x12443 (- ?x7729 eta_0)))
 (let (($x12445 (> ?x12443 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_0)) $x12445)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x12105 (- ?x4178 eta_0)))
 (let (($x12107 (> ?x12105 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_1)) $x12107)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_2)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_3)) $x11539)))))
(assert
 (let ((?x302 (+ 1.0 eta_1)))
 (let ((?x11548 (- ?x302 eta_0)))
 (let (($x11550 (> ?x11548 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_1 xp_4)) $x11550)))))
(assert
 (let ((?x10899 (+ (- 4.0) eta_1)))
 (let ((?x12784 (- ?x10899 eta_0)))
 (let (($x12786 (> ?x12784 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_0)) $x12786)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x12443 (- ?x7729 eta_0)))
 (let (($x12445 (> ?x12443 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_1)) $x12445)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x12105 (- ?x4178 eta_0)))
 (let (($x12107 (> ?x12105 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_2)) $x12107)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_3)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_2 xp_4)) $x11539)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_0)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_1)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_2)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_3)) $x11620)))))
(assert
 (let ((?x425 (+ 1.0 eta_2)))
 (let ((?x11629 (- ?x425 eta_0)))
 (let (($x11631 (> ?x11629 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_3 xp_4)) $x11631)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x12508 (- ?x7786 eta_0)))
 (let (($x12510 (> ?x12508 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_0)) $x12510)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_1)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_2)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_3)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_4 xp_4)) $x11620)))))
(assert
 (let ((?x10957 (+ (- 5.0) eta_2)))
 (let ((?x12846 (- ?x10957 eta_0)))
 (let (($x12848 (> ?x12846 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_0)) $x12848)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x12508 (- ?x7786 eta_0)))
 (let (($x12510 (> ?x12508 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_1)) $x12510)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_2)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_3)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_5 xp_4)) $x11681)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_0)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_1)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_2)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_3)) $x11733)))))
(assert
 (let ((?x593 (+ 1.0 eta_3)))
 (let ((?x11742 (- ?x593 eta_0)))
 (let (($x11744 (> ?x11742 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_6 xp_4)) $x11744)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_0)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_1)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_2)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_3)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_7 xp_4)) $x11733)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x12602 (- ?x7873 eta_0)))
 (let (($x12604 (> ?x12602 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_0)) $x12604)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_1)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_2)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_3)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_8 xp_4)) $x11797)))))
(assert
 (let ((?x11049 (+ (- 6.0) eta_3)))
 (let ((?x12937 (- ?x11049 eta_0)))
 (let (($x12939 (> ?x12937 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_0)) $x12939)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x12602 (- ?x7873 eta_0)))
 (let (($x12604 (> ?x12602 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_1)) $x12604)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_2)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_3)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_9 xp_4)) $x11826)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_0)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_1)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_2)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_3)) $x11884)))))
(assert
 (let ((?x793 (+ 1.0 eta_4)))
 (let ((?x11893 (- ?x793 eta_0)))
 (let (($x11895 (> ?x11893 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_10 xp_4)) $x11895)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_0)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_1)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_2)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_3)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_11 xp_4)) $x11884)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_0)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_1)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_2)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_3)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_12 xp_4)) $x11951)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x12725 (- ?x7998 eta_0)))
 (let (($x12727 (> ?x12725 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_0)) $x12727)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_1)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_2)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_3)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_13 xp_4)) $x11983)))))
(assert
 (let ((?x11177 (+ (- 7.0) eta_4)))
 (let ((?x13063 (- ?x11177 eta_0)))
 (let (($x13065 (> ?x13063 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_0)) $x13065)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x12725 (- ?x7998 eta_0)))
 (let (($x12727 (> ?x12725 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_1)) $x12727)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_2)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_3)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_3) (+ yp_14 xp_4)) $x12015)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_0)) (> (- (+ (- 4.0) eta_0) eta_0) 0.0)))
(assert
 (let ((?x10856 (+ (- 3.0) eta_0)))
 (let ((?x12756 (- ?x10856 eta_0)))
 (let (($x12758 (> ?x12756 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_1)) $x12758)))))
(assert
 (let ((?x7668 (+ (- 2.0) eta_0)))
 (let ((?x12415 (- ?x7668 eta_0)))
 (let (($x12417 (> ?x12415 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_2)) $x12417)))))
(assert
 (let ((?x4117 (+ (- 1.0) eta_0)))
 (let ((?x12077 (- ?x4117 eta_0)))
 (let (($x12079 (> ?x12077 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_0 xp_3)) $x12079)))))
(assert
 (let ((?x10899 (+ (- 4.0) eta_1)))
 (let ((?x12784 (- ?x10899 eta_0)))
 (let (($x12786 (> ?x12784 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_0)) $x12786)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x12443 (- ?x7729 eta_0)))
 (let (($x12445 (> ?x12443 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_1)) $x12445)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x12105 (- ?x4178 eta_0)))
 (let (($x12107 (> ?x12105 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_2)) $x12107)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_3)) $x11597)))))
(assert
 (let ((?x289 (+ 0.0 eta_1)))
 (let ((?x11537 (- ?x289 eta_0)))
 (let (($x11539 (> ?x11537 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_1 xp_4)) $x11539)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_0)) (> (- (+ (- 5.0) eta_1) eta_0) 0.0)))
(assert
 (let ((?x10899 (+ (- 4.0) eta_1)))
 (let ((?x12784 (- ?x10899 eta_0)))
 (let (($x12786 (> ?x12784 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_1)) $x12786)))))
(assert
 (let ((?x7729 (+ (- 3.0) eta_1)))
 (let ((?x12443 (- ?x7729 eta_0)))
 (let (($x12445 (> ?x12443 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_2)) $x12445)))))
(assert
 (let ((?x4178 (+ (- 2.0) eta_1)))
 (let ((?x12105 (- ?x4178 eta_0)))
 (let (($x12107 (> ?x12105 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_3)) $x12107)))))
(assert
 (let ((?x367 (+ (- 1.0) eta_1)))
 (let ((?x11595 (- ?x367 eta_0)))
 (let (($x11597 (> ?x11595 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_2 xp_4)) $x11597)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x12508 (- ?x7786 eta_0)))
 (let (($x12510 (> ?x12508 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_0)) $x12510)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_1)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_2)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_3)) $x11681)))))
(assert
 (let ((?x412 (+ 0.0 eta_2)))
 (let ((?x11618 (- ?x412 eta_0)))
 (let (($x11620 (> ?x11618 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_3 xp_4)) $x11620)))))
(assert
 (let ((?x10957 (+ (- 5.0) eta_2)))
 (let ((?x12846 (- ?x10957 eta_0)))
 (let (($x12848 (> ?x12846 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_0)) $x12848)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x12508 (- ?x7786 eta_0)))
 (let (($x12510 (> ?x12508 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_1)) $x12510)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_2)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_3)) $x11707)))))
(assert
 (let ((?x490 (+ (- 1.0) eta_2)))
 (let ((?x11679 (- ?x490 eta_0)))
 (let (($x11681 (> ?x11679 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_4 xp_4)) $x11681)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_0)) (> (- (+ (- 6.0) eta_2) eta_0) 0.0)))
(assert
 (let ((?x10957 (+ (- 5.0) eta_2)))
 (let ((?x12846 (- ?x10957 eta_0)))
 (let (($x12848 (> ?x12846 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_1)) $x12848)))))
(assert
 (let ((?x7786 (+ (- 4.0) eta_2)))
 (let ((?x12508 (- ?x7786 eta_0)))
 (let (($x12510 (> ?x12508 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_2)) $x12510)))))
(assert
 (let ((?x4265 (+ (- 3.0) eta_2)))
 (let ((?x12170 (- ?x4265 eta_0)))
 (let (($x12172 (> ?x12170 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_3)) $x12172)))))
(assert
 (let ((?x535 (+ (- 2.0) eta_2)))
 (let ((?x11705 (- ?x535 eta_0)))
 (let (($x11707 (> ?x11705 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_5 xp_4)) $x11707)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_0)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_1)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_2)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_3)) $x11797)))))
(assert
 (let ((?x580 (+ 0.0 eta_3)))
 (let ((?x11731 (- ?x580 eta_0)))
 (let (($x11733 (> ?x11731 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_6 xp_4)) $x11733)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x12602 (- ?x7873 eta_0)))
 (let (($x12604 (> ?x12602 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_0)) $x12604)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_1)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_2)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_3)) $x11826)))))
(assert
 (let ((?x658 (+ (- 1.0) eta_3)))
 (let ((?x11795 (- ?x658 eta_0)))
 (let (($x11797 (> ?x11795 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_7 xp_4)) $x11797)))))
(assert
 (let ((?x11049 (+ (- 6.0) eta_3)))
 (let ((?x12937 (- ?x11049 eta_0)))
 (let (($x12939 (> ?x12937 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_0)) $x12939)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x12602 (- ?x7873 eta_0)))
 (let (($x12604 (> ?x12602 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_1)) $x12604)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_2)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_3)) $x11855)))))
(assert
 (let ((?x703 (+ (- 2.0) eta_3)))
 (let ((?x11824 (- ?x703 eta_0)))
 (let (($x11826 (> ?x11824 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_8 xp_4)) $x11826)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_0)) (> (- (+ (- 7.0) eta_3) eta_0) 0.0)))
(assert
 (let ((?x11049 (+ (- 6.0) eta_3)))
 (let ((?x12937 (- ?x11049 eta_0)))
 (let (($x12939 (> ?x12937 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_1)) $x12939)))))
(assert
 (let ((?x7873 (+ (- 5.0) eta_3)))
 (let ((?x12602 (- ?x7873 eta_0)))
 (let (($x12604 (> ?x12602 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_2)) $x12604)))))
(assert
 (let ((?x4333 (+ (- 4.0) eta_3)))
 (let ((?x12261 (- ?x4333 eta_0)))
 (let (($x12263 (> ?x12261 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_3)) $x12263)))))
(assert
 (let ((?x748 (+ (- 3.0) eta_3)))
 (let ((?x11853 (- ?x748 eta_0)))
 (let (($x11855 (> ?x11853 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_9 xp_4)) $x11855)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_0)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_1)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_2)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_3)) $x11951)))))
(assert
 (let ((?x2880 (+ 0.0 eta_4)))
 (let ((?x11882 (- ?x2880 eta_0)))
 (let (($x11884 (> ?x11882 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_10 xp_4)) $x11884)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_0)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_1)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_2)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_3)) $x11983)))))
(assert
 (let ((?x827 (+ (- 1.0) eta_4)))
 (let ((?x11949 (- ?x827 eta_0)))
 (let (($x11951 (> ?x11949 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_11 xp_4)) $x11951)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x12725 (- ?x7998 eta_0)))
 (let (($x12727 (> ?x12725 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_0)) $x12727)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_1)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_2)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_3)) $x12015)))))
(assert
 (let ((?x852 (+ (- 2.0) eta_4)))
 (let ((?x11981 (- ?x852 eta_0)))
 (let (($x11983 (> ?x11981 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_12 xp_4)) $x11983)))))
(assert
 (let ((?x11177 (+ (- 7.0) eta_4)))
 (let ((?x13063 (- ?x11177 eta_0)))
 (let (($x13065 (> ?x13063 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_0)) $x13065)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x12725 (- ?x7998 eta_0)))
 (let (($x12727 (> ?x12725 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_1)) $x12727)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_2)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
 (let ((?x12045 (- ?x905 eta_0)))
 (let (($x12047 (> ?x12045 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_3)) $x12047)))))
(assert
 (let ((?x877 (+ (- 3.0) eta_4)))
 (let ((?x12013 (- ?x877 eta_0)))
 (let (($x12015 (> ?x12013 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_13 xp_4)) $x12015)))))
(assert
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_0)) (> (- (+ (- 8.0) eta_4) eta_0) 0.0)))
(assert
 (let ((?x11177 (+ (- 7.0) eta_4)))
 (let ((?x13063 (- ?x11177 eta_0)))
 (let (($x13065 (> ?x13063 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_1)) $x13065)))))
(assert
 (let ((?x7998 (+ (- 6.0) eta_4)))
 (let ((?x12725 (- ?x7998 eta_0)))
 (let (($x12727 (> ?x12725 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_2)) $x12727)))))
(assert
 (let ((?x4450 (+ (- 5.0) eta_4)))
 (let ((?x12384 (- ?x4450 eta_0)))
 (let (($x12386 (> ?x12384 0.0)))
 (=> (= (+ yp_0 xp_4) (+ yp_14 xp_3)) $x12386)))))
(assert
 (let ((?x905 (+ (- 4.0) eta_4)))
(let ((?x12045 (- ?x905 eta_0)))
(let (($x12047 (> ?x12045 0.0)))
(=> (= (+ yp_0 xp_4) (+ yp_14 xp_4)) $x12047)))))
(check-sat)
