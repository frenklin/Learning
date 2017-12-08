#!/usr/bin/env python
# complexity O(n*log(n)) + O(n)
# space O(n) for result, assume inplace sort

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key = lambda i: i.start)
        
        result = [intervals[0]]
        for current in intervals:            
            if result[-1].end >= current.start:
                result[-1].end = max(result[-1].end, current.end)                
            else:
                result.append(current)
        return result


#[1,6],[8,10],[15,18]
intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]

s = Solution()

r = s.merge(intervals)

for i in r:
    print("{} {}".format(i.start, i.end))