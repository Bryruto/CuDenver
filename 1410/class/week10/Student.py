class Student:
    #class variables




    def __init__(self, name:str, student_id:int, courses_taken:list,
                 campus_address:str, home_address:str, gpa:float):
        self.name = name
        self.student_id = student_id
        self.courses_taken = courses_taken  # list of course names or codes
        self.campus_address = campus_address
        self.home_address = home_address
        self._gpa = gpa #private__  #protected_ dont use outside class 

    #getter
    def get_gpa(self):
        return self._gpa

    #setter 
    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self._gpa = gpa
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    # ----- Optional helper method -----
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.student_id}")
        print(f"Courses Taken: {', '.join(self.courses_taken)}")
        print(f"Campus Address: {self.campus_address}")
        print(f"Home Address: {self.home_address}")
        print(f"GPA: {self._gpa:.2f}")


# Example usage:
def main():
    students = []
    best = 0 
    holder = 0
    with open("student_data.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) != 6:
                continue  # skip malformed lines
            name, student_id, courses_str, campus_addr, home_addr, gpa_str = parts
            courses = courses_str.split(";")
            gpa = float(gpa_str)
            s = Student(name, student_id, courses, campus_addr, home_addr, gpa)
            students.append(s)

            if gpa > best:
                best = gpa
                holder = s


    # Show first few
    for s in students[:5]:
        s.display_info()
        print("-" * 40)

    print("top student")
    holder.display_info()
    
main()
