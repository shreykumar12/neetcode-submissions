class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                boxInd = (r // 3 * 3) + (c // 3)
                if board[r][c] == '.':
                    continue
                if (board[r][c] in box[boxInd] or
                    board[r][c] in cols[c] or
                    board[r][c] in rows[r]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[boxInd].add(board[r][c])
        
        return True

