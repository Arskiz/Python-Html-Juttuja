import random
import time
import os

score = 0
used_hints = 0
last_hint_index = 99999
words = ["human", "ice cream"]
hints = ["Animal, that's very intelligent. Starts with 'h' and ends with 'n'.", "Cream, that's iced up."]
index = 0

def pick_word():
    global words
    choice = random.choice(words)
    return choice

def clear_terminal():
    os.system('cls')

def scramble_word(word):
    letters = []
    scrambled_word = ""
    for letter in word:
        letters.append(letter)
    for i in range(len(word)):
        choice = random.choice(letters)
        scrambled_word += choice
        letters.remove(choice)
    return scrambled_word

def game_over():
    
    global score
    global words
    print("You lost the game with points", str(score) + "!")
    print("-------------------------------")
    score = 0
    
def game_win():
    global score
    print("You won the game with points:", str(score) + "!")
    print("-------------------------------")

def main():
    global last_hint_index
    global used_hints
    global hints
    global score
    global words
    global index
    
    max_guesses = 6
    guesses = max_guesses
    if len(words) > 0:
        current_word = pick_word()
        index = words.index(current_word)
        clear_terminal()
        print("Welcome to Scramble word game! Your task is to guess the obfuscated word!")
        time.sleep(0.5)
        print("-------------------------------")
        print("Obfuscated word is:", "[" + scramble_word(current_word) + "]")
    else:
        game_win()
        quit()
    try:
        while True:
            print("-------------------------------")
            if(last_hint_index != words.index(current_word)):
                print("Write 'hint' to get a hint.")
            guess = input("Your guess: ")
            
            if(guess != current_word and guess != "hint"):
                if(guesses > 0):
                    guesses -=1
                    print("-------------------------------")
                    print("Wrong guess! You have", guesses, "guesses remaining!")
                else:
                    game_over()
                
            if(guess == current_word):
                print("-------------------------------")
                print("Correct!!", "The word was", current_word + "!")
                received_score = int(1 * (len(current_word) * guesses))
                score += received_score
                print("Points gathered:", str(received_score), "Points:", str(score))
                print("-------------------------------")
                hints.remove(hints[index])
                words.remove(current_word)
                last_hint_index = 99999
                time.sleep(1)
                main()
                break
            
            if(guess == "hint" or guess == "Hint"):
                
                used_hints +=1
                last_hint_index = index
                print("-------------------------------")
                print("Hint:", hints[index])
                print("Hint DEBUG:", str(index), hints[index], words.index(current_word))
            
            if(len(guess) != len(current_word) and guess != "hint" and guess != "Hint"):
                print("AND you must guess the amount of letters in the obfuscated word, not over or under!")
                time.sleep(1)
                
    except KeyboardInterrupt:
        clear_terminal()
        print("Socket closed by user...")
        time.sleep(1)
        clear_terminal()
                    
main()