def main():
    alian_colors = "red"

    if alian_colors != "red":
        print()

    if alian_colors == alian_colors:
        print("You earned 5 points part1")

    #alian part 2
    alian_colors = "green"

    #run the if block 
    if alian_colors == "green":
        print("You earned 5 points part2")

    else:
        print("you earned 10 points part2") 

    #run the else block

    alian_colors = "blue"

    if alian_colors == "green":
        print("You earned 5 points part2")

    else:
        print("you earned 10 points part2") 
    

    #alian part 3 chain
    colors = ["red", "green" ,"blue"]
    for i in colors:
        if i== "green":
            print("you earned 5 points part 3")
        
        elif i == "blue":
            print("you earned 10 points part 3")
        
        else:
            print("you earned 15 points part 3")

    #age part4 all positive ages
    ages = [2,3,10,17,52,70]

    for i in ages:
        if i < 2:
            print("this person is a baby",i)
        elif 2<= i <4:
            print("this person is a toddler",i)
        elif 4 <= i <13:
            print("this person is a kid",i)
        elif 13 <= i <20:
            print("this person is a teenager",i)
        elif 20 <= i < 65:
            print("this person is a adult",i)
        else:
            print("this person is an elder",i)

    #fruits part 5

    fav_fruits = ["banana","apple","kiwi"]

    if "banana" in fav_fruits:
        print("i love bananas")
    if "apple" not in fav_fruits:
        print()
    if "apple" in fav_fruits:
        print("000000 apple 0000")
    if "kiwi" not in fav_fruits:
        print()
    if 2 not in fav_fruits:
        print("2 is not a fruits")


main()