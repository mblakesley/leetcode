# https://leetcode.com/problems/binary-search
class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
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

    # Recursive version, for comparison
    def search_recursive(self, nums: list[int], i_min: int, i_max: int, target: int) -> int:
        if i_max < i_min:
            return -1
        i_mid = (i_min + i_max)//2
        mid = nums[i_mid]
        if mid < target:
            return self.search_recursive(nums, i_mid+1, i_max, target)
        elif mid > target:
            return self.search_recursive(nums, i_min, i_max-1, target)
        return i_mid
