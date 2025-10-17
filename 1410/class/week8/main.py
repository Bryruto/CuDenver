from file import *

def main():
    book = read_from("pg2701.txt")
    
    words = book.split(" ")

    word_count = word_counter(words)

    char_count = char_counter(words)


main()