#!/usr/bin/env python

class QueueItem:
    def __init__(self, val, count):
        self.val = val
        self.count = count


class Monoqueue:

  
    def __init__(self):
        self.m_deque = []
    
    def push(self, val):
        count = 0        
        while len(self.m_deque)>0 and self.m_deque[-1].val < val:        
            count += self.m_deque[-1].count + 1
            self.m_deque.pop()
        self.m_deque.append(QueueItem(val, count))

    def max(self):
        return self.m_deque[0].val

    def pop(self):        
        if self.m_deque[0].count > 0:        
            self.m_deque[0].count -= 1
            return        
        self.m_deque.pop(0)
        


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        results = []
        mq = Monoqueue()
        k = min(k, len(nums))
        i = 0
        for i in range(len(nums)):
            mq.push(nums[i])
            if i > k - 2:
                results.append(mq.max()) 
                mq.pop()     
        
        return results
        

s = Solution()

print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


print(s.maxSlidingWindow([7,2,4], 2))



'''
queue = []
res = []
for idx, n in enumerate(nums):
    while queue and nums[queue[-1]] < n:
        queue.pop()
    queue.append(idx)
    if queue[0] == (idx-k):
        queue.pop(0)
    if idx >= (k-1):
        res.append(nums[queue[0]])
return res
'''