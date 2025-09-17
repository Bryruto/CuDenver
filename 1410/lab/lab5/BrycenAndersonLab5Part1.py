# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 9/17/2025

# Description: This is part 1 of lab 5. 
#ask for frist name and last naem then make a username and email form them

# Status: Runs as expected.
def main():
    frist_name = input("Frist name:").strip().lower()
    last_name = input("Last name:").strip().lower()
    email = (frist_name + "." +last_name+ "@ucdenver.edu").strip()

    user_name = last_name+frist_name[0]

    print(f"username:{user_name}\nemail:{email}")
main()