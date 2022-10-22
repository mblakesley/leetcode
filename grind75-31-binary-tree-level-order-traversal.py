from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        vals_by_level = []
        node_queue: list[tuple] = [(root, 0)] if root else []  # tuples of (node, level/index)
        while node_queue:
            node, level = node_queue.pop(0)  # BFS
            if level == len(vals_by_level):  # looks funky, but just checks if we need to start a new "level" list
                vals_by_level.append([])
            vals_by_level[level].append(node.val)
            if node.left:
                node_queue.append((node.left, level + 1))
            if node.right:
                node_queue.append((node.right, level + 1))
        return vals_by_level

    # My original version, back when I first did the problem, using my old "now & next" pattern.
    # In hindsight, this pattern arose from me trying to do BFS/queue when 2 vars are at play.
    # Nowadays, a queue of tuples seems obvious, but back then, I only thought of queues as holding scalars.
    # So I used a queue of scalars and snuck in a 2nd dimension via the "now & next" mechanism.
    def level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
        vals_by_level = []
        curr_level = [root] if root else []
        while curr_level:
            next_level = []
            vals = []
            for node in curr_level:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            vals_by_level.append(vals)
            curr_level = next_level
        return vals_by_level
