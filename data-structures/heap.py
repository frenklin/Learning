#!/usr/bin/env python
"""Search Binary Heap"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import sys
import numpy as np

class BinaryHeap:
    def __init__(self):
        self.heap = [0]
        self.heapSize = 0

    @classmethod
    def fromlist(self, items: list):        
        instance = self()        
        i = len(items) // 2
        instance.heapSize = len(items)
        instance.heap = [0] + items[:]
        while (i > 0):
            self.percDown(instance, i)
            i = i - 1
        return instance

    def __add__(self, heap):
        if isinstance(heap, BinaryHeap):
            return BinaryHeap.fromlist(list(self.mergelists(heap.heap[1:], self.heap[1:])))
        return NotImplemented

    def mergelists(self, list1, list2):
        if len(list1) is 0:
            return list2
        if len(list2) is 0:
            return list1
        if list1[0] < list2[0]:
            return np.append(list1[0], self.mergelists(list1[1:], list2))
        else:
            return np.append(list2[0], self.mergelists(list1, list2[1:]))


    def percUp(self, i):
        while i // 2 > 0:
            print(self.heap)
            if self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    def percDown(self,i):
        while (i * 2) <= self.heapSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.heapSize:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def pop(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize = self.heapSize - 1
        self.heap.pop()
        self.percDown(1)
        return retval

    def push(self, item):
        self.heap.append(item)
        self.heapSize = self.heapSize + 1
        self.percUp(self.heapSize)

    def peek(self):
        return self.heap[1]



if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')

    bh1 = BinaryHeap.fromlist([9,5,6,2,3,17])    
    bh2 = BinaryHeap.fromlist([10,1,18,9,30,19])    
    bh = bh1 + bh2
    #print(bh1.merge(bh2))
    
    bh.push(11)

    print(bh.peek())
    print(bh.pop())
    print(bh.pop())
    print(bh.pop())
    print(bh.pop())
    print(bh.pop())
    print(bh.pop())
    print(bh.pop())
    print(bh.pop())
    print(bh.pop())