class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        '''
        dp[i] meaning min remaining chars at index i
        '''

        dp={}

        def dfs(index):
            if index==len(s): return 0

            if index in dp: return dp[index]

            temp=1+dfs(index+1)

            for word in dictionary:
                if s[index:index+len(word)]==word:
                    temp=min(temp, dfs(index+len(word)))

            dp[index]=temp
            return temp


        return dfs(0)

            