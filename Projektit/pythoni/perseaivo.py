import string
import os

def calculate(stuff):
    print("amounts of letters in", stuff + ":", str(len(stuff)))
    character = input("what character?")
    amount = int(input("and how many do you want to generate?"))
    print(character*amount)
    
calculate("((((((((((((((((((((((((((((((((((((((((((((")

