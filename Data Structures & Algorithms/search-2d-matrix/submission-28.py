class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0

        while r < rows and target > matrix[r][cols -1]:
            r += 1
        if r == rows:
            return False
        start = 0
        end = cols - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[r][mid] == target:
                return True
            elif target < matrix[r][mid]:
                end = mid - 1
            elif target > matrix[r][mid]:
                start = mid + 1
        return False
        