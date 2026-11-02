from prepare import prepare 
from BucketSort import bucketSort
from radixsort import RadixSort
from merges import fast_merge,merge

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
    
    #merge first and last 
    fast_merge()
    merge()

#this is so main will only run if i run this file
if __name__ == "__main__":
    main()
