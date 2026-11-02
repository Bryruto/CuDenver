#this is for fast merge 
def fast_merge(arrs_in_arr:list):
    pass

#this will be merging them in order slower
def merge(arrs_in_arr:list):

    #so lets just merge 2 arrays at a time for slower normal merge 
    while len(arrs_in_arr) > 1:

        #making my tmp array and 2 others that i will merge
        tmp = []
        arr1 = arrs_in_arr.pop()
        arr2 = arrs_in_arr.pop()
        
        # these are my left and right pointers
        #also the length just a bit fast this way
        l,r,size1,size2 = 0,0,len(arr1),len(arr2) 
        
        #add elements back into 1 array
        while l < size1 and r < size2:
            
            if arr1[l] <= arr2[r]:
                tmp.append(arr1[l])
                l+=1
        
            else:
                tmp.append(arr2[r])
                r+=1
        
        #any left in leftside add them
        while l < size1:
            tmp.append(arr1[l])
            l=+1

        #any left in rightside add them 
        while r < size2:
            tmp.append(arr2[r])
            r=+1
        
        #this is not great i should move this 
        arrs_in_arr.append(tmp)
    

    return arrs_in_arr[0]


        


def test_merges():
    test_fast_merge()
    test_merge()

def test_fast_merge():
    assert fast_merge([
    [1, 5, 9, 15],
    [2, 6, 10, 20],
    [0, 3, 7, 12],
    [4, 8, 11, 16],
    [1, 6, 13, 18],
    [],
    [5, 14, 21]]) == [0, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21]

def test_merge():
    assert merge([
    [1, 5, 9, 15],
    [2, 6, 10, 20],
    [0, 3, 7, 12],
    [4, 8, 11, 16],
    [1, 6, 13, 18],
    [],
    [5, 14, 21]]) == [0, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21]



if __name__ == "__main__":
    test_merges()
