import string

def read_from(file:str)->str:
    big_string = ""
    translater = str.maketrans('','',string.punctuation)#makes a maping if punctuation to ''
    with open(file) as f:
        for line in f:#line by line == str by str
            big_string += line.lower() + " "

    big_string.translate(translater)

    return big_string

def word_counter(words:list)->dict:
    word_count = {} #word -> count
    for word in words:
        word.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    

def char_counter(word:str)->dict:
    char_count = {} #char ->count
    for char in word:
        if char in char_count:
            char_count[word] += 1
        else:
            char_count[word] = 1

def sort_dict(sort_me:dict)->dict:
    mid = len(sort_me) //2
    left = sort_me[:mid] 
    right = sort_me[mid:]

    #left side
    l_tmp = len(left)
    while l_tmp > 1:
        pass
    
    #right side
    r_tmp = len(right)
    while r_tmp > 1:
        pass

    




def main():
    book = read_from("pg2701.txt")
    words = book.split(" ")
    word_count = word_counter(words)
    


main()

