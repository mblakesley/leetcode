from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    # Recursive version. This is the first time I really learned the value of recursion over iteration!
    # Time complexity: O(n)
    # Space complexity: O(n)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2  # Cute way to handle multiple scenarios

    # Iterative version, for comparison. It sucks. It has to straddle 2 layers as it iterates.
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
