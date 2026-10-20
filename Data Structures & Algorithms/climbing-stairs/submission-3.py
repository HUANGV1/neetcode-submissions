class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
              _
            _
          _
        _ 

        """


        left, right=0, 1

        for _ in range(n): #2
            
            temp=left #0
            left=left+right #3
            right=temp

        return left+right