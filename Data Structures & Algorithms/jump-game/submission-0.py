class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        goal = last

        i = last - 1

        while i >= 0:
            if(nums[i] + i >= goal):
                goal = i
            
            i-=1

        return goal == 0


            


        