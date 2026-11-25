class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ret=[]
        path=[]
        used=[False] * len(nums)

        def dfs():
            if len(path)==len(nums):
                ret.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]: continue

                # skip making duplicate permutations. ensure first duplicate is always selected before the second duplicate.
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: continue

                used[i]=True
                path.append(nums[i])

                dfs()

                path.pop()
                used[i]=False

        dfs()
        return ret

            