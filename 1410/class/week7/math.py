def main():
    num = eval(input("num:"))

    for n in range(num):
        for i in range(num):
            print(f"{n+1} * {i+1} = {(n+1) * (i+1)}")
    

main()