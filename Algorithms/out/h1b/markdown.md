# Run-Length Encoding Assignment

## Student Information
- **Name:** Brycen Anderson
- **Student ID:** 111017061
- **Class:** CSCI 3412-001 — Algorithms
- **Homework #:** HW1b
- **Due Date:** september 14, 2026

---

# Python Code

## Collatz.py
```
    class MaxHeap:
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
        heap = MaxHeap()
        for num in range(1,10000000+1):
            length, best = collat(num)
            heap.push((length, num, best))
        for i in range(10):
            length, num, best = heap.pop()
            print(f"{i+1}. Collatz sequence for {num}: {length} {best}") 
```


### Program Output
```
    [bryruto@Brycen-archlinux h1b]$ python collatz.py
    1. Collatz sequence for 8400511: 686 159424614880
    2. Collatz sequence for 8865705: 668 15208728208
    3. Collatz sequence for 6649279: 665 15208728208
    4. Collatz sequence for 9973919: 663 15208728208
    5. Collatz sequence for 6674175: 621 125218704148
    6. Collatz sequence for 7532665: 616 1017886660
    7. Collatz sequence for 7332399: 616 150311737960
    8. Collatz sequence for 5649499: 613 1017886660
    9. Collatz sequence for 8474249: 611 1017886660
    10. Collatz sequence for 6355687: 608 1017886660
    [bryruto@Brycen-archlinux h1b]$ mv markdown.dm markdown.md
    [bryruto@Brycen-archlinux h1b]$ 
```

#### Analysis
##### approach
    I used a while loop to generate each Collatz sequence and track its length and max value. I stored the results with the length number in my own max heap then poppeed 10 times for top 10.
    
##### optimizations
    The while loop avoids recursive calls and i store only each sequence length and max instead of the entire sequence. The heap lets me retrieve then longest sequences without fully sorting the results. 
    
##### reflections
    There is one thing i want to try but dont have any time to would be memorization like cache so when i land on a number ive already seen i would know how many steps are left over all though this was fun thank you.




## duplicate.py
```
    import random 
    from Efficiency import timeEfficiency
    from tabulate import tabulate

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

    if __name__ == "__main__":
        inputsize = [1000,5000,10000,20000]
        #output = [["Input Size","Brute Force","Sort-and-Scan","Dictionary"]]
        for size in inputsize:
            arr = [random.randint(1,1000) for _ in range(size)]
        #   output.append([str(size),timeEfficiency(AlgoA,arr),timeEfficiency(AlgoB,arr),timeEfficiency(AlgoC,arr)])
        #print(tabulate(output,headers="firstrow",tablefmt="fancy_grid"))
            a,b,c = AlgoA(arr),AlgoB(arr),AlgoC(arr) 
            print(f"\nInput List Size:{size}\n")
            print("Duplicate Detection Results:")
            print("-"*39)
            print(f"Brute Force:\nNumber of duplicated values:{c}\nExecution time:{timeEfficiency(AlgoA,arr)}\n")
            print(f"Sort-and-Scan:\nNumber of duplicated values:{b}\nExecution time:{timeEfficiency(AlgoB,arr)}\n")
            print(f"Dictionary:\nNumber of duplicated values:{c}\nExecution time:{timeEfficiency(AlgoC,arr)}")
            print("-"*39)
            print(f"All three algorithms algorithms produced the same result:{a==b==c}")
```


### Program Output
```
    [bryruto@Brycen-archlinux h1b]$ python duplicate.py

    Input List Size:1000

    Duplicate Detection Results:
    ---------------------------------------
    Brute Force:
    Number of duplicated values:265
    Execution time:10.727 ms

    Sort-and-Scan:
    Number of duplicated values:265
    Execution time:114340 ns

    Dictionary:
    Number of duplicated values:265
    Execution time:78541 ns
    ---------------------------------------
    All three algorithms algorithms produced the same result:True

    Input List Size:5000

    Duplicate Detection Results:
    ---------------------------------------
    Brute Force:
    Number of duplicated values:969
    Execution time:112.711 ms

    Sort-and-Scan:
    Number of duplicated values:970
    Execution time:623900 ns

    Dictionary:
    Number of duplicated values:969
    Execution time:350881 ns
    ---------------------------------------
    All three algorithms algorithms produced the same result:False

    Input List Size:10000

    Duplicate Detection Results:
    ---------------------------------------
    Brute Force:
    Number of duplicated values:997
    Execution time:261.138 ms

    Sort-and-Scan:
    Number of duplicated values:997
    Execution time:1.176 ms

    Dictionary:
    Number of duplicated values:997
    Execution time:631550 ns
    ---------------------------------------
    All three algorithms algorithms produced the same result:True

    Input List Size:20000

    Duplicate Detection Results:
    ---------------------------------------
    Brute Force:
    Number of duplicated values:1000
    Execution time:543.134 ms

    Sort-and-Scan:
    Number of duplicated values:1000
    Execution time:2.423 ms

    Dictionary:
    Number of duplicated values:1000
    Execution time:1.268 ms
    ---------------------------------------
    All three algorithms algorithms produced the same result:True
    [bryruto@Brycen-archlinux h1b]$ 
```

#### Analysis
    1.Dictionary it takes up the most space making it always the fastest. 
    2.As we increase the input size brute force time increase rapidly
    3.Sorting places equal values next to each other so duplicates can be counted in n time but sorting takes time. 
    4.The additional memory stores each number count allowing average O(1) lookups and updates.
    5.The dictionary uses extra memory to avoid repeated searching. in my result this made it faster than brute force showing the benefit of trading memroy for speed.


## Efficiency.py
```
    import time

    def timeEfficiency(funcName, *args,**keys):
        start = time.perf_counter_ns()
        result = funcName(*args,**keys)
        end = time.perf_counter_ns()
        elapsed = end - start
        took = ""
        
        if elapsed >= 1000000000:
            took = f"{elapsed/1000000000:.3f} seconds"
        elif elapsed >= 1000000:
            #took = f"{elapsed / 1000000:.3f} ms"
            print(f"{{'start':{start},'end':{end},'time efficiency':{elapsed} ms,'result':{result}}}") 
        else:
            #took = f"{elapsed} ns"
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
        return result #len(result) for output

    if __name__ == "__main__":
        timeEfficiency(listPrimeNumbers,int(input("Enter a number for the list of prime numbers: ")))
        #timeEfficiency(listPrimeNumbers,1000)#{'start':24447.450872426,'end':24447.451097096,'time efficiency':0.00022466999871539883,'result':168}
        #timeEfficiency(listPrimeNumbers,10000)#{'start':24447.451113356,'end':24447.454186867,'time efficiency':0.0030735109976376407,'result':1229}
        #timeEfficiency(listPrimeNumbers,50000)#{'start':24447.454202547,'end':24447.476868071,'time efficiency':0.02266552400033106,'result':5133}
        #timeEfficiency(listPrimeNumbers,100000)#{'start':24447.476911841,'end':24447.533546693,'time efficiency':0.05663485200057039,'result':9592}
        #timeEfficiency(listPrimeNumbers,3000000000)
    ```

### Program Output
```
    [bryruto@Brycen-archlinux h1b]$ python Efficiency.py
    Enter a number for the list of prime numbers: 100000
    List of prime numbers of 100000
    {'start':10375246182684,'end':10375303288460,'time efficiency':57105776 ms,'result':9592}
    [bryruto@Brycen-archlinux h1b]$ 
```

#### Analysis
    My Implementation uses time Efficiency() to measure execution time and listPrimeNumbers() to check numbers 2 to n and give all primes.to test the time Efficiency. 

    listPrimeNumbers(): O(n^2)ish not really i remembered a discrete structures lesson talking about how the largest prime of any number will be the square root of that number plus 1. I used that to increase the speed of finding primes

    timeEfficiency(): Adds constant time to what ever function it runs O(1)

## guess.py
```
    import random 

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


    if __name__ == "__main__":
        sim(10000,1,1000)
        sim(10000,1,10000)
        sim(10000,1,1000000)
```

### Program Output
```
    [bryruto@Brycen-archlinux h1b]$ python guess.py
    The random number between 1 and 1000:Total number of guesses:119511 Avg:11.95
    The random number between 1 and 10000:Total number of guesses:165535 Avg:16.55
    The random number between 1 and 1000000:Total number of guesses:257702 Avg:25.77
    [bryruto@Brycen-archlinux h1b]$ 
```


#### Analysis
    My implementation uses two functions:sim(number_of_games,min_value,max_value) and game(min_value,max_value) the simulation function takes the number of games a min and max values. Then game will get the answer and a while loop for every guess if to high move max down if to low move min up till the guess == answer then return number of guesses.Sum all guesses then divide by number_of_games for average 

    game():The best case guesses correctly immediately. On average guesses shrink the remaining range by a substantial fraction.In the worst case each guess eliminates only one value. O(log n)

    sim():Calls game() t times multiplying its time complexity by n. O(t log n)
