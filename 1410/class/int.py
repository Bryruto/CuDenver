def main():
    i = int(input("give me the int:"))
    if i > 0:
        numbers = [num+1 for num in range(i)]
        print(numbers)
        print(sum(numbers))
main()