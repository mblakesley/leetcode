# https://leetcode.com/problems/01-matrix/
class Solution:
    # rather please with myself at this solution, even though it's not DP, so O(m*n) on memory
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        queue = []
        remaining = set()  # normally this would hurt on speed, but here, we have to scan the matrix anyway
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if not mat[i][j]:
                    queue.append((i, j))
                else:
                    remaining.add((i, j))
        while queue:
            i, j = queue.pop(0)
            val = mat[i][j]
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if (x, y) in remaining:
                    mat[x][y] = val + 1
                    queue.append((x, y))
                    remaining.discard((x, y))
        return mat
