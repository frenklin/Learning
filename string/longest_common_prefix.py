#!/usr/bin/env python

def longestCommonPrefix(strs):
    if len(strs) is 0:
        return ""
    minLen = 1000000
    for s in strs:
        minLen = min(minLen, len(s))
    low = 1
    high = minLen
    while low <= high:
        middle = (low + high) // 2
        if isCommonPrefix(strs, middle):
            low = middle + 1
        else:
            high = middle - 1    
    return strs[0][:(low + high) // 2]

def isCommonPrefix(strs, l):
    str1 = strs[0][:l]        
    for i in range(1, len(strs)):
        if not strs[i].startswith(str1):            
            return False
    return True


print(longestCommonPrefix(["asd","asd123asd", "asdgfhj443", "asdzxcsdrg", "asd123a"]))