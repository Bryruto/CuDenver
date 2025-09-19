sen=input("Text: ")
l = 0# count the letters
w =0#count the words
p = 0#count the sentences
w= len(sen.split()) # count the white space cool but not what i need rn
for char in sen:
    c=char.isalpha()
    if c:
        l+=1
    if char == "." or char=="!" or char=="?":
        p +=1
L = (l/w)*100
S = (p/w)*100
grade =round(0.0588 * L - 0.296 * S - 15.8)
if grade < 1:
    print ("Before Grade 1")
elif grade > 15:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
    # Prompt the user for some text

    # Count the number of letters, words, and sentences in the text

    #Compute the Coleman-Liau index

    #Print the grade level
