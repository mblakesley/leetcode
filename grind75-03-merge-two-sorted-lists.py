from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        if not node1 and not node2:
            return None

        head3 = node3 = ListNode()
        while node1 and node2:
            if node1.val < node2.val:
                node3.val = node1.val
                node1 = node1.next
            else:
                node3.val = node2.val
                node2 = node2.next
            node3.next = ListNode()
            node3 = node3.next

        if not node1:
            node3.val = node2.val
            node3.next = node2.next
        elif not node2:
            node3.val = node1.val
            node3.next = node1.next

        return head3
