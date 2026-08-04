class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxA = 0
        visit = set()

        def bfs(r, c):
            q = deque()
            area = 1
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for y, x in dirs:
                    r, c = row + y, col + x
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == 1 and 
                        (r, c) not in visit):
                            area += 1
                            q.append((r, c))
                            visit.add((r, c))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    a = bfs(r, c)
                    maxA = max(maxA, a)
        
        return maxA
