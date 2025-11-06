# Name:  Brycen Anderson

# Class: CSCI 1411-003

# Due Date: 11/05/2025

# Description: This is of lab 11
#the game tic tac toe 

# Status: Runs as expected.
import sys
board = [[ " " for _ in range(3)] for _ in range(3)]



def reset_grid(board:list)->None:
    return [[ " " for _ in range(3)] for _ in range(3)]



def check_row(row:int)->bool:
    """
    Function Name: check_row
    Description: checks for 3 in that row
    Parameter: row
    Returns bool
    """
    x = 0
    o = 0
    for i in range(3):
        if "x" == board[row][i]:
            x +=1 
        elif "o" == board[row][i]:
            o +=1
    if x == 3 or o == 3:
        return True
    return False  



def check_column(column:int)->bool:
    """
    Function Name: check_column
    Description: checks for 3 in that column
    Parameter: column int
    Returns bool
    """
    x = 0
    o = 0
    for i in range(3):
        if 'x' == board[i][column]:
            x += 1
        elif "o" == board[i][column]:
            o +=1
    if x == 3 or o == 3:
        return True
    return False



def check_diagonal(i:int,y:int,d1,d2)->bool:
    """
    Function Name: check_diagonal
    Description: checks for 3 in that diagonal
    Parameter: row and column and d1 d2 list
    Returns bool
    """
    x = 0
    o = 0
    for r, c in d1:
        if board[r][c] == "x":
            x += 1
        elif board[r][c] == "o":
            o += 1
    if x == 3 or o == 3:
        return True

    x = 0
    o = 0
    for r, c in d2:
        if board[r][c] == "x":
            x += 1
        elif board[r][c] == "o":
            o += 1
    if x == 3 or o == 3:
        return True

    return False



def place_entry(cord:str,r:int,c:int)->bool:
    """
    Function Name: place_entry
    Description: adds to the board
    Parameter: str int int
    Returns bool
    """
    if board[r][c] == " ":
        board[r][c] = cord
        return True
    print("That location is already taken")
    return False



def playable()-> bool:
    """
    Function Name: playable
    Description: checks to see if there are any spaces left
    Parameter: None
    Returns bool
    """
    for i in board:
        for e in i:
            if e == " ":
                return True
    return False



def print_grid():
    """
    Function Name: print_grid
    Description: builds the boards after player moves
    Parameter: none 
    Returns none 
    """
    r = 0 
    print("_"*13, end = "\n\n")
    for _ in range(3):
        print(f"| {board[r][0]} | {board[r][1]} | {board[r][2]} |")
        print("_"*13,end = "\n\n")
        r += 1



def valid_input(row:int,column:int):
    """
    Function Name: valid_input
    Description: see if row and column are 1-3 
    Parameter: int int
    Returns bool 
    """
    valid = [i for i in range(1,4,1)]
    if row+1 in valid and column+1 in valid:
        return True 
    return False



def main():
    """
    Function Name: main
    Description: ask for inputs and run game loop
    Parameter: none
    Returns none 
    """
    next_turn = 1
    d1 = [(i,i) for i in range(3)]
    d2 = [(i, 2 - i) for i in range(3)]
    name1 = input("enter player1 name: ")
    name2 = input("enter player2 name: ")
    winner = "Tie"
    while True:
        try:
            if next_turn == 1:
                r_p1,c_p1 = input(f"{name1} enter location to be marked (row, col): ").split(" ")
                r_p1,c_p1 = int(r_p1)-1 ,int(c_p1)-1


                if valid_input(r_p1,c_p1) == False:
                    print("Error: Your row or column number is out of bound")
                    next_turn +=1
                    continue
                else:
                    if place_entry("x",r_p1,c_p1):
                        print_grid()



                if check_row(r_p1) or check_column(c_p1) or check_diagonal(r_p1,c_p1,d1,d2):
                    winner = name1
                    break


                next_turn += 1

            else:
                r_p2,c_p2 = input(f"{name2} enter location to be marked (row, col): ").split(" ")
                r_p2,c_p2 = int(r_p2)-1,int(c_p2)-1


                if valid_input(r_p2,c_p2) == False:
                    print("Error: Your row or column number is out of bound")
                    next_turn -=1
                    continue
                else:
                    if place_entry("o",r_p2,c_p2):
                        print_grid()

                if check_row(r_p2) or check_column(c_p2) or check_diagonal(r_p2,c_p2,d1,d2):
                    winner = name2
                    break

                next_turn -=1


            if not playable():
                break
        except KeyboardInterrupt:
            sys.exit("i dont want to keep you")
            
        except:
            print("real Error: tic tac")
    
    if winner != "Tie":
        print(winner,"You won the game")
    else:
        print(winner)
    
    if input("Do You want to play again (y or n)").lower() == "y":
        global board 
        board = reset_grid(board)
        main()
main()

