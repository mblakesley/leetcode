# https://leetcode.com/problems/container-with-most-water/
class Solution:
    # the real trick here is understanding the nature of the problem
    # in this approach, we start with the widest container and look for progressively narrower but taller containers
    # 30th percentile
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        v_max = 0
        while i < j:
            v = min(height[i], height[j]) * (j - i)
            v_max = max(v_max, v)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return v_max
