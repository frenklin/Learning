# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_l1 = l1
        current_l2 = l2
        v = l1.val + l2.val
        root_result = ListNode(v % 10)
        carry = v // 10
        current_result = root_result
        while current_l1.next or current_l2.next:
            v1 = 0
            v2 = 0
            if current_l1.next:
                current_l1 = current_l1.next
                v1 = current_l1.val
            if current_l2.next:
                current_l2 = current_l2.next
                v2 = current_l2.val
            v = v1 + v2 + carry
            current_result.next = ListNode(v % 10)
            current_result = current_result.next
            carry = v  // 10
        if carry == 1:
            current_result.next = ListNode(carry)
        return root_result


