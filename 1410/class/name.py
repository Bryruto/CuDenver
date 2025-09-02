import sys 

def main():
    counter = eval(input("how many people are you with"))
    for _ in range(counter):
        try:
            name = get_name()
            age = get_age()

            if age >= 21:
                print(f"you can go {name}")

            else:
                print("you cant go",name)
        except:
            print("age is invaild enter a string")

def get_name():
    name = input("enter your name:")
    return name

def get_age():
    age = eval(input("what is your age:"))
    return age
    
main()