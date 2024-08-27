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
        _, is_bal = self.height_balance_check(root)
        return is_bal

    def height_balance_check(self, root: Optional[TreeNode]) -> tuple[int, bool]:
        # returns (max_height, is_balanced)
        if not root:
            return (0, True)
        lh, l_isbal = self.height_balance_check(root.left)
        rh, r_isbal = self.height_balance_check(root.right)
        # a node is only balanced if its children are balanced and it itself is balanced
        return max(lh, rh) + 1, l_isbal and r_isbal and abs(lh - rh) <= 1
