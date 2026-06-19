from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional[ListNode] = None

# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hare = head, head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False
