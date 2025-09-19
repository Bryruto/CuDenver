def main():
    while True:
        try:
            fuel = get_fuel()
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    if 99 <= fuel:
        print('F')
    elif 1 >= fuel:
        print('e')
    else:
        print(f"{fuel}%")
def get_fuel():
    fuel = input("Fraction ")#ask for a fraction
    x,y = fuel.split('/')
    x = int(x)
    y = int(y)
    if x>y:
        raise ValueError
    return round((x/y) *100)

main()





