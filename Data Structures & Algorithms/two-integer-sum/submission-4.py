class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}

        for index, num in enumerate(nums):
            seen_target = target - num
            if seen_target in seen:
                return [seen[seen_target], index]
            seen[num]=index
