#!/usr/bin/env python


class SudokuSolver:
    
    def  __init__(self):
        self.row_mask = 9*[0]
        self.col_mask = 9*[0]
        self.area_mask = 9*[0]   
        
    def load_masks(self, board):
        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c]=='.':
                    continue
                
                idx =  int(board[r][c]) - 1                
                area = (r//3) * 3 + c//3
                
                if self.row_mask[r] >> idx & 1 or self.col_mask[c] >> idx & 1 or self.area_mask[area] >> idx & 1:
                    return False
                
                self.row_mask[r] = self.row_mask[r] | 1 << idx
                self.col_mask[c] = self.col_mask[c] | 1 << idx
                self.area_mask[area] = self.area_mask[area] | 1 << idx
                
        return True                
                
    def solveSudoku(self, board):               
        if not self.load_masks(board):
            return None
        
        self.solve(board, 0, 0)

    def solve(self, board, row, col):

        if row >= 9:
            return True        

        if col >= 9:
            return self.solve(board, row+1, 0)        
        
        if board[row][col] != '.':
            return self.solve(board, row, col+1)
        
        area = 0
        for i in range(0, 9):
            area = (row//3) * 3 + col//3

            if self.row_mask[row] >> i  & 1 or self.col_mask[col] >> i & 1 or self.area_mask[area] >> i & 1:
                continue            
            
            board[row][col] = i + 1
            self.row_mask[row] = self.row_mask[row] | 1 << i
            self.col_mask[col] = self.col_mask[col] | 1 << i
            self.area_mask[area] = self.area_mask[area] | 1 << i

            if self.solve(board, row, col+1):
                return True            

            #backtrace
            board[row][col] = '.'
            
            self.row_mask[row] = self.row_mask[row] ^ 1 << i
            self.col_mask[col] = self.col_mask[col] ^ 1 << i
            self.area_mask[area] = self.area_mask[area] ^ 1 << i            
        
        return False
    




b = [[".",".",".",".","4",".","9",".","."],
     [".",".","2","1",".",".","3",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","3"],
     [".",".",".","2",".",".",".",".","."],
     [".",".",".",".",".","7",".",".","."],
     [".",".",".","6","1",".",".",".","."],
     [".",".","9",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","9","."]]


solver = SudokuSolver()

solver.solveSudoku(b)

print(b)