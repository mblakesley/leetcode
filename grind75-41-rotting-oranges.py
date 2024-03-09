# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh = set()
        newly_rotten = set()
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    fresh.add((r, c))
                elif cell == 2:
                    newly_rotten.add((r, c))

        minute = 0
        while fresh and newly_rotten:
            rot_neighbors = set()
            for r, c in newly_rotten:
                rot_neighbors |= {(r, c+1), (r, c-1), (r+1, c), (r-1, c)}
            newly_rotten = fresh & rot_neighbors
            fresh -= newly_rotten
            minute += 1

        return minute if not fresh else -1
