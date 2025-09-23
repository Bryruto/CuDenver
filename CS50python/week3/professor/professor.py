import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        isanswer = int(input(f"{x} + {y} = "))
        if answer == isanswer:
            score +=1
        else:
            wrong = True
            attempt = 1
            while wrong == True:
                print("EEE")
                isanswer = int(input(f"{x} + {y} = "))
                if answer == isanswer:
                    score +=1
                    wrong = False
                else:
                    attempt +=1
                    if attempt == 3:
                        print(f"{x} + {y} = {answer}")
                        break
    print(f"Score:{score}")

def get_level():
    while True:
        try:
            level = int(input("Level"))
            if 1 > level or level > 3:
                raise ValueError
            return level
            break
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        i=random.randint(0,9)
    elif level == 2:
        i=random.randint(10,99)
    elif level == 3:
        i=random.randint(100,999)
    return i


if __name__ == "__main__":
    main()

