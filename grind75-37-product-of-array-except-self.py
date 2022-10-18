# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    # O(n), though this is 1 or 2 n's too many, for a bit more readability
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        identity = 1  # multiplicative identity
        prefixes, suffixes = [identity], [identity]

        for i, num in enumerate(nums[:-1]):
            prefixes.append(prefixes[i] * num)

        for i, num in enumerate(reversed(nums[1:])):  # don't include the last item when reversed, aka the 1st item
            suffixes.append(suffixes[i] * num)
        suffixes.reverse()

        return [p * s for p, s in zip(prefixes, suffixes)]
