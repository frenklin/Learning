#!/usr/bin/env python
"""Dijkstra two stack"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import sys
import math


class FindSmallestKthElementIn2Arrays:

    def find(self, arr1, arr2, k):
        print(arr1, arr2, k)

        if k > len(arr1) + len(arr2):
            return "Out of range"

        if len(arr1)==0:
            return arr2[k-1]
        if len(arr2)==0:
            return arr1[k-1]

        if k == len(arr1) + len(arr2):
            if arr1[len(arr1)-1] > arr2[len(arr2)-1]:
                return arr1[len(arr1)-1]
            else:
                return arr2[len(arr2)-1]

        if k == 1:
            if arr1[0] < arr2[0]:
                return arr1[0]
            else:
                return arr2[0]

        # arr1_mid = math.floor(k/2)
        arr2_mid = arr1_mid = math.floor(k/2)

        if len(arr1) < arr1_mid:
            arr1_mid = len(arr1)
            arr2_mid = k - arr1_mid

        if len(arr2) < arr2_mid:
            arr2_mid = len(arr2)
            arr1_mid = k - arr2_mid

        #print(arr1_mid, arr2_mid)
        if arr1[arr1_mid-1] < arr2[arr2_mid-1]:
            # print(['L',arr1[arr1_mid:], arr2[:arr2_mid], k, arr1_mid])
            return self.find(arr1[arr1_mid:], arr2[:arr2_mid], k-arr1_mid)
        elif arr1[arr1_mid-1] > arr2[arr2_mid-1]:
            # print(['R',arr1[:arr1_mid], arr2[arr2_mid:], k, arr2_mid])
            return self.find(arr1[:arr1_mid], arr2[arr2_mid:], k-arr2_mid)
        else:
            return self.find(arr1[1:], arr2, k-1)




#
#['L', [7, 8, 9, 10, 100], [5, 6, 71, 86, 93, 100, 110], 7]
#['L', [10, 100], [5, 6, 71], 4]
#['R', [10], [71], 2]
#= 71
#

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')
    
    t1 = FindSmallestKthElementIn2Arrays()

    arr1 = [0, 1, 3, 3, 4,  6,  6,     7,  8,  9, 10, 100]
    arr2 = [5, 6, 71, 86,93,100,110,   123,150,200,255,3000]
    
    #res = t1.find(arr1, arr2, 13)
    #print("= {}".format(res))
    #res = t1.find(arr1, arr2, 6)
    #print("= {}".format(res))
    #res = t1.find(arr1, arr2, 9)
    #print("= {}".format(res))
    assert(t1.find(arr1, arr2, 1) == 0)
    assert(t1.find(arr1, arr2, 2) == 1)
    assert(t1.find(arr1, arr2, 3) == 3)
    assert(t1.find(arr1, arr2, 4) == 3)
    assert(t1.find(arr1, arr2, 5) == 4)
    assert(t1.find(arr1, arr2, 6) == 5)
    assert(t1.find(arr1, arr2, 7) == 6)
    assert(t1.find(arr1, arr2, 8) == 6)
    assert(t1.find(arr1, arr2, 9) == 6)
    assert(t1.find(arr1, arr2, 10) == 7)
    assert(t1.find(arr1, arr2, 11) == 8)
    assert(t1.find(arr1, arr2, 12) == 9)
    assert(t1.find(arr1, arr2, 13) == 10)
    assert(t1.find(arr1, arr2, 14) == 71)
    assert(t1.find(arr1, arr2, 24) == 3000)
    
