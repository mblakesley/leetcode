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
        vals_by_level = []
        nows = [root] if root else []
        while nows:
            nexts = []
            vals = []
            for now in nows:
                vals.append(now.val)
                if now.left:
                    nexts.append(now.left)
                if now.right:
                    nexts.append(now.right)
            vals_by_level.append(vals)
            nows = nexts
        return vals_by_level
