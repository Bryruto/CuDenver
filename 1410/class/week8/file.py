import string

def read_from(file:str)->str:
    big_string = ""
    translater = str.maketrans('','',string.punctuation)#makes a maping if punctuation to ''
    with open(file) as f:
        for line in f:#line by line == str by str
            big_string += line.lower() + " "

    big_string.translate(translater)

    return big_string

def word_counter(words:list)->dict:#im here i need to sort the count dict
    word_count = {} #word -> count
    for word in words:
        word.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
    

def char_counter(word:str)->dict:
    char_count = {} #char ->count
    for char in word:
        if char in char_count:
            char_count[word] += 1
        else:
            char_count[word] = 1
    return char_count

def sort_dict(sort_me:dict)->dict:
    result = []
    pairs = list(sort_me.items())

    mid = len(pairs) // 2
    right = pairs[mid:]
    left = pairs[:mid]

    i,j = 0,0

    while i < len(left) and j < len(right):
        

    


