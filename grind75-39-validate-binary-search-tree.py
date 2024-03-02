from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst(root, -float('inf'), float('inf'))

    def is_valid_bst(self, node: Optional[TreeNode], v_min: float, v_max: float) -> bool:
        if not node:
            return True
        if not v_min < node.val < v_max:
            return False
        return self.is_valid_bst(node.left, v_min, node.val) and self.is_valid_bst(node.right, node.val, v_max)
        # Note: This long line has a purpose: short-circuit logic. Breaking it up for clarity makes it less efficient.
