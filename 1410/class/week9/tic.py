import sys 
open_moves = [(r,c) for r in range(3) for c in range(3)]
mapping = {real:easy for real,easy in zip([(r,c) for r in range(1,10,4) for c in range(1,10,4)] , [(r,c) for r in range(3) for c in range(3)])}#i love zip 
owns = {}

#this is bad code but it was fun 
#print(mapping)

o = {"row0":0,"row1":0,"row2":0,
     "col0":0,"col1":0,"col2":0,
     "d1":0,"d2":0
     }

x = {"row0":0,"row1":0,"row2":0,
     "col0":0,"col1":0,"col2":0,
     "d1":0,"d2":0
     }
 
def build_a_board():#there must be a better way no time tho
    for i in range(11):
        for y in range(11):
            if i == 3 or i == 7:
                print("# ", end="")
            elif y == 3 or y == 7:
                print("# ", end="")
            else:
                if (i, y) in mapping:
                    tmp = mapping[(i, y)]
                    if tmp in owns:
                        print(owns[tmp], end=" ")  
                    else:
                        print("  ", end="")                    
                else:
                    print("  ", end="")             
        print()


def is_winner(i:int):#check if winner 
    if i == 0:
        for v in x.values():
            if v == 3:
                return "winner is x"
        
    else:
        for v in o.values():
            if v == 3:
                return "winner is o"
    return ""



def main():
    winner = ""
    i = 0
    print("Tic-Tac-Toe enter 0-2,0-2 ex 2,2 or 2,1 or 1,1")
    while not winner:
        build_a_board()
        if not open_moves:
            sys.exit("no winners")

        if i == 0:
            p1 = input("player 1:")
            if p1 == "stop":#this is for me :\
                break
            s1,s2 = p1.split(",")
            p1 = (int(s1),int(s2))

            if p1 in open_moves:
                owns[p1] = "x"
                open_moves.remove(p1)
                x["row"+str(p1[0])] += 1
                x["col"+str(p1[1])] += 1
                
                if p1[0] == p1[1]:
                    x["d1"] += 1              
                if p1[0] + p1[1] == 2:
                    x["d2"] += 1              

                winner = is_winner(i)
                i += 1
            else:
                print("bad move")#didnt want to do a loop/// its still a loop read to see why 

        else:
            p2 = input("player 2:")
            if p2 == "stop":
                break

            s1,s2 = p2.split(",")
            p2 = (int(s1),int(s2))
            if p2 in open_moves:
                owns[p2] = "o"
                open_moves.remove(p2)
                o["row"+str(p2[0])] +=1
                o["col"+str(p2[1])] += 1

                if p2[0] == p2[1]:
                    o["d1"] += 1
                if p2[0] + p2[1] == 2:
                    o["d2"] += 1

                winner = is_winner(i)
                i-= 1
            else:
                print("bad move ")
    print(winner)
main()