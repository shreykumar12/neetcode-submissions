class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        startColor = image[sr][sc]
        if startColor == color:
            return image
        visit = set()
        image[sr][sc] = color
        rows, cols = len(image), len(image[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for y, x in dirs:
                    r, c = row + y, col + x
                    if r in range(rows) and c in range(cols) and image[r][c] == startColor:
                        image[r][c] = color
                        q.append((r, c))
                        visit.add((r, c))
        
        bfs(sr, sc)
        return image
                    
