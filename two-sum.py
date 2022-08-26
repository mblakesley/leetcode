class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # a dict of old vals & their indexes
        old_vals: dict = {}
        for i, num in enumerate(nums):
            complement: int = target - num
            if complement in old_vals:
                return [old_vals[complement], i]
            old_vals[num] = i
