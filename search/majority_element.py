#!/usr/bin/env python


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        cnt = 1
        for item in nums[1:]:
            if cnt == 0:
                cnt += 1
                result = item
            elif result == item:
                cnt += 1
            else:
                cnt -=1
        return result


s = Solution()

print(s.majorityElement([2,3,3,7,7,7,3,3]))
