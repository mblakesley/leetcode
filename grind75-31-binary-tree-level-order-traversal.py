from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        lot = []  # level order traversal
        now_q, next_q = [root], []
        while now_q:
            level = []
            for node in now_q:  # sneaky BFS that only works with the two-list-swap pattern
                if node:
                    level.append(node.val)
                    next_q.extend([node.left, node.right])
            lot.append(level)
            now_q, next_q = next_q, []
        return lot[:-1]  # remove the last level since it'll always be empty
