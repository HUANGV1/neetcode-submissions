class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        recursively iterate through wordDict and see if can be removed from s. then recursively iterate through the remaining substring after removing the word in s. base cases: s is empty: return True. s is not empty and cannot find word, store the remaining substring in hashmap = False.

        len(dp)=s representing substring with starting from i to the end

        """

        dp={}

        def dfs(i):
            if i in dp:
                if not dp[i]:
                    return False
            if i==len(s):
                return True
            
            for word in wordDict:
                length=len(word)
                if s[i:i+length]==word:
                    if dfs(i+length):
                        return True

            # no words in substring
            if i not in dp:
                dp[i]=False
            return False

        return dfs(0)