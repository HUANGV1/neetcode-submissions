class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        '''
        k=2

        2,-1,1,2

        count=1+1+2
        prefix, count
        0   1
        1   1
        2   1+1
        4   1
        '''

        prefix_map=collections.defaultdict(int)
        prefix_map[0]=1

        prefix=0
        count=0
        for num in nums:
            prefix+=num

            target=prefix-k
            if target in prefix_map:
                count+=prefix_map[target]

            prefix_map[prefix]+=1

        return count

