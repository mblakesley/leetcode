class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        scolor: int = image[sr][sc]
        tcolor: int = color
        # don't kick off filling unnecessarily
        if color == scolor:
            return image

        r_max: int = len(image)
        c_max: int = len(image[0])

        pixel_stack: list[tuple[int, int]] = [(sr, sc)]
        while pixel_stack:
            r, c = pixel_stack.pop()
            if image[r][c] != scolor:
                continue
            image[r][c] = tcolor
            if r-1 >= 0:
                pixel_stack += [(r-1, c)]
            if r+1 < r_max:
                pixel_stack += [(r+1, c)]
            if c-1 >= 0:
                pixel_stack += [(r, c-1)]
            if c+1 < c_max:
                pixel_stack += [(r, c+1)]
        return image
