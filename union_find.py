#!/usr/bin/env python
"""WeightedQuickUnion/Union/Quick Find"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import sys
import time
import random
import numpy
import matplotlib.pyplot as plt

STEPS = 500

class QuickFind:    
    def __init__(self, n):
        self.n = n
        self.arr = numpy.arange(n, dtype=int)

    def union(self, a, b):
        if a < self.n and b < self.n:
            aid = self.arr[a]
            self.arr[a] = self.arr[b]
            for i in range(0, self.n):
                if aid == self.arr[i]:
                    self.arr[i] = self.arr[b]
        else:
            print("Overflow Exception")

    def connected(self, a, b):
        if a < self.n and b < self.n:
            return self.arr[a] == self.arr[b]
        else:
            print("Overflow Exception")


class QuickUnion:
    def __init__(self, n):
        self.n = n
        self.arr = numpy.arange(n, dtype=int)

    def root(self, i):
        while i != self.arr[i]:
            i = self.arr[i]
        return i

    def union(self, a, b):
        if a < self.n and b < self.n:
            root_a = self.root(a)
            self.arr[root_a] = self.root(b)
        else:
            print("Overflow Exception")

    def connected(self, a, b):
        if a < self.n and b < self.n:
            return self.root(a) == self.root(b)
        else:
            print("Overflow Exception")


class WeightedQuickUnion:
    def __init__(self, n):
        self.arr_weigths = {}
        self.n = n
        self.arr = numpy.arange(n, dtype=int)

    def root(self, i):
        while i != self.arr[i]:
            i = self.arr[i]
        return i

    def union(self, a, b):
        if a < self.n and b < self.n:
            root_a = self.root(a)
            root_b = self.root(b)
            if self.arr_weigths.get(root_a, 1) < self.arr_weigths.get(root_b, 1):
                self.arr[root_a] = root_b
                self.arr_weigths[root_b] = self.arr_weigths.get(root_a, 1) + self.arr_weigths.get(root_b, 1)
            else:
                self.arr[root_b] = root_a
                self.arr_weigths[root_a] = self.arr_weigths.get(root_b, 1) + self.arr_weigths.get(root_a, 1)
        else:
            print("Overflow Exception")

    def connected(self, a, b):
        if a < self.n and b < self.n:
            return self.root(a) == self.root(b)
        else:
            print("Overflow Exception")


def quick_find_union_test(n):
    test = QuickFind(n)
    for i in range(0, n):
        test.union(i, random.randint(0, n-1))

def quick_union_union_test(n):
    test = QuickUnion(n)
    for i in range(0, n):
        test.union(i, random.randint(0, n-1))

def quick_union_connected_test(n):
    test = QuickUnion(n)
    for i in range(0, n):
        test.connected(i, random.randint(0, n-1))

def weighted_quick_union_union_test(n):
    test = WeightedQuickUnion(n)
    for i in range(0, n):
        test.union(i, random.randint(0, n-1))

def weighted_quick_union_connected_test(n):
    test = WeightedQuickUnion(n)
    for i in range(0, n):
        test.connected(i, random.randint(0, n-1))


def get_calc_time(func, steps):
    """Mesure computation time"""
    start_calc = time.process_time()
    result = []
    for i in range(1, steps):
        func(i)
        result.append(time.process_time()-start_calc)
    return result

def run_and_plot(steps):
    """Run & plot"""
    plot1 = get_calc_time(quick_find_union_test, steps)
    plot2 = get_calc_time(quick_union_union_test, steps)
    plot3 = get_calc_time(quick_union_connected_test, steps)

    plot4 = get_calc_time(weighted_quick_union_union_test, steps)
    plot5 = get_calc_time(weighted_quick_union_connected_test, steps)

    plt.plot(plot1, label="Quick Find Union Time")
    plt.plot(plot2, label="Quick Union Union Time")
    plt.plot(plot3, label="Quick Union Connected Time")
    plt.plot(plot4, label="Weighted Quick Union Union Time")
    plt.plot(plot5, label="Weighted Quick Union Connected Time")

    plt.tight_layout()
    plt.legend()
    plt.show()

def test():
    print('QuickFind')
    test1 = QuickFind(10)
    test1.union(3, 4)
    test1.union(3, 8)
    test1.union(3, 0)
    print(test1.connected(2, 3))
    print(test1.connected(4, 3))
    print(test1.arr)

    print('QuickUnion')
    test2 = QuickUnion(10)
    test2.union(3, 4)
    test2.union(3, 8)
    test2.union(3, 0)
    print(test2.connected(2, 3))
    print(test2.connected(4, 3))
    print(test2.arr)

    print('WeightedQuickUnion')
    test3 = WeightedQuickUnion(10)
    test3.union(3, 4)
    test3.union(3, 8)
    test3.union(3, 0)
    print(test3.connected(2, 3))
    print(test3.connected(4, 3))
    print(test3.arr)
    print(test3.arr_weigths)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')

    run_and_plot(STEPS)
    