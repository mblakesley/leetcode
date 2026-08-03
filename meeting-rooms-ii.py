import heapq

# https://leetcode.com/problems/meeting-rooms-ii
class Solution:
    # Naive
    # Time complexity: Average O(n log n) but worst case O(n^2)
    # Space complexity: O(1) but worst case O(n)
    def minMeetingRooms_naive(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        rooms = []  # Each room's last end time
        for start, end in intervals:
            for i, prev_end in enumerate(rooms):
                if start >= prev_end:
                    rooms[i] = end
                    break
            else:
                rooms.append(end)
        return len(rooms)

    # Heap-based
    # Time complexity: O(n log n) from sort & worst-case heap scenario
    # Space complexity: O(1) but worst case O(n)
    def minMeetingRooms_heap(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        rooms_heap = [intervals[0][1]] if intervals else []  # Each room's last end time
        for start, end in intervals[1:]:
            if start >= rooms_heap[0]:
                heapq.heapreplace(rooms_heap, end)
            else:
                heapq.heappush(rooms_heap, end)
        return len(rooms_heap)

    # Wonky version with disjointed starts & ends
    # Time complexity: O(n log n) from sort
    # Space complexity: O(n)
    def minMeetingRooms_split(self, intervals: list[list[int]]) -> int:
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)
        rooms = 0
        i = 0
        for start in starts:
            if start < ends[i]:  # ends[i] is equivalent to heap[0]
                rooms += 1  # Need a new room
            else:
                i += 1
        return rooms
