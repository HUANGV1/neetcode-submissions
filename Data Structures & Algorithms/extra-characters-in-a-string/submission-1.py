class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dp={}

        def dfs(index):
            if index==len(s): return 0

            if index in dp:
                return dp[index]

            # skip this letter
            ret=dfs(index+1) + 1

            for word in dictionary:
                if s[index:index+len(word)]==word:
                    ret=min(ret, dfs(index+len(word)))
                    
            dp[index]=ret
            return ret

        return dfs(0)