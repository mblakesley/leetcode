# https://leetcode.com/problems/flood-fill
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        target = image[sr][sc]
        if target == color:
            return image
        r_max, c_max = len(image) - 1, len(image[0]) - 1
        to_check = [(sr, sc)]
        checked = {(sr, sc)}  # seems like this speeds it up a bit
        while to_check:
            r, c = to_check.pop()
            if 0 <= r <= r_max and 0 <= c <= c_max and image[r][c] == target:
                image[r][c] = color
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    r2, c2 = r + dr, c + dc
                    if (r2, c2) not in checked:
                        to_check.append((r2, c2))
                        checked.add((r2, c2))
        return image
