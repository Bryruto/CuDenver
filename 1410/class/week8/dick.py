from functions import *
    

def main():
    words_str = ""
    with open("pg2701.txt","r",encoding="utf-8") as file:
        for line in file:
            words_str += line

    clean_txt = clean_str(words_str.lower())
    
    char_count = count_char(clean_txt)

    txt = clean_txt.split()
    word_count = count_word(txt)
    
    char_count = sort(list(char_count.items()))
    word_count = sort(list(word_count.items()))

    print_result(dict(char_count),dict(word_count))

    
    
main()