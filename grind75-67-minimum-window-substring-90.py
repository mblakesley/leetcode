from collections import Counter


# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    # 90th percentile - two-pointer crab walk
    def minWindow(self, s: str, t: str) -> str:
        needs = Counter(t)
        unmet_needs = sum(needs.values())
        i = 0  # i/j = first/last char of min_str
        min_str = s + t  # impossibly long str

        for j in range(len(s)):
            j_need = needs.get(s[j])
            if j_need is None:
                continue
            if j_need > 0:
                unmet_needs -= 1
            needs[s[j]] = j_need - 1  # gaining j_char, aka s[j]

            # if current window has everything we need, see if we can tighten it up by paring chars off the front
            if not unmet_needs:
                for i in range(i, j+1):
                    i_char = s[i]
                    i_need = needs.get(i_char)
                    if i_need is not None:
                        if i_need == 0:
                            break
                        needs[i_char] = i_need + 1  # dropping i_char
                min_str = min((min_str, s[i:j+1]), key=len)

                i += 1  # kick out the needed i_char so the substr is incomplete, forcing more exploration on j-side
                needs[i_char] = i_need + 1
                unmet_needs += 1

        return min_str if min_str != s + t else ''
