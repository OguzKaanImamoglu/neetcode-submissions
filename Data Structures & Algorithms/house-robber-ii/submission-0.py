class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        first_nums = nums[:-1]
        last_nums = nums[1:]

        dp1 = [0]*len(first_nums)
        dp1[0] = first_nums[0]

        dp2 = [0]*len(last_nums)
        dp2[0] = last_nums[0]
        
        for i in range(1,len(first_nums)):
            dp1[i] = max(dp1[i-1], dp1[i-2] + first_nums[i])

        for i in range(1,len(last_nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2] + last_nums[i])

        return max(dp1[-1], dp2[-1])