# https://leetcode.com/problems/flood-fill
class Solution:
    # I didn't use a "seen" set for this one b/c I don't think it's much faster.
    # The per-pixel logic is quite simple and the dupes are maxed at 4/pixel.
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        src_color = image[sr][sc]
        dest_color = color
        r_max = len(image)-1
        c_max = len(image[0])-1
        to_fill = [(sr, sc)] if src_color != dest_color else []

        while to_fill:
            r, c = to_fill.pop()
            if 0 <= r <= r_max and 0 <= c <= c_max and image[r][c] == src_color:
                image[r][c] = dest_color
                to_fill.extend(
                    [(nr, nc) for (nr, nc) in ((r+1, c), (r-1, c), (r, c+1), (r, c-1))]
                )
        return image
