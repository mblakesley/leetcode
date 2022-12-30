# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    # 93rd percentile
    def longestPalindrome(self, s: str) -> str:
        max_pal = s[0]
        for i in range(1, len(s)):  # starts @ 1 b/c s[0] can only be pivot if len = 1
            even_pal = self.find_max_pal(s[:i], s[i:])           # pivot: i - 0.5 (so to speak)
            odd_pal = self.find_max_pal(s[:i], s[i + 1:], s[i])  # pivot: i
            max_pal = max((max_pal, even_pal, odd_pal), key=len)
        return max_pal

    def find_max_pal(self, half1: str, half2: str, pivot_char: str = '') -> str:
        # returns max pal from the string halves + pivot char
        i = 0
        for a, b in zip(reversed(half1), half2):  # half1 is "backwards" to begin with
            if a != b:
                break
            i += 1
        return half2[:i][::-1] + pivot_char + half2[:i]
