def bucketSort(arr):
    # return an empty array if there are no numbers
    if not arr:
        return []
    
    # hashmap of arrays where each array is a bucket
    buckets = {}
    # start the bucket ranges at the smallest number
    smallest, largest = min(arr), max(arr)
    # each bucket covers 10000 integer values
    bucket_width = 10_000

    # put each number in its range bucket
    for num in arr:
        # subtract smallest so the first bucket starts at 0
        # if smallest is 0 then 0 through 9999 go in bucket 0
        # and 10000 through 19999 go in bucket 1
        index = (num - smallest) // bucket_width
        # make the bucket if it is not there yet
        if index not in buckets:
            buckets[index] = []
        # add the number and keep duplicates too
        buckets[index].append(num)

    # make a new array for the sorted result
    result = []
    # find which bucket holds the largest number
    last_bucket = (largest - smallest) // bucket_width

    # go through the buckets from smallest range to largest
    for index in range(last_bucket + 1):
        # skip ranges that have no numbers
        if index not in buckets:
            continue

        bucket = buckets[index]

        # insertion sort each bucket
        # start at the second number since the first is already sorted
        for i in range(1, len(bucket)):
            # save the number before moving anything
            value = bucket[i]
            j = i - 1

            # move bigger numbers right to make room
            while j >= 0 and bucket[j] > value:
                bucket[j + 1] = bucket[j]
                j -= 1

            # put the saved number in its sorted position
            bucket[j + 1] = value

        # add the sorted bucket to the result
        result.extend(bucket)

    return result

# run the bucket sort tests
def test_bucketSort():
    test_bucket_empty()
    test_bucket_sorts()

# test if the array is empty
def test_bucket_empty():
    assert bucketSort([]) == [], "the array is empty"

# check sorting and make sure duplicates are kept
def test_bucket_sorts():
    assert bucketSort([42, 0, 99, 17, 42, 5, 88, 1, 73, 17, 50, 2, 99, 36, 64, 0]) == [0, 0, 1, 2, 5, 17, 17, 36, 42, 42, 50, 64, 73, 88, 99, 99], "the sort is not working"


if __name__ == "__main__":
    # run tests when this file is run directly
    test_bucketSort()
