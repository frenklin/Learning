#!/usr/bin/env python

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def removeNthFromEnd(head, n):    
        item = head
        del_item = None
        while not item is None:
            if n == 0:                
                del_item = del_item.next if not del_item is None else head
            else:
                n-=1
            item = item.next        

        if del_item == None:
            return head.next
        else:                    
            del_item.next = del_item.next.next if not del_item.next is None else None        
        return head
    

head = ListNode(1)
nodes = head
nodes.next = ListNode(2)
#for i in range(1,10):
#    nodes.next = ListNode(i)
#    nodes = nodes.next


head = removeNthFromEnd(head, 2) # [1]

nodes = head
while not nodes is None:
    print(nodes.val)
    nodes = nodes.next

