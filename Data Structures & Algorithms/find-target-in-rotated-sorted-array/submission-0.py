class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        mp={}

        for i, num in enumerate(nums):
            mp[num]=i

        if target in mp:
            return mp[target]

        return -1