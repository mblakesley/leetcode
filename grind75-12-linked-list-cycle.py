from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional[ListNode] = None


# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    # speed is O(n), memory is O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        node: ListNode = head
        nodes_seen: set = set()
        while node.next:
            if node in nodes_seen:
                return True
            nodes_seen.add(node)
            node = node.next
        return False

    # example of memory-efficient version:
    # speed is O(n^2), but memory is only O(1)
    # plus, we could speed this up using tortoise & hare strategy
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr_node: ListNode = head
        i = 0
        while True:
            # i = 0 -> need to look 1 ahead. i = 1 -> need to look 2 ahead. etc
            future_node: ListNode = curr_node
            for _ in range(i + 1):
                next_node: Optional[ListNode] = future_node.next
                if not next_node:
                    return False
                if next_node == curr_node:
                    return True
                future_node = next_node
            curr_node = curr_node.next
            i += 1
