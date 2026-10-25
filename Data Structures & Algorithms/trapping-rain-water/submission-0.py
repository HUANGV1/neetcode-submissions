class Solution:
    def trap(self, height: List[int]) -> int:
        
        # find max height on left of index 
        max_left=[0]*len(height)
        max_left[0]=height[0]

        for i in range(1, len(height)):
            max_left[i]=max(max_left[i-1], height[i-1])

        # find max height on right of index 
        n = len(height)-1
        max_right=[0]*len(height)
        max_right[n]=height[n]

        for i in range(n-1, -1, -1):
            max_right[i]=max(max_right[i+1], height[i+1])

        # find how much water per index
        '''
        water above index i = max(0, min(max_left[i], max_right[i])-height[i])
        '''
        amount = 0
        for i in range(len(height)):
            amount+=max(0, min(max_left[i], max_right[i])-height[i])

        return amount
