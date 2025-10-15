# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 10/15/2025

# Description: This is of lab 8
#to debug a program that goes on forever this program flips a coin and tells you how many are heads

# Status: Runs as expected.
def main():
    import random
    print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
    input()
    flips = 0
    heads = 0
    while flips < 1000:
        if random.randint(0, 1) == 1:
            heads = heads + 1
            print ('Number of heads', heads)
        if flips == 900:
            print('900 flips and there have been ' + str(heads) + ' heads.')
        if flips == 100:
            print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
        if flips == 500:
            print('Half way done, and heads has come up ' + str(heads) + ' times.')
        flips +=1

    print()
    print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
    #maybe should add how far off you are or somthing like that
    print('Were you close?')
main()