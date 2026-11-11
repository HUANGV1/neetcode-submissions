class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret=[]

        sub=[]

        

        def dfs(subsum, i):
            if subsum>=target:
                if subsum==target:
                    ret.append(sub.copy())
                return

            for i in range(i, len(nums)):
                subsum+=nums[i]
                sub.append(nums[i])
                dfs(subsum, i)
                sub.pop()
                subsum-=nums[i]

        dfs(0, 0)

        return ret