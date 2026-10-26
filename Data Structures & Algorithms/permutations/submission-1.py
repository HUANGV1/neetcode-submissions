class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        ret=[]

        sub=[]



        def dfs(remaining):
            if len(remaining)<=0:
                ret.append(sub.copy())
                return

            # see what i can used
    
            for item in remaining:
                sub.append(item)
                new_remaining=[x for x in remaining if x!=item]
                dfs(new_remaining)
                sub.pop()

        dfs(nums)
        return ret