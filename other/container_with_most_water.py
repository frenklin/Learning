#!/usr/bin/env python
""" |_|_|_| - find most water"""

def maxArea(height):
    maxarea = 0
    l = 0
    r = len(height) - 1
    while l < r:
        maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l = l + 1
        else:
            r = r -1
        
    return maxarea



print(maxArea([1,1]))

print(maxArea([2,3,4,5,18,17,6]))