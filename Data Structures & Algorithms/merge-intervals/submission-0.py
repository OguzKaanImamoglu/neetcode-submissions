class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda x: x[0])
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if(result[-1][1] >= intervals[i][0]):
                new_inter = [result[-1][0],max(result[-1][1] ,intervals[i][1])]
                result.pop()
                result.append(new_inter)
            else:
                result.append(intervals[i])

        
        return result

        