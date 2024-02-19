from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # Can be done in one line, but IMO modifying curr AND curr.next simultaneously is asking for trouble
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_
        return prev
