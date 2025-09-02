height = int(input("height:"))
width = 0
while height != 0:
    width += 1
    height -=1
    for y in range(width):
        print("#", end="")
    print()


