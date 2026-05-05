class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:

            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for x, y in directions:
                    r, c = row + x, col + y
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1
            



