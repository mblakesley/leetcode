from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    # Recursive - 90th percentile
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list3 = ListNode(list1.val)
        list3.next = self.mergeTwoLists(list1.next, list2)
        return list3
