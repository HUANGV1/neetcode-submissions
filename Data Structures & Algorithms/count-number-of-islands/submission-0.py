class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search(row, col):
            if row>=rows or row<0 or col>=cols or col<0 or grid[row][col]!="1":
                return
            

            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            grid[row][col]="X"
            

            for direc in directions:
                row_change=direc[0]
                col_change=direc[1]

                search(row+row_change, col+col_change)

            
                

        count=0
        rows=len(grid)
        cols=len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    count+=1
                    search(row, col)


        return count
