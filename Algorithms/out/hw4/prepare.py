def prepare(file_Name:str, k=100): # k is the number of inner arrays
    if k < 1:
        raise ValueError("k must be at least 1")

    with open(file_Name,"r") as file:
        #make array of arrays 
        array_of_arrays = []
        # make array with all elements
        nums = file.read().split()

    #so nums is now my array with all the elements
    size, extra = divmod(len(nums), k)
    start = 0
    for i in range(k):
        end = start + size + (i < extra)
        array_of_arrays.append([int(num) for num in nums[start:end]])
        start = end

    return array_of_arrays

# pytest prepare.py 
def test_prepare():
    test_size()
    test_Pre_Array_size()
    test_prepare_fixtmp()

def test_prepare_fixtmp():
    arr = prepare("rand1000000.txt")

    assert len(arr) == 100, "Should have 100 sublists"
    assert all(len(sub) == 10_000 for sub in arr), "All sublists should have 10,000 elements"
    assert arr[0] is not arr[1], "Sublists should be separate objects"

#all of my files will have a main for testing that file 
def test_size():
    arr = prepare("rand1000000.txt")
    assert len(arr) == 100, "should be the 100 sublist"

#test should be in separate file 
def test_Pre_Array_size():
    arr = prepare("rand1000000.txt")
    for i in range(len(arr)):
        assert len(arr[i]) == 10_000,"should have 10,000 elements per sublist"

if __name__ == "__main__":
    test_prepare()
