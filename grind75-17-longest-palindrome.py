# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts: dict = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        pair_chars = 0
        for count in counts.values():
            pair_chars += count - count % 2
        return pair_chars + int(pair_chars < len(s))
