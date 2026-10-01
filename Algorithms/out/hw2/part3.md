
# Loop Invariant Proof - Dutch National Flag Algorithms

## Student Information

- **Name:** Brycen Anderson
- **Student ID:** 111017061
- **Class:** CSCI 3412-001 — Algorithms
- **Homework #:** HW2
- **Due Date:** September 28, 2026

---

### What is loop invariant proof

A loop invariant proof state that for every nth loop the loop will stay true and
will produce the correct result at the end. So starts, true stays true, ends true.

### Iterations

Before low is 0
Low through mid - 1 is 1
From mid - high is not checked
after high is 2

### Initially

Low = 0
Mid = 0
High = len(nums) - 1
nothing has been checked so the array is sorted/unchecked.

### 3 cases

#### case 1

If nums at position mid equals 0 swap nums at position low and nums at position
high.Increment low and mid.

#### case 2

If nums at position mid equals 1 Increment mid

#### case 3

If nums at position mid equals 2 swap nums at position high and nums at position
mid decrement high.

### Termination

(int pointers in neetcode/leetcode all the time so i think its ok)
If the pointer mid is past high pointer then terminate the loop.
