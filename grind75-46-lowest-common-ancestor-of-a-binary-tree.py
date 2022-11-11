from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val: int = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.parent: Optional[TreeNode] = None


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution:
    # the neato recursive solution that would NEVER have occurred to me and still blows my mind
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None
        if root in (p, q):
            return root
        l_result = self.lowestCommonAncestor(root.left, p, q)
        r_result = self.lowestCommonAncestor(root.right, p, q)
        if l_result and r_result:
            return root
        return l_result or r_result


    # a better path-finding implementation, though it cheats a bit by storing a new attribute in the TreeNodes
    def lca_better_path_finding(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        targets = (p.val, q.val)
        found = 0
        node_stack = [(root, None)]
        while found < 2:
            node, parent = node_stack.pop()  # DFS
            node.parent = parent
            if node.val in targets:
                found += 1
            if node.left:
                node_stack += [(node.left, node)]
            if node.right:
                node_stack += [(node.right, node)]

        p_path = set()
        while p:
            p_path |= {p}
            p = p.parent
        while q not in p_path:
            q = q.parent
        return q


    # my original path-finding solution
    # the approach is fine, but the implementation is slow (5%) due to the complex stack, apparently
    def lca_worse_path_finding(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path, q_path = None, None
        node_stack = [(root, (root,))]  # stack of tuples of (node, (path))
        while not p_path or not q_path:
            node, path = node_stack.pop()  # DFS
            if not p_path and node.val == p.val:
                p_path = path
            if not q_path and node.val == q.val:
                q_path = path

            if node.left:
                node_stack += [(node.left, (*path, node.left))]
            if node.right:
                node_stack += [(node.right, (*path, node.right))]

        # find last index before p_path & q_path diverge
        for a, b in reversed(list(zip(p_path, q_path))):
            if a.val == b.val:
                break
        return a
