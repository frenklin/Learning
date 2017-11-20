#!/usr/bin/env python

def generateParenthesis(n):
    result = []
    generator(result, n, n, '')
    return result


def generator(result, left, right, s):
    if left==0 and right==0:
        result.append(s)
        return    
    if left>0:
        generator(result, left-1, right, s+'(')    
    if right>0 and right>left:
        generator(result, left, right-1, s+')')
    





print(generateParenthesis(3))