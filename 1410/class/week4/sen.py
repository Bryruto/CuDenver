def main():
    sen = input("give me a sentence 1000 chars or less:")
    print(f"characters in your input:{len(sen)}")

    counter = 0
    word = 0
    for i in sen:
        if i.isupper():
            counter +=1
        if i == " ":
            word +=1

    print(f"words:{word} caps:{counter} char:{len(sen)}")
main()