# https://leetcode.com/problems/01-matrix/
class Solution:
    # rather pleased with myself at this solution (me from the future: 'cuz I stumbled upon dynamic programming!)
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        cell_queue = []
        remaining = set()  # normally this would hurt on speed, but here, we have to scan the matrix anyway
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if not mat[i][j]:
                    cell_queue.append((i, j))
                else:
                    remaining.add((i, j))

        while cell_queue:  # BFS
            i, j = cell_queue.pop(0)
            val = mat[i][j]
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if (x, y) in remaining:
                    mat[x][y] = val + 1
                    cell_queue.append((x, y))
                    remaining.discard((x, y))
        return mat
