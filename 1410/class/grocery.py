def main():
    grocery_list = []

    item = input("what item do you want to add to the list:")

    while item:
        grocery_list.append(item)
        item = input("next item")
    
    for i in range(len(grocery_list)):
        print(f"{1+i}:{grocery_list[i]}")

main()