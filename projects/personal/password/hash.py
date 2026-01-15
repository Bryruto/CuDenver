abc = 26
def my_hash(word):

    

    word_size = len(word)
    hashed = ""

    new = list(word)
    for i in range(word_size-1):
        for j in range((word_size-1)-i):
            tmp = new[j+i]
            new[j+i] = new[(j+1)+i]
            new[(j+1)+i] = tmp
    word = "".join(new).replace(" " , "")

    for index in range(word_size):

        if word[index].isupper():
            num = ord(word[index])+1 - 65
            num += len(word)

            num %= 26
            
            hashed += chr(num + 65)

        elif word[index].islower():
            num = ord(word[index]) - 97
            num += (len(word)//2) 

            num %= 26

            hashed += chr(num + 97)
            
        else:
            hashed += word[index]
        
    return hashed.strip()


def fix(word):
    word_size = len(word)
    hashed = ""

    new = list(word)
    for i in range(word_size-2, -1, -1):
        for j in range((word_size-1)-i-1, -1, -1):
            tmp = new[(j+1)+i]
            new[(j+1)+i] = new[j+i]
            new[j+i] = tmp
    word = "".join(new)


    for index in range(word_size):

        if word[index].isupper():
            num = ord(word[index]) - 65
            num -= len(word)

            num %= 26
            
            hashed += chr(num + 65)

        elif word[index].islower():
            num = ord(word[index]) - 97
            num -= (len(word)//2) 

            num %= 26

            hashed += chr(num + 97)
        
        else:
            hashed += word[index]
    return hashed.strip().replace(" " , "")