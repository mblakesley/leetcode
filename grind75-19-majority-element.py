# https://leetcode.com/problems/majority-element/
class Solution:
    # More intuitive than Bayer-Moore, but that's a neat trick
    def majorityElement(self, nums: list[int]) -> int:
        half_len = len(nums) // 2
        counts = {}
        for num in nums:
            count = counts.get(num, 0) + 1
            if count > half_len:
                return num
            counts[num] = count
