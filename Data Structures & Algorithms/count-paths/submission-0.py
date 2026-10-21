class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # m is row index
        # n is col index

        dp=[[1]*n for _ in range(m)]

        #start_col, start_row=1, 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]