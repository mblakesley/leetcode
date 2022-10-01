from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


# https://leetcode.com/problems/clone-graph/
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return node  # fuck off with this Optional[] shit
        to_clone = [node]
        old_new_map = {}

        # explore graph, cloning node vals
        while to_clone:
            old = to_clone.pop()
            new = Node(val=old.val, neighbors=[])
            old_new_map[old] = new
            for neighbor in old.neighbors:
                if neighbor not in old_new_map:
                    to_clone.append(neighbor)

        # go back & populate neighbors
        for old, new in old_new_map.items():
            for neighbor in old.neighbors:
                new.neighbors.append(old_new_map[neighbor])

        return old_new_map[node]
