"""
Name:Brycen Anderson
Class: CSCI 1411-003
Due Date:11/12/2025
Status:works as expected 
"""
from BankAccount import BankAccount

account = BankAccount()
t = int(input("Enter number of transactions:"))
count = 0
for i in range(t):
    doing = input("Enter transaction type: ").lower()
    if doing == "deposit":
        if account.deposit(float(input("Enter transaction amount: "))):
            count+=1
    
    if doing == "withdraw":
        if account.withdraw(float(input("Enter transaction amount: "))):
            count+=1

print(f"After {count} transactions, your balance is:{account.get_balance()}")
        