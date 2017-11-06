#!/usr/bin/env python
"""QuickSort algorithm"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import sys

# 1, log(N), N, NlogN, N*N, N*N*N, 2^N

class QuickSort:

    swap_count = 0

    def QuickSort(self):
        self.arr=[]
        self.swap_count = 0

    def Sort(self, arr):
        self.arr = arr
        self._sort(0, len(arr)-1)
        return self.arr

    def _sort(self, lo, hi):
        if lo < hi:
            p = self._part(lo, hi)
            print("p = {}".format(p))
            self._sort(lo, p - 1)
            self._sort(p + 1, hi)

    def _part(self, lo, hi):
        piv = self.arr[hi]
        i = lo + 1
        for j in range(lo, hi):
            if self.arr[j] <= piv:
                i = i + 1
                print("swap1 i,j = ({}, {})".format(i-1,j))
                (self.arr[i-1], self.arr[j]) = self._swap(self.arr[i-1], self.arr[j])
        print("swap i,j = ({}, {})".format(i,j))
        (self.arr[i], self.arr[hi]) = self._swap(self.arr[i], self.arr[hi])
        return i + 1


    def _swap(self, v1, v2):
        self.swap_count = self.swap_count + 1
        assert(self.swap_count<150)
        print(self.arr, self.swap_count)
        return v2, v1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')

    t1 = QuickSort() 
    #test = [5, 7, 9, 3, 21, 7, 8, 9, 0, 5, 4, 3, 2, 1, 2, 4, 6, 7, 8, 9, 0]
    test = [5, 7, 9, 3, 21]

    res = t1.Sort(test)

    print(res)
    