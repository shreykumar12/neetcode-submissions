class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if heights[r] < heights[l]:
                water = heights[r] * (r-l)
                maxW = max(maxW, water)
                r-=1
            else:
                water = heights[l] * (r-l)
                maxW = max(maxW, water)
                l += 1
        return maxW


