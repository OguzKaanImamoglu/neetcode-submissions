class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        result = []
        for i, j in enumerate(nums):
            diff = target - j
            if j in table.keys():
                return [table[j],i]
            table[diff] = i
            

        
        return result
