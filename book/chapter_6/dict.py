import random
def part1(names:dict)->None:
    names["first_name"] = input("first name:")
    names["last_name"] = input("last name:")
    names["city"] = input("city:")

    for k,v in names.items():
        print(k,v)
    names.clear()

def part2(names:dict)->None:
    my_list =["p" + str(i) for i in range(5)]
    for i in my_list:
        names[i] = random.randint(1,100)
    
    for k,v in names.items():
        print(k,v)

def part3():
    quotes = {
            "Alina Wheeler": "Design is intelligence made visible.",
            "Sam Levenson":"Don't watch the clock; do what it does. Keep going.",
            "George Addair":"Everything you've ever wanted is sitting on the other side of fear."
            }

    for k,v in quotes.items():
        print(k,v)

def main():
    names = {}
    part1(names)
    part2(names)
    part3()
main()