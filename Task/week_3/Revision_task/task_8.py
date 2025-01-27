# Revision Task: 8. write a python program to count the number of zeros in a list, L=[1,0,0,1,0,0,2,0,3,-5,0,0]

lst = list(map(int,input("Enter your list: ").split()))

zero_cnt = 0 
for i in lst:
    if i == 0:
        zero_cnt+=1
print("Total 0 in the list: ",zero_cnt)