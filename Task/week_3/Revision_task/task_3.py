# Revision Task: 3. write a python program to find average of 'n' numbers taken from user input

# way 1
# nums = list(map(int,input("Enter your numbers: ").split()))

# average = sum(nums) / len(nums)

# print(average)

# way 2
n = int(input("Enter the size of numbers: "))

nums2 = []

for i in range(n):
    num = float(input(f"Enter the number of index {i+1}: "))
    nums2.append(num)

average2 = sum(nums2) / n

print(average2)