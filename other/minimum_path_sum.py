#!/usr/bin/env python

class Solution:

    def minPathSum(self, grid):
        
        rows = len(grid)
        if rows == 0:
            return 0
        
        cols = len(grid[0])
        if cols == 0:
            return 0
        
        res = [[ 0 for i in range(0, cols)] for i in range(0, rows)]

        for col in range(cols, 0, -1):
            for row in range(rows, 0, -1):
                self.grid_sum(res, grid, col, row)
        
        return res[0][0]

    def grid_sum(self, res, grid, col, row):          
        col = col - 1 # to arr index
        row = row - 1                         
        if col == len(grid[0])-1 and row == len(grid)-1:                        
            res[row][col] = grid[row][col]            
        elif col == len(grid[0])-1:                                                                
            res[row][col] = grid[row][col] + res[row+1][col]                  
        elif row == len(grid)-1:                                    
            res[row][col] = grid[row][col] + res[row][col + 1]        
        else:                                   
            res[row][col] = grid[row][col] + min(res[row+1][col], res[row][col+1])
        
        
    #def minPathSum(self, grid):        
    #    if not grid:
    #        return 0
    #    
    #    prev = [float("inf") for i in range(len(grid[0]))]
    #    prev[-1] = 0
    #
    #    for row in grid[::-1]:
    #        current = []
    #        for x in range(len(row))[::-1]:
    #            current.append(min(prev[x], current[-1] if current else float("inf")) + row[x])            
    #        prev = current[::-1]
    #            
    #    return current[-1]



#a = [[1,3,1],
#     [1,5,1],
#     [4,2,1]]

a = [[1,2,5,6,7],[3,2,1,4,5]]

s = Solution()

print(s.minPathSum(a))