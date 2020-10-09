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



class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0

        # branchless loop optimization
        while l < r:
            result = max(result, min(height[l], height[r]) * (r - l))
            delta1 = height[l] - height[r]
            delta2 = height[r] - height[l]
            r = r + 1 * ((-delta1 & ~delta1) >> 31) - 1 * abs(((delta1 - 1) & ~delta1) >> 31)
            l = l - 1 * ((-delta2 & ~delta2) >> 31)
        return result

