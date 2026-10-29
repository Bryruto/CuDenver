import prepare 
import radixsort
import countingsort 

#this is main
def main():
    #array of 100,10,000 elements per
    array = prepare("rand1000000.txt")
    
    #take file first 50 elements
    array_radixSort = array[:50]
    for arr in array_radixSort: 
        RadixSort(arr)

    #take file last 50 elements 
    array_BucketSort = array[49:]
    
    
#this is so main will only run if i run this file
if __name__ == "__main__":
    main()
