class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
              _
            2
          1
        1 

        """


        left, right=1, 1

        for _ in range(n-1): 
            
            temp=right
            #new right
            right=left+right
            #new left
            left=temp

        return right


        """
        1: temp=1, right=1 left=1
        2: temp=1, right=2, left=1
        """