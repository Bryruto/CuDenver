"""
Make a data store -
-global available moves 
-owners of spaces 
-dict mapping so 
-do slices of available moves to make row1 row2 row3
-loop available moves if tuple index 1 if 0 = col1 1 = col2 2 = col3

make variable i used to see if even or odd so we can go back and forth  

loop an unknown number of times till winner or no more moves

    build board
        use data store owners of spaces
        iterate size of board vairable r
            iterate size of board vairable c
                if r % 3 == 0 
                    output _
                if r >= 3 and (c % 3 == )
                    output |
                if (r % 2 == 0) and (c % 3 == 1):
                    if maping[(r,c)]
                        add owners[maping[(r,c)]]
                
                        

    output the board with all marks so far
   
    if even 
        ask for input on a tic-tac-toe board 

        store input in variable called player 1 / player 1 will use x to mark board
    if odd 
        ask for input on tic-tac-toe board 

        store the input in variable called player 2 will use o to mark board 

    check if that that makes 3 in a row 

            loop through 3 row possibilities 

                check to see if the same player owns them

    check if that that makes 3 in a column
            loop through 3 column possibilities 

                check to see if the same player owns them 

    check if that makes 2 In a diagonal
            loop through 2 diagonal possibilities 

                check to see if the same player owns them 

"""
'''
Make a data store -
-global available moves 
-owners of spaces 
-dict mapping so 
-do slices of available moves to make row1 row2 row3
-loop available moves if tuple index 1 if 0 = col1 1 = col2 2 = col3
def is_won(dict):
'''
open_moves = [(r,c) for r in range(3) for c in range(3)]
owners = {}
mapping ={(r,c):open_moves
          for r in range(9) for c in range(9) if (r % 3 == 2 and r >=2) and c % 3 == 1
          }

math = tuple((r,c) for r in range(9) for c in range(9) if (r % 3 == 2 and r >=2) and c % 3 == 1)

print(math)



def main():
    pass
main()