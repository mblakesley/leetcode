from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    # Iterative. Simple & clean.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            prev, curr.next, curr = curr, prev, curr.next  # A bit confusing to read yet also clear
        return prev

    # Recursive. The rare scenario where recursive isn't as nice.
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return tail
