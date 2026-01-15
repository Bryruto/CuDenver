from players import Player
import random 

def main():
    number_of_players = int(input("Max:6 Min:2\nhow many players are there:"))
    for height in range(5):
        if height == 0 or height+1 == 5:
            print("#"*5)
        if height+1 == 5:
            break  
        for width in range(5):
            if width == 0 or width+1 == 5:
                print("#",end="")
            else:
                print(" ",end="")
        print()

            #check to see if a player is body is on this spot
            
main()