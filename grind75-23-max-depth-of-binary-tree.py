from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.max_depth(root)

    def max_depth(self, root: TreeNode) -> int:
        ld = rd = 0
        if root.left:
            ld = self.maxDepth(root.left)
        if root.right:
            rd = self.maxDepth(root.right)
        return max(ld, rd) + 1
