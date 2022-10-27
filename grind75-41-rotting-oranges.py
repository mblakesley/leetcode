# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minute = 0
        fresh: set[tuple] = set()  # set of (x, y)
        rotten_queue: list[tuple] = []  # list of (x, y, minute rotten)
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 1:
                    fresh.add((x, y))
                elif cell == 2:
                    rotten_queue += [(x, y, minute)]

        if not fresh:
            return minute

        while rotten_queue:  # BFS
            x, y, minute = rotten_queue.pop(0)
            neighbors: set[tuple] = {(x+1, y), (x, y+1), (x-1, y), (x, y-1)}
            neighbors &= fresh  # we only care about fresh neighbors
            fresh -= neighbors
            rotten_queue += [(*neighbor, minute + 1) for neighbor in neighbors]

        return minute if not fresh else -1
