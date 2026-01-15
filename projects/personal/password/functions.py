from hash import fix,my_hash
import sys


def add_to_file(admin):
    
    amount = int(input("AMOUNT OF APPS:"))

    for _ in range(amount):
        app = input("ENTER APP NAME:").strip()

        password = input("ENTER PASSWORD TO APP:").strip()
        
        with open("passwords.txt","a") as file:
            adding = f"app:{app} , password:{my_hash(password)} \n"
            file.write(adding)

            print("you added",adding)




def look_at_file():
    
    looking_for = input("ENTER * TO SEE ALL ENTER APP NAME:").strip().lower()
        
    if looking_for:
        with open("passwords.txt", "r") as file:
            for line in file:

                if not line:
                    sys.exit("the data in the txt file has been altered")

                tmp_app,tmp_password = ((line.replace("app:","").replace("password:","")).strip()).split(",")

                if looking_for == "*":
                    print(f"APP:{tmp_app} PASSWORD:{fix(tmp_password)}\n")

                elif tmp_app.strip() == looking_for.strip():
                    print(f"APP:{tmp_app} \nPASSWORD:{fix(tmp_password)}")



def delete_from_file(app_name):
    pass#todo


def new_user():
    pass#todo

def sign_in():
    pass#todo



