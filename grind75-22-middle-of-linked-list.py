from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    # Two pointers
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise
