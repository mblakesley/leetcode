# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot = nums[0]
        if target == pivot:
            return 0

        i_min, i_max = 0, len(nums) - 1
        while i_min <= i_max:
            i_half = (i_min + i_max) // 2
            sample = nums[i_half]
            if sample == target:
                return i_half
            look_higher = sample < target

            # when target & sample are on opposite sides of the pivot,
            # we need to look in opposite direction than normal
            if sample < pivot < target or sample >= pivot > target:  # note: it's possible for sample == pivot, but only in latter scenario
                look_higher = not look_higher

            if look_higher:
                i_min = i_half + 1
            else:
                i_max = i_half - 1

        return -1
