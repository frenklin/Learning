#!/usr/bin/env python

"""Sliding Window Optimized  
Time: O(n)
Space: O(min(m, n)) map size
"""

def getLongestSubstring(s):        
    map = dict()
    """slide window"""
    j = 0
    i = 0
    maxlen = 0   
    result = "" 
    while j < len(s):        
        if s[j] in map:
            i = max(map.get(s[j]), i)
        if j - i + 1 > maxlen:
            maxlen = j - i + 1
            result = s[i:j+1]
        map[s[j]] = j + 1            
        j = j + 1
    return result



print(getLongestSubstring("abcabcgbb"))