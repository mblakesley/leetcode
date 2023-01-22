# https://leetcode.com/problems/minimum-height-trees/
class Solution:
    # 70th percentile - could be done faster by tracking neighbors of neighbors less granularly
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        node_map = {i: set() for i in range(n)}
        for i, j in edges:  # bidirectional
            node_map[i] |= {j}
            node_map[j] |= {i}

        # start from the tips & prune inwards. the last 1-2 nodes are "max height" / "most central"
        tips = [k for k, v in node_map.items() if len(v) == 1]  # tips only have 1 connection
        new_tips = []
        while len(node_map) > 2:
            for tip in tips:
                neighbor = node_map.pop(tip).pop()
                neighbors_neighbors = node_map[neighbor]
                neighbors_neighbors -= {tip}
                if len(neighbors_neighbors) == 1:  # only add neighbors if they're now tips
                    new_tips += [neighbor]
            tips, new_tips = new_tips, []

        return list(node_map.keys())
