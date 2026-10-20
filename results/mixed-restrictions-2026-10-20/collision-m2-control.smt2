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
 (let ((?x75 (- (+ 0.0 eta_0) eta_1)))
 (let (($x78 (> ?x75 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_0)) $x78))))
(assert
 (let ((?x93 (+ 1.0 eta_0)))
 (let ((?x94 (- ?x93 eta_1)))
 (let (($x97 (> ?x94 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_0 xp_1)) $x97)))))
(assert
 (let ((?x111 (+ 1.0 eta_1)))
 (let ((?x112 (- ?x111 eta_1)))
 (let (($x115 (> ?x112 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_1 xp_1)) $x115)))))
(assert
 (let ((?x118 (+ (- 1.0) eta_1)))
 (let ((?x119 (- ?x118 eta_1)))
 (let (($x124 (> ?x119 0.0)))
 (=> (= (+ yp_1 xp_0) (+ yp_2 xp_0)) $x124)))))
(assert
 (let ((?x75 (- (+ 0.0 eta_0) eta_1)))
 (let (($x78 (> ?x75 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_0)) $x78))))
(assert
 (let ((?x93 (+ 1.0 eta_0)))
 (let ((?x94 (- ?x93 eta_1)))
 (let (($x97 (> ?x94 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_0 xp_1)) $x97)))))
(assert
 (let ((?x111 (+ 1.0 eta_1)))
 (let ((?x112 (- ?x111 eta_1)))
 (let (($x115 (> ?x112 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_1 xp_1)) $x115)))))
(assert
 (let ((?x118 (+ (- 1.0) eta_1)))
 (let ((?x119 (- ?x118 eta_1)))
 (let (($x124 (> ?x119 0.0)))
 (=> (= (+ yp_2 xp_1) (+ yp_2 xp_0)) $x124)))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_0 xp_1)) (> (- (+ 1.0 eta_0) eta_0) 0.0)))
(assert
 (let ((?x165 (- (+ 0.0 eta_1) eta_0)))
 (let (($x167 (> ?x165 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_0)) $x167))))
(assert
 (=> (= (+ yp_0 xp_0) (+ yp_1 xp_1)) (> (- (+ 1.0 eta_1) eta_0) 0.0)))
(assert
 (let ((?x118 (+ (- 1.0) eta_1)))
 (let ((?x190 (- ?x118 eta_0)))
 (let (($x192 (> ?x190 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_0)) $x192)))))
(assert
 (let ((?x165 (- (+ 0.0 eta_1) eta_0)))
 (let (($x167 (> ?x165 0.0)))
 (=> (= (+ yp_0 xp_0) (+ yp_2 xp_1)) $x167))))
(assert
 (=> (= (+ yp_0 xp_1) (+ yp_0 xp_0)) (> (- (+ (- 1.0) eta_0) eta_0) 0.0)))
(assert
 (let ((?x118 (+ (- 1.0) eta_1)))
 (let ((?x190 (- ?x118 eta_0)))
 (let (($x192 (> ?x190 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_0)) $x192)))))
(assert
 (let ((?x165 (- (+ 0.0 eta_1) eta_0)))
 (let (($x167 (> ?x165 0.0)))
 (=> (= (+ yp_0 xp_1) (+ yp_1 xp_1)) $x167))))
(assert
 (=> (= (+ yp_0 xp_1) (+ yp_2 xp_0)) (> (- (+ (- 2.0) eta_1) eta_0) 0.0)))
(assert
 (let ((?x118 (+ (- 1.0) eta_1)))
(let ((?x190 (- ?x118 eta_0)))
(let (($x192 (> ?x190 0.0)))
(=> (= (+ yp_0 xp_1) (+ yp_2 xp_1)) $x192)))))
(check-sat)
