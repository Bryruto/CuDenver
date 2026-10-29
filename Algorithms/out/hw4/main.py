import prepare 
import radixsort
import countingsort


#this is main
def main():
    #array of 100,10,000 elements per
    array = prepare("rand1000000.txt")
    
    first = []
    #take file first 50 elements
    for index in array[:50]: 
        first.append(RadixSort(value))
    
    last = []
    #take file last 50 elements 
    array_BucketSort = array[49:]
    for arr in array[49:]:
        last.append(BuckSort(arr))
    
    #merge first and last 
    
#this is so main will only run if i run this file
if __name__ == "__main__":
    main()
