import pandas
import polars as pl

def main():
    file = "random_names_10000.csv"
    pythonic(file)
    #try1(file)

    
def pythonic(file):
    df = pandas.read_csv(file)
    print(df["FirstName"])
    unique = list(set(df["FirstName"]))
    for name in unique:
        print(f"{name}:{list(df["FirstName"]).count(name)}")

    
def try1(file):
    name_count = {}
    with open(file,"r") as file:
        next(file)
        for line in file:
            fname,lname,number =line.split(",")
            if fname in name_count:
                name_count[fname] +=1
            elif fname not in name_count:
                name_count[fname] = 1
        for name in name_count:
            print(f"{name}:{name_count[name]}")
    
main()
