# Video 6 Task 1 

# Find The Largest One
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

if x>y and x>z:
    print("x is largest")
elif y>x and y>z:
    print("y is largest")
else:
    print("z is largest")