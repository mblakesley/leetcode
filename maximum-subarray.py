# https://leetcode.com/problems/maximum-subarray
class Solution:
    # re-uses my algo from "best-time-to-buy-and-sell-stock"
    # more lines than Kadane's algo, but feels more intuitive than Kadane's
    def maxSubArray(self, nums: list[int]) -> int:
        # rt = running total
        rt: int = 0
        rt_min: int = 0
        max_rt_sum: int = nums[0]

        for num in nums:
            rt += num
            rt_sum: int = rt - rt_min
            max_rt_sum = max(max_rt_sum, rt_sum)
            rt_min = min(rt_min, rt)

        return max_rt_sum
