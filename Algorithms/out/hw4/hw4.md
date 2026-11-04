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

```python
    # returns array of arrays or you can say matrix or 2d array
    def prepare(file_Name:str):
        
        with open(file_Name,"r") as file:
            #make array of arrays 
            array_of_arrays = []
            # make array with all elements
            nums = file.read().split()

        #so nums is now my array with all the elements
        tmp = []
        for num in nums:
            if len(tmp) == 10_000:
                array_of_arrays.append(tmp)
                tmp.clear()
            tmp.append(num)
        return array_of_arrays

# pytest prepare.py 
    def test_prepare():
        test_size()
        test_Pre_Array_size()

#all of my files will have a main for testing that file 
    def test_size():
        arr = prepare("rand1000000.txt")
        assert len(arr) == 100 - 1, "should be the 100 sublist"

#test should be in separate file 
    def test_Pre_Array_size():
        arr = prepare("rand1000000.txt")
        for i in range(len(arr)):
            assert len(arr[i]) == 10_000,"should have 10,000 elements per sublist"

    if __name__ == "__main__":
        test_prepare()
```

#### output prepare

```kitty
[bryruto@Brycen-archlinux hw4]$ pytest prepare.py
====================== test session starts ===================================
platform linux -- Python 3.14.8, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/bryruto/CuDenver/Algorithms/out/hw4
plugins: platformdirs-4.13.5, anyio-4.15.1, mock-3.16.0
collected 3 item

prepare.py ...                                                         [100%]

==================== 3 passed in 0.28s =======================================
```

#### explain prepare

So for this i used 'with open' so that i can open the file and it will
automatically close for me when i leave the scope.I knew that .read() would
read the whole file and .split() will split with a delimiter ' ' by default
which will then make everything a huge array after that i make them into
array of array by counting up till 10_000 then appending to my array_of_arrays
then to make sure it would work and to force myself to write test
i used pytest to test my function making sure all lengths were right.

### Part 2 100 sub-list

#### Radix Sort

```python

#return nothing pass by ref 
def RadixSort(arr:list):
    #check to see if the array is empty if so return empty
    if not arr:
        return []

    # while not sorted only running 1 array at a time
    count=0
    while not is_it_sorted(arr):

        #make array of 0's
        counts = [0 for _ in range(10)]

        #loop through nums 
        for num in arr:  
            #find the index of where you want those arrays
            index = (num//(10**count)) % 10
            counts[index]+=1

        #then we want to add them up
        sum = 0
        for i in range(len(counts)):
            if counts[i] == 0:
                continue

            sum += counts[i]
            counts[i] = sum
        
        new_arr = arr.copy()

        #now we want to store all elements in order 
        for i in range(len(arr) -1,-1,-1):
            index = arr[i]
            
            #this is repeated work how do i make this better
            index = (arr[i]//(10**count)) % 10
            
            new_arr[counts[index]-1] = arr[i]
            counts[index]-=1
        
        arr[:] = new_arr #update to the new array
        count+=1

    return arr


#this just will look to see if we need to swap any values if we do not sorted yet
def is_it_sorted(arr:list)->bool:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


#these are the test 
def test_RadixSort():
    test_empty()
    test_sorts_right()

#test for if the array is empty
def test_empty():
    assert RadixSort([]) == [],"the array is empty"

#test for if sorting is working 
def test_sorts_right():
    assert RadixSort([170, 45, 75, 90, 802, 24, 2, 66]) == [2,24,45,66,75,90,170,802]


if __name__ == "__main__":
    test_RadixSort()
```

##### Explain

My radix sort first checks if the array is sorted, then uses counting sort to
organize each digit until the array is sorted. I use cumulative counts to find
the correct positions and loop backward to keep the sorting stable. The time
complexity is O(dn) because each digit requires O(n) work, where d is the
number of digits. The space complexity is O(n) because I create a copy of the
original array, while my counting array only uses O(1) space.

#### Bucket Sort

For my bucket sort, I first check if the array is empty , then use
a hash map to count how many times each number appears. I find the smallest and
largest values to determine the range I need to iterate through, then append
each number based on its count. The time complexity is O(n + r), where n is the
number of elements and r is the range between the smallest and largest values.
The space complexity is O(n) because I store the counts in a hash map and create
a new sorted array

#### Merges

##### Slow Merge - O(nk)

For the slower merge, I took two sorted lists and merged them together,
then kept merging the result with the next list until only one was left.
This takes O(nk) time because the same numbers can be processed multiple times.

##### Fast Merge - O(n log k)

For the faster Merge, I used recursion to split the lists into two groups until
only one list was left in each group.  Then I merged them back together using my
slower merge function. This takes O(n log k) time because I'm merging the lists
in smaller groups instead of continuously growing one big list.

##### Comparison

As k increases, the slower merge takes more time because it has to keep going
through the growing list.The faster merge handles this better because it divides
the work into halves, meaning it doesn't have to go through the same numbers as
many times.

##### Speedup

Speedup: I calculated the speedup by dividing the slower merge's time by the
faster merge's time

#### Time Efficiency Function

I implemented a function that records the starting time in nanoseconds, executes
a given function, and subtracts the starting time from the ending time.
The elapsed time is converted into the appropriate unit for readability.
