class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        t = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        if not fresh:
            return 0

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for y, x in dirs:
                    r, c = row + y, col + x
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == 1):
                        q.append((r, c))
                        grid[r][c] = 2
                        fresh -= 1
            t += 1
            if fresh == 0:
                return t
            print(q)
            print(t)

        return t if fresh == 0 else -1

        

        