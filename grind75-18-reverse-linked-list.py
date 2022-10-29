from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    # constructive version
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_prev = None
        while head:
            rev_head = ListNode(val=head.val, next=rev_prev)
            head = head.next
            rev_prev = rev_head
        return rev_prev
