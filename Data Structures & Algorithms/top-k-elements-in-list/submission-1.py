class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import defaultdict

        seen = defaultdict(int)

        for num in nums:
            seen[num]+=1
        
        seen_sorted = sorted(seen, key=lambda x: seen[x], reverse=True)

        return seen_sorted[:k]