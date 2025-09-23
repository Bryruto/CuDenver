def main():
    filename=input()
    with open(filename,"r") as file:
        counter = 0
        for line in file:
            counter +=1
            print(f"this is line {counter}:{line}")       
main()