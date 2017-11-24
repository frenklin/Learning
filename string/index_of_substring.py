#!/usr/bin/env python
# http://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/
# time  O(m+n)
# space O(n)


def getZarr(s):
    n = len(s)   
    L = R = 0
    Z = n*[0]
    for i in range(1, n):                
        if i > R:        
            L = R = i             
            while R < n and s[R-L] == s[R]:
                R+=1
            Z[i] = R-L
            R-=1        
        else:              
            k = i-L 
            if Z[k] < R-i+1:
                 Z[i] = Z[k]            
            else:
                L = i
                while R < n and s[R-L] == s[R]:
                    R+=1
                Z[i] = R-L
                R-=1            
    return Z



def strStr(haystack, needle):        
    concat = needle + "$" + haystack
    l = len(concat)     
    Z = getZarr(concat) 
    
    for i in range(0, l):    
        if Z[i] == len(needle):
            return i - len(needle)
    return -1



print(strStr("mississippi", "issip"))



#"iiiiiiiiiiiiiiiiiiiiiii" - n
#"iiiiiiiiiip"  - m

#  m=n/2        (n^2)/2