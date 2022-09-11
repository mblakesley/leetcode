from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


# https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    # double-pointer style
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise


    # single-pointer style
    def middleNodeSinglePointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        len_ = 0
        while node:
            len_ += 1
            node = node.next
        i_half = len_ // 2
        node = head
        i = 0
        while i < i_half:
            node = node.next
            i += 1
        return node
