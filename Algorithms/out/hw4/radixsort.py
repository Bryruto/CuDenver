#return nothing pass by ref 
def RadixSort(arr:list):
    
    #check to see if the array is empty if so return empty
    if arr.empty():
        return []
    
    # while countingSort returns true 
    digit = 10
    while countingSort(arr):
    return 

#these are the test 
def test_RadixSort():
    test_empty()
    test_sorts_right()

#test for if the array is empty
def test_empty():
    assert RadixSort([]) == [],"the array is empty"

#test for if sorting is working 
def test_sorts_right():
    assert RadixSort([3,2,1]) == [3,2,1]


if __name__ == "__main__":
    test_RadixSort()
