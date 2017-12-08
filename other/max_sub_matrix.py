#!/usr/bin/env python
#           max             min
# max <- matrix[i,j] - matrix[i1,j1] i>i1, j>j1
def maxsub(matrix):
    raise "not implemented"
    n = len(matrix)
    for i in range(n, 0):
        for j in range(n, 0):
            if i+1 > n and j+1 > n:
                n[i][j] = matrix[i][j]
            elif j+1 > n:
                if matrix[i, j] > n [] 
                n[i][j] = matrix[i][j]





# O(n^2)


a = [[1,2,3],
     [4,5,6]
     [7,8,9]]
print(maxsub(a))