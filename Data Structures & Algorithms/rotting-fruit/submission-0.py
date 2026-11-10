class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        direcs=([0,1],[0,-1],[1,0],[-1,0])
        rows=len(grid)
        cols=len(grid[0])


        q=deque()

        fresh=0

        rounds=0

        # set amount of fresh fruit + add to queue location of rotten fruits
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1: fresh+=1
                elif grid[row][col]==2: q.append([row, col])

        # go through queue and for each rotten fruit, set its neighbouring fruit to rotten

        while q and fresh>0:
            rounds+=1

            for _ in range(len(q)):
                row, col = q.popleft()
                

                for delta_row, delta_col in direcs:
                    new_row=row+delta_row
                    new_col=col+delta_col   
                    if 0<=new_row<=rows-1 and 0<=new_col<=cols-1 and grid[new_row][new_col]==1:
                        q.append([new_row, new_col])
                        grid[new_row][new_col]=2
                        fresh-=1

        return rounds if fresh==0 else -1



