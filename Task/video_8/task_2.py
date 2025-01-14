# Video 8 Task 2

# Print pattern

# a.
# ****
# ****
# ****
# ****

for i in range(0,4):
    for j in range(0,3):
        print("*",end="")
    print("*")

# b.
# *
# **
# ***
# ****

for i in range(0,4):
    for j in range(i):
        print("*",end="")
    print("*")

# c.
# 1
# 2 2
# 3 3 3 
# 4 4 4 4 

for i in range(0,4):
    for j in range(i):
        print(i+1,end=" ")
    print(i+1)

# d.
# 1
# 1 3
# 1 3 5
# 1 3 5 7

for i in range(1,5):
    x = 1
    for j in range(i):
        print(x,end=" ")
        x+=2
    print()