"""
Name:Brycen Anderson
Class: CSCI 1411-003
Due Date:11/12/2025
Status:works as expected 
"""
class BankAccount:
    """this is a bankaccount(self,balance) 
        you can deposit 
        you can withdraw
        tracks the balance starting at 0 if not given a balance
        """
    def __init__(self,balance = 0.0):
        self.balance = balance
        

    def deposit(self,amount):
        try:
            if amount > 0:
                self.balance += amount
                print(f"Transaction was successful. Your account balance is ${self.balance:.2f}")
                return True 
            else:
                raise SyntaxError(f"Deposit amount ${amount:.2f} is less than 0. Transaction rejected")
        except SyntaxError as e:
            print(e)
            return False

    def withdraw(self,amount):
        try:
            if amount < self.balance:
                self.balance -= amount
                print(f"Transaction was successful. Your account balance is ${self.balance:.2f}")
                return True 
            else:
                raise SyntaxError(f"Withdraw amount ${amount} is higher than balance of ${self.balance:.2f}\nTransaction rejected")
        except SyntaxError as e:
            print(e)
            return False
        
    def get_balance(self):
        return f"{self.balance:.2f}"