#Author:Brycen Anderson
# Due Date:10/15/25
#
# This is a simple math quiz program that will generate two
# random numbers between 1 and 10, it will display those
# numbers and ask the user to enter the sum of those numbers.
# If the user answers the question correctly then it will display
# the message that the answer is correct. If the user answers the
# question incorrectly then it will display the message Nope with
# the correct answer
# .
# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 10/15/2025

# Description: This is of lab 7
#gives you 2 numbers to add and answer the question

# Status: Runs as expected.
def main():
    import random
    number1 = random.randint (1, 10)
    number2 = random.randint (1, 10)
    print ('What is', number1, '+', number2, '?')
    answer = int(input('answer:'))
    if answer == number1 + number2:#or int(answer)
        print ('Your answer is correct')
    else:
        print ('Nope! The correct answer is', number1 + number2)

main()
