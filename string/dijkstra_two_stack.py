#!/usr/bin/env python
"""Dijkstra two stack"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import sys

class DijkstraTwoStackCacl:

    def cacl(self, arr):
        values = []
        operators = []
        for i in range(0, len(arr)):
            if str.isdecimal(arr[i]) or str.isnumeric(arr[i]):
                values.append(float(arr[i]))
            elif arr[i] in ['+', '-', '*', '/']:
                operators.append(arr[i])
            elif arr[i] == ')':
                values.append(self._doCalc(values, operators))
            elif arr[i] in ['(', ' ']:
                pass
            else:
                print('Error: unknown item {}'.format(arr[i]))
        return values.pop()

    def _doCalc(self, values, operators):
        while len(operators) > 0:
            values.append(self._doOperation(values.pop(), values.pop(), operators.pop()))
        return values.pop()


    def _doOperation(self, val1, val2, operation):
        print("{} {} {}".format(val2, operation, val1))
        if operation == '+':
            return val2 + val1
        elif operation == '-':
            return val2 - val1
        elif operation == '*':
            return val2 * val1
        elif operation == '/':
            return val2/val1
        else:
            print('Unknown operation {}'.format(operation))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('Nope args')

    t1 = DijkstraTwoStackCacl()

    res = t1.cacl('( 1 + ( 2 * 128 ) - ( 77 - 13 ) )'.split(' '))

    print(res)
