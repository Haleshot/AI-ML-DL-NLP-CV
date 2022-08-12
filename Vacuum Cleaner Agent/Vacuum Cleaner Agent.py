# Program to check whether a room is clean or not
# Input is randomly generated.

import random
import numpy as np
a, b = input("Enter the rows and columns for Rooms A and B : ").split()
a = int(a)
b = int(b)
c = 0
mat = np.random.randint(2, size = (a, b))
print(mat)

for i in range(a):
    for j in range(b):
        if mat[i][j] == 1:
            print("The Room {}{} is clean, no cleaning required. Moving to the next room.".format(i, j))

        else:
            mat[i][j] == 0
            c += 1 * 1000
            print("The Room {}{} is dirty, the cleaning process starts now...".format(i, j))

print("The Final Price is = ₹", c)

""" 
Program for user input
for i in range(a):
    row = []
    for j in range(b):
        row.append(input())
    mat.append(row)

mat = np.array(mat)
Replace the lines 26 - 33 from the 10th line.
"""