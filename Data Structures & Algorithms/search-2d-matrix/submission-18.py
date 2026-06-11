class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        r = 0

        while r < rows and matrix[r][cols - 1] < target:
            r += 1
        if r == rows:
            return False
        
        start, end = 0, cols - 1

        while start <= end:
            mid = int((start + end) / 2)
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                start = mid + 1
            elif matrix[r][mid] > target:
                end = mid - 1
        
        return False
