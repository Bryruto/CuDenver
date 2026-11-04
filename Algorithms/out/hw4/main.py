from prepare import prepare 
from BucketSort import bucketSort
from radixsort import RadixSort
from merges import fast_merge,merge
from TestFuction import timeEfficiency

#this is main
def main():
    #array of 100,10,000 elements per
    array = prepare("rand1000000.txt")
    
    first,last = [],[]
    #take file first 50 elements
    for arr in array[:50]: 
        first.append(RadixSort(arr))
    
    #take file last 50 elements 
    array_BucketSort = array[49:]
    for arr in array[49:]:
        last.append(bucketSort(arr))
        
    #do both merge fast and merge slow and check result is equal on both
    time_fast_merge = timeEfficiency(fast_merge,array.copy())
    time_merge = timeEfficiency(merge,array.copy())
    
    # i passed back as array so i can index the print staments the way i want
    print()
    print(time_fast_merge[0])
    print("-" * 50)

    print()
    print(time_merge[0])
    print("-" * 50)

    print()
    print(f"DO THEY MATCH = {time_fast_merge[1] == time_merge[1]}")
    

#this is so main will only run if i run this file
if __name__ == "__main__":
    main()
