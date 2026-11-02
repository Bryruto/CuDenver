def bucketSort(arr):
    if not arr:
        return []
    
    #make the bucket in way of a hashmap
    buckets = {}# numbers -> counts
    largest, smallest = arr[0],arr[0]

    #looping through the elements to make all the buckets
    for num in arr:
        if num in buckets:
            buckets[num] += 1
        else:
            buckets[num] = 1
        
        largest = max(largest,num)
        smallest = min(smallest,num)
    
    #make a array for the result
    result = []
        
    # then clear out the bucket inorder 
    for i in range(smallest,largest + 1):
        if i in buckets:
            for j in range(buckets[i]): 
                result.append(i)

    #return the result
    return result

#run test on Bucket sort 
def test_bucketSort():
    test_bucket_empty()
    test_bucket_sorts()

#test if the array is empty 
def test_bucket_empty():
    assert bucketSort([]) == [], "the array is empty"

def test_bucket_sorts():
    assert bucketSort([42, 0, 99, 17, 42, 5, 88, 1, 73, 17, 50, 2, 99, 36, 64, 0]) == [0, 0, 1, 2, 5, 17, 17, 36, 42, 42, 50, 64, 73, 88, 99, 99], "the sort is not working"


if __name__ == "__main__":
    test_bucketSort()
