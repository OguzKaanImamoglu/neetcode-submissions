"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        n = len(starts)
        starts.sort()
        ends.sort()
        rooms, max_rooms, i, j = 0, 0, 0, 0

        
        # 0 5 15
        # 10 20 40

        while i < n and j < n:
            if starts[i] < ends[j]:
                rooms += 1
                i += 1
                max_rooms = max(max_rooms, rooms)
            else:
                j += 1
                rooms -= 1

        return max_rooms
            
