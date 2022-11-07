# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()  # cheating?
        new_intvls = []
        max_ = -1  # 0 is lowest possible intvl value
        for start, end in intervals:
            if max_ < start:  # no merge
                new_intvls += [[start, end]]
                max_ = end
            else:  # merge
                new_intvls[-1][1] = max_ = max(max_, end)
        return new_intvls
