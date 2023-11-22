
def prints(type, text="Log In"):
    paragraph = 0
    title = 1
    
    for i in range(type + 1):
        if i == paragraph:
            print("------------------------")
        elif i == title:
            print("-------["+ text +"]-------")

def main():
    prints(0)
    prints(1)



main()