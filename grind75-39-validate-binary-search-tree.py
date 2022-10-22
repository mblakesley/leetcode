from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    # Iterative, i.e., the preferred way
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_stack: list[tuple] = [(root, None, None)]  # tuples of (node, node min, node max)
        while node_stack:
            node, n_min, n_max = node_stack.pop()  # DFS
            if n_min is not None and node.val <= n_min:
                return False
            if n_max is not None and node.val >= n_max:
                return False

            if node.left:
                node_stack.append((node.left, n_min, node.val))
            if node.right:
                node_stack.append((node.right, node.val, n_max))
        return True


    # Recursive version, which was easier to think thru at first
    def is_valid_bst_recursive(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst(root)

    def is_valid_bst(self, root: Optional[TreeNode], r_min: Optional[int] = None, r_max: Optional[int] = None) -> bool:
        if not root:
            return True
        if r_min is not None and root.val <= r_min:
            return False
        if r_max is not None and root.val >= r_max:
            return False

        left = self.is_valid_bst(root.left, r_min, root.val)
        right = self.is_valid_bst(root.right, root.val, r_max)
        return left and right
