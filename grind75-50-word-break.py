# https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        len_s = len(s)
        word_lens = {len(word) for word in wordDict}
        word_breaks = set()  # indexes of word breaks (which is also first letter of new word after word break)
        i_stack = [0]
        while i_stack:
            i = i_stack.pop()  # DFS
            for word_len in word_lens:
                new_i = i + word_len
                if new_i > len_s:
                    continue
                if s[i:new_i] in wordDict:
                    if new_i == len_s:
                        return True
                    # only add to queue if we haven't seen it before
                    if new_i not in word_breaks:
                        word_breaks |= {new_i}
                        i_stack += [new_i]
        return False
