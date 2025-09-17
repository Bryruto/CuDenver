# Name:  Brycen Anderson

# Class: CSCI 1411-00X 

# Due Date: 9/10/2025

# Description: This is part 2 of lab 4. 
#give a lenght and width and cost 
#find perimeter, amount of segments,total cost,wasted money and wasted trim

# Status: Runs as expected.
import math

def main():
    cost = 1.88
    length = eval(input("What is the length:"))
    width = eval(input("what is the width:"))
    perim = find_p(length,width)

    need = amount(perim)
    wasted = (need) - (perim/12)
    total= money(need,cost) 

    print(f"your box has a perimeter of :{perim}")
    print(f"The number of trim segments that you have to buy:{need}")
    print(f"Total cost:{total}")
    print(f"Amount of trim wasted:{wasted}")
    print(f"cost of wasted trim:${wasted * cost}")

def find_p(length:float,width:float)->float:
    return 2 * length + 2 * width

def amount(perim:float)->int:
    return math.ceil(perim/12)

def money(need:int,cost:float):
    return need * cost
    



main()