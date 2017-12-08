class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cols = len(word1) + 1
        rows = len(word2) + 1

        arr = [[0 for _ in range(cols)] for _ in range(rows)]
        for col in range(len(arr[0])):
            arr[0][col] = col
        
        for row in range(len(arr)):
            arr[row][0] = row

        for row in range(1, rows):
            for col in range(1, cols):
                if word1[col-1] == word2[row-1]:
                    arr[row][col] = arr[row - 1][col - 1]
                else:
                    arr[row][col] = 1 + min(arr[row-1][col], arr[row][col-1], arr[row-1][col-1])
        return arr[rows-1][cols-1]




w1 = "w11"
w2 = "aw21"

s = Solution()
print(s.minDistance(w1, w2))

