# Week 2 Video 2 Task 1

# Way One
def transpose1(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]

# Nested loop
def transpose2(m):
    r = len(m)
    c = len(m[0])
    result = [[0]*r for _ in range(c) ]
    for i in range(r):
        for j in range(c):
            result[j][i] = m[i][j]
    return result
        
matrix = [[1,2,3,4,5],[6,7,8,9,10]]

print(transpose1(matrix))
print(transpose2(matrix))