while True:
    try:
        coins = float(input("coins: "))
    except ValueError:
        print("coins please")
    else:
        break
counter =0
cents = round(coins * 100)
while cents != 0:
    if cents >= 25:
        counter +=1
        cents -=25
    elif cents >=10:
        counter +=1
        cents -=10
    elif cents >=5:
        counter +=1
        cents -=5
    elif cents >=1:
        counter +=1
        cents -=1
print(f"coins:{counter}")



