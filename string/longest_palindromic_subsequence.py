#complexity: 
#space

class Solution(object):

    def longestPalindromeSubseqFaster2(self, s):
        
        d = {}
        
        def f(i ,j):
            if s[i:j] not in d:
                print(s[i:j])
                maxL = 0               
                uniqueChars = set(s[i:j])
                
                for char in uniqueChars:
                    ii, jj = s.find(char, i), s.rfind(char, i, j)
                    
                    if ii==jj:
                        maxL = max(maxL, 1)                        
                    else:                                            
                        maxL = max(maxL, 2 + f(ii+1, jj))
                d[s[i:j]] = maxL
            return d[s[i:j]]            
        
        
        res = f(0, len(s))
        print(res)
        print(d)
        return res



    def longestPalindromeSubseqFaster(self, s):
        d = {}
        def f(s):
            if s not in d:
                maxLength = 0    
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxLength = max(maxLength, 1 if i==j else 2+f(s[i+1:j]))
                d[s] = maxLength
            return d[s]
        res = f(s)
        print(d)
        return res


    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
     
        res = [[ 0 for i in range(0, len(s)+1)] for i in range(0, len(s)+1)]
        
        for diag in range(len(s)):
            for inx in range(len(s)-diag):
                if diag == 0:
                    res[inx][inx+diag] = 1
                else:                    
                    if s[inx] == s[inx+diag]:                        
                        res[inx][inx+diag] = 2 + res[inx+1][inx+diag-1] #if i + 1 <= j - 1 else 2
                    else:                 
                        res[inx][inx+diag] = max(res[inx+1][inx+diag], res[inx][inx+diag-1])
                        
     #   for s in res:
     #       print(s)
     #   print(res[0][-2])
        return  res[0][-2]

s = Solution()


assert(s.longestPalindromeSubseqFaster2('aabaaca') == 5)
assert(s.longestPalindromeSubseqFaster2('bbbabc') == 4)
assert(s.longestPalindromeSubseqFaster2('fabfcdeff') == 5)
assert(s.longestPalindromeSubseqFaster2('fabfcdeff') == 5)

assert(s.longestPalindromeSubseqFaster2('aabbgaa') == 6)
assert(s.longestPalindromeSubseqFaster2('acabbacca') == 8)
assert(s.longestPalindromeSubseqFaster2('aabbaa') == 6)


#print(s.longestPalindromeSubseqFaster('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg'))