amount = 50
while True:
    print(f"Amount Due: {amount}")
    coins = int(input("Insert: "))
    if coins == 25 or coins == 10 or coins == 5:
        amount -= coins
    if amount <= 0:
       amount= str(amount).strip().replace('-',"")
       print(f"Change Owed: {amount}")
       break


