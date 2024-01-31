from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional[ListNode] = None


# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    # O(n) time, O(1) space using classic hare & tortoise strategy
    # 80th percentile
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hair = head, head
        while hair and hair.next:
            tortoise = tortoise.next
            hair = hair.next.next
            if tortoise == hair:
                return True
        return False
