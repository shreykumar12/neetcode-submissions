class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # record cells that flow to the pacific ocean and cells that flow into
        # the atlanctic ocean into their own sets
        # use dfs starting from the cells that we know for sure flow into an ocean
        # (the border cells) and go inwards to explore other cells that water can flow 
        # from into that respective ocean
        # at the end we add the cells in both sets to the result array and return it

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()


        # recursive dfs checking if the cell passed in
        # is flowing into an ocean and if it is add it to
        # that visited set
        # recruse on the neighbors of that cell
        def dfs(r, c, prevHeight, visit):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or 
                prevHeight > heights[r][c]):
                return
            visit.add((r, c))
            dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            for y, x in dirs:
                row, col = r + y, c + x
                dfs(row, col, heights[r][c], visit)
            

        # run dfs on top and bottom rows
        # we know these cells are guarentted touching 
        # one of the oceans
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)
        
        # run dfs on the left and right columns
        # we know these cells are gaurantted to touch an ocean also
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)
        
        # find the unions in the sets and add them to result
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        
        return res



