abc = 26
def my_hash(word):

    word_size = len(word)
    hashed = "" 
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

#add a unhash get it working then add more 

def fix(word):

    word_size = len(word)
    hashed = ""
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
    return hashed.strip()