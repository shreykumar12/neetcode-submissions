class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            while q:
                row, col = q.popleft()
                for y, x in dirs:
                    r, c = row + y, col + x
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == '1' and 
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        
        return islands