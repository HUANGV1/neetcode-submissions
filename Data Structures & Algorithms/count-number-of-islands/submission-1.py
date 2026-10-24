class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direcs=[(-1,0),(1,0),(0,-1),(0,1)]
        rows=len(grid)
        cols=len(grid[0])

        count=0

        def dfs(row, col):
            if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]!='1':
                return

            grid[row][col]='X'
            
            for direc in direcs:
                delta_row=direc[0]
                delta_col=direc[1]
                dfs(row+delta_row, col+delta_col)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    count+=1
                    dfs(row, col)

        return count