# https://leetcode.com/problems/unique-paths/
class Solution:
    # mathy problem - it's Pascal's Triangle converted into a grid, starting at (0,0). 20th percentile
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*m for _ in range(n)]
        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i:
                    grid[j][i] += grid[j][i-1]
                if j:
                    grid[j][i] += grid[j-1][i]
        return grid[-1][-1]

    # Richard's solution using math. Apparently arbitrary PTriangle vals can be calculated.
    def using_math_lib(self, m: int, n: int) -> int:
        from math import comb
        return comb(m + n - 2, min(m, n) - 1)
