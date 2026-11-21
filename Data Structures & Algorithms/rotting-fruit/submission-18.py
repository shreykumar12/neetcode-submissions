class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mins = 0
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh:
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for i in range(len(q)):
                r, c = q.popleft()
                for y, x in dirs:
                    row = r + y
                    col = c + x
                    if (row in range(rows) and
                        col in range(cols) and 
                        grid[row][col] == 1):
                        q.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            mins += 1
        
        return mins if fresh == 0 else -1
                    