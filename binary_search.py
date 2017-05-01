#!/usr/bin/env python
"""Binary search"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import sys


class BinarySearch:

    def Search(self, arr, key):
        lo = 0
        hi = len(arr)
        while lo <= hi:
            mid = lo + int((hi -lo)/2)
            if key < arr[mid]:
                hi = mid - 1
            elif key > arr[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

class ThreeSum(BinarySearch):
    def SearchThreeNums(self, arr, key):
        res = []
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                ind = self.Search(arr, key - 1 * (arr[i] + arr[j]))
                if ind > -1:
                    res.append([arr[i], arr[j], arr[ind]])
        return res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')

    t1 = BinarySearch()

    arr = [1, 2, 3, 4, 5, 6, 7, 88, 100, 101, 105, 133, 202, 505, 2333, 5000, 7002]
    index = t1.Search(arr, 505)

    print(index)
    print(arr[index])

    t2 = ThreeSum()

    nums = t2.SearchThreeNums(arr, 508)

    print(nums)

