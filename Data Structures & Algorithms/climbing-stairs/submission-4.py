class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
              _
            2
          1
        0 

        """


        left, right=0, 1

        for _ in range(n): 
            
            temp=right
            #new right
            right=left+right
            #new left
            left=temp

        return right