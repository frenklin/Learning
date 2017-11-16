#!/usr/bin/env python
""" int palindrome check """


def ispalindrome(x):
    if x < 0:
        return False
    len = 1
    while (x//len) >= 10:        
        len = len * 10        

    while x != 0:            
        left = x // len
        right = x % 10        
        if left!=right:
            return False        
        x =  x % len // 10
        len = len // 100
    return True




print(ispalindrome(131))
print(ispalindrome(1331))
print(ispalindrome(13831))
print(ispalindrome(13841))