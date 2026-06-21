# https://leetcode.com/problems/longest-palindrome/
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def longestPalindrome(self, s: str) -> int:
        ltr_count_map = {}  # {ltr: count}
        for char in s:
            ltr_count_map[char] = ltr_count_map.get(char, 0) + 1
        unpaired = sum(count % 2 for count in ltr_count_map.values())
        paired = len(s) - unpaired
        return paired + 1 if unpaired else paired  # Palindromes can have 1 unpaired letter in the middle

    # Cute alternative involving little cycles. Feels like it might be relevant again later.
    def longestPalindrome(self, s: str) -> int:
        unpaired_chars = set()
        max_palindrome = 0
        for char in s:
            if char not in unpaired_chars:
                unpaired_chars.add(char)
            else:
                unpaired_chars.remove(char)
                max_palindrome += 2
        return max_palindrome + 1 if unpaired_chars else max_palindrome  # Palindromes can have 1 unpaired letter in the middle
