# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low, high = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                return root
