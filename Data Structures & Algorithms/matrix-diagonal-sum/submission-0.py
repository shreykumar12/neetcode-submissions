class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        seen = set()
        res = 0

        r, c = 0, 0

        # First pass - get the main diagonal
        while r < rows and c < cols:
            pair = (r, c)
            seen.add(pair)

            res += mat[r][c]
            r += 1
            c += 1
        
        r, c = 0, cols - 1

        while r < rows and c >= 0:
            pair = (r, c)
            if pair in seen: 
                r += 1
                c -= 1
                continue
            res += mat[r][c]
            r += 1
            c -= 1

        return res
        
