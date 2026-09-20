import random 
import time

def game(min:int,max:int)->int:#avg
    times = 1
    guess = random.randint(min,max)
    answer = random.randint(min,max) 
    
    while guess != answer:
        if(guess > answer):
            max = guess -1
        else:
            min = guess + 1 

        guess = random.randint(min,max)
        times += 1

    return times

def sim(num_of_games:int,min:int,max:int):
    sum = 0
    for i in range(num_of_games):
        sum += game(min,max)
    print(f"The random number between {min} and {max}:Total number of guesses:{sum} Avg:{sum/num_of_games:.02f}")



#Efficiency.py

def timeEfficiency(funcName, *args,**keys):#switch print with took as needed
    start = time.perf_counter_ns()
    result = funcName(*args,**keys)
    end = time.perf_counter_ns()
    elapsed = end - start
    took = ""
    
    if funcName != listPrimeNumbers:#this is a fix for now
        if elapsed >= 1000000000:
            took = f"{elapsed/1000000000:.3f} seconds"
        elif elapsed >= 1000000:
            took = f"{elapsed / 1000000:.3f} ms"
        else:
            took = f"{elapsed} ns"
    else:
        if elapsed >= 1000000000:
            print(f"{{'start':{start},'end':{end},'time efficiency':{elapsed} seconds,'result':{result}}}") 
        elif elapsed >= 1000000:
            print(f"{{'start':{start},'end':{end},'time efficiency':{elapsed} ms,'result':{result}}}") 
        else:
            print(f"{{'start':{start},'end':{end},'time efficiency':{elapsed} ns,'result':{result}}}") 
    return took

def listPrimeNumbers(theMaxNum:int):#list
    #print(f"Enter a number for the list of prime numbers: {theMaxNum}")#short cut 
    print(f"List of prime numbers of {theMaxNum}")
    result = []
    for i in range(2,theMaxNum + 1):
        for j in range(2,int(i**0.5) + 1):
            if i%j == 0:
                break
        else:
            result.append(i)
    return len(result)

#duplicate.py
from tabulate import tabulate #makes output look proper like 

def AlgoA(arr:list)->int:
    #print("Algorithm A")
    #print(f"input {arr}\n")
    #print("output: ")

    
    total = 0
    #word = ""
    seen = []
    for i in range(len(arr)):
        count = 1
        if arr[i] not in seen:
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j]: 
                    count += 1
            if count > 1:
                total += 1
                #word += f"{arr[i]}->{count} times\n"
        seen.append(arr[i])
    return total


def AlgoB(arr:list):
    #print("Algorithm B")
    #print(f"Original:\n{arr}")
    tmp_arr = sorted(arr)
    #print(f"After sorting:\n{tmp_arr}")
    
    total=0
    #word = ""
    count = 1
    for i in range(len(tmp_arr)-1):
        if(tmp_arr[i] == tmp_arr[i+1]):
            count += 1
        else:
            if count > 1:
                total += 1
                #word += f"{tmp_arr[i]}->{count} times\n"
            count = 1

    return total + 1


def AlgoC(arr:list):
    #print("Algorithm C")
    total = 0
    #word = ""
    nums_count = {}
    for num in arr:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1

    for num,count in nums_count.items():
        if(count > 1):
            total += 1
            #word += f"{num}->{count} times\n"
    
    return total


#collatz.py
class MaxHeap:#max heap class 
    def __init__(self):
        self.heap = []
    
    def size(self):
        return len(self.heap)
    def push(self,value):
        self.heap.append(value)
        curr = len(self.heap)-1
        
        while curr > 0 and self.heap[(curr-1)//2] < self.heap[curr]:
            p = (curr-1)//2
            self.heap[curr],self.heap[p] = self.heap[p], self.heap[curr]
            curr = p
        

    def pop(self):
        if not self.heap:
            return 0,0,0
        
        max = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            i = 0
            self.heap[0] = last

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                
                if left >= len(self.heap):
                    break

                larger = right if right < len(self.heap) and self.heap[right] > self.heap[left] else left

                if self.heap[i] >= self.heap[larger]:
                    break

                self.heap[i],self.heap[larger] = self.heap[larger],self.heap[i]
                i = larger

        return max



def collat(num):
    length = 1
    best = 0
    
    while num != 1:
        if num % 2 == 0:
            num //=2
        else:
            num = 3*num+1
        length += 1
        best = max(best,num)
    return length,best




if __name__ == "__main__":
    #main for guess 
    if input("('y','n')run guess.py:") == 'y' or 'Y' or 'yes' or 'ye':
        sim(10000,1,1000)
        sim(10000,1,10000)
        sim(10000,1,1000000)#change if to much
    
    #main for Efficiency 
    if input("('y','n')run Efficiency.py:") == 'y' or 'Y' or 'yes' or 'ye':
        #timeEfficiency(listPrimeNumbers,int(input("Enter a number for the list of prime numbers: ")))
        timeEfficiency(listPrimeNumbers,1000)#{'start':24447.450872426,'end':24447.451097096,'time efficiency':0.00022466999871539883,'result':168}
        timeEfficiency(listPrimeNumbers,10000)#{'start':24447.451113356,'end':24447.454186867,'time efficiency':0.0030735109976376407,'result':1229}
        timeEfficiency(listPrimeNumbers,50000)#{'start':24447.454202547,'end':24447.476868071,'time efficiency':0.02266552400033106,'result':5133}
        timeEfficiency(listPrimeNumbers,100000)#{'start':24447.476911841,'end':24447.533546693,'time efficiency':0.05663485200057039,'result':9592}
    
    #main for duplicate
    if input("('y','n')run duplicate.py:") == 'y' or 'Y' or 'yes' or 'ye': 
        inputsize = [1000,5000,10000,20000]
        #output = [["input size","brute force","sort-and-scan","dictionary"]]
        for size in inputsize:
            arr = [random.randint(1,1000) for _ in range(size)]
        #   output.append([str(size),timeefficiency(algoa,arr),timeefficiency(algob,arr),timeefficiency(algoc,arr)])
        #print(tabulate(output,headers="firstrow",tablefmt="fancy_grid"))
            a,b,c = AlgoA(arr),AlgoB(arr),AlgoC(arr) 
            print(f"\ninput list size:{size}\n")
            print("duplicate detection results:")
            print("-"*39)
            print(f"brute force:\nnumber of duplicated values:{c}\nexecution time:{timeEfficiency(AlgoA,arr)}\n")
            print(f"sort-and-scan:\nnumber of duplicated values:{b}\nexecution time:{timeEfficiency(AlgoB,arr)}\n")
            print(f"dictionary:\nnumber of duplicated values:{c}\nexecution time:{timeEfficiency(AlgoC,arr)}")
            print("-"*39)
            print(f"all three algorithms algorithms produced the same result:{a==b==c}")
    
    #main for collatz.py
    if input("this program will take a long time lower range for faster output\n('y','n')run collatz.py:") == 'y' or 'Y' or 'yes' or 'ye':      
        heap = MaxHeap()
        for num in range(1,1000+1):#this is what you must change
            length, best = collat(num)
            heap.push((length, num, best))
        for i in range(10):
            length, num, best = heap.pop()
            print(f"{i+1}. Collatz sequence for {num}: {length} {best}") 
