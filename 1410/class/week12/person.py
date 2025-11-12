def main():
    with open(input("file to open: "),"r") as file:
        for line in file:
            try:
                list_person = line.split(",")
                length = len(list_person)
                if length == 5:
                    for p in list_person:
                        print(p.strip(),end = " ")
                    print()
                else:
                    raise ValueError(length)
            except ValueError as e:
                print(e)
                pass
main()