# https://leetcode.com/problems/word-search/
class Solution:
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # 80th percentile
    def exist(self, board: list[list[str]], word: str) -> bool:
        # holistic checks - easy enough to do manually, just tedious
        from collections import Counter
        if not Counter(ltr for row in board for ltr in row) >= Counter(word):
            return False
        if len(word) == 1:
            return True

        self.board = board
        self.r_max, self.c_max = len(board), len(board[0])

        starts = [(r, c) for r in range(self.r_max) for c in range(self.c_max) if board[r][c] == word[0]]
        return any(self.next(*start, word[1:], set()) for start in starts)

    def next(self, r: int, c: int, ltrs: str, prev_cells: set) -> bool:
        nexts = []
        for dr, dc in self.dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.r_max and 0 <= nc < self.c_max:
                if self.board[nr][nc] == ltrs[0] and (nr, nc) not in prev_cells:
                    if len(ltrs) == 1:
                        return True
                    nexts += [(nr, nc)]
        return any(self.next(*cell, ltrs[1:], prev_cells | {(r, c)}) for cell in nexts)
