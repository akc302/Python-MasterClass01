# Definition for singly-linked list.

from typing import Optional

from Leetcode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur = dummy= ListNode()

        while list1 and list2:
            if  list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        print(dummy)
        return dummy.next








a1 = Solution()
a1.mergeTwoLists([1,2,4],  [1,3,4])