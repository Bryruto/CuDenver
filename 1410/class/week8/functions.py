import re
marks = [
    ".", ",", "!", "?", ";", ":", "-", "—", "_",
    "(", ")", "[", "]", "{", "}", "'", '"',
    "...", "/", "\\", "|", "@", "#", "$", "%",
    "^", "&", "*", "+", "=", "<", ">", "~", "`"
]

def clean_str(words:str)->str:
    while any(p in words for p in marks):
        for p in marks:
            words = words.replace(p," ")
    return words

def count_char(word:str)->dict:
    char_dict = {}
    word = re.sub(r'[^\w]', '', word) #word = word.replace(" ","") what i did this why is better 
    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def count_word(words:list) -> dict:
    word_dict = {}
    for word in words:
        word = word.strip()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def sort(pairs:list)->list:#this took me the most time 
    if len(pairs) <= 1:
        return pairs
    
    mid = len(pairs) //2
    left = sort(pairs[:mid])
    right = sort(pairs[mid:])

    return merge(left,right)
    

def merge(l:list,r:list)->list:
    merged = []

    while l and r:
        if l[0][1] > r[0][1]:
            merged.append(l[0])
            l.pop(0)
        else:
            merged.append(r[0])
            r.pop(0)
        
    while l:
        merged.append(l[0])
        l.pop(0)

    while r:    
        merged.append(r[0])
        r.pop(0)

    return merged

def print_result(a:dict,b:dict)->None:
    print("word count")
    i = 0
    for key,value in b.items():
        print(f"{value:<7} {key:^10}")
        i += 1
        if i == 10:
            break
    
    print()
    print("character count")
    i = 0
    for key,value in a.items():
        print(f"{value:<7} {key:^10}")
        i += 1
        if i == 10:
            break
