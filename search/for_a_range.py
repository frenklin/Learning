#!/usr/bin/env python

def search(nums, target):
    ret = [-1, -1]
    if not nums:
        return ret
    start, end = 0, len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid
    if nums[start] != target:
        return ret
    ret[0] = start
    end = len(nums) - 1
    while start < end:
        mid = (start + end + 1) // 2
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid
    ret[1] = end
    return ret





print(search([1], 1))

a=[4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 9, 9, 10]
print(search(a, 8))


