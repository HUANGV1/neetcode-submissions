class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ret=[]

        def dfs(i, els, total):
            if total==target:
                ret.append(els.copy())
                return
            
            for j in range(i, len(nums)):
                if total+nums[j]>target:
                    return
                els.append(nums[j])
                dfs(j, els, total+nums[j])
                els.pop()

        dfs(0, [], 0)

        return ret