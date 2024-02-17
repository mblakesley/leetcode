# https://leetcode.com/problems/01-matrix/
class Solution:
    # Technically just BFS, not also DP, but IMO they seem similar in this problem
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        from collections import deque  # Only 'cuz python lacks a built-in queue
        cell_queue = deque()
        remaining = set()
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                if not cell:
                    cell_queue.append((r, c))
                else:
                    remaining.add((r, c))
        while cell_queue:
            r, c = cell_queue.popleft()
            next_val = mat[r][c] + 1
            for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if (nr, nc) in remaining:
                    mat[nr][nc] = next_val
                    cell_queue.append((nr, nc))
                    remaining.remove((nr, nc))
        return mat
