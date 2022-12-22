from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/binary-tree-right-side-view/
class Solution:
    # 85th percentile
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        right_side = []
        curr_lvl, next_lvl = [root], []
        while curr_lvl:
            right_side += [curr_lvl[0].val]  # curr_lvl is always ordered right node to left node
            for node in curr_lvl:
                next_lvl += [node.right] if node.right else []
                next_lvl += [node.left] if node.left else []
            curr_lvl, next_lvl = next_lvl, []
        return right_side
