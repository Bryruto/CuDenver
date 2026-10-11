import time
import matplotlib.pyplot as plt

global quicktimes, bubbletimes
quicktimes,bubbletimes= [],[]

#plot the points and map 
def plot(size:list[int]):
    alllllllll = [quicktimes,bubbletimes]
    colors = ["blue","orange","green","red","purple","brown","pink","gray"]
    

    plt.plot(size,bubbletimes,label="Bubble Sort" ,marker=".",ms=15,markerfacecolor="blue")
    plt.plot(size,quicktimes,label="Quicksort Sort",marker=".",ms=15,markerfacecolor="orange")
    
    plt.title("Time(seconds) vs Number of elements",fontsize=20)
    plt.ticklabel_format(axis="x",style="plain",useOffset=False)
    plt.ylabel("Time (seconds)")
    plt.xlabel("Number of elements")
    plt.tight_layout()
    plt.grid(axis="both",linewidth=2,color="black",linestyle="dotted")
    plt.show()

def timeEfficiency(funcName, *args,**keys):
    start = time.perf_counter_ns()
    result = funcName(*args,**keys)
    end = time.perf_counter_ns()
    elapsed = end - start
    took = ""
    if funcName.__name__ == bubblesort:
        bubbletimes.append(elapsed/1000000000)
    else:
        quicktimes.append(elapsed/1000000000) 
    

    if elapsed >= 3600000000000:
        took = f"{elapsed/3600000000000:.3f} hours"
    elif elapsed >= 60000000000:
        took = f"{elapsed/60000000000:.3f} minutes"
    elif elapsed >= 1000000000:
        took = f"{elapsed/1000000000:.3f} seconds"
    elif elapsed >= 1000000:
        took = f"{elapsed / 1000000:.3f} ms"
    else:
        took = f"{elapsed} ns" 
    
    return "Function Name: " + str(funcName.__name__)  + "\nReal Time:" + took + "\nOutPut\n" + str(result[:10]) + "\n"   

#bubble up the largest number in array then n-1 for every loop O(n^2) time still tho
#Brycen Bubble sort
def bubblesort(arr:list[int]):
    #this is for n-1 1 less element to look at after each loop
    n = len(arr)
    #if flip 1 or more loop if not stop
    flip = 1
    while flip:
        flip = 0
        for i in range(n-1):
            #if i is larger than i+1 swap
            if(arr[i] > arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                flip+=1
        #end is sorted
        n-=1
    return arr

#Brycen Quicksort 
def quicksort(arr:list[int],start:int,end:int):
    #base case
    if end - start + 1 <= 1:
        return arr

    #pivot value
    pivot = arr[end]

    #pointer to the start of this array
    left = start

    #partition
    for i in range(start,end):
        if arr[i] < pivot:
            arr[left],arr[i] = arr[i],arr[left]
            left += 1

    #move pivot in middle of left and right sides
    arr[end] = arr[left]
    arr[left] = pivot
    
    #sort right and left sides 
    quicksort(arr,start,left-1)
    quicksort(arr,left + 1,end)

    return arr
    

def quickBubbleSort(arr:list[int],start:int,end:int,k:int):
    if k == len(arr):
        n = len(arr)
        flip = 1
        while flip:
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    flip+= 1
            n-=1
        return arr
    
    pivot = arr[end]
    left = start
    
    for i in range(start,end):
        if arr[left] < pivot:
            arr[left],arr[i] = arr[i],arr[left]
            left+=1

def findingk():
    pass # test k for all till 1 k is faster then take 3 less than and 3 greater times 
    #
    
def main():
    fileNames = ["rand1000.txt","rand10000.txt","rand100000.txt","rand250000.txt","rand500000.txt","rand1000000.txt"]
    size = [1000,10000,100000,250000,500000,1000000]
    n = 0
    for name in fileNames:
        with open(name,"r") as file:
            arr = [int(value) for value in file.read().split()]
            print(f"size:{size[n]}\n" + timeEfficiency(quicksort,arr.copy(),0,len(arr)-1))
            print(f"size:{size[n]}\n" + timeEfficiency(bubblesort,arr.copy()))
            #print(f"size:{size[n]}" + timeEfficiency(quickBubbleSort,arr.copy()))
            n += 1

            #if input("Look at output Enter when done and it will go to the next q to quit-> ") == 'q':
            #   break
    plot(size)
if __name__ == "__main__":
    main()
