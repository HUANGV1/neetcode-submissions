class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        '''
        dp[i] represents if im able to create s[i:] from wordDict
        '''
        dp={}
        
        def dfs(index):

            if index in dp:
                return dp[index]
                
            # reached end
            if index==len(s): 
                dp[index]=True
                return True

            for word in wordDict:
                length=len(word)
                if s[index:index+length]==word:
                    if dfs(index+length): return True

            dp[index]=False
            return False

        return dfs(0)