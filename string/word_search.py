#!/usr/bin/env python
# bfs is P-complete difficult to parallelize effectively, difficult to solve in limited space.
# compexity O(board_leng*word_len)
# space stack tmp

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def f(row, col, step):
            if step == len(word):
                return True
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or word[step]!=board[row][col]:
                return False
            tmp=board[row][col]
            board[row][col]='##' # 2 chars can't be eq 1 char
            ret=f(row-1, col, step+1) or f(row+1, col, step+1) or f(row, col-1, step+1) or f(row, col+1, step+1)
            board[row][col]=tmp
            return ret

        for col in range(cols):
            for row in range(rows):                
                if f(row, col, 0):
                    return True

        return False
        



board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]

s = Solution()

print(s.exist(board, "ABCCED"))
print(s.exist(board, "SEE"))
print(s.exist(board, "ABCB"))