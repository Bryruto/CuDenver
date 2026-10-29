#i need to find a way to track the times i divide and times i mod and how to pass that to this function
def countingSort(arr:list,digit=0):
    #check to see if it is empty
    if not arr: 
        return False
    
    #hash map for the counts need to have list because no real pointers in python 
    counts = {}

    # loop through arr and getting counts for the number
    for num in arr:
        index = num
        if digit:
            index = (num/10**digit) % 10 
        else:
            index = num % 10
        
        #if key index is in the array you append  
        if index in counts:
            counts[index].append(num)

        #if not you add the list/array
        else:
            counts[index] = [num]
        
    #force the dictionary to go inorder if not a key skip
    result = []
    for key in range(10):
        if key in counts:
            for num in counts[key]:
                result.append(num)

    return result

def test_countingSort():
    assert countingSort([1,3,2,3,5,1,5,3,1]) == [1,1,1,2,3,3,3,5,5],"wrong order didnt sort"

if __name__ == "__main__":
    test_countingSort()
