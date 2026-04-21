class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0

        while l < r:
            width = r - l
            if heights[l] < heights[r]:
                area = heights[l] * width
                l += 1
            else:
                area = heights[r] * width
                r -= 1
            if area > maxA:
                maxA = area
                
        return maxA
                
