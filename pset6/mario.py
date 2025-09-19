import sys
while True:
    try:
        height = int(input("size: "))
        if height <= 0 or height > 8:
            print("Height must be between 0 and 8.")
        else:
            break
    except ValueError:
        print("Not int")

width = 0
while height != 0:
    width += 1
    height -=1
    for x in range(height):
        print(" ", end="")
    for y in range(width):
        print("#", end="")
    print("  ",end= "")
    for w in range(width):
        print("#",end="")
    print()

