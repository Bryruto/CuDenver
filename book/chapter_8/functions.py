#already know a lot of this by heart so i ran though this chapter sorry no time today

#import functions 
#this lets you use the functions in that module like this functions.function(arguments)

#from module_name import function_name, as many as you want
# this makes it so you can just use it like it was defind in this module function()

#from module_name import * 
#so you can have the whole module without the dot notation

#import functions as f 
#from module_name import function_name as name 
# the two above are renaming functions or modules 





def part1():
    return "you are learning about functions this chapter"

def part2(title:str)->str:#type hints
    return title + " is my favorite book"

#def part3(word = "") this is a default argument if the user does not give you a word it will be "" 

#def part4(*words) this arbirary number of arguments one to as many as you like makes it a tuple 
#def part4(**words) this is also arbirary number of arguments but its a dict instead of a tuple

#part5(part2(title = "hello")) this is keyword arguments use this to avoid having all arguments in perfect order 

def part6(*toppings:tuple)->None:#type hints
    for i in toppings:
        print(i)

def part7(first_name:str,last_name:str,**user_info:dict)->dict:#all that is passed more just goes into the dict but first and last names needs to be in there
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    return user_info

def main():
    #print(part1())
    #print(part2(input("book:")))#this is positional means order matters 
    #part6("ham","cheese","mustard")
    print(part7(first_name="Brycen",last_name="Anderson",home = "3057 bright moon dr",handed = "right"))
main()