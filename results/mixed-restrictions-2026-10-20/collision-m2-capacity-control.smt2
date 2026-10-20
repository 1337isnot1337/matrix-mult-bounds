; benchmark generated from python API
(set-info :status unknown)
(declare-fun xp_0 () Int)
(declare-fun xp_1 () Int)
(declare-fun yp_0 () Int)
(declare-fun yp_1 () Int)
(declare-fun yp_2 () Int)
(declare-fun eta_0 () Real)
(declare-fun eta_1 () Real)
(assert
 (let (($x13 (>= xp_0 0)))
 (and $x13 (< xp_0 2))))
(assert
 (let (($x17 (>= xp_1 0)))
 (and $x17 (< xp_1 2))))
(assert
 (and (distinct xp_0 xp_1) true))
(assert
 (let (($x48 (>= yp_0 0)))
 (and $x48 (< yp_0 3))))
(assert
 (let (($x52 (>= yp_1 0)))
 (and $x52 (< yp_1 3))))
(assert
 (let (($x55 (>= yp_2 0)))
 (and $x55 (< yp_2 3))))
(assert
 (and (distinct yp_0 yp_1 yp_2) true))
(assert
 (= eta_0 0.0))
(assert
 (< xp_0 xp_1))
(assert
 (let ((?x83 (+ yp_0 xp_0)))
 (let ((?x81 (+ yp_1 xp_0)))
 (and (distinct ?x81 ?x83) true))))
(assert
 (let ((?x84 (+ yp_0 xp_1)))
 (let ((?x81 (+ yp_1 xp_0)))
 (and (distinct ?x81 ?x84) true))))
(assert
 (let ((?x83 (+ yp_0 xp_0)))
 (let ((?x82 (+ yp_2 xp_1)))
 (and (distinct ?x82 ?x83) true))))
(assert
 (let ((?x84 (+ yp_0 xp_1)))
 (let ((?x82 (+ yp_2 xp_1)))
 (and (distinct ?x82 ?x84) true))))
(assert
 (let ((?x84 (+ yp_0 xp_1)))
 (let ((?x83 (+ yp_0 xp_0)))
 (and (distinct ?x83 ?x84) true))))
(assert
 (or (and (= xp_0 0) (= xp_1 1))))
(assert
 (let ((?x127 (- (+ 0.0 eta_0) eta_1)))
 (let (($x129 (> ?x127 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_0)) $x129))))
(assert
 (let ((?x138 (+ 1.0 eta_0)))
 (let ((?x139 (- ?x138 eta_1)))
 (let (($x141 (> ?x139 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_1)) $x141)))))
(assert
 (let ((?x150 (+ 1.0 eta_1)))
 (let ((?x151 (- ?x150 eta_1)))
 (let (($x154 (> ?x151 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_1)) $x154)))))
(assert
 (let ((?x159 (+ (- 1.0) eta_1)))
 (let ((?x160 (- ?x159 eta_1)))
 (let (($x163 (> ?x160 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_0)) $x163)))))
(assert
 (let ((?x127 (- (+ 0.0 eta_0) eta_1)))
 (let (($x129 (> ?x127 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_0)) $x129))))
(assert
 (let ((?x138 (+ 1.0 eta_0)))
 (let ((?x139 (- ?x138 eta_1)))
 (let (($x141 (> ?x139 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_1)) $x141)))))
(assert
 (let ((?x150 (+ 1.0 eta_1)))
 (let ((?x151 (- ?x150 eta_1)))
 (let (($x154 (> ?x151 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_1)) $x154)))))
(assert
 (let ((?x159 (+ (- 1.0) eta_1)))
 (let ((?x160 (- ?x159 eta_1)))
 (let (($x163 (> ?x160 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_0)) $x163)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_1)) (> (- (+ 1.0 eta_0) eta_0) 0.0)))
(assert
 (let ((?x190 (- (+ 0.0 eta_1) eta_0)))
 (let (($x192 (> ?x190 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_0)) $x192))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_1)) (> (- (+ 1.0 eta_1) eta_0) 0.0)))
(assert
 (let ((?x159 (+ (- 1.0) eta_1)))
 (let ((?x215 (- ?x159 eta_0)))
 (let (($x217 (> ?x215 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_0)) $x217)))))
(assert
 (let ((?x190 (- (+ 0.0 eta_1) eta_0)))
 (let (($x192 (> ?x190 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_1)) $x192))))
(assert
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_0)) (> (- (+ (- 1.0) eta_0) eta_0) 0.0)))
(assert
 (let ((?x159 (+ (- 1.0) eta_1)))
 (let ((?x215 (- ?x159 eta_0)))
 (let (($x217 (> ?x215 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_0)) $x217)))))
(assert
 (let ((?x190 (- (+ 0.0 eta_1) eta_0)))
 (let (($x192 (> ?x190 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_1)) $x192))))
(assert
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_0)) (> (- (+ (- 2.0) eta_1) eta_0) 0.0)))
(assert
 (let ((?x159 (+ (- 1.0) eta_1)))
(let ((?x215 (- ?x159 eta_0)))
(let (($x217 (> ?x215 0.0)))
(=> (= (+ yp_0 xp_1) (+ yp_2 xp_1)) $x217)))))
(check-sat)
