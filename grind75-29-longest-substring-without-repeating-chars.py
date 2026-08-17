# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    # Sliding window + set
    # Time complexity: O(n)
    # Aux space complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        uniq_chars = set()
        max_uniq = 0
        for r, r_char in enumerate(s):
            if r_char not in uniq_chars:
                uniq_chars.add(r_char)
                max_uniq = max(max_uniq, len(uniq_chars))
            else:
                l_char = s[l]
                while l_char != r_char:
                    uniq_chars.remove(s[l])
                    l += 1
                    l_char = s[l]
                l += 1  # Advance L but leave the char in the set
        return max_uniq

    # TODO: There's a solution using only a dict of {char: index}. It's slightly more performant but more abstract.
