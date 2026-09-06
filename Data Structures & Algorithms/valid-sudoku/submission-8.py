class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                boxInd = (r // 3 * 3) + (c // 3)

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[boxInd]):
                    print(boxInd, boxes[boxInd])
                    print(r, c)
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[boxInd].add(board[r][c])
        
        return True

