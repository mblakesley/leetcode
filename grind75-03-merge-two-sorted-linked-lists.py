from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    # Recursive - recursion is powerful here b/c we can move forward, fiddle w/nodes, then return & assign the result
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2  # sneaky way to handle multiple scenarios

    # Iterative - For comparison. We have to straddle a couple layers as we iterate.
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        start = list1
        while list1.next and list2:
            if list1.next.val > list2.val:
                list1.next, list2 = list2, list1.next
            list1, list1.next = list1.next, list1.next.next
        list1.next = list1.next or list2
        return start
