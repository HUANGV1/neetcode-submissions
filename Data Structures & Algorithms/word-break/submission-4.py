class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp={}


        def dfs(i):
            if i==len(s):
                return True # because we successfully got to the end

            if i in dp:
                return dp[i]

            for word in wordDict:
                length=len(word)
                if s[i:i+length]==word:
                    if dfs(i+length): 
                        dp[i+length]=True
                        return True

            dp[i]=False
            return False

        return dfs(0)

            