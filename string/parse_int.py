#!/usr/bin/env python

INT_MAX = 2147483647
INT_MIN = -2147483648

def parse(s):
    sign = 1
    base = 0
    i = 0
    if len(s) is 0:
        return 0
    while s[i] == ' ':
        i = i + 1
    if s[i] == '-' or s[i] == '+':
        sign = -1 if s[i] == '-' else 1
        i= i + 1    

    while i < len(s):        
        if s[i].isnumeric():            
            if (base >  INT_MAX // 10 or (base == INT_MAX // 10 and int(s[i]) > 7)):
                if sign == 1: 
                    return INT_MAX
                else: 
                    return INT_MIN        
            base  = 10 * base + int(s[i])
        else:
            return base * sign
            
        i = i + 1
    return base * sign



print(parse("2147483648"))