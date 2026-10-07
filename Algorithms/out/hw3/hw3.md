
# Everything hw2 part 3 is here or you can go to its markdown

## Student Information

- **Name:** Brycen Anderson
- **Student ID:** 111017061
- **Class:** CSCI 3412-001 — Algorithms
- **Homework #:** HW2
- **Due Date:** September 28, 2026

---

## Problem Solving

### part 1 problem Array of matching pairs [5 points]

In a very large library, each book has a unique cover. Due to a recent
renovation, all the books and their covers have been separated and piled
up without any sorting. Your task is to devise an efficient algorithm that
matches each book to its corresponding cover. One critical restriction is that
you cannot directly compare two books or two covers. In other words, they can't
be sorted. Comparisons can only be made between a book and its cover to
determine whether they match or which is larger,based on predefined criteria.

#### Answer 1.1)

My first thought is to brute force it first that's easy take one book.
compare against all covers remove a cover and book when found just go to
the next book and do the same. But that is O(n^2) time so lets not.

##### My second thought

###### array of books

[["Red Rising","Golden Son","Morning Star","Iron Gold"
,"Dark Age","Light Bringer","Red god"]]

###### Array of covers

[["Red god","Iron Gold","Light Bringer","Morning Star",
"Golden Son","Dark Age","Red Rising"]]

1. Pick a random book. Compare it with every cover, finding its matching cover
and separating the remaining covers into smaller and larger groups

2. Use that matching cover to separate the remaining books into smaller and
larger groups also.

3. Repeat within the corresponding smaller groups and larger groups until every
pair is matched.

### 1.2

1) Yes. A comparison-based sort determines order by comparing elements.
Heapsort compares parent and child values to build and maintain the heap.

2) No. A stable sort preserves the original order 1a,1b,1c but heapsort
will give something like 1b,1c,1a not stable.

3) min heap [1a,1b]. swapping the root with the last element produces [1b,1a],
reversing the equal elements of the original array. but still it is sorted

4) No. Heapsort runs in O(n log n) regardless of the initial input
but the number of comparisons and swaps may vary.

5) Heapsort is useful when sorting a large array with limited extra memory and guarantees
O(n log n) worst-case time. It uses O(1) extra space, unlike mergesort and
avoids quicksort's O(n^2) worst case.

### part 2 Time Efficiency Exercise [10 points]

a = 4
b = 2
d = 1

T(n) = 4T(n/2) + n
T(n) = 4(4T(n/4) + n/2) + n
T(n) = 16T(n/4) + 3n
T(n) = 16(4T(n/8) + n/4) + 3n
T(n) = 64T(n/8) + 7n

T(n) = 4^k * T(n/2^k) + (2^k - 1)n
k = log n
2^k = n
4^k = n^2

T(n) = n^2T(1) + (n-1)n
since T(1) is constant,T(n) = O(n^2)

#### 2.2

A)

```python
def example1 (n):
    count = 0
    for i in range(n):
        j = 1
        while j < n:
            count += 1
            j *= 2  
    return count
```

T(n) = n log n
The outer loop runs n times. The inner loop runs log2 n times because j doubles
every iteration.

B)

```python
def example2 (n):
    count = 0
    for i in range(n):                    
        for j in range(n):                
            for k in range(min(2, i+1)):  
                for l in range(min(3, j+1)):  
                    count += 1                    
    return count
```

T(n) = n * n * 2 * 3
T(n) = O(n^2)
The 1st outer most loops n times 2nd loop also loops n times but the inner loops
will at most loop 2 * 3 = 6 times per pair of outer loop iterations.

#### 2.3

1) log2 n = O(log n) grows slower than any positive power of n

2) sqroot(2n) = O(n^1/2) you can so sqroot(n) like n^1/2 which is better then
most but not log n

3) 3n^2 + 5n + 10 = O(n^2) is dominated by n^2 giving O(n^2)

4) n^3 = O(n^3) this will grows very fast for all n multiply n by itself 3 times

5) 2^n = O(2^n) grows very fast 2*2 for every n added

6) n^n = O(n^n) this 1^1 but then 2^2 then 3^3 this will shoot to the sky in
operations.

### part 3

#### A 

so insertion sort is O(k^2) operations if merging is O(n/k) then if you 
do insertion sort when you get to k elements instead of splitting all the way down 
this will be k^2 * n/k 
T(n) = O(nk)

#### B 

mergesort is O(n lg(n/k)) because you have n elements you split those n elements k 
times till subset of n is 1 then you build going back up with recursion. but it must 
look at every element to compare them so the total is O(n) * O(lg(n/k)) = O(n lg(n/k))

#### C

what is the largest k so that insertion sort makes the mergesort algorithm faster before it 
gets to a point where insertion sort slows the program. 


