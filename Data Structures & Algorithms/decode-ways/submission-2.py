class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0]=='0': return 0

        dp={}

        ways=0

        def dfs(index):
            if index in dp:
                return dp[index]

            if index==len(s): 
                return 1

            if s[index]=='0': 
                return 0

            ways=dfs(index+1)
        
            if index+1<len(s) and 10<=int(s[index:index+2])<=26:
                ways+=dfs(index+2)

            dp[index]=ways
            return ways

        return dfs(0)