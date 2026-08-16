# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
class Solution:
    # Time complexity: O(n)
    # Aux space complexity: O(1)
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lo = 0
        hi = len(numbers)-1
        while lo < hi:
            curr = numbers[lo] + numbers[hi]
            if curr == target:
                return [lo+1, hi+1]
            elif curr > target:  # Fundamental insight: Curr is the LOWEST sum Hi can produce. So we must discard Hi.
                hi -= 1
            else:  # Vice versa here.
                lo += 1
        return []
