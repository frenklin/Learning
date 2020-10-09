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


def threeSumClosest2(nums: List[int], target: int) -> int:
    nums.sort()
    diff = float('inf')
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(target - s) < abs(diff):
                diff = target - s
            if s < target:
                l += 1
            else:
                r -= 1
        if diff == 0:
            break
    return target - diff


#O(n^2*log(n))
def threeSumClosest2(nums: List[int], target: int) -> int:
    diff = float('inf')
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            complement = target - nums[i] - nums[j]
            hi = bisect_right(nums, complement, j + 1)
            lo = hi - 1
            if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                diff = complement - nums[hi]
            if lo > j and abs(complement - nums[lo]) < abs(diff):
                diff = complement - nums[lo]
        if diff == 0:
            break
    return target - diff
