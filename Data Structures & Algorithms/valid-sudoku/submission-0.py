class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = {}
        for i in range(len(board)):
            row = set()
            col = set()
            for j in range(len(board[i])):
                grid = (i//3, j//3)
                squares[grid] = squares.get(grid, set())
                if board[i][j] in row and board[i][j] != ".":
                    return False
                if board[j][i] in col and board[j][i] != ".":
                    return False
                if board[i][j] in squares[grid] and board[i][j] != ".":
                    return False 

                row.add(board[i][j])
                col.add(board[j][i])
                squares[grid].add(board[i][j])
        
        return True
