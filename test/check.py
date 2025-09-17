from collections import namedtuple

School = namedtuple("School"["name","city","state", "enrollment"])

school_name = input()
city_located = input()
state_located = input()
enrollment_count = int(input())

school = School(school_name, city_located, state_located, enrollment_count)

print(f"School name: {school.name}, City: {school.city}, State: {school.state}, Enrollment: {school.enrollment}")