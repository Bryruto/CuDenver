def main():
    foods= ["bacon","chicken","turkey","noodles","potstickers","wings","sadwitch","bmt","salad"]

    middle = int(len(foods)/2-1) #because if you / any number it is now a float you but you cant use a float as an index 

    print(f"the first items in the list are {foods[ :3]}")#first 3 items
    print(f"the 3 items in the middle are {foods[middle:middle+3]}")#middle items
    print(f"the last 3 items in the list are {foods[ -3: ]}")#last items 

    pizzas = ["cheese","pepperoni","meat lovers"]

    for pie in pizzas:
        print(f" I love {pie} pizza : you can do it this way becuase python is cool -> for pie in pizzas\n")

    for i in range(len(pizzas)):
        print(f" I like {pizzas[i]} pizza : i did this with index on the list -> for i in range(len(pizzas))\n")

    print("these are my top 3 pizzas\n")

    friend_pie = pizzas[:] #this is a copy you cant just say = becuase then they become the same thing 

    same = pizzas #if i  do anything to one the other will change to

    pizzas.append("new")

    friend_pie.append("not on the other list")

    print("my pizzas are")
    for i in range(len(pizzas)):
        print(pizzas[i],end =",")

    print("if i just use same = pizzas")
    for i in range(len(same)):
        print(same[i],end =",")

    print("my friend pizzas are")
    for i in range(len(friend_pie)):
        print(friend_pie[i],end =",")

main()
