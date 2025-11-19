# BankAccount.py
# Author: 
# Date: 

#import Transaction class
from Transaction import *

def main():
    """Display main menu and class functions based on the selected action"""

    print ('Welcome to Bank Account Application')
    print ()

    done = False

    # Create an empty list of transactions
    list_of_transactions = []

    #Loop as long as done is False
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - Read data from the file')
        print ('B - Display list of transactions')
        print ('C - Add a new transaction')
        print ('D - Calculate current balance')
        print ('E - Save data to a file')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C, D, E, or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            read_data (list_of_transactions)
        elif (action == 'B' or action == 'b'):
            display_list (list_of_transactions)
        elif (action == 'C' or action == 'c'):
            add_transaction (list_of_transactions)
        elif (action == 'D' or action == 'd'):
            calculate_balance (list_of_transactions)
        elif (action == 'E' or action == 'e'):
            save_data (list_of_transactions)
        elif (action == 'Q' or action == 'q'):
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')

def read_data (list_of_transactions:list):
    """Read data from the input file, create transaction object and add it to
       the list of transactions"""
       # Ask user for name of the input file, read each line of the data,
    try:
        f = input("Input file: ")
        with open(f,"r") as file:
       # split line using colon (:) is delimiter, create transaction object
            for line in file:
                a,b,c =line.split(":")
                list_of_transactions.append(Transaction(a,b,c))
        # and add it to the list of transaction. Display error message if the
    except Exception as e:
        print("file is not found",e)
       # input file is not found.
    print ('Read Data Function')
    


def display_list (list_of_transactions):
   """ Displays list of transactions """

   # Sort the list of transactions by date and display list of transactions
   tmp = sorted(list_of_transactions,key = lambda x:x.date)
   # in form of a table
   print (f"{'date':<10} {'type':<10} {'amount':<10}")
   print("="*30)
   for i in list_of_transactions:
       print(f"{i.date:<10} {i.transaction_type:<10} {i.amount:<10}")
   print("="*30)
   print ('display list Function')
   
           


def add_transaction (list_of_transactions):
    """Adds a new transaction to list of Transactions"""

    # Ask user for date, type, and amount of transaction, create a transaction
    ty = ["deposit", "withdraw", "bank charge", "interest"]
    try:
        tmp = Transaction(input("Enter date using the format yyyymmdd: ").lower().strip(),input("Enter transaction type: ").lower().strip(),input("Enter transaction amount: ").lower().strip())
        if tmp.transaction_type not in ty or float(tmp.amount) < 0:
            raise ValueError("not valid")
        list_of_transactions.append(tmp)
    except Exception as e:
        print(e)
    # object and append it to the list of transactions.
    # Display an error message if the transaction type is not valid or amount
    # is negative. Valid transaction types are deposit, withdraw, bank charge
    # and interest
    print ('Add Transaction Function')



def calculate_balance (list_of_transactions):

    """Calculates the current balance"""

    # Start with initializing balance to zero
    balance = 0
    # For each transaction in the list of transactions you will
    for tran in list_of_transactions:
    # add the amount to balance if the transaction type is deposit or interest
        if tran.transaction_type == "deposit" or tran.transaction_type == "interest":
            balance += float(tran.amount)
    # subtract the amount if transaction type is withdraw or bank charge
        else:
            balance -= float(tran.amount)
    # Print the balance on the screen
    print(f"this is your balance:{balance:.2f}")
    print ('Calculate Balance Function')
            
        


def save_data (list_of_transactions):
    """ Saves list of transaction to a file"""
    # Ask user for name of the output file, sort the list of transactions by date
    with open(input("file name: "),"w") as file:
        for i in list_of_transactions:
            file.write(f"{i.date}:{i.transaction_type}:{i.amount:.2f}")
    # and save the data using the following format:
    # date:transaction_type:amount
    # Display a message that data was saved to the output file
    print("data was saved")
    print ('Save Data Function')

main()