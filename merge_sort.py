#!/usr/bin/env python
"""MergeSort algorthms"""
__author__ = "Roman S"
__copyright__ = "Copyleft"


import sys
import math
import queue
import numpy as np



class MergeSort:
    def Sort(self, arr):
        if len(arr) > 1:
            half = math.ceil(len(arr)/2)
            return self._merge(self.Sort(arr[:half]), self.Sort(arr[half:]))
        else:
            return arr

    def _merge(self, ar1, ar2):
        # print(ar1, ar2)
        if len(ar1) == 0:
            return ar2
        if len(ar2) == 0:
            return ar1
        if ar1[0] < ar2[0]:
            return np.append(ar1[0], self._merge(ar1[1:], ar2))
        else:
            return np.append(ar2[0], self._merge(ar1, ar2[1:]))


class IterativeMergeSort(MergeSort):    
    def Sort(self, arr):
        q = queue.Queue(len(arr))
        for i in range(0, len(arr)):
            q.put([arr[i]])
        while q.qsize() > 1:
            q.put(self._merge(q.get(), q.get()))
        return q.get()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')    
    
    t1 = MergeSort()
    t2 = IterativeMergeSort()
    test = [5,7,9,3,21,7,8,9,0,5,4,3,2,1,2,4,6,7,8,9,0]
        
    res = t1.Sort(test)
    res2 = t2.Sort(test)

    print(res)
    print(res2)