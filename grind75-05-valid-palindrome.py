# https://leetcode.com/problems/valid-palindrome
class Solution:
    # O(n) time
    def isPalindrome(self, s: str) -> bool:
        s_plain = ''.join(filter(str.isalnum, s)).lower()
        return s_plain == s_plain[::-1]
