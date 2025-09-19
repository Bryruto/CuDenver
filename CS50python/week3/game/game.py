import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level <=0:
            raise ValueError()
        break
    except ValueError:
        pass

number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            print("Just right!")
            sys.exit()
        elif guess <= 0:
            raise ValueError()
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")

    except ValueError:
        pass

