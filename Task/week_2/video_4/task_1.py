# Week 2 Video 4 Task 1

# a = 1,18  reshape(6,3)
# b = 20,38
# a+b

import numpy as np

a = np.arange(1,19)
b = np.arange(20,38)

def addition(a,b):
    result = a + b
    return result

x = addition(a,b)
print(x)
x = x.reshape(6,3)
print(x.astype(int))