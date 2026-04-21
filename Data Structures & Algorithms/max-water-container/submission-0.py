class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            width = abs(l - r)
            if heights[l] < heights[r]:
                currArea = heights[l] * width
                if currArea > area:
                    area = currArea
                else:
                    l += 1
            else:
                currArea = heights[r] * width
                if currArea > area:
                    area = currArea
                else:
                    r -= 1
        return area 

            