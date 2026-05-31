# https://leetcode.com/problems/two-sum
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_index_map = {}  # {num: index}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_index_map:
                return [seen_index_map[complement], i]
            seen_index_map[num] = i
        return []
