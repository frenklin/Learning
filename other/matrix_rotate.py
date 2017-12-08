#!/usr/bin/env python


def rotate(matrix):
    raise "not implemented yet"
    
    n = len(matrix)
    print(n)
    res = n*[n*[]]
    for col in range(n):
        for row in range(n):
            print(n-row)
            print(col)
            res[n-row][col] = matrix[col][row]
    return res






a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(rotate(a))

# 3 6 9
# 2 5 8
# 1 4 7


#cols
# 0 0 0
# 1 1 1
# 2 2 2

# rows
# 2 1 0
# 2 1 0
# 2 1 0