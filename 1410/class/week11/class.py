class Student:
#class variables
    Student_count = 0

    def __init__(self, name:str, gpa:float):
        self.name = name
        Student.Student_count +=1
        self.id= self.Student_count
        self.gpa = gpa #private__ #protected_ dont use outside class

#getter
def get_gpa(self):
    return self.gpa
#setter
def set_gpa(self, gpa):
    if 0.0 <= gpa <= 4.0:
        self.gpa = gpa
    else:
        raise ValueError("GPA must be between 0.0 and 4.0")

    

def main():
    student_list = []
    while True:
        try:
            new = Student(input("name:"),input("age:"))
            student_list.append(new)
            if input("do you want to do one more:") != "yes":
                break
        except:
            print("try one more time")
    for s in student_list:
        print(f"Name: {s.name}\nGPA: {s.gpa}\nid: {s.id}")
        print("_"*20)
    print(f"count:{Student.Student_count}")
    
main()