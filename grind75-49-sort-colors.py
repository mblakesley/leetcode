# https://leetcode.com/problems/sort-colors/
class Solution:
    # Dutch national flag problem
    # O(1n). A bit different than Djikstra's but mine seems simpler & clearer. Does that make me arrogant?
    # note: mine is unstable, but so is his, though mine is "more unstable", so to speak
    def sortColors(self, nums: list[int]) -> None:
        first_one = 0
        first_two = 0
        for i, num in enumerate(nums):
            if num != 2:
                nums[first_two], nums[i] = nums[i], nums[first_two]
                if num == 0:
                    nums[first_one], nums[first_two] = nums[first_two], nums[first_one]
                    first_one += 1
                first_two += 1

    # O(2n)? not in-place. seems like cheating.
    def sort_colors_naive(self, nums: list[int]) -> None:
        colors = (0, 1, 2)
        counter = {color: 0 for color in colors}
        while nums:
            num = nums.pop()
            counter[num] += 1
        for color in colors:
            nums += [color]*counter[color]
