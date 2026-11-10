class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_rate=1
        max_rate=max(piles)

        while min_rate<max_rate:

            mid=(min_rate+max_rate)//2 # current time we're testing

            time=0

            for pile in piles:
                time+=-(-pile // mid)

            if time<=h:
                max_rate=mid
            else:
                min_rate=mid+1

        return min_rate
                
            