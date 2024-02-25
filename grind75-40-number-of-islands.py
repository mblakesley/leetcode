# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        land_tiles = set()  # set of (r, c) tuples
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == '1':
                    land_tiles.add((r, c))

        island_count = 0
        while land_tiles:
            island_count += 1
            curr_island = [land_tiles.pop()]
            while curr_island:
                r, c = curr_island.pop()
                for neighbor in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if neighbor in land_tiles:
                        land_tiles.discard(neighbor)
                        curr_island.append(neighbor)

        return island_count
