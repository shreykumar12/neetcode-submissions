class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = 0

        while r < rows:
            while r < rows-1 and target > matrix[r][cols - 1]:
                r += 1
            start = 0
            end = cols - 1
            while start <= end:
                mid = (start + end) // 2
                if matrix[r][mid] > target:
                    end = mid - 1
                elif matrix[r][mid] < target:
                    start = mid + 1
                else:
                    return True
            return False
        
        return False
