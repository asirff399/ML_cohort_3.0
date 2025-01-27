# Revision Task: 6. write a program to store seven fruits in a list entered by the user

fruits = []

for f in range(7):
    fruit = input(f"Enter the name of fruit number {f+1}: ")
    fruits.append(fruit)

print("Your Fruits: ",fruits)