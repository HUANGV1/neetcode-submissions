class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0

        minbuy=prices[0]

        for sell in prices:
            maxprof=max(maxprof, sell-minbuy)
            minbuy=min(minbuy, sell)
        
        return maxprof