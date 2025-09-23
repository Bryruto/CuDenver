import pandas
import csv
def main():
    file = "random_names_10000.csv"
    with open(file,"r") as file:
        for line in file:
            fname,lname,number =line.split(",")
            print(fname)
main()