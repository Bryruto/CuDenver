from functions import add_to_file,look_at_file

def main():
    while True:
        try:
            print(f"ADMIN PASSWORD:", end = "")
            admin= input().strip()

            print(f"VIEW PASSWORDS ENTER 1 | ADDING PASSWORDS ENTER 2:",end = "")
            enter = int(input())

            if enter != 1 and enter != 2:
                raise ValueError
            break
        except:
            print("Not a valid input")
            pass
    

    if enter == 1:
        look_at_file(admin)
        
    else:
        add_to_file(admin)

main()