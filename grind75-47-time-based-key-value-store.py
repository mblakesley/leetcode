# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:
    def __init__(self):
        self.time_map = {}  # {key: [(timestamp, val), ...]

    # O(1) due to important note in exercise description: "all timestamps used for set() are strictly increasing"
    def set(self, key: str, value: str, timestamp: int) -> None:
        time_vals = self.time_map.setdefault(key, [])
        time_vals += [(timestamp, value)]  # updates time_map

    # O(log n) - binary search
    def get(self, key: str, timestamp: int) -> str:
        time_vals = self.time_map.get(key)
        if not time_vals:
            return ''
        i_min = 0
        i_max = len(time_vals) - 1
        while i_min <= i_max:
            i_half = (i_max + i_min) // 2
            time, val = time_vals[i_half]
            if time < timestamp:
                i_min = i_half + 1
            elif time > timestamp:
                i_max = i_half - 1
            else:
                return val
        # it's counter-intuitive, but i_max is what we want here
        return time_vals[i_max][1] if i_max >= 0 else ''
