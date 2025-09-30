def main():
    car = "tesla"
    print("i think car == 'Tesla'| it's going to be False")
    print(car == "Tesla")

    print("i think car == 'tesla' | it's going to be True")
    print(car == "tesla")

    two = "three"
    print("i think two != 'two' | is going to be True")
    print(two != "two")

    print("i think two == 'THERE'.lower() | is going to be True")
    print(two == "THREE".lower())

    print("i think two == 'THERE'.lower() and car == 'Tesla'| is going to be False")
    print(two == 'THREE'.lower() and car == 'Tesla')

    print("i think two == 'THERE'.lower() or car == 'Tesla'| is going to be True")
    print(two == 'THREE'.lower() or car == 'Tesla')

    my_list = ["brycen","caden"]
    print("i think 'brycen' in my_list | is going to be True")
    print("brycen" in my_list)

    print("i think 'caden' not in my_list |is going to be False")
    print("caden" not in my_list)

    num = 20 
    print("i think num == 20 | is going to be True")
    print(num == 20)

    print("i think num < 20 | is going to be False")
    print(num < 20)

    print("i think num > 20 | is going to be False")
    print(num > 20)

    print("i think num <= 20 | is going to be True")
    print(num <= 20)
main()