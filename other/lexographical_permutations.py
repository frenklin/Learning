#!/usr/bin/env python

import itertools

class PermutationsGenerator:

    def __init__(self, n):
        self.n = n
        self.items = None

    def __iter__(self):
        return self

    def fill(self):
        self.items = [i for i in range(1, self.n + 1)]

    def __next__(self):
        if not self.items:
            self.fill()
            return self.items

        if len(self.items) < 2:
            raise StopIteration

        dec = len(self.items) - 2

        while dec >= 0 and self.items[dec] > self.items[dec + 1]:
            if dec == 0:
                raise StopIteration
            dec -= 1

        larger = len(self.items) - 1
        while self.items[larger] < self.items[dec]:
            larger -=1 
        
        self.items[larger] += self.items[dec]
        self.items[dec] = self.items[larger] - self.items[dec]
        self.items[larger] -= self.items[dec]

        self.items = self.items[:(dec+1)] + self.items[(dec+1):][::-1]

        return self.items



gen = PermutationsGenerator(4)


for i in gen:
    print(i)

# hello cheating itertools )
#print(list(itertools.permutations([1,2,3,4])))