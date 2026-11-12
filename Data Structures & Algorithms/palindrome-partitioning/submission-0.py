class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        '''

        "aab"
        a,a,b

        aa,b


        '''

        ret=[]
        sub=[]

        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]: return False
                l+=1
                r-=1
            return True

        def dfs(index):
            if index>=len(s): 
                ret.append(sub.copy())
                return

            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    sub.append(s[index:i+1])
                    dfs(i+1)
                    sub.pop()

        dfs(0)
        return ret

        