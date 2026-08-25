class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        lastEnd = float("-inf")
        intervals.sort(key = lambda x: x[1])
        result = 0

        for i in intervals:
            if i[0] >= lastEnd:
                lastEnd = i[1]
            else:
                result += 1

        return result
        