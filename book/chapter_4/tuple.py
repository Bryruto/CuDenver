def main():
    buffet = ("mac and cheese","brownie","steak","sandwitch","apple")

    print("original buffet")
    for food in buffet:
        print(food)

    buffet = ("mac and cheese","brownie","steak","foot","cake")# cant change but you can reassign
    
    print("reassign buffet")
    for food in buffet:
        print(food)
main()