# https://leetcode.com/problems/binary-search
class Solution:
    # O(log n) time
    def search(self, nums: list[int], target: int) -> int:
        min_, max_ = 0, len(nums) - 1
        while min_ <= max_:
            mid = (min_ + max_) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                max_ = mid - 1
            else:
                min_ = mid + 1
        return -1
