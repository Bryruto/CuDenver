import sys
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        print(" Adieu, adieu, to " ,end = "")
        if len(names) ==1:
            for n in names:
                print(f"{n}", end = " ")
        elif len(names) ==2:
             print(f"{names[0]} and {names[1]}")
        elif len(names) >2:
            size = len(names)
            for n in names:
                print(f"{n},", end = " ")
                if n == names[size-2]:
                    break
            print(f"and {names[size-1]}")
        print()
        sys.exit()

