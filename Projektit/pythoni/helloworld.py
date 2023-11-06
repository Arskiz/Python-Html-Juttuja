import time

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word = []

wordStatus = ""

def printCool(letter):
    global wordStatus
    for i in range(len(abc)):
        if(letter == abc[i - 1]):
            wordStatus.join(letter)
            print(wordStatus)
        else:
            print(wordStatus + abc[i -1])
            
            continue
            

def main(args):
    for letter in args:
       word.append(letter)
       printCool(letter)

main("hello world")