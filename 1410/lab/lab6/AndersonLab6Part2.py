# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 9/24/2025

# Description: This is part 2 of lab 6
#ask for packages purchased cost is always 99 and find the discount% discount$ and total

# Status: Runs as expected.
import sys
def main():
    try:
        amount = eval(input("Packages Purchased: "))
        if amount < 0:
            raise ValueError
    except:
        sys.exit("Invalid")
    if 10 < amount <=19:
        discount = 20
    elif 20< amount <= 49:
        discount = 30
    elif 50 < amount <=99:
        discount = 40
    elif amount > 100:
        discount = 50
    else:
        discount = 0
    amount *=99
    discount_amount = (amount * discount)/100
    total = amount - discount_amount

    print(f"the discount is: {discount:.02f}% \nthe overall discount is: ${discount_amount:.02f}\nthe total is: ${total:.02f}")

main()