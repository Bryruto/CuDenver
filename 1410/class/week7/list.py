def main():

    names = []
    while True:
        name = input("enter stop to stop name: ").lower()
        if name == "stop":
            break
        names.append(name)
    try1(names)


def try1(names):
    count = 0
    new_list = []
    
    for n in reversed(names):
        print(n)
   
    for n in reversed(names):
        new_list.append(n[::-1])
        for _ in n:
            count+=1

    print("count is:",count)
    for n in new_list:
        print(n) 

main()