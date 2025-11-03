def part1():
    car = input("what car would you like: ")
    print(f"lets see if we have a {car}")

def part2():
    table = int(input("how many people are in your party: "))
    if table >= 8:
        print("you must wait for a table")
    else:
        print("table is ready")

def part3():
    num = int(input("enter a number:"))

    if num % 10 == 0:
        print(f"{num} is a multiple of 10")
    else:
        print(f"{num} is not a multiple of 10")

def part4():
    prompt = "\nenter a topping"
    prompt += "\nenter quit to stop:"

    topping = ""
    while topping != "quit":
        topping = input(prompt)
        if topping != "quit":
            print("adding "+ topping)

def part5():
    i = 0
    while i < 5:
        age = int(input("what is your age:"))
        if age < 3:
            print("your ticket is free")
        elif 3 < age < 12:
            print("your ticket is $10")
        else:
            print("your ticket is $15")
        i+=1

def part6():#sam thing as 5 done 4 5 6 are all the ways you use a while loop
    i = 0
    while True:
        age = int(input("what is your age:"))
        if age < 3:
            print("your ticket is free")
        elif 3 < age < 12:
            print("your ticket is $10")
        else:
            print("your ticket is $15")
        i +=1
        if i == 3:
            break
def part7():#loop forever infinity
    while True:
        pass

def part8():
    sandwich = ["BLT",
    "Grilled Cheese",
    "Club Sandwich",
    "Reuben",
    "Tuna Melt",
    "Turkey and Swiss",
    "Roast Beef Au Jus",
    "Ham and Cheese",
    "Egg Salad",
    "Chicken Salad",
    "Bánh Mì",]
    made = []
    while sandwich:
        making = sandwich.pop()
        print(f"making {making} sandwich")
        made.append(making)
    
    print()
    while made:
        print(f"made {made.pop()} sandwich")


def part9():
    sandwich = ["BLT",
    "Grilled Cheese",
    "Club Sandwich",
    "Ham and Cheese",
    "Tuna Melt",
    "Turkey and Swiss",
    "Roast Beef Au Jus",
    "Ham and Cheese",
    "Egg Salad",
    "Chicken Salad",
    "Ham and Cheese",]

    made = []
    print("out of Ham and Cheese")
    while "Ham and Cheese" in sandwich:
        sandwich.remove("Ham and Cheese")

    while sandwich:
        making = sandwich.pop()
        print(f"making {making} sandwich")
        made.append(making)
    
    print()
    while made:
        print(f"made {made.pop()} sandwich")

def part10():
    flag = True
    dreams = {}
    while flag == True:
        name = input("what is your name: ")
        dream = input("what is your dream: ")

        ok = input("would you like to take another poll")
        if  ok == "no":
            flag = False

        dreams[name] = dream
    for k,v in dreams.items():
        print(f"{k} : {v}")
        
def main():
    #part1()
    #part2()
    #part3()
    #part4()
    #part5()
    #part6()
    #part7()
    #part8()
    #part9()
    part10()
main()