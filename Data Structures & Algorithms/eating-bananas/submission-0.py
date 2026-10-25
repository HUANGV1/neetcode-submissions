class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        k = bananas eaten per hour
        h = available hours

        hk = bananas eaten
        sum banana=10

        l=1
        r=4

        for each pile, time to eat = pile/k rounded up

        1,2,3,4

        """

        lowest_k=1
        greatest_k=max(piles)

        while lowest_k<greatest_k:
            mid=(lowest_k+greatest_k)//2

            # go through piles and see if total time needed is less than or equal to h, if so, move greatest_k=mid-1, else lowest = mid+1
            time=0
            for pile in piles:
                time+=(pile + mid - 1) // mid
            
            if time<=h:
                greatest_k=mid
            else:
                lowest_k=mid+1

        return lowest_k
        
