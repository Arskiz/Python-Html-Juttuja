import os
import time

tictactoe = [[0,0,0], [0,0,0], [0,0,0]]


currentTicTacToe = ["",
                    "",
                    "",
                    "",
                    ""]

def set_ticTacToe(target): # Line goes from top to bottom so 0 -> 2 
    
    lineRowType = []
    
    line = None
    row = None
    type = None
    
    for letter in target:
        lineRowType.append(letter)
        
    line = int(lineRowType[0])
    row = int(lineRowType[1])
    type = lineRowType[2]
        
        
    print("Rivi:", str(line), "Kohta:", str(row), "Tyyppi:", type)
    time.sleep(2)
    
    if(line in range(1,3) and row in range(1,3)):
        if(type != "x" or type != "o"):
            if line == 1:
                    tictactoe[0][row -1] = charToMatrix(type)
            if line == 2:
                    tictactoe[1][row -1] = charToMatrix(type)
            if line == 3:
                    tictactoe[2][row -1] = charToMatrix(type)
    else:
        clearTerminal()
        print("|-----------------------------------------|")
        print("Väärä Syntaksi! Lue ohje sijainnin antoon!!")
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

    
    
def clearTerminal():
    os.system("cls")

        

def main():
    clearTerminal()
    try:
        print("Hei! Tervetuloa ristinollaan!")
        time.sleep(1)
        global currentTicTacToe
        while True:

            currentTicTacToe[0] = (" " + convertMatrix(tictactoe[0][0]) + " | " + convertMatrix(tictactoe[0][1]) + " | " + convertMatrix(tictactoe[0][2]))

            currentTicTacToe[1] = ("---+---+---")    
    
            currentTicTacToe[2] = (" " + convertMatrix(tictactoe[1][0]) + " | " + convertMatrix(tictactoe[1][1]) + " | " + convertMatrix(tictactoe[1][2]))

            currentTicTacToe[3] = ("---+---+---")   
            
            currentTicTacToe[4] = (" " + convertMatrix(tictactoe[2][0]) + " | " + convertMatrix(tictactoe[2][1]) + " | " + convertMatrix(tictactoe[2][2]))
            
            time.sleep(0.1) # Save cpu usage   
                

            print("-----------------------------")
            for i in currentTicTacToe:
                print(i)
            print("-----------------------------")
                
            time.sleep(0.1)
            print("Sijainti kirjoitetaan tässä muodossa: ESIM: [11x] <--> ensimmäinen kirjain tarkoittaa että ylhäältä alhaalle päin katsottuna ylin rivi, toinen kirjain tarkoittaa horizontaalissa muodossa olevaa 3 eri kohtaa joita voi täyttää. viimeinen eli vaihtoehdot x tai o ovat tyyppi sille että kuka suorittaa siirron, x vai o")
            print("-----------------------------")
            turn = input("Kirjoita sijainti: ")
            
            if(len(turn) != 3):
                print("Opettele Paska! Liian vähän kirjoitit ja ihan päin neekeriä!")
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