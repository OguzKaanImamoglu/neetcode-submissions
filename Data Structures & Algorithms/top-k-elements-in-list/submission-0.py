class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for item in nums:
            if item not in d:
                d[item] = 1
            else:
                d[item] +=1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in d.items():
            buckets[count].append(num)

        index = len(buckets)-1
        while len(res) < k:
            for i in buckets[index]:
                res.append(i)
            index -=1

        return res


