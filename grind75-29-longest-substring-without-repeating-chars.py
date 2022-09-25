# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        max_ = 0
        for char in s:
            if char not in substr:
                substr += char
                max_ = max(max_, len(substr))
            else:
                # this is faster than split(). maybe 'cuz it short-circuits?
                i = substr.index(char)
                substr = substr[i+1:] + char
        return max_
