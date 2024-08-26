# https://leetcode.com/problems/binary-search
class Solution:
    # O(log n) time
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            num = nums[mid]
            if num == target:
                return mid
            if num < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
