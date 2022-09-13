# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set_ = set()
        for num in nums:
            if num in set_:
                return True
            set_.add(num)
        return False

    # less performant 1-liner (no short-circuit)
    def contains_duplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
