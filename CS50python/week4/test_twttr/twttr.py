def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    new = ""
    for char in word:
        match char:
            case 'A' | 'E' | 'I' | 'O' | 'U' | 'a' | 'e' | 'i' | 'o' | 'u':
                char = ""
        new += char
    return new


if __name__ == "__main__":
    main()
