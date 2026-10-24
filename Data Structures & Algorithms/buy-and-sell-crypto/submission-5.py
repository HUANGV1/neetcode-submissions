class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res=0

        for i in range(len(prices)):
            sell_price=prices[i]
            lowest=min(prices[:i+1])
            res=max(res, sell_price-lowest)

        return res