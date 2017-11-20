#!/usr/bin/env python

def isValid(s):
    d = {"(":")", "{":"}" , "[":"]"}
    st = list()    
    for c in s:
        if c in d:            
            st.append(c)
        elif c in d.values():            
            if len(st)==0 or c != d[st.pop()]:
                return False
        else:
            return False
        
    return True if len(st) == 0 else False


print(isValid("(){}{()}"))

print(isValid("(){}{()}{"))

