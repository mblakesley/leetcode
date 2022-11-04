# https://leetcode.com/problems/permutations/
class Solution:
    def oneline_permute(self, nums: list[int]) -> list[list[int]]:
        return [nums] if len(nums) == 1 else [[num] + perm for i, num in enumerate(nums) for perm in self.oneline_permute(nums[:i] + nums[i+1:])]

    def multiline_permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        perms = []
        for i, num in enumerate(nums):
            subperms = self.multiline_permute(nums[:i] + nums[i+1:])
            for subperm in subperms:
                perms += [[num] + subperm]
        return perms
