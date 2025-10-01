# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 9/24/2025

# Description: This is of lab 7
#ask for a number greater than or = to 2 then find all primes and compisite number till they reach input number 

# Status: Runs as expected.
def main():
    while True:
        try:
            num= eval(input("Enter a number greater than or equal to 2:"))
            if num < 2:
                print("Number must be greater than or equal to 2:")
                raise ValueError
            break
        except:
            continue                 
    primes = prime(num)
    composites = composite(num)

    if primes:
        print("List of prime numbers:")
        for i in primes:
            print(i,end= " ")
    print()
    if composites:
        print("List of composite numbers:")
        for i in composites:
            print(i,end=" ")
    else:
        print("There are no composite numbers in that range")

def prime(num):
    primes = []
    for i in range(2,num+1):
        for j in range(2,int(i**0.5) + 1):
            if i % j == 0:
                break
        else:# didnt know for else was a thing till just now
            primes.append(i)
    return primes

# i see now i can just say not prime wow
def composite(num):
    composites = []
    i = 0
    for i in range(4,num+1):
        for j in range(2,int(i**0.5)+ 1):
            if i % j == 0:
                composites.append(i)
                break
    return composites



main()