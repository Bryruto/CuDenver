def main():
    my_pets = ["alfred" , 'tabitha', 'william' , 'arla']
    uppered_pets= []

    for pet in my_pets:
        uppered_pets.append(pet.upper())
    print(uppered_pets)

    print(list(map(str.upper, my_pets)))

    #below is a lambda function 
    #a lambda is a 1 line function that is annoynomous 
    #is a not defined till run time dynamic function 
    print(list(filter((lambda x : "l" in x), my_pets)))

    #reduce makes a list turn into 1 value 
    from functools import reduce 
    print(reduce(lambda x,y: x + len(y),my_pets,0))

    #what is a good algorithm
    #correctness, efficiency 

    #efficiency matters only when the data size grows 

    #Algorithms is a branch of math 
    #we only use in comp sci proving correctness, measuring time complexity/efficiency , and Algorithms comparison 

    #Fuindamental Math Topics 

    #proof by Mathematical Induction -- the best way to prove 
        #loop invariant Proof method 

    #logarithm (base2) 

    #summations
        #manipulating finite sums (linearity)
        #find (n+1) + (n+2) + (n+3) ..... (n-1)
        
        #if there is a common factor you can pull that out 
        #if ak + bk you can split sum ak + sum bk

    #Arithmetic series 
        #the difference between any two consecutive terms in a series 

        #add up the first and last terms
        #multiply the outcome by the number of terms
        #divide by 2
        # am , am+1 , am+2 .... an

        #((am + an) * (n-m+1))/2

        #((n+1)n)/2 = (n^2 + n)/2    when m = 1 ,am = 1 and an = n 

    #Geometric series
        #A geometric series is a sequence in which the ratio between two consecutive terms is constant 

        #the formula for each term 
            #ai = b * q^i for i>= 0, which follows by induction on i, a0 = b 

        #the formula for the sum 
            #b + bq + bq^2 + ..... bq^(n-1)
        
        #this is similar to a polynomial form if b = 1, q = x
            #1 + x + x^2 + .... + x^(n-1)

        #Now consider the product of 
            #1 + x + x^2 + ... + x^(n-1) 

        #all in all 
            #general formula where b is the first term and the rate is x 

            #ex 
                #(2^n-1)/(2-1) = 2^n-1

    #approximation by integrals 
        #estimating a summation by integrals when f is either monotonically increasing or monotonically decreasing 

    #Harmonic series 
        #monotonically increasing series Harmonic series is the infinite series formed by summing all positive unit fractions

        #Hn = 1 + 1/2 + 1/3 + ... + 1/n 

    #proof techniques 
        #Mathematical induction 
            #if n is a true then n + 1 true then n + 2 all the way to n-1 are true 
            
            #two cases to be proved 
            #base case is true 
            #induction step must be true


main()