import Mathlib

namespace ScalarProfile

def increment (f : ℕ → ℚ) (n : ℕ) : ℚ := f (n + 1) - f n

def DiscreteConcave (f : ℕ → ℚ) : Prop :=
  ∀ n, 1 ≤ n → increment f (n + 1) ≤ increment f n

def TriplingAt (f : ℕ → ℚ) (a b : ℕ) : Prop :=
  3 * f b ≤ f (3 * b + a - 1)

theorem increment_le_base {f : ℕ → ℚ} {a n : ℕ}
    (hconcave : DiscreteConcave f) (ha : 1 ≤ a) :
    increment f (a + n) ≤ increment f a := by
  induction n with
  | zero => simp
  | succ n ih =>
      have hstep := hconcave (a + n) (by omega)
      exact le_trans (by simpa [increment, Nat.add_assoc] using hstep) ih

theorem concave_growth_upper {f : ℕ → ℚ} {a n : ℕ}
    (hconcave : DiscreteConcave f) (ha : 1 ≤ a) :
    f (a + n) - f a ≤ (n : ℚ) * increment f a := by
  induction n with
  | zero => simp
  | succ n ih =>
      have hstep := increment_le_base hconcave ha (n := n)
      have hidentity :
          f (a + (n + 1)) - f a =
            increment f (a + n) + (f (a + n) - f a) := by
        simp only [increment]
        rw [← Nat.add_assoc a n 1]
        ring
      rw [hidentity, Nat.cast_succ]
      nlinarith

theorem finite_tripling_slope_bound {f : ℕ → ℚ} {a b : ℕ}
    (hconcave : DiscreteConcave f) (ha : 1 ≤ a) (hb : 1 ≤ b)
    (htripling : TriplingAt f a b) :
    2 * f b ≤ ((2 * b + a - 1 : ℕ) : ℚ) * increment f b := by
  let steps : ℕ := 2 * b + a - 1
  have hindex : b + steps = 3 * b + a - 1 := by
    dsimp [steps]
    omega
  have hupper := concave_growth_upper hconcave hb (a := b) (n := steps)
  have htripling' : 3 * f b ≤ f (b + steps) := by
    simpa [TriplingAt, hindex] using htripling
  have hsteps : (steps : ℚ) = ((2 * b + a - 1 : ℕ) : ℚ) := by
    simp [steps]
  rw [hsteps] at hupper
  nlinarith

end ScalarProfile
