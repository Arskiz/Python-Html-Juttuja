import time
import os

fibo = [0,1]



def fib(n):
    
    global fibo
    a = 0
    b = 1
    
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        fibo.append(c)
        
    os.system('cls')
    print(f"Fibonacci is: {fibo}")


if __name__ == "__main__":
    os.system('cls')

a = int(input("How many fibonacci numbers you'd like to generate?: "))
if a > 0:
    fib(a)
    
    
    

    
