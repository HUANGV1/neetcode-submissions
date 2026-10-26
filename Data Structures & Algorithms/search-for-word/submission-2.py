class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        rows=len(board)
        cols=len(board[0])

        def dfs(row, col, i):
            if i==len(word)-1:
                return True

            board[row][col]='X'

            for d_row, d_col in directions:
                new_row=row+d_row
                new_col=col+d_col

                if new_row<rows and new_row>=0 and new_col<cols and new_col>=0:
                    if board[new_row][new_col]==word[i+1]:
                        if dfs(new_row, new_col, i+1): return True

            board[row][col]=word[i]
            
            return False



        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0]:
                    if dfs(row, col, 0): return True

        return False
