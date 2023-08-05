# https://leetcode.com/problems/two-sum
class Solution:
    # O(n) solution using dicts - 80th percentile
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        old_vals: dict = {}  # { old val: old index }
        for i, num in enumerate(nums):
            complement: int = target - num
            old_index = old_vals.get(complement)
            if old_index is not None:
                return [old_index, i]
            old_vals[num] = i
