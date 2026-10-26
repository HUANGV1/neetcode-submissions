class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret=[]

        subset=[]

        def dfs(i):
            if i>=len(nums):
                ret.append(subset.copy())
                return

            # include i
            subset.append(nums[i])
            dfs(i+1)

            # don't include if
            subset.pop()
            dfs(i+1)

        dfs(0)

        return ret