#!/usr/bin/env python

# Time O(N*log(k))
# Space O(1)

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def mergeKLists(lists):
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists

def merge2Lists(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next
    if not l1:
        point.next=l2
    else:
        point.next=l1
    return head.next


def getListNodes(i, j):
    head = ListNode(i)
    item = head
    for i in range(i+1, j):
        item.next = ListNode(i)
        item = item.next
    return head


ls = [getListNodes(0,10), getListNodes(11,22), getListNodes(7,21)]


re = mergeKLists(ls)

while not re is None:
    print(re.val)
    re = re.next
