class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]
        
        if n <= 2:
            return dp[n-1]

        for i in range(2,n):
            dp.append(dp[i-2]+dp[i-1])

        return dp[n-1]



        

        