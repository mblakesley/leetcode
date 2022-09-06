from math import factorial


# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        sml_step = 1
        big_step = 2
        max_big = n // big_step

        combo_list = []
        big_count = 0
        while big_count <= max_big:
            leftover = n - big_count * big_step
            sml_count, r = divmod(leftover, sml_step)
            if not r:
                combo_list += [(sml_count, big_count)]
            big_count += 1

        ways = 0
        for x, y in combo_list:
            # I'm sure there's a better way, I just don't care right now
            ways += factorial(x+y) // (factorial(x) * factorial(y))
        return ways
