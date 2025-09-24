# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 9/24/2025

# Description: This is part 1 of lab6 
#given 3 input grades find the avgrage and letter grade then output

# Status: Runs as expected.
import sys
def main():
    grades = check()
    avg = sum(grades)/3
    if 90<= avg <= 100:
        grade = "A"
    elif 80 <= avg <=90:
        grade = "B"
    elif 70<= avg <= 80:
        grade = "C"
    elif 60 <= avg <= 70:
        grade = "D"
    elif avg < 60:
        grade = "F"
    else:
        grade = "Undefined"
    print(f"Average test score is:{avg:.03f}")
    print("This is your grade:",grade)

def check():
    grades = []
    try:
        for _ in range(3):
            temp = eval(input(f"Enter test score{_+1}:"))
            if temp < 0:
                sys.exit("Test score must be numeric and positive")
            grades.append(temp)
    except:
        sys.exit("Test score must be numeric and positive")
    return grades
main()