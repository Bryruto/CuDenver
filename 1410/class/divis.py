from random import randint
def main():

    x = randint(1,50)
    
    for i in range(x):
        if (i+1)%3 == 0:
            print(f"{i+1}: is divisible ")
        else:
            print(f"{i+1}: is not divisible")
    

main()

