# https://leetcode.com/problems/spiral-matrix/
class Solution:
    # look-ahead version. more straightforward but presumably slower for big matrixes. 75th percentile.
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        unseen = {(r, c) for r in range(len(matrix)) for c in range(len(matrix[0]))}
        r, c = 0, -1
        spiral = []
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))  # (E, S, W, N)
        i = 0
        while unseen:
            dr, dc = dirs[i % 4]
            while (r + dr, c + dc) in unseen:
                r, c = r + dr, c + dc
                spiral += [matrix[r][c]]
                unseen -= {(r, c)}
            i += 1
        return spiral

    # mathy & harder to understand, but presumably faster for bigger matrixes. line 17 is a bit much. 50th percentile.
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        width, height = len(matrix[0]), len(matrix)
        r, c = 0, -1
        spiral = []
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))  # (E, S, W, N)
        i = 0
        next_move_count = width
        while next_move_count > 0:
            dr, dc = dirs[i % 4]
            for _ in range(next_move_count):
                r, c = r + dr, c + dc
                spiral += [matrix[r][c]]
            i += 1
            next_move_count = (width, height)[i % 2] - (i + 1)//2  # pattern for 9x9: 9,8,8,7,7,6 -> delta of 0,1,1,2,2,3
        return spiral


