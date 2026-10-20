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
 (< xp_0 xp_2))
(assert
 (let ((?x115 (+ yp_1 xp_0)))
 (let ((?x112 (+ yp_3 xp_0)))
 (and (distinct ?x112 ?x115) true))))
(assert
 (let ((?x116 (+ yp_2 xp_1)))
 (let ((?x112 (+ yp_3 xp_0)))
 (and (distinct ?x112 ?x116) true))))
(assert
 (let ((?x117 (+ yp_1 xp_1)))
 (let ((?x112 (+ yp_3 xp_0)))
 (and (distinct ?x112 ?x117) true))))
(assert
 (let ((?x118 (+ yp_2 xp_2)))
 (let ((?x112 (+ yp_3 xp_0)))
 (and (distinct ?x112 ?x118) true))))
(assert
 (let ((?x119 (+ yp_0 xp_0)))
 (let ((?x112 (+ yp_3 xp_0)))
 (and (distinct ?x112 ?x119) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x112 (+ yp_3 xp_0)))
 (and (distinct ?x112 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x112 (+ yp_3 xp_0)))
 (and (distinct ?x112 ?x121) true))))
(assert
 (let ((?x115 (+ yp_1 xp_0)))
 (let ((?x113 (+ yp_4 xp_1)))
 (and (distinct ?x113 ?x115) true))))
(assert
 (let ((?x116 (+ yp_2 xp_1)))
 (let ((?x113 (+ yp_4 xp_1)))
 (and (distinct ?x113 ?x116) true))))
(assert
 (let ((?x117 (+ yp_1 xp_1)))
 (let ((?x113 (+ yp_4 xp_1)))
 (and (distinct ?x113 ?x117) true))))
(assert
 (let ((?x118 (+ yp_2 xp_2)))
 (let ((?x113 (+ yp_4 xp_1)))
 (and (distinct ?x113 ?x118) true))))
(assert
 (let ((?x119 (+ yp_0 xp_0)))
 (let ((?x113 (+ yp_4 xp_1)))
 (and (distinct ?x113 ?x119) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x113 (+ yp_4 xp_1)))
 (and (distinct ?x113 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x113 (+ yp_4 xp_1)))
 (and (distinct ?x113 ?x121) true))))
(assert
 (let ((?x115 (+ yp_1 xp_0)))
 (let ((?x114 (+ yp_5 xp_2)))
 (and (distinct ?x114 ?x115) true))))
(assert
 (let ((?x116 (+ yp_2 xp_1)))
 (let ((?x114 (+ yp_5 xp_2)))
 (and (distinct ?x114 ?x116) true))))
(assert
 (let ((?x117 (+ yp_1 xp_1)))
 (let ((?x114 (+ yp_5 xp_2)))
 (and (distinct ?x114 ?x117) true))))
(assert
 (let ((?x118 (+ yp_2 xp_2)))
 (let ((?x114 (+ yp_5 xp_2)))
 (and (distinct ?x114 ?x118) true))))
(assert
 (let ((?x119 (+ yp_0 xp_0)))
 (let ((?x114 (+ yp_5 xp_2)))
 (and (distinct ?x114 ?x119) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x114 (+ yp_5 xp_2)))
 (and (distinct ?x114 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x114 (+ yp_5 xp_2)))
 (and (distinct ?x114 ?x121) true))))
(assert
 (let ((?x117 (+ yp_1 xp_1)))
 (let ((?x115 (+ yp_1 xp_0)))
 (and (distinct ?x115 ?x117) true))))
(assert
 (let ((?x118 (+ yp_2 xp_2)))
 (let ((?x115 (+ yp_1 xp_0)))
 (and (distinct ?x115 ?x118) true))))
(assert
 (let ((?x119 (+ yp_0 xp_0)))
 (let ((?x115 (+ yp_1 xp_0)))
 (and (distinct ?x115 ?x119) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x115 (+ yp_1 xp_0)))
 (and (distinct ?x115 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x115 (+ yp_1 xp_0)))
 (and (distinct ?x115 ?x121) true))))
(assert
 (let ((?x117 (+ yp_1 xp_1)))
 (let ((?x116 (+ yp_2 xp_1)))
 (and (distinct ?x116 ?x117) true))))
(assert
 (let ((?x118 (+ yp_2 xp_2)))
 (let ((?x116 (+ yp_2 xp_1)))
 (and (distinct ?x116 ?x118) true))))
(assert
 (let ((?x119 (+ yp_0 xp_0)))
 (let ((?x116 (+ yp_2 xp_1)))
 (and (distinct ?x116 ?x119) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x116 (+ yp_2 xp_1)))
 (and (distinct ?x116 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x116 (+ yp_2 xp_1)))
 (and (distinct ?x116 ?x121) true))))
(assert
 (let ((?x119 (+ yp_0 xp_0)))
 (let ((?x117 (+ yp_1 xp_1)))
 (and (distinct ?x117 ?x119) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x117 (+ yp_1 xp_1)))
 (and (distinct ?x117 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x117 (+ yp_1 xp_1)))
 (and (distinct ?x117 ?x121) true))))
(assert
 (let ((?x119 (+ yp_0 xp_0)))
 (let ((?x118 (+ yp_2 xp_2)))
 (and (distinct ?x118 ?x119) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x118 (+ yp_2 xp_2)))
 (and (distinct ?x118 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x118 (+ yp_2 xp_2)))
 (and (distinct ?x118 ?x121) true))))
(assert
 (let ((?x120 (+ yp_0 xp_1)))
 (let ((?x119 (+ yp_0 xp_0)))
 (and (distinct ?x119 ?x120) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x119 (+ yp_0 xp_0)))
 (and (distinct ?x119 ?x121) true))))
(assert
 (let ((?x121 (+ yp_0 xp_2)))
 (let ((?x120 (+ yp_0 xp_1)))
 (and (distinct ?x120 ?x121) true))))
(assert
 (or (and (= xp_0 0) (= xp_1 1) (= xp_2 2)) (and (= xp_0 0) (= xp_1 2) (= xp_2 1)) (and (= xp_0 1) (= xp_1 0) (= xp_2 2))))
(assert
 (let ((?x379 (+ 0.0 eta_0)))
 (let ((?x380 (- ?x379 eta_2)))
 (let (($x382 (> ?x380 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_0)) $x382)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x392 (- ?x391 eta_2)))
 (let (($x394 (> ?x392 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_1)) $x394)))))
(assert
 (let ((?x404 (+ 2.0 eta_0)))
 (let ((?x405 (- ?x404 eta_2)))
 (let (($x407 (> ?x405 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_0 xp_2)) $x407)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x418 (- ?x417 eta_2)))
 (let (($x420 (> ?x418 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_0)) $x420)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x427 (- ?x426 eta_2)))
 (let (($x429 (> ?x427 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_1)) $x429)))))
(assert
 (let ((?x438 (+ 2.0 eta_1)))
 (let ((?x439 (- ?x438 eta_2)))
 (let (($x442 (> ?x439 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_1 xp_2)) $x442)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x455 (- ?x454 eta_2)))
 (let (($x458 (> ?x455 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_0)) $x458)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x418 (- ?x417 eta_2)))
 (let (($x420 (> ?x418 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_1)) $x420)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x427 (- ?x426 eta_2)))
 (let (($x429 (> ?x427 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_2 xp_2)) $x429)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x477 (- ?x476 eta_2)))
 (let (($x480 (> ?x477 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_1)) $x480)))))
(assert
 (let ((?x485 (+ 2.0 eta_2)))
 (let ((?x486 (- ?x485 eta_2)))
 (let (($x489 (> ?x486 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_3 xp_2)) $x489)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x495 (- ?x494 eta_2)))
 (let (($x498 (> ?x495 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_0)) $x498)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x477 (- ?x476 eta_2)))
 (let (($x480 (> ?x477 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_4 xp_2)) $x480)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x511 (- ?x510 eta_2)))
 (let (($x513 (> ?x511 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_0)) $x513)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x495 (- ?x494 eta_2)))
 (let (($x498 (> ?x495 0.0)))
 (=> (= (+ yp_3 xp_0) (+ yp_5 xp_1)) $x498)))))
(assert
 (let ((?x379 (+ 0.0 eta_0)))
 (let ((?x380 (- ?x379 eta_2)))
 (let (($x382 (> ?x380 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_0)) $x382)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x392 (- ?x391 eta_2)))
 (let (($x394 (> ?x392 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_1)) $x394)))))
(assert
 (let ((?x404 (+ 2.0 eta_0)))
 (let ((?x405 (- ?x404 eta_2)))
 (let (($x407 (> ?x405 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_0 xp_2)) $x407)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x418 (- ?x417 eta_2)))
 (let (($x420 (> ?x418 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_0)) $x420)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x427 (- ?x426 eta_2)))
 (let (($x429 (> ?x427 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_1)) $x429)))))
(assert
 (let ((?x438 (+ 2.0 eta_1)))
 (let ((?x439 (- ?x438 eta_2)))
 (let (($x442 (> ?x439 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_1 xp_2)) $x442)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x455 (- ?x454 eta_2)))
 (let (($x458 (> ?x455 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_0)) $x458)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x418 (- ?x417 eta_2)))
 (let (($x420 (> ?x418 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_1)) $x420)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x427 (- ?x426 eta_2)))
 (let (($x429 (> ?x427 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_2 xp_2)) $x429)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x477 (- ?x476 eta_2)))
 (let (($x480 (> ?x477 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_1)) $x480)))))
(assert
 (let ((?x485 (+ 2.0 eta_2)))
 (let ((?x486 (- ?x485 eta_2)))
 (let (($x489 (> ?x486 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_3 xp_2)) $x489)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x495 (- ?x494 eta_2)))
 (let (($x498 (> ?x495 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_0)) $x498)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x477 (- ?x476 eta_2)))
 (let (($x480 (> ?x477 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_4 xp_2)) $x480)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x511 (- ?x510 eta_2)))
 (let (($x513 (> ?x511 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_0)) $x513)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x495 (- ?x494 eta_2)))
 (let (($x498 (> ?x495 0.0)))
 (=> (= (+ yp_4 xp_1) (+ yp_5 xp_1)) $x498)))))
(assert
 (let ((?x379 (+ 0.0 eta_0)))
 (let ((?x380 (- ?x379 eta_2)))
 (let (($x382 (> ?x380 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_0)) $x382)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x392 (- ?x391 eta_2)))
 (let (($x394 (> ?x392 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_1)) $x394)))))
(assert
 (let ((?x404 (+ 2.0 eta_0)))
 (let ((?x405 (- ?x404 eta_2)))
 (let (($x407 (> ?x405 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_0 xp_2)) $x407)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x418 (- ?x417 eta_2)))
 (let (($x420 (> ?x418 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_0)) $x420)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x427 (- ?x426 eta_2)))
 (let (($x429 (> ?x427 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_1)) $x429)))))
(assert
 (let ((?x438 (+ 2.0 eta_1)))
 (let ((?x439 (- ?x438 eta_2)))
 (let (($x442 (> ?x439 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_1 xp_2)) $x442)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x455 (- ?x454 eta_2)))
 (let (($x458 (> ?x455 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_0)) $x458)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x418 (- ?x417 eta_2)))
 (let (($x420 (> ?x418 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_1)) $x420)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x427 (- ?x426 eta_2)))
 (let (($x429 (> ?x427 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_2 xp_2)) $x429)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x477 (- ?x476 eta_2)))
 (let (($x480 (> ?x477 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_1)) $x480)))))
(assert
 (let ((?x485 (+ 2.0 eta_2)))
 (let ((?x486 (- ?x485 eta_2)))
 (let (($x489 (> ?x486 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_3 xp_2)) $x489)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x495 (- ?x494 eta_2)))
 (let (($x498 (> ?x495 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_0)) $x498)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x477 (- ?x476 eta_2)))
 (let (($x480 (> ?x477 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_4 xp_2)) $x480)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x511 (- ?x510 eta_2)))
 (let (($x513 (> ?x511 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_0)) $x513)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x495 (- ?x494 eta_2)))
 (let (($x498 (> ?x495 0.0)))
 (=> (= (+ yp_5 xp_2) (+ yp_5 xp_1)) $x498)))))
(assert
 (let ((?x379 (+ 0.0 eta_0)))
 (let ((?x634 (- ?x379 eta_1)))
 (let (($x636 (> ?x634 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_0)) $x636)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x643 (- ?x391 eta_1)))
 (let (($x645 (> ?x643 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_1)) $x645)))))
(assert
 (let ((?x404 (+ 2.0 eta_0)))
 (let ((?x654 (- ?x404 eta_1)))
 (let (($x656 (> ?x654 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_2)) $x656)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x665 (- ?x426 eta_1)))
 (let (($x667 (> ?x665 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_1)) $x667)))))
(assert
 (let ((?x438 (+ 2.0 eta_1)))
 (let ((?x670 (- ?x438 eta_1)))
 (let (($x672 (> ?x670 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_2)) $x672)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x675 (- ?x454 eta_1)))
 (let (($x677 (> ?x675 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_0)) $x677)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x665 (- ?x426 eta_1)))
 (let (($x667 (> ?x665 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_2)) $x667)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_0)) $x685)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x694 (- ?x476 eta_1)))
 (let (($x696 (> ?x694 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_1)) $x696)))))
(assert
 (let ((?x485 (+ 2.0 eta_2)))
 (let ((?x708 (- ?x485 eta_1)))
 (let (($x710 (> ?x708 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_3 xp_2)) $x710)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_0)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_1)) $x685)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x694 (- ?x476 eta_1)))
 (let (($x696 (> ?x694 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_4 xp_2)) $x696)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x742 (- ?x510 eta_1)))
 (let (($x744 (> ?x742 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_0)) $x744)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_1)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_5 xp_2)) $x685)))))
(assert
 (let ((?x379 (+ 0.0 eta_0)))
 (let ((?x634 (- ?x379 eta_1)))
 (let (($x636 (> ?x634 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_0)) $x636)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x643 (- ?x391 eta_1)))
 (let (($x645 (> ?x643 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_1)) $x645)))))
(assert
 (let ((?x404 (+ 2.0 eta_0)))
 (let ((?x654 (- ?x404 eta_1)))
 (let (($x656 (> ?x654 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_2)) $x656)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x665 (- ?x426 eta_1)))
 (let (($x667 (> ?x665 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_1)) $x667)))))
(assert
 (let ((?x438 (+ 2.0 eta_1)))
 (let ((?x670 (- ?x438 eta_1)))
 (let (($x672 (> ?x670 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_2)) $x672)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x675 (- ?x454 eta_1)))
 (let (($x677 (> ?x675 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_0)) $x677)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x665 (- ?x426 eta_1)))
 (let (($x667 (> ?x665 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_2)) $x667)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_0)) $x685)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x694 (- ?x476 eta_1)))
 (let (($x696 (> ?x694 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_1)) $x696)))))
(assert
 (let ((?x485 (+ 2.0 eta_2)))
 (let ((?x708 (- ?x485 eta_1)))
 (let (($x710 (> ?x708 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_3 xp_2)) $x710)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_0)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_1)) $x685)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x694 (- ?x476 eta_1)))
 (let (($x696 (> ?x694 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_4 xp_2)) $x696)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x742 (- ?x510 eta_1)))
 (let (($x744 (> ?x742 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_0)) $x744)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_1)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_5 xp_2)) $x685)))))
(assert
 (let ((?x818 (+ (- 1.0) eta_0)))
 (let ((?x819 (- ?x818 eta_1)))
 (let (($x821 (> ?x819 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_0)) $x821)))))
(assert
 (let ((?x379 (+ 0.0 eta_0)))
 (let ((?x634 (- ?x379 eta_1)))
 (let (($x636 (> ?x634 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_1)) $x636)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x643 (- ?x391 eta_1)))
 (let (($x645 (> ?x643 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_0 xp_2)) $x645)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x675 (- ?x454 eta_1)))
 (let (($x677 (> ?x675 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_0)) $x677)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x665 (- ?x426 eta_1)))
 (let (($x667 (> ?x665 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_1 xp_2)) $x667)))))
(assert
 (let ((?x839 (+ (- 2.0) eta_1)))
 (let ((?x840 (- ?x839 eta_1)))
 (let (($x842 (> ?x840 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_0)) $x842)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x675 (- ?x454 eta_1)))
 (let (($x677 (> ?x675 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_2 xp_1)) $x677)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_0)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_1)) $x685)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x694 (- ?x476 eta_1)))
 (let (($x696 (> ?x694 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_3 xp_2)) $x696)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x742 (- ?x510 eta_1)))
 (let (($x744 (> ?x742 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_0)) $x744)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_1)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_4 xp_2)) $x685)))))
(assert
 (let ((?x876 (+ (- 3.0) eta_2)))
 (let ((?x877 (- ?x876 eta_1)))
 (let (($x879 (> ?x877 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_0)) $x879)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x742 (- ?x510 eta_1)))
 (let (($x744 (> ?x742 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_1)) $x744)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_1 xp_1) (+ yp_5 xp_2)) $x724)))))
(assert
 (let ((?x818 (+ (- 1.0) eta_0)))
 (let ((?x819 (- ?x818 eta_1)))
 (let (($x821 (> ?x819 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_0)) $x821)))))
(assert
 (let ((?x379 (+ 0.0 eta_0)))
 (let ((?x634 (- ?x379 eta_1)))
 (let (($x636 (> ?x634 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_1)) $x636)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x643 (- ?x391 eta_1)))
 (let (($x645 (> ?x643 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_0 xp_2)) $x645)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x675 (- ?x454 eta_1)))
 (let (($x677 (> ?x675 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_0)) $x677)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x665 (- ?x426 eta_1)))
 (let (($x667 (> ?x665 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_1 xp_2)) $x667)))))
(assert
 (let ((?x839 (+ (- 2.0) eta_1)))
 (let ((?x840 (- ?x839 eta_1)))
 (let (($x842 (> ?x840 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_0)) $x842)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x675 (- ?x454 eta_1)))
 (let (($x677 (> ?x675 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_2 xp_1)) $x677)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_0)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_1)) $x685)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x694 (- ?x476 eta_1)))
 (let (($x696 (> ?x694 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_3 xp_2)) $x696)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x742 (- ?x510 eta_1)))
 (let (($x744 (> ?x742 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_0)) $x744)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_1)) $x724)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x683 (- ?x682 eta_1)))
 (let (($x685 (> ?x683 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_4 xp_2)) $x685)))))
(assert
 (let ((?x876 (+ (- 3.0) eta_2)))
 (let ((?x877 (- ?x876 eta_1)))
 (let (($x879 (> ?x877 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_0)) $x879)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x742 (- ?x510 eta_1)))
 (let (($x744 (> ?x742 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_1)) $x744)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x722 (- ?x494 eta_1)))
 (let (($x724 (> ?x722 0.0)))
 (=> (= (+ yp_2 xp_2) (+ yp_5 xp_2)) $x724)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x949 (- ?x391 eta_0)))
 (let (($x951 (> ?x949 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_1)) $x951)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_2)) (> (- (+ 2.0 eta_0) eta_0) 0.0)))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x960 (- ?x417 eta_0)))
 (let (($x962 (> ?x960 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_0)) $x962)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x971 (- ?x426 eta_0)))
 (let (($x973 (> ?x971 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_1)) $x973)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_2)) (> (- (+ 2.0 eta_1) eta_0) 0.0)))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x996 (- ?x454 eta_0)))
 (let (($x998 (> ?x996 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_0)) $x998)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x960 (- ?x417 eta_0)))
 (let (($x962 (> ?x960 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_1)) $x962)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x971 (- ?x426 eta_0)))
 (let (($x973 (> ?x971 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_2)) $x973)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x1013 (- ?x682 eta_0)))
 (let (($x1015 (> ?x1013 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_0)) $x1015)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x1024 (- ?x476 eta_0)))
 (let (($x1026 (> ?x1024 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_1)) $x1026)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_3 xp_2)) (> (- (+ 2.0 eta_2) eta_0) 0.0)))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x1052 (- ?x494 eta_0)))
 (let (($x1054 (> ?x1052 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_0)) $x1054)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x1013 (- ?x682 eta_0)))
 (let (($x1015 (> ?x1013 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_1)) $x1015)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x1024 (- ?x476 eta_0)))
 (let (($x1026 (> ?x1024 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_4 xp_2)) $x1026)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x1072 (- ?x510 eta_0)))
 (let (($x1074 (> ?x1072 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_0)) $x1074)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x1052 (- ?x494 eta_0)))
 (let (($x1054 (> ?x1052 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_1)) $x1054)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x1013 (- ?x682 eta_0)))
 (let (($x1015 (> ?x1013 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_5 xp_2)) $x1015)))))
(assert
 (let ((?x818 (+ (- 1.0) eta_0)))
 (let ((?x1092 (- ?x818 eta_0)))
 (let (($x1094 (> ?x1092 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_0)) $x1094)))))
(assert
 (let ((?x391 (+ 1.0 eta_0)))
 (let ((?x949 (- ?x391 eta_0)))
 (let (($x951 (> ?x949 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_2)) $x951)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x996 (- ?x454 eta_0)))
 (let (($x998 (> ?x996 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_0)) $x998)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x960 (- ?x417 eta_0)))
 (let (($x962 (> ?x960 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_1)) $x962)))))
(assert
 (let ((?x426 (+ 1.0 eta_1)))
 (let ((?x971 (- ?x426 eta_0)))
 (let (($x973 (> ?x971 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_2)) $x973)))))
(assert
 (let ((?x839 (+ (- 2.0) eta_1)))
 (let ((?x1110 (- ?x839 eta_0)))
 (let (($x1112 (> ?x1110 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_0)) $x1112)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x996 (- ?x454 eta_0)))
 (let (($x998 (> ?x996 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_1)) $x998)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x960 (- ?x417 eta_0)))
 (let (($x962 (> ?x960 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_2)) $x962)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x1052 (- ?x494 eta_0)))
 (let (($x1054 (> ?x1052 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_0)) $x1054)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x1013 (- ?x682 eta_0)))
 (let (($x1015 (> ?x1013 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_1)) $x1015)))))
(assert
 (let ((?x476 (+ 1.0 eta_2)))
 (let ((?x1024 (- ?x476 eta_0)))
 (let (($x1026 (> ?x1024 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_3 xp_2)) $x1026)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x1072 (- ?x510 eta_0)))
 (let (($x1074 (> ?x1072 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_0)) $x1074)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x1052 (- ?x494 eta_0)))
 (let (($x1054 (> ?x1052 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_1)) $x1054)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x1013 (- ?x682 eta_0)))
 (let (($x1015 (> ?x1013 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_4 xp_2)) $x1015)))))
(assert
 (let ((?x876 (+ (- 3.0) eta_2)))
 (let ((?x1154 (- ?x876 eta_0)))
 (let (($x1156 (> ?x1154 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_0)) $x1156)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x1072 (- ?x510 eta_0)))
 (let (($x1074 (> ?x1072 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_1)) $x1074)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x1052 (- ?x494 eta_0)))
 (let (($x1054 (> ?x1052 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_5 xp_2)) $x1054)))))
(assert
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_0)) (> (- (+ (- 2.0) eta_0) eta_0) 0.0)))
(assert
 (let ((?x818 (+ (- 1.0) eta_0)))
 (let ((?x1092 (- ?x818 eta_0)))
 (let (($x1094 (> ?x1092 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_0 xp_1)) $x1094)))))
(assert
 (let ((?x839 (+ (- 2.0) eta_1)))
 (let ((?x1110 (- ?x839 eta_0)))
 (let (($x1112 (> ?x1110 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_0)) $x1112)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x996 (- ?x454 eta_0)))
 (let (($x998 (> ?x996 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_1)) $x998)))))
(assert
 (let ((?x417 (+ 0.0 eta_1)))
 (let ((?x960 (- ?x417 eta_0)))
 (let (($x962 (> ?x960 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_1 xp_2)) $x962)))))
(assert
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_0)) (> (- (+ (- 3.0) eta_1) eta_0) 0.0)))
(assert
 (let ((?x839 (+ (- 2.0) eta_1)))
 (let ((?x1110 (- ?x839 eta_0)))
 (let (($x1112 (> ?x1110 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_1)) $x1112)))))
(assert
 (let ((?x454 (+ (- 1.0) eta_1)))
 (let ((?x996 (- ?x454 eta_0)))
 (let (($x998 (> ?x996 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_2 xp_2)) $x998)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x1072 (- ?x510 eta_0)))
 (let (($x1074 (> ?x1072 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_0)) $x1074)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x1052 (- ?x494 eta_0)))
 (let (($x1054 (> ?x1052 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_1)) $x1054)))))
(assert
 (let ((?x682 (+ 0.0 eta_2)))
 (let ((?x1013 (- ?x682 eta_0)))
 (let (($x1015 (> ?x1013 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_3 xp_2)) $x1015)))))
(assert
 (let ((?x876 (+ (- 3.0) eta_2)))
 (let ((?x1154 (- ?x876 eta_0)))
 (let (($x1156 (> ?x1154 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_0)) $x1156)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
 (let ((?x1072 (- ?x510 eta_0)))
 (let (($x1074 (> ?x1072 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_1)) $x1074)))))
(assert
 (let ((?x494 (+ (- 1.0) eta_2)))
 (let ((?x1052 (- ?x494 eta_0)))
 (let (($x1054 (> ?x1052 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_4 xp_2)) $x1054)))))
(assert
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_0)) (> (- (+ (- 4.0) eta_2) eta_0) 0.0)))
(assert
 (let ((?x876 (+ (- 3.0) eta_2)))
 (let ((?x1154 (- ?x876 eta_0)))
 (let (($x1156 (> ?x1154 0.0)))
 (=> (= (+ yp_0 xp_2) (+ yp_5 xp_1)) $x1156)))))
(assert
 (let ((?x510 (+ (- 2.0) eta_2)))
(let ((?x1072 (- ?x510 eta_0)))
(let (($x1074 (> ?x1072 0.0)))
(=> (= (+ yp_0 xp_2) (+ yp_5 xp_2)) $x1074)))))
(check-sat)
