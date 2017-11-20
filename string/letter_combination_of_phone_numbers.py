#!/usr/bin/env python

d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

def letterCombinations(digits):         
    res = [""]
    for i in digits:
        if i in d:
            if i in d:
                t = []
                for c in d[i]:
                    for s in res:                
                        t += [s + str(c)]
                res = t
    return res if digits else []

    
           

print(letterCombinations("2"))

