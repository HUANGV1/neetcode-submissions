class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret=[]

        sub=[]

        

        def dfs(subsum, i):
            if subsum>=target:
                if subsum==target:
                    subcopy=sorted(sub.copy())
                    if subcopy not in ret:
                        ret.append(subcopy)
                return

            for i in range(i, len(nums)):
                subsum+=nums[i]
                sub.append(nums[i])
                dfs(subsum, i)
                sub.pop()
                subsum-=nums[i]
            # for num in nums:
            #     subsum+=num
            #     sub.append(num)
            #     dfs(subsum)
            #     sub.pop()
            #     subsum-=num
        dfs(0, 0)

        return ret