#lambda is a single expression that returns a value 1 line function
string = """ 

squared = lambda num : num * num 

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(2))

addup = lambda a,b,c : a + b + c

print(addup(1,3,2))
result-> \n

"""
squared = lambda num : num * num 

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(2))

addup = lambda a,b,c : a + b + c

print(addup(1,3,2))


####################################
string = """
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10) #as the x
addTwenty = funcBuilder(20) # as the x 

print(addTen(7))#as the num
print(addTwenty(7))# as the num
result->\n
""" 
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10) #as the x
addTwenty = funcBuilder(20) # as the x 

print(addTen(7))#as the num
print(addTwenty(7))# as the num

#####################################
string = """
numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num * num,numbers)

print(list(squared_nums))
result->\n
    """
numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num * num,numbers)
print(string)
print(list(squared_nums))

#####################################
string = """
lambda num : num % 2 != 0 #odd numbers bool 

odd_nums = filter(lambda num : num % 2 != 0,numbers) 

print(list(odd_nums))
result->\n
    """

lambda num : num % 2 != 0 #odd numbers bool 

odd_nums = filter(lambda num : num % 2 != 0,numbers) 
print(string)
print(list(odd_nums))


######################################
string = """
from functools import reduce 
#reduce will just add everything together

lambda acc, curr: acc + curr

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc,curr: acc + curr, numbers,10)

print(total)

print(sum(numbers,10))
result->\n
"""

from functools import reduce 
#reduce will just add everything together

lambda acc, curr: acc + curr

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc,curr: acc + curr, numbers,10)

print(string)
print(total)

print(sum(numbers,10))

#######################################

names = ["Dave Gray","sara Ito", "john Jacob", "jinglenheimerschmidt"]

char_count = reduce(lambda acc,curr: acc + len(curr),names,0)

string = """
names = ["Dave Gray","sara Ito", "john Jacob", "jinglenheimerschmidt"]

char_count = reduce(lambda acc,curr: acc + len(curr),names,0) """

print(f"{string}\n result")
print(char_count)
























