class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0

        while l < r:
            if heights[l] > heights[r]:
                area = heights[r] * (r - l)
                maxA = max(maxA, area)
                r -= 1
            else:
                area = heights[l] * (r - l)
                maxA = max(maxA, area)
                l += 1
        return maxA
            