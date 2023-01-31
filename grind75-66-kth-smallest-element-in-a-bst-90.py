from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class Solution:
    # 90th percentile - traversal short-circuits & we only store val of interest
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kth_smallest(root, k)[0]

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> tuple:  # (val, k)
        if not root:
            return None, k

        val, k = self.kth_smallest(root.left, k)
        if val is not None:
            return val, k

        # important note: $k is only modified for each root.val. this means parents need to accept children's $k's.
        k -= 1
        if not k:
            return root.val, k

        return self.kth_smallest(root.right, k)


    # 60th percentile - slower but dead simple; has a bit of elegance in its own way
    def slow_kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.get_vals(root)[k - 1]

    def get_vals(self, root: Optional[TreeNode]):
        if not root:
            return []
        return self.get_vals(root.left) + [root.val] + self.get_vals(root.right)
