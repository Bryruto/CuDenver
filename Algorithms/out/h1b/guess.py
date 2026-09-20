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
