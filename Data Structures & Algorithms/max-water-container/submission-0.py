class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_vol=0

        l, r = 0, len(heights)-1

        while l<r:
            height=min(heights[l],heights[r])
            volume=(r-l)*height

            max_vol=max(max_vol, volume)

            if heights[l]<=heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1

        return max_vol

