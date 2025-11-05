board = [[ " " for _ in range(3)] for _ in range(3)]

def reset_grid(board:list)->None:
    board = [[ " " for _ in range(3)] for _ in range(3)]

def check_row(row:int)->bool:
    x = 0
    o = 0
    for i in range(1,4,1):
        if "x" == board[row][i]:
            x +=1 
        elif "o" == board[row][i]:
            o +=1
    if x == 3 or o == 3:
        return True
    return False  
def check_column(column:int)->bool:
    x = 0
    o = 0
    for i in range(1,4,1):
        if 'x' == board[i][column]:
            x += 1
        elif "o" == board[i][column]:
            o +=1
    if x == 3 or o == 3:
        return True
    return False
def check_diagonal(i:int,y:int,d1,d2)->bool:
    x = 0
    o = 0
    for e in d1:
        if "x" == e:
            x += 1
        elif "o" == e:
            x += 1
    if x == 3 or o == 3:
        return True
    
    x = 0
    o = 0 
    for e in d2:
        if "x" == e:
            o += 1
        elif "o" == e:
            o += 1  
    if x == 3 or o == 3:
        return True
    return False

def place_entry(cord:str,r:int,c:int):
    if board[r][c] == " ":
        board[r][c] = cord
        return True
    return False

def playable():
    pass

def main():
    next_turn = 1
    d1 = [(i,i) for i in range(3)]
    d2 = [(i,b) for i,b in zip([i for i in range(1,4,1)],[b for b in range(3,-1,-1)])]
    while True:
        if next_turn == 1:
            r_p1 = input("row:")
            c_p1 = input("column:")
            next_turn += 1
        else:
            r_p2 = input("row:")
            c_p2 = input("column:")
            next_turn -=1

main()

