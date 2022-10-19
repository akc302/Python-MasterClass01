# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    pass


class Solution:
    def __int__(self):
        self.headVal=None

    def addTwoNumbers(self,l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i=len(l1)-1
        j=len(l2)-1
        print(l1[i], l2[j])
        l3=[]
        k=0
        while i>=0 and j>=0:
            l3.append(l1[i]+l2[j])
            i=i-1
            j=j-1
        l3.reverse()

        return l3



a1=Solution()
print(a1.addTwoNumbers( l1 = [2,4,3], l2 = [5,6,4]))





