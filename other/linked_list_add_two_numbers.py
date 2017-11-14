#!/usr/bin/env python

"""
Add Two Numbers 
Time complexity : O(max(m,n))
Space complexity : O(max(m,n))
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):        
    result = None
    currentNode = None
    carr = 0 
    while l1 != None or l2 != None:
        val1 = l1.val if l1 != None else 0
        val2 = l2.val if l2 != None else 0    
        if result == None:
            result = ListNode((val1 + val2) % 10) 
            currentNode = result            
        else:            
            currentNode.next = ListNode((val1 + val2 + carr) % 10)             
            currentNode = currentNode.next
        carr = 1 if (val1 + val2 + carr) > 9 else 0
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None
    if carr == 1:
        currentNode.next = ListNode(1)
    return result


nodes1 = ListNode(5)
nodes1.next = ListNode(4)
nodes1.next.next = ListNode(3)

nodes2 = ListNode(5)
nodes2.next = ListNode(6)
nodes2.next.next = ListNode(4)


result = addTwoNumbers(nodes1, nodes2)
while result !=None:
    print(result.val)
    result = result.next


