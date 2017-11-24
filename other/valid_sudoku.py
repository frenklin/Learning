#!/usr/bin/env python


def isValidSudoku(board):
    col_flags = 9*[0]
    inner_sq = 3*[0]
    for i in range(0,9):
        row_flags = 0
        for j in range(0,9):
            if board[i][j]=='.':
                continue

            cell_val = int(board[i][j])-1

            if row_flags >> cell_val & 1 :                
                print('j={} i={} v={} {}'.format(j, i, board[i][j], 'invalid ro'))
                return False                                                

            if col_flags[j] >> cell_val & 1:
                print('j={} i={} v={} {}'.format(j, i, board[i][j], 'invalid col'))
                return False                                

            if inner_sq[j//3] >> cell_val & 1:
                print('j={} i={} v={} {}'.format(j, i, board[i][j], 'invalid sq'))
                return False

            inner_sq[j//3] = inner_sq[j//3] | 1 << cell_val
            row_flags = row_flags | 1 << cell_val
            col_flags[j] = col_flags[j] | 1 << cell_val
            
        if i % 3 == 2:
            inner_sq = 3*[0]

    return True
        



a = [[1,7,3,4,5,6,7,8,9],
     [2,2,3,4,5,6,7,8,9],
     [3,2,3,4,5,6,7,8,9],
     [4,2,3,4,5,6,7,8,9],
     [5,2,3,4,5,6,7,8,9],
     [6,2,3,4,5,6,7,8,9],
     [7,2,3,4,5,6,7,8,9],
     [8,2,3,4,5,6,7,8,9],
     [9,2,3,4,5,6,7,8,9]]

b = [[".",".",".",".","4",".","9",".","."],
     [".",".","2","1",".",".","3",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","3"],
     [".",".",".","2",".",".",".",".","."],
     [".",".",".",".",".","7",".",".","."],
     [".",".",".","6","1",".",".",".","."],
     [".",".","9",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","9","."]]


print(isValidSudoku(a))
print(isValidSudoku(b))



