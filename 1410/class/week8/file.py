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

def sort_dict(sort_me:dict)->dict: #wanted to learn merge sort then i though i would understand it a lot better if i dont do it recusively 
    
    pairs = list(sort_me.items())

    width = 1
    while width < len(pairs):
        for i in range(0,len(pairs),width*2):#start at 0 go to size of array then increment width times 2 
            left = pairs[i:i + width]# get a slice of the array for the left but only first part so i = 0 it gets 0,1 if i = 2 then 2,3 so on till width gets incremented then it takes bigger slices 
            right = pairs[i:i + width * 2]
            
            results = []
            l,r = 0,0 # the index becuase i cant and dont want to mess with the data just the order 
            while r < len(right) and l < len(left):
                if left[l][1] < right[r][1]: #at index r or l in the array then index 1 to compare the values
                    results.append(left[l])
                    l += 1 #this is how i got around deleting 
                else:
                    results.append(right[r])
                    r += 1
            #one of these sould have somes values still in them cant do if else because index error 
            pairs.extend(left[r:])
            pairs.extend(right[r:])
            pairs[i:i + width * 2] = results #slice out the part of the list we that is a little more sorted
        width *= 2 
    return dict(pairs)


#i should have just done it recusively 

    


