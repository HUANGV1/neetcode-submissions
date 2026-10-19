class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProf=0

        buy_price=prices[0]

        for price in prices:
            prof=price-buy_price

            maxProf=max(maxProf, prof)

            buy_price=min(buy_price, price)

        return maxProf