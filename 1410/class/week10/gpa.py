class Student:
    count = 0
    def __init__(self,name,id=0,courses_taken = [],school_address = "3057Brightmoon dr",gpa = 0.0):
        self.name = name
        Student.count += 1
        self.id = Student.count
        self.courses_taken = courses_taken
        self.school_address = school_address
        self.gpa = gpa 

def main():
    brycen = Student("brycen",["math","other"])
    print(brycen)
main()