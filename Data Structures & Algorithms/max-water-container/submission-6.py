class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                water = (r - l) * heights[l]
                maxW = max(water, maxW)
                l += 1
            else:
                water = (r - l) * heights[r]
                maxW = max(water, maxW)
                r -= 1
        
        return maxW