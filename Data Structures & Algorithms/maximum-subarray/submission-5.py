class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        res = float('-inf')
        
        for i in nums:
            if i > total + i:
                total = i
            else:
                total += i
            
            if total > res:
                res = total

            
        return res


        