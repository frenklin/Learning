#!/usr/bin/env python


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []        
        res1, res2, cnt1, cnt2 = None, None, 0, 0                
        for n in nums:                    
            if n == res1:
                cnt1 += 1                
            elif n == res2:
                cnt2 += 1
            elif cnt1 == 0:
                res1, cnt1 = n, 1
            elif cnt2 == 0:
                res2, cnt2 = n, 1                
            else:
                cnt1 -= 1
                cnt2 -= 1                    
        
        return [i for i in (res1, res2) if nums.count(i) > len(nums) // 3]



s = Solution()
print(s.majorityElement([1,2,3,3,4]))