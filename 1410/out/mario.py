def main():
    height = int(input("give me a height:"))
    mario1(height)
    mario2(height)
    mario3(height)
    mario4(height)

def mario1(height:int):
    for i in range(height):
        print("#", end = "")
        for _ in range(i):
            print("#" ,end = '')
        print()

def mario2(height:int):
    width = 0
    while height != 0:
        height-=1
        width +=1
        for _ in range(width):
            print("#",end = "")
        print()

#under this i didnt do
def mario3(height:int):
    for i in range(height):
        print("#" * (i + 1)) #forgot about str * number is str number times 

#aaaaaaaaaaa recursion 
def mario4(height:int,row = 1):
    if row > height:
        return
    print("#" * row)
    mario4(height, row + 1)
        
main()
