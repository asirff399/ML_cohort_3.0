# Week 2 Video 2 Task 1

# addition of 2 1D matrix

def addition(a,b):
    result = [0*len(a) for _ in range(len(a))]
    for i in range(len(a)):
        result[i] = a[i] + b[i]
    return result

matrix1 = [34,54,64,24,74]
matrix2 = [94,34,78,23,84]

print(addition(matrix1,matrix2))