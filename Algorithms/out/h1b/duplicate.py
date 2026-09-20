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

