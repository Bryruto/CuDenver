import time
import matplotlib.pyplot as plt

global quicktimes, bubbletimes,k
quicktimes,bubbletimes,k= [],[],[]

#plot the points and map 
def plot(size:list[int]):
    #plotting for bubble,quick, together plotting
    plt.plot(size,bubbletimes,label="Bubble Sort" ,marker=".",ms=15,markerfacecolor="blue")
    plt.plot(size,quicktimes,label="Quick Sort",marker=".",ms=15,markerfacecolor="orange")
    plt.plot(size,k,label="QuickBubble Sort",marker=".",ms=15,markerfacecolor="green")

    #title of graph
    plt.title("Time(seconds) vs Number of elements",fontsize=20)
    
    #label x and y, space evenly 
    plt.ticklabel_format(axis="x",style="plain",useOffset=False)
    plt.ylabel("Time (seconds)")
    plt.xlabel("Number of elements")
    plt.tight_layout()
    plt.grid(axis="both",linewidth=2,color="black",linestyle="dotted")
    plt.show()

def timeEfficiency(funcName, *args,**keys):
    #start timer
    start = time.perf_counter_ns()
    
    #run program
    result = funcName(*args,**keys)
    
    #end timer get total time 
    end = time.perf_counter_ns()
    elapsed = end - start
    
    #formating and adding to plotting arrays
    took = ""
    if funcName.__name__ == "bubblesort":
        bubbletimes.append(elapsed/1000000000)
    elif funcName.__name__ == "quicksort":
        quicktimes.append(elapsed/1000000000)
    else:
        k.append(elapsed/1000000000)
    

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
    
    return ["Function Name: " + str(funcName.__name__)  + "\nReal Time:" + took + "\nOutPut\n" + str(result[:10]) + "\n",elapsed/1000000000]

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
    if end - start + 1 <= 1:
        return arr

    #base case is now just bubblesort 
    if end - start + 1 <= k:
        n = end
        flip = 1
        while flip:
            flip = 0
            for i in range(start,n):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    flip+= 1
            n-=1
        return arr
    
    #set pivot
    pivot = arr[end]
    left = start
    
    #loop through array
    for i in range(start,end):
        if arr[i] < pivot:
            arr[left],arr[i] = arr[i],arr[left]
            left+=1

    arr[end] = arr[left]
    arr[left] = pivot

    quickBubbleSort(arr,start,left-1,k)
    quickBubbleSort(arr,left+1,end,k)

    return arr

def findingk():
    with open("rand1000000.txt", "r") as file:
        arr = [int(value) for value in file.read().split()]

    times = {}

    #check 100 elements prob to much
    for cutoff in range(1, 101):
        times[cutoff] = timeEfficiency(quickBubbleSort, arr.copy(), 0, len(arr) - 1, cutoff)[1]

        #i added to make sure its running
        print(f"Finished cutoff {cutoff}: {times[cutoff]:.6f} seconds",flush=True)

    # Select the cutoff with the lowest measured time
    best_k = min(times, key=lambda cutoff: times[cutoff])

    print(f"\nBest cutoff from 1-100: {best_k} elements\n")

    #to show where the best k is 
    for offset, label in zip(
        [-7, -5, -3, 0, 3, 5, 7],
        ["k-7", "k-5", "k-3", "k", "k+3", "k+5", "k+7"]
    ):
        cutoff = best_k + offset

        #i can't sort 0 elements
        if cutoff < 1:
            print(f"{label}: N/A (cutoff {cutoff} is below 1)")
            continue

        if cutoff not in times:
            times[cutoff] = timeEfficiency( quickBubbleSort, arr.copy(), 0, len(arr) - 1, cutoff)[1]
        
        print(f"{label}: {times[cutoff]:.6f} seconds")

    return best_k
    
def main():
    best_k = findingk()
    k.clear()
    fileNames = ["rand1000.txt","rand10000.txt","rand100000.txt","rand250000.txt","rand500000.txt","rand1000000.txt"]
    size = [1000,10000,100000,250000,500000,1000000]
    n = 0
    for name in fileNames:
        with open(name,"r") as file:
            arr = [int(value) for value in file.read().split()]
            print(f"Array size:{size[n]}\n" + timeEfficiency(quicksort,arr.copy(),0,len(arr)-1)[0])
            print(f"Array size:{size[n]}\n" + timeEfficiency(bubblesort,arr.copy())[0])
            print(f"Array size:{size[n]}\n" + timeEfficiency(quickBubbleSort,arr.copy(),0,len(arr)-1,best_k)[0])
            n += 1

            #if input("Look at output Enter when done and it will go to the next q to quit-> ") == 'q':
            #   break
    plot(size)
if __name__ == "__main__":
    main()
