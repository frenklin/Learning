#!/usr/bin/env python

def search(nums, target):
    left, right=0, len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if target==nums[mid]:
            return mid
        if nums[mid]>=nums[left]:
            if target>=nums[left] and target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        if nums[mid]<nums[right]:
            if target>nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    return -1





a=[4, 5, 6, 7, 0, 1, 2]


print(search(a, 1))

print(search([1], 2))
