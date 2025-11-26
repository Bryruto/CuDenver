import random as r
#from random import randint

class Die:
    count = 0
    def __init__(self,sides):
        self.sides = sides
        Die.count +=1 

    def roll_die(self):
        print(f"die:{self.count}->{r.randint(1,self.sides)}")

