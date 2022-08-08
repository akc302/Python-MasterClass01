# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Leetcode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l3 = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1
                l1= l1.next
            if l2:
                carry+= l2
                l2 = l2.next
            l3.val = carry % 10
            carry = carry // 10

            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        return head












