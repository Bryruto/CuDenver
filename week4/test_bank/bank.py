def main():
    word = input("Greeting: ").lower().strip()
    print(value(word))


def value(greeting):
    if "hello" in greeting:
        cash = 0
    elif "h" == greeting[0] or "H" == greeting[0]:
        cash = 20
    else:
        cash = 100
    return f"${cash}"

if __name__ == "__main__":
    main()
