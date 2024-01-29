# https://leetcode.com/problems/two-sum
class Solution:
    # O(n) solution using dicts - 80th percentile
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        comp_index_map = {}  # {complement: index}
        for i, num in enumerate(nums):
            if num in comp_index_map:
                return [comp_index_map[num], i]
            comp_index_map[target - num] = i
        return []
