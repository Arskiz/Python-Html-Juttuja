import random
import time
import os

score = 0
used_hints = 0
last_hint_index = 99999
words = ["ihminen", "rupikonna"]
hints = ["Eläin, joka on hyvin älykäs. Alkaa i-kirjaimella ja loppuu n-kirjaimella.", "Eläin jossa on rupia´. Tykkää Vedestä"]

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
    print("Hävisit pelin pisteillä", str(score) + "!")
    print("-------------------------------")
    score = 0
    
def game_win():
    global score
    print("Voitit pelin pisteillä:", str(score) + "!")
    print("-------------------------------")

def main():
    global last_hint_index
    global used_hints
    global hints
    global score
    global words
    max_guesses = 6
    guesses = max_guesses
    if len(words) > 0:
        current_word = pick_word()
        clear_terminal()
        print("Tervetuloa scramble word peliin! Tehtävänäsi on arvata sana joka on obfuskoitu!")
        time.sleep(0.5)
        print("-------------------------------")
        print("Obfuskoitu sana on:", "[" + scramble_word(current_word) + "]")
    else:
        game_win()
        quit()
    try:
        while True:
            print("-------------------------------")
            if(last_hint_index != words.index(current_word)):
                print("Kirjoita 'vihje' saadaksesi vihjeen kyseiseen sanaan jos et tajua.")
            guess = input("Arvauksesi: ")
            
            if(guess != current_word and guess != "vihje"):
                if(guesses > 0):
                    guesses -=1
                    print("-------------------------------")
                    print("Väärä arvaus! Sinulla on", guesses, "yritystä arvata sana enää!")
                else:
                    game_over()
                
            if(guess == current_word):
                print("-------------------------------")
                print("Oikein!!", "Sana oli", current_word + "!")
                received_score = int(1 * (len(current_word) * guesses))
                score += received_score
                print("Pisteitä ansaittu:", str(received_score), "Pisteet:", str(score))
                print("-------------------------------")
                words.remove(current_word)
                last_hint_index = 99999
                time.sleep(1)
                main()
                break
            
            if(guess == "vihje" or guess == "Vihje"):
                index = words.index(current_word)
                used_hints +=1
                last_hint_index = index
                print("-------------------------------")
                print("Vihje:", hints[index])
                print("Vihje DEBUG:", str(index), hints[index], words.index(current_word))
            
            if(len(guess) != len(current_word) and guess != "vihje" and guess != "Vihje"):
                print("JA sinun täytyy arvata sanan mukaisen määrän kirjaimia!!! Ei yli eikä alle!!!")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("Socket closed by user...")
        time.sleep(0.7)
        os.system('cls')
                    
main()