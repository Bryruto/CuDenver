from file import *

def main():
    book = read_from("pg2701.txt")
    
    words = book.split(" ")

    word_count = word_counter(words)
    word_count = sort_dict(word_count)

    char_count = char_counter(book)
    char_count = char_counter(char_count)


    p = 1
    for key,value in word_count.items():
        print(f"{p}:{key} seen ->{value} Times")
        p += 1

    p = 1
    for key,value in char_count.items():
        print(f"{p}:{key} seen ->{value} Times")
        p += 1
main()