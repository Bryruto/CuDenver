"""
Name:Brycen Anderson
Class: CSCI 1411-003
Due Date:11/12/2025
Status:works as expected 
"""
#Import Student class
from Student import *
def main():
    name = input ('Enter your name: ')
    # Create a student object with 0 credit and 0 quality points
    s1 = Student (name, 0,0)
    # Ask for number of courses and grades
    count = int (input ('Enter number of grades: '))
    # Ask for credit hours and total quality point for each course
    # and add the course using add_grade method in student class.
    for i in range (count):
        credit = float (input('Enter credit hours for course ' + str(i+1) + ': '))
        gp = float (input ('Enter grade points for course ' + str(i+1) + ': '))
        s1.add_grade (gp, credit)
    # Display information include student name, total credit hours, total
    # quality points and gpa
    print ('Student name:', name)
    print ('Total Credit Hours {0:.2f}'.format(s1.getHours()))
    print ('Total Quality Points {0:.2f}'.format(s1.getQPoints()))
    print ('GPA {0:.2f}'.format(s1.gpa()))
main()