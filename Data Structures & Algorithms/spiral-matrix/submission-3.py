class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            col = left
            if left <= right:
                while col <= right:
                    res.append(matrix[top][col])
                    col += 1
            top += 1
            row = top
            while row <= bottom:
                res.append(matrix[row][right])
                row += 1
            right -= 1
            col = right
            if bottom >= top:
                while col >= left:
                    res.append(matrix[bottom][col])
                    col -= 1
            bottom -= 1
            row = bottom
            if left <= right:
                while row >= top:
                    res.append(matrix[row][left])
                    row -= 1
            left += 1
        return res
            
            

        
