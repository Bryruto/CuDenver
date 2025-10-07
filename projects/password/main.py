from hash import my_hash,fix
import sys
def main():#ask for input from user 
    while True:
        try:
            print(f"""WELLCOME TO KEYMASTER PASSWORDS ENTER 1 | ADDING PASSWORDS ENTER 2:""",end = "")
            enter = int(input())

            if enter != 1 and enter != 2:
                raise ValueError
            break
        except:
            print("Not a valid input")
            pass

    if enter == 1:#if 1 then they want to see the passwords
        print(f"""KEY MASTER ENTER * TO SEE ALL ENTER APP NAME:""", end = "")
        app = input().strip().lower()
        #the app they want the password for

        print(f"""KEY MASTER ENTER ADMIN PASSWORD HERE:""", end = "")
        admin_password = input().strip()

        if app and admin_password == "idk":#make it so you can make more then one admin if you have time 
            with open("passwords.txt", "r") as file:
                for line in file:#update to only give them the app they requested 
                    if not line:
                        sys.exit("the data in the txt file has been altered")
                    tmp_app,tmp_password = ((line.replace("app:","").replace("password:","")).strip()).split(",")
                    if app == "*":
                        print(f"APP:{tmp_app} PASSWORD:{fix(tmp_password)}\n")
                    elif tmp_app.strip() == app.strip():#cant find bug right now this is a fix but there is a bug i think in line 29 where there is white space
                        print(f"APP:{tmp_app} \nPASSWORD:{fix(tmp_password)}")


    else: #if 2 then they want to add to keychain
        print(f"""KEY MASTER ENTER ADMIN PASSWORD HERE:""", end = "")
        admin_password = input().strip()

        print(f"""KEY MASTER ENTER APP NAME:""", end = "")
        app = input().strip()
        #add if the app is in there or not and show what they added

        print(f"""KEY MASTER ENTER PASSWORD TO APP:""", end = "")
        password = input().strip()
        #add a wellcome and found account

        if admin_password =="idk":
            with open("passwords.txt","a") as file:
                adding = f"app:{app} , password:{my_hash(password)} \n"
                file.write(adding)
                print("you added",adding)

main()