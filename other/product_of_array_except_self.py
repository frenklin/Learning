
#https://leetcode.com/problems/product-of-array-except-self/solution
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        le = len(nums)
        r, l = [0] * le, [0] * le
        l[0], r[le-1] = 1, 1

        for i in range(0, le - 1):
            l[i + 1] = nums[i] * l[i]
            r[le - i - 2] = nums[le - i - 1] * r[le - i - 1]

        return [r[i]*l[i] for i in range(0, le)]

