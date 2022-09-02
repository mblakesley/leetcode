# https://leetcode.com/problems/binary-search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # min & max are inclusive
        i_min: int = 0
        i_max: int = len(nums) - 1
        while i_min <= i_max:
            i_half: int = i_min + (i_max - i_min)//2
            num: int = nums[i_half]
            if target == num:
                return i_half
            elif target < num:
                i_max = i_half - 1
            else:
                i_min = i_half + 1
        return -1
