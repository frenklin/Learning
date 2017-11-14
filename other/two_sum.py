#!/usr/bin/env python

"""
One-pass Hash Table
Time complexity : O(n)
Space complexity : O(n)
hash table lookup O(1)
"""



def twoSum(nums, sum):
    items = dict()
    for i in range(len(nums)):                 
        look = sum - nums[i]            
        if look in items and items[look] != i:
            return (items[look], i)
        items[nums[i]] = i
        
        
print(twoSum((1,3,4,5), 7))