class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows=len(board)
        cols=len(board[0])

        directions=[(-1,0),(1,0),(0,1),(0,-1)]

        def searchdfs(leng, row, col, curr_index):
            if leng==len(word):
                return True

            board[row][col]="X"

            for direc in directions:
                rowdiff, coldiff=direc[0], direc[1]

                if row+rowdiff<rows and row+rowdiff>=0 and col+coldiff<cols and col+coldiff>=0 and curr_index!=len(word)-1:

                    if board[row+rowdiff][col+coldiff]==word[curr_index+1]:
                        if searchdfs(leng+1, row+rowdiff, col+coldiff, curr_index+1): return True

            board[row][col]=word[curr_index]
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0]:
                    if searchdfs(1, row, col, 0):
                        return True

        return False