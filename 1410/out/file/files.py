import csv
import pandas
def main():
    with open("fileiOData","r") as file:
        print("this is fileiOData")
        for line in file:
            print(line)
    with open("fileiOData2","r") as file:
        print("this is fileiOData2")
        for line in file:
            print(line)
    with open("people.txt","r") as file:
        print("this is people.txt")
        for line in file:
            print(line)

main()