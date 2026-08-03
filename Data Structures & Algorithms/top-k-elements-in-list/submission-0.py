class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq={}

        for num in nums:
            freq[num]=freq.get(num, 0)+1

        # sort by value ascending

        sorted_freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True)[:k])

        ret = []
        for num, freq in sorted_freq.items():
            ret.append(num)

        return ret