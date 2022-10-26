# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # find all land tiles
        all_lands: set[tuple] = set()
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == "1":
                    all_lands.add((x, y))

        isles = 0
        while all_lands:
            adjacent_lands = [all_lands.pop()]
            isles += 1
            # find all adjacent land tiles & remove them from the pool
            while adjacent_lands:
                x, y = adjacent_lands.pop()
                neighbors = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
                for neighbor in neighbors:
                    if neighbor in all_lands:
                        all_lands.remove(neighbor)
                        adjacent_lands.append(neighbor)
        return isles
