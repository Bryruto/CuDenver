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
def part4():
    runs_through = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
    "Mississippi": "United States",
    "Colorado": "United States",
    }

    for k,v in runs_through.items():
        print(f"{k} runs through {v}")
def part5():
    pullers = ["john","sam","kyle","sam"]
    pro = {
        "Brycen":"python",
        "caden":"c",
        "jake":"c++",
        "kylie":"python"
    }

    for p in pullers:
        if p not in pro:
            pro[p] = input("favorite language:")
        else:
            print("already have you favorite language")
    print(set(pro.values()))

def part6():
    brycen = {
        "name":"Brycen Anderson",
        "school":"cudenver",
        "major":"computer science",
    }

    caden = {
        "name":"Caden Anderson",
        "school":"csu",
        "major":"sports medicine",
    }

    kylie = {
        "name":"Kylie Anderson",
        "school":"pikes peak",
        "major":"dentist"
    }

    people = [brycen,caden,kylie]

    for i in people:
        for k,v in i.items():
            print(f"{k}:{v}")
        print()

def part7():
    dog = {
        "species":"dog",
        "owner":"brycen", 
    }

    cat = {
        "species":"cat",
        "owner":"caden", 
    }

    hamster = {
        "species":"hamster",
        "owner":"kylie", 
    }

    pets = [dog, cat, hamster]

    for p in pets:
        for k,v in p.items():
            print(f"{k}:{v}")
        print()
def part10():#skipping part 9 
    my_list =["p" + str(i) for i in range(5)]
    my_dict = {}

    for i in my_list:
        my_dict[i] = []
        for n in range(int(random.randint(1,3))):
            my_dict[i].append(random.randint(1,100))
        print(my_dict[i])
        
def part11():
    """
    Part 11. Make a dictionary called Cities. Use a names of three cities as keys in your dictionary. 
    Create a dictionary of information about each city and include the country that the city is in. 
    It's a proximate population and one fact about the city.
    The keys for each city dictionary should be something like country, population, and fact. 
    Print the names of each city and all the information you have stored about it.
    """ 
    cities = {
        "denver":{
            "country":"USA",
            "population":729019,
            "fact":"There are about 200 named mountain peaks visible from Denver — including 32 that are over 13,000 feet high",
        },
        "colorado springs":{
            "country":"USA",
            "population":494219,
            "fact":"Pikes Peak looms over the city and inspired the song 'America the Beautiful.'",
        },
        "phoenix":{
            "country":"USA",
            "population":1675144,
            "fact":"The area was once irrigated by the ancient Hohokam people who built sophisticated canals that underlie today's city.",
        },
    }

    for city in cities:#key are strings not the dict itself so you need to go into the dict to get the vaules
        for info in cities[city].values():
            print(info)
        
def main():
    names = {}
    #part1(names)
    #part2(names)
    #part3()
    #part4()
    #part5()
    #part6()
    #part7()
    #part10()
    #part11()
main()