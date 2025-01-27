# Revision Task: 2. write a python program to find remainder when a number 'x' taken from user input is divided by another number 'y' which is also taken from user input

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

def findRemainder(a,b):
    ans = a % b
    print("The reminder is",ans)

findRemainder(x,y)