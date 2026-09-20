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
    return len(result)

if __name__ == "__main__":
    timeEfficiency(listPrimeNumbers,int(input("Enter a number for the list of prime numbers: ")))
#timeEfficiency(listPrimeNumbers,1000)#{'start':24447.450872426,'end':24447.451097096,'time efficiency':0.00022466999871539883,'result':168}
#timeEfficiency(listPrimeNumbers,10000)#{'start':24447.451113356,'end':24447.454186867,'time efficiency':0.0030735109976376407,'result':1229}
#timeEfficiency(listPrimeNumbers,50000)#{'start':24447.454202547,'end':24447.476868071,'time efficiency':0.02266552400033106,'result':5133}
#timeEfficiency(listPrimeNumbers,100000)#{'start':24447.476911841,'end':24447.533546693,'time efficiency':0.05663485200057039,'result':9592}
#timeEfficiency(listPrimeNumbers,3000000000)

#it's way to fast on my pc hahaha 


