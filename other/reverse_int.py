#!/usr/bin/env python

"""Reverse Integer"""


def reverse(x):    
        result=0
        sign= 1 if x > 0 else -1                
        x = x * sign        
        while x > 0:
            result = result*10 + x % 10
            x = x // 10
        if result > 5: #2147483647: #32 signed int               
            return 0
        return sign*result

print("{} == 321".format(reverse(1534236469)))
print("{} == -321".format(reverse(-123)))
print("{} == 21".format(reverse(120)))

