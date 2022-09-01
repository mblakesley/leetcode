# https://leetcode.com/problems/valid-palindrome
class Solution:
    # O(n)!
    def isPalindrome(self, s: str) -> bool:
        # for some reason, list + [::-1] is slow, but list + join() is fast
        s_plain: str = ''.join([char.lower() for char in s if char.isalnum()])
        # ideally we'd only check half the str
        return s_plain == s_plain[::-1]


print(Solution().isPalindrome('A man, a plan, a canal: Panama!'))
