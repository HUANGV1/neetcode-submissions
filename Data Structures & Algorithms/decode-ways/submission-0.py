class Solution:
    def numDecodings(self, s: str) -> int:
        """
        any zero belongs to the digit in front of it: only possibilities are 10 and 20
        thinking of using bottom up (tabulation) - no
        recursion + memo

        """

        if s[0]=='0':
            return 0

        dp={}

        def dfs(i): # num ways to describe substring s[i:]
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0

            if i in dp:
                return dp[i]

            # take the first digit only
            ways=dfs(i+1)

            # take the first two digits

            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
                ways+=dfs(i+2)

            dp[i]=ways
            return ways

        return dfs(0)