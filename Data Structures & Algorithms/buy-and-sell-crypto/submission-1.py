class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        localMin = prices[0]

        for i in range(1,len(prices)):
            if prices[i]-localMin > res:
                res = prices[i]-localMin
            if prices[i] < localMin:
                localMin = prices[i]
             
        return res


        