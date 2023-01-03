from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:
    # these traversal methods are hard to understand but,
    # as always with binary trees, only so many things are possible, and this simple & clean logic falls out
    # 70th percentile
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        i = inorder.index(preorder[0])
        node = TreeNode(val=preorder.pop(0))
        node.left = self.buildTree(preorder, inorder[:i])
        node.right = self.buildTree(preorder, inorder[i+1:])
        return node
