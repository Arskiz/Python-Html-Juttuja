import os
import time

tictactoe = [[0,0,0], [0,0,0], [0,0,0]]

startingUser = "x"
user = startingUser


currentTicTacToe = ["",
                    "",
                    "",
                    "",
                    ""]

def set_ticTacToe(target): # Line goes from top to bottom so 0 -> 2 
    global user
    lineRowType = []
    
    line = None
    row = None
    type = None
    
    for letter in target:
        lineRowType.append(letter)
        
    line = int(lineRowType[0])
    row = int(lineRowType[1])
    type = lineRowType[2]
        
    if type == user and line > 0 < 4 and row > 0 < 4:
        if line == 1:
                tictactoe[0][row -1] = charToMatrix(type)
        if line == 2:
                tictactoe[1][row -1] = charToMatrix(type)
        if line == 3:
                tictactoe[2][row -1] = charToMatrix(type)
        if(user == "x"):
            user = "o"
        elif(user == "o"):
            user = "x"
    else:
        clearTerminal()
        print("|-----------------------------------------|")
        print("Wrong syntax! Read help!")
        print("|-----------------------------------------|")
        time.sleep(1)
        
    
            
            
                
        
def convertMatrix(matrix):
    if matrix == 0:
        return " "
    elif matrix == 1:
        return "x"
    elif matrix == 2:
        return "o"
    
def charToMatrix(char):
    if char ==" ":
        return 0
    if char == "x":
        return 1
    if char == "o":
        return 2

def handleVictory():
    x = charToMatrix("x")
    o = charToMatrix("o")
    
    # horizontal check
    for i in range(3):
        if(tictactoe[i][0] == x):
            if(tictactoe[i][1] == x):
                if(tictactoe[i][2] == x):
                    return("x")
        elif(tictactoe[i][0] == o):
            if(tictactoe[i][1] == o):
                if(tictactoe[i][2] == o):
                    return("o")

    # vertical check
    for i in range(3):
        if(tictactoe[0][i] == x):
            if(tictactoe[1][i] == x):
                if(tictactoe[2][i] == x):
                    return("x")
        elif(tictactoe[0][i] == o):
            if(tictactoe[1][i] == o):
                if(tictactoe[2][i] == o):
                    return("o")

    # diagonal check
    if(tictactoe[0][0] == x and tictactoe[1][1] == x and tictactoe[2][2] == x) or \
       (tictactoe[0][0] == o and tictactoe[1][1] == o and tictactoe[2][2] == o):
        return("x" if tictactoe[0][0] == x else "o")

    if(tictactoe[0][2] == x and tictactoe[1][1] == x and tictactoe[2][0] == x) or \
       (tictactoe[0][2] == o and tictactoe[1][1] == o and tictactoe[2][0] == o):
        return("x" if tictactoe[0][2] == x else "o")
    
            

    
    
def clearTerminal():
    os.system("cls")

        

def main():
    global user
    clearTerminal()
    try:
        print("Hey! Welcome to Tic Tac Toe!")
        time.sleep(1)
        global currentTicTacToe
        while True:

            currentTicTacToe[0] = (" " + convertMatrix(tictactoe[0][0]) + " | " + convertMatrix(tictactoe[0][1]) + " | " + convertMatrix(tictactoe[0][2]))

            currentTicTacToe[1] = ("---+---+---")    
    
            currentTicTacToe[2] = (" " + convertMatrix(tictactoe[1][0]) + " | " + convertMatrix(tictactoe[1][1]) + " | " + convertMatrix(tictactoe[1][2]))

            currentTicTacToe[3] = ("---+---+---")   
            
            currentTicTacToe[4] = (" " + convertMatrix(tictactoe[2][0]) + " | " + convertMatrix(tictactoe[2][1]) + " | " + convertMatrix(tictactoe[2][2]))
            
            time.sleep(0.1) # Save cpu usage   
                
            winner = handleVictory()
            
            if(winner == "x" or winner == "o"):
                print("Winner is:", winner + "!!")
                time.sleep(5)
                break
            
            print("-----------------------------")
            for i in currentTicTacToe:
                print(i)
            print("-----------------------------")
            

            time.sleep(0.1)
            print("The position is written in this form: ex: [11x] <--> the first letter means that the top line as seen from the top to the bottom, the second letter means that there are 3 different positions in the horizontal format that can be filled in. the last one i.e. the options x or o are the type for who performs the move, x or o.")
            print("-----------------------------")
            turn = input(user + ", Write location: ")
            
            if(len(turn) != 3):
                print("You wrote it wrong. Too short or too long.")
                time.sleep(0.4)
            else:
                set_ticTacToe(turn)

            clearTerminal()

    except KeyboardInterrupt:
        clearTerminal()
        print("Interrupted by user!")
        time.sleep(0.5)
        clearTerminal()
        
        
main()