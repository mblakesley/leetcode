# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class Solution:
    # answer simplicity courtesy of Richard
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current_lca: TreeNode = root
        while True:
            if current_lca.val > p.val and current_lca.val > q.val:
                current_lca = current_lca.left
            elif current_lca.val < p.val and current_lca.val < q.val:
                current_lca = current_lca.right
            else:
                return current_lca
