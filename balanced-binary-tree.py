from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/balanced-binary-tree/
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.balanced_max_height(root) != -1

    def balanced_max_height(self, node: TreeNode) -> int:
        """if balanced, return max height OF ITSELF, else return -1"""
        l_max_height: int = self.balanced_max_height(node.left) if node.left else 0
        r_max_height: int = self.balanced_max_height(node.right) if node.right else 0
        if l_max_height == -1 or r_max_height == -1 or abs(l_max_height - r_max_height) > 1:
            return -1
        return max(l_max_height, r_max_height) + 1
