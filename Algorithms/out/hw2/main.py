import time
import random
import matplotlib.pyplot as plt

insertcomp,mergecomp = 0,0
mergetime = []
inserttime = []

#plot the points and map 
def plot():
    size = [1000,10000,100000,250000,500000,1000000]
    plt.plot(size,mergetime,label="merge Sort" ,marker=".",ms=15,markerfacecolor="blue")
    plt.plot(size,inserttime,label="insertion Sort",marker=".",ms=15,markerfacecolor="orange")
    
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
    
    if(funcName.__name__ == "mergeSort"):
        comp = mergecomp
        mergetime.append(elapsed/1000000000)
    else:
        comp = insertcomp
        inserttime.append(elapsed/1000000000)
    
    if elapsed >= 1000000000:
        took = f"{elapsed/1000000000:.3f} seconds"
    elif elapsed >= 1000000:
        took = f"{elapsed / 1000000:.3f} ms"
    else:
        took = f"{elapsed} ns" 
    
    #i just added when i had to its a little much now hahaha
    return "Function Name: " + str(funcName.__name__) + f"\nComparisons: {comp}" + "\nReal Time:" + took + "\nOutPut\n" + str(result)  

#break into smaller and smaller slices till 1 element
def mergeSort(arr,s,e):
    if e-s + 1 <= 1:
        return arr

    m = (s + e) //2 
    mergeSort(arr,s,m)
    mergeSort(arr,m+1,e)
    merge(arr,s,m,e)

    return arr

#merge elements from 2 arrays back into 1 
def merge(arr, s, m, e):
    global mergecomp
    l = arr[s:m +1]
    r = arr[m+1:e+1]
    i,j,k = 0,0,s
    
    while i< len(l) and j < len(r):
        mergecomp += 1
        if l[i] <= r[j]:
            arr[k] = l[i]
            i +=1
        else: 
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

#sort array starting with 2 elements then do with 3 so on so forth till at n-1 elements 
def insertionSort(arr):
    global insertcomp
    for i in range(1,len(arr)):
        j = i - 1
        while j >= 0:
            insertcomp += 1 
            if arr[j+1] >= arr[j]:
                break
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j -= 1
    return arr

#yay python 
def arrayNeededIAmlazy(low,high,number):
    return [random.randint(low,high) for _ in range(number)]

def main():
    #arr = arrayNeededIAmlazy(int(input("lowest number: ")),int(input("largest number: ")),int(input("Total size: ")))
    global mergecomp, insertcomp
    fileNames = ["rand1000.txt","rand10000.txt","rand100000.txt","rand250000.txt","rand500000.txt","rand1000000.txt"]
    for name in fileNames:
        with open(name,"r") as file:
            arr = [int(value) for value in file.read().split()]
            mergecomp,insertcomp = 0,0
            print(timeEfficiency(mergeSort,arr.copy(),0,len(arr)-1))
            print(timeEfficiency(insertionSort,arr.copy()))
            if input("Look at output Enter when done and it will go to the next q to quit-> ") == 'q':
               break
    plot()
if __name__ == "__main__":
    main()
