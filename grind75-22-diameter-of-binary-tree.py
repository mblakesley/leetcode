from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.measure_branches(root)[1]

    def measure_branches(self, node: Optional[TreeNode]) -> tuple[int, int]:
        """Given tree starting at $node, return [max height, max diameter]"""
        lh = ld = rh = rd = 0
        if node.left:
            lh, ld = self.measure_branches(node.left)
            lh += 1
        if node.right:
            rh, rd = self.measure_branches(node.right)
            rh += 1
        return max(lh, rh), max(ld, rd, lh + rh)
