number = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower().strip()

match number:
    case "forty-two"| "forty two" | "42":
        print("yes")
    case _:
        print("no")
