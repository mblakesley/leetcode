# https://leetcode.com/problems/valid-palindrome
class Solution:
    # O(n)!
    def isPalindrome(self, s: str) -> bool:
        # yay comprehensions, but also, string immutability means looped '+=' is inefficient
        s_plain: str = ''.join([char.lower() for char in s if char.isalnum()])
        return s_plain == s_plain[::-1]
