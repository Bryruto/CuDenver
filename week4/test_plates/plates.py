def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    times = 0
    for char in s:
        if char.isalpha() == False:
            return False
        times += 1
        if times ==2:
            break

    if len(s) > 6 or len(s) <2:
        return False

    done = False
    run_time = 0
    for char in s:
        run_time +=1
        if char.isnumeric() == True:
            if s[run_time-1] == '0':
                return False
            elif s[run_time-1:-1].isnumeric():
                done = True
                break
        if done == True:
            break

    for p in s:
        if p == '.' or p == '!' or p== '?':
            return False
    return True
if __name__ == "__main__":
    main()
