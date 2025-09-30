def main():
    #usernames part 1 and 2  2 is just check if empty 
    usernames = ["admin","person1","preson2","person3","person4"]
    if usernames:
        for name in usernames:
            if name == "admin":
                print("hello admin would you like to see a status report")
            else:
                print("Hello",name)

    #part 3 user and current users check if name is available
    current = ["admin","person5","preson6","person7","person4"]

    for name in current:
        if name in usernames:
            print("that name is not available")
        else:
            print("name is available")

    #part 3 
    nums = [i+1 for i in range(9)]
    for num in nums:
        if num == 1:
            num =str(num)+"st"
        elif num == 2:
            num = str(num)+"nd"
        elif num == 3:
            num= str(num)+"rd"
        else:
            num = str(num)+"th"
        print(num)

main()