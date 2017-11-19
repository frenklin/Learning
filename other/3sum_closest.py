#!/usr/bin/env python

def threeSumClosest(nums, target):
    nums.sort()
    result = []        
    delta = 2147483647
    i = 0        
    while i<len(nums)-2:
        #if nums[i] > target:
        #    break
        start = i + 1
        end = len(nums) - 1            
        
        while start < end:            
            s = nums[i] + nums[end] + nums[start]
            if delta > abs(s - target):
                result = s #[nums[i], nums[end], nums[start]]
                delta = abs(target - s)
                if delta is 0:
                    return s
            if  s - target > 0:
                while  start < end and nums[end] == nums[end - 1]:
                    end -= 1
                end -= 1
            else:
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                start += 1
        while i<len(nums)-2 and nums[i]==nums[i+1]:
            i += 1            
        i += 1
    return result


print(threeSumClosest([1,1,-1,-1,3], 3)) # 3

#print(threeSumClosest([1,1,1,1], 0)) # 3

