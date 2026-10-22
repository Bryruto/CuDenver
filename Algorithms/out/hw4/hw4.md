# Student Information

- **Name:** Brycen Anderson
- **Student ID:** 111017061
- **Class:** CSCI 3412-001 — Algorithms
- **Homework #:** HW3
- **Due Date:** 10/11/2026

---

## Part A

### Part 1 Pseudocode

NOTE- This is 2 function's split and merge of merge sort

1) Take array of array's
2) split array of array's in half till you hit only 1 array
    2a) find middle store that in variable middle
    2b) split array of array's to left and right array of array's
    2c) store those in variables left and right array
    NOTE - middle is the end of right and start for left
    2d) call split for both right and left array of arrays
3) loop till left and right are empty
    3a) compare left[l] and right[r]
    3b) add what ever value is smaller to result array
    3c) add 1 to l or r
4) loop left array if any
    4a) add to result array
    4b) add 1 to l
5) loop right array if any
    5a) add to result array
    5b) add 1 to r
6) return result

### Part 2 Explain

So for this problem my idea is to merge sort the array's not the element's
I will run this till it hits the base case then combine the 2 array's
elements into 1 array.The time complexity of split part of merge sort
is O(log k) where k is the number of arrays in the array,then at the merge
part we will look at every element in the 2 array's giving T(2n) but that ok
because we don't care about constants and get O(n).Then combine
the split and merge part to get O(n log k) total time complexity.

## Part B

### Part 1 Prepare


