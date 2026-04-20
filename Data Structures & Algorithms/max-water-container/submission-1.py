class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights)-1
        l = 0

        maxArea = 0

        while l < r:

            area = (r - l) * min(heights[r],heights[l])
            
            if area > maxArea:
                maxArea = area

            if heights[r] < heights[l]:
                r -= 1
            
            else: l += 1

        
        return maxArea
