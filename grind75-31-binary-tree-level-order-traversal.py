from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    # Time complexity: O(n)
    # Aux space complexity: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        next_ = [root] if root else []
        node_vals: list[list[int]] = []
        while next_:
            curr, next_ = next_, []
            node_row = []
            for node in curr:
                if node:
                    node_row.append(node.val)
                    if node.left:
                        next_.append(node.left)
                    if node.right:
                        next_.append(node.right)
            node_vals.append(node_row)
        return node_vals
