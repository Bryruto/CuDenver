#create a main funtcion
def main():
    #ask for input
    s = input()
    #send s through th convert function
    s= convert(s)
    print(s)
#create a convert function
def convert(s):
    s = s.replace(":)" ,"🙂").replace(":(" ,"🙁")
    return s
#only convert every :) to 🙂 and :( to 🙁
main()


