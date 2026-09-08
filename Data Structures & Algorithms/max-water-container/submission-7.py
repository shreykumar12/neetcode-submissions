class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            if heights[l] > heights[r]:
                area = heights[r] * (r - l)
                maxW = max(area, maxW)
                r -= 1
            else:
                area = heights[l] * (r - l)
                maxW = max(area, maxW)
                l += 1
        
        return maxW