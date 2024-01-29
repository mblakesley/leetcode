from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/balanced-binary-tree/
class Solution:
    # 90th percentile
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.bal_depth(root)[0]

    def bal_depth(self, node: Optional[TreeNode]) -> tuple[bool, int]:
        if not node:
            return True, 0
        l_bal, l_depth = self.bal_depth(node.left)
        r_bal, r_depth = self.bal_depth(node.right)
        if not l_bal or not r_bal:  # minor short-circuit
            return False, 0
        return abs(l_depth - r_depth) <= 1, max(l_depth, r_depth) + 1
