# Video 9-10 Task 1: Lists
# Write a program that:

# 1. Creates a list of 5 numbers.
nums = [31,42,13,54,25]

# 2. Adds a new number to the list.
nums.append(66)

# 3. Removes the second number from the list.
nums.remove(42)

# 4. Prints the sum of all numbers in the list.
sum = 0
for i in nums:
    sum+=i

print(sum)