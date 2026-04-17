class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full = 0
        for i in range(len(nums)+1):
            full = full ^ i

        arr = 0
        for i in nums:
            arr = arr ^ i

        return arr ^ full

        