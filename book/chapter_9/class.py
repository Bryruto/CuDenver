
class Restaurant:#building a class
    def __init__(self,name,food_type):#constructer
        self.name = name #instance attributes
        self.food_type = food_type

    def describe_restaurant(self):#method// instance method 
        print(f"Name: {self.name}\nfood type: {self.food_type}")# dot notation to use attributes 
    
    def open_restaurant(self):#method// instance method 
        print("we are open")

def part1():
    restaurant = Restaurant("brycen","asian")#creating a instance of a class Restaurant 
    print(restaurant.name)# dot notation on instance to use attributes 
    print(restaurant.food_type)
    restaurant.describe_restaurant()#calling a instance method
    restaurant.open_restaurant()

def part2():
    r1 = Restaurant("taco","mexican")
    r2 = Restaurant("sams","pizza")
    r3 = Restaurant("hey","food type ehheheheheh")

    r1.describe_restaurant()
    r2.describe_restaurant()
    r3.describe_restaurant()

class User:
    def __init__(self,first_name:str,last_name:str,age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}")
        print("-"*40)

    def greet_user(self):
        print(f"Hello {self.first_name}, {self.last_name}")

def part3():
    brycen = User("brycen","anderson",21)
    caden = User("caden","anderson",22)
    kylie = User("kylie","anderson",19)

    users =[brycen,caden,kylie]
    for user in users:
        user.describe_user()
    for user in users:
        user.greet_user()

class NotRestaurant: 
    def __init__(self,name,food_type,number_served = 0):# i set a defualt value so if i dont get a number_served its 0 at start
        self.name = name 
        self.food_type = food_type
        self.number_served = number_served# can also do it like this self.number_served = 0 and then not worry about it in the arguments 

    def set_number_served(self,num:int):
        self.number_served = num

    def increment(self,num:int):
        if num < 0:
            pass
        else:
            self.number_served += num


def part4():
    sams = NotRestaurant("sams","asian")
    print(sams.number_served)

    sams.number_served += 2
    print(sams.number_served)

    sams.set_number_served(23)
    print(sams.number_served)

    sams.increment(23)
    print(sams.number_served)

class NotUser:
    def __init__(self,first_name:str,last_name:str,age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

def part5():
    user = NotUser("user","user",19)

    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()

    print(user.login_attempts)

    user.reset_login_attempts()

    print(user.login_attempts)

class Ice_cream(Restaurant):
    def __init__(self, name, food_type,flavors):
        super().__init__(name, food_type)
        self.flavors = flavors

    def get_flavors(self):
        for f in self.flavors:
            print(f)

def part6():
    ice = Ice_cream("ice","desert",["chocolate","vanilla","banana"])
    ice.get_flavors()

"""class Admin(User):
    def __init__(self,first_name:str,last_name:str,age:int,privileges:list):
        super().__init__(first_name,last_name,age)
        self.privileges = privileges

    def show_privileges(self):
        for p in self.privileges:
            print(p)

def part7():
    brycen = Admin("brycen","Anderson",21,privileges=["delete","add","sub"])
    brycen.show_privileges()
"""
class Admin(User):
    def __init__(self,first_name:str,last_name:str,age:int,privileges=[]):
            super().__init__(first_name,last_name,age)
            self.privileges = Privileges(privileges)

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        for p in self.privileges:
            print(p)

def part8():
    brycen_anderson = Admin("brycen","anderson",20,["add","sub","delete"])
    brycen_anderson.privileges.show_privileges()

class car:
    pass


def main():
    #part1()
    #part2()
    #part3()
    #part4()
    #part5()
    #part6()
    #part7()
    part8()

if __name__ == "__main__":
    main()