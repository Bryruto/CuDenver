import sys

def main():
    try:
        name = get_name()

        age = get_age()

        print("Hello",name)

        if age >= 21:
            print("you are not eligible ")
        else:
            print("you are not eligible ")
    except ValueError:
        sys.exit("invalid syntax make make sure you use an int for age and string for name")

def get_name():
    name = input("whats your name:")
    return name

def get_age():
    age = int(input("whats your age:"))
    return age

main()