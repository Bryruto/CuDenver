from functions import add_to_file,look_at_file
import sys

def main():
    while True:
        try:
            admin= input("ADMIN PASSWORD:").strip()
            
            if admin != "idk":
                sys.exit("you dont have access")

            enter = int(input("VIEW PASSWORDS ENTER 1 | ADDING PASSWORDS ENTER 2:"))

            if enter != 1 and enter != 2:
                raise ValueError
            break
        except:
            print("Not a valid input")
            pass
    

    if enter == 1:
        look_at_file()
        
    else:
        add_to_file()

main()