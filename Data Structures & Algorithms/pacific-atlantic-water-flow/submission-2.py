class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, prevHeight, visit):
            if (r not in range(rows) or
                c not in range(cols) or
                heights[r][c] < prevHeight or
                (r, c) in visit):
                return
            visit.add((r, c))
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for y, x in dirs:
                row, col = r + y, c + x
                dfs(row, col, heights[r][c], visit)


        # top and bottom rows
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)
        
        #left and right cols
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        
        return res

