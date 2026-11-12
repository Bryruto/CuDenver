#this is for fast merge 
def fast_merge(arrs_in_arr:list):
    #check to see if its empty 
    if len(arrs_in_arr) == 0:
        return []

    #check to see if at base case
    if len(arrs_in_arr) <= 1:
        return arrs_in_arr[0]

    #get the middle of the array
    mid = len(arrs_in_arr)// 2

    #left and right sub array
    left = arrs_in_arr[:mid]
    right = arrs_in_arr[mid:]
    
    #sort left and right sub arrays 
    left = fast_merge(left)
    right = fast_merge(right) 

    return merge([left,right])

# slow merge by scanning the current number in every list
def merge(arrs_in_arr:list):
    # keep track of the next unused position in each list
    positions = [0] * len(arrs_in_arr)
    total_elements = sum(len(arr) for arr in arrs_in_arr)
    result = []

    # choose one number for each position in the result
    for _ in range(total_elements):
        smallest = None
        smallest_list = -1

        # look at the first remaining number in every nonempty list
        for i, arr in enumerate(arrs_in_arr):
            # skip lists that have no numbers left
            if positions[i] >= len(arr):
                continue

            value = arr[positions[i]]
            # save the smallest number and which list it came from
            if smallest_list == -1 or value < smallest:
                smallest = value
                smallest_list = i

        result.append(smallest)
        # only advance in the list that supplied the smallest number
        positions[smallest_list] += 1

    return result

        


def test_merges():
    test_fast_merge()
    test_merge()
    test_merge_edge_cases()

def test_fast_merge():
    assert fast_merge([
    [1, 5, 9, 15],
    [2, 6, 10, 20],
    [0, 3, 7, 12],
    [4, 8, 11, 16],
    [1, 6, 13, 18],
    [5, 14, 21]]) == [0, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21]

def test_merge():
    assert merge([
    [1, 5, 9, 15],
    [2, 6, 10, 20],
    [0, 3, 7, 12],
    [4, 8, 11, 16],
    [1, 6, 13, 18],
    [5, 14, 21]]) == [0, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21]


# check empty lists and duplicates and uneven list lengths
def test_merge_edge_cases():
    cases = [
        [],
        [[]],
        [[], [], []],
        [[-3, 0, 0, 5]],
        [[], [-5, 2, 2], [], [-2, 2, 4], []],
        [[1], [0, 2, 3, 4, 5, 6], [2, 2]],
    ]

    for arrs in cases:
        original = [arr.copy() for arr in arrs]
        expected = sorted(num for arr in arrs for num in arr)
        assert merge(arrs) == expected
        assert fast_merge(arrs) == expected
        # both merges should leave the input lists unchanged
        assert arrs == original


if __name__ == "__main__":
    test_merges()
