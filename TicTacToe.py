import sys

def cls():
    print ("\n" * 100)
    
def PrintBoard():
    cls()
    global gameboard
    print(gameboard[0][0],"|",gameboard[0][1],"|",gameboard[0][2])
    print("----------")
    print(gameboard[1][0],"|",gameboard[1][1],"|",gameboard[1][2])
    print("----------")
    print(gameboard[2][0],"|",gameboard[2][1],"|",gameboard[2][2])
                    
def AskPlayerMove(Player,p):
    Move = int(input("%s please type your move:" %Player))
    MakeMove(p,Move)

def MakeMove(P,M):
    global gameboard
    global Turn
    if P == 1:
        if M == 1:
            gameboard[2][0] = "X"
            Turn = 2
        elif M == 2:
            gameboard[2][1] = "X"
            Turn = 2
        elif M == 3:
            gameboard[2][2] = "X"
            Turn = 2
        elif M == 4:
            gameboard[1][0] = "X"
            Turn = 2
        elif M == 5:
            gameboard[1][1] = "X"
            Turn = 2
        elif M == 6:
            gameboard[1][2] = "X"
            Turn = 2
        elif M == 7:
            gameboard[0][0] = "X"
            Turn = 2
        elif M == 8:
            gameboard[0][1] = "X"
            Turn = 2
        elif M == 9:
            gameboard[0][2] = "X"
            Turn = 2
    if P == 2:
        if M == 1:
            gameboard[2][0] = "O"
            Turn = 1
        elif M == 2:
            gameboard[2][1] = "O"
            Turn = 1
        elif M == 3:
            gameboard[2][2] = "O"
            Turn = 1
        elif M == 4:
            gameboard[1][0] = "O"
            Turn = 1
        elif M == 5:
            gameboard[1][1] = "O"
            Turn = 1
        elif M == 6:
            gameboard[1][2] = "O"
            Turn = 1
        elif M == 7:
            gameboard[0][0] = "O"
            Turn = 1
        elif M == 8:
            gameboard[0][1] = "O"
            Turn = 1
        elif M == 9:
            gameboard[0][2] = "O"
            Turn = 1
    CheckWin()

def CheckWin():
    global Turn
    if (gameboard[0][0] == gameboard[0][1] == gameboard[0][2]):
        if gameboard[0][0] == "X":
            Declare(PlayerOne)
        elif gameboard[0][0] == "O":
            Declare(PlayerTwo)
    if (gameboard[1][0] == gameboard[1][1] == gameboard[1][2]):
        if gameboard[1][0] == "X":
            Declare(PlayerOne)
        elif gameboard[1][0] == "O":
            Declare(PlayerTwo)
    if (gameboard[2][0] == gameboard[2][1] == gameboard[2][2]):
        if gameboard[2][0] == "X":
            Declare(PlayerOne)
        elif gameboard[2][0] == "O":
            Declare(PlayerTwo)
    if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2]):
        if gameboard[0][0] == "X":
            Declare(PlayerOne)
        elif gameboard[0][0] == "O":
            Declare(PlayerTwo)
    if (gameboard[2][0] == gameboard[1][1] == gameboard[0][2]):
        if gameboard[2][0] == "X":
            Declare(PlayerOne)
        elif gameboard[2][0] == "O":
            Declare(PlayerTwo)
    if (gameboard[0][0] == gameboard[1][0] == gameboard[2][0]):
        if gameboard[0][0] == "X":
            Declare(PlayerOne)
        elif gameboard[0][0] == "O":
            Declare(PlayerTwo)
    if (gameboard[0][1] == gameboard[1][1] == gameboard[2][1]):
        if gameboard[0][1] == "X":
            Declare(PlayerOne)
        elif gameboard[0][1] == "O":
            Declare(PlayerTwo)
    if (gameboard[0][2] == gameboard[1][2] == gameboard[2][2]):
        if gameboard[0][2] == "X":
            Declare(PlayerOne)
        elif gameboard[0][2] == "O":
            Declare(PlayerTwo)
    PrintBoard()
    if Turn == 1:
        AskPlayerMove(PlayerOne,Turn)
    elif Turn == 2:
        AskPlayerMove(PlayerTwo,Turn)
        
def Declare(p):
    print("AND THE WINNER IS:.........",p)
    sys.exit()

gameboard = [["-","-","-"],["-","-","-"],["-","-","-"]]
PlayerOne = input("Please type Name for player that will use X: ")
PlayerTwo = input("Please type Name for player that will use O: ")
Turn = 1
PrintBoard()
AskPlayerMove(PlayerOne,Turn)


             
