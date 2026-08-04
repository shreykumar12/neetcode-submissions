class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:

            for i in range(len(q)):
                row, col = q.popleft()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for y, x in dirs:
                    r, c = row + y, col + x
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == 1):
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r, c))
            time += 1

        return time if fresh == 0 else -1

            
