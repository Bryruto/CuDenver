def main():
    word = list("brycen")
    new = ""
    for i in word:
        new+=i
    print(new) 

    new = ""
    for i in range(len(word)-1):
        for j in range((len(word)-1)-i):
            tmp = word[j+i]
            word[j+i] = word[(j+1)+i]
            word[(j+1)+i] = tmp
             

    new = ""
    for i in range(len(word)-2, -1, -1):
        for j in range((len(word)-1)-i-1, -1, -1):
            tmp = word[(j+1)+i]
            word[(j+1)+i] = word[j+i]
            word[j+i] = tmp


main()