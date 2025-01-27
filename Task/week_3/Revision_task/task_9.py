# Revision Task: 9. write a program to take user input of 8 numbers and count the unique numbers

nums = list(map(int,input("Enter 8 number: ").split()))

unique_nums = set(nums)
unique_cnt = len(unique_nums)

print("Unique numbers: ",unique_nums)
print("Total unique numbers: ",unique_cnt)
