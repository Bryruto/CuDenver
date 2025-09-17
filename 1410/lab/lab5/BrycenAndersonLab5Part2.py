# Name:  Brycen Anderson

# Class: CSCI 1411-003 

# Due Date: 9/1/2025

# Description: This is part 2 of lab 5 
#ask for details about an item and display all information after finding total amount
# amount taxed and grand_total 

# Status: Runs as expected.
def main():
    item_name = input("item name:")
    item_quantity = eval(input("item quantity:"))
    item_price = eval(input("item price:"))
    tax_rate = eval(input("Tax rate:"))

    total_amount = item_quantity * item_price
    amount_taxed = total_amount * tax_rate / 100
    grand_total = total_amount + amount_taxed

    print(f"item name:{item_name}\nitem_quantity:{item_quantity}\nitem price:${item_price:.2f}\ntotal amount:${total_amount:.2f}\ntax amount:${amount_taxed:.2f}\ngrand total:${grand_total:.2f}")
main()