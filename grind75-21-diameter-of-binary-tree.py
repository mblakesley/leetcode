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
        return self.diameter_depth(root)[0]

    def diameter_depth(self, node: Optional[TreeNode]) -> tuple[int, int]:
        if not node:
            return 0, 0
        l_diameter, l_depth = self.diameter_depth(node.left)
        r_diameter, r_depth = self.diameter_depth(node.right)
        return max(l_diameter, r_diameter, l_depth + r_depth), max(l_depth, r_depth) + 1
