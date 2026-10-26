class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[]
        res=[0]*len(temperatures)

        for i in range(len(temperatures)):
            if i==0:
                stack.append(i)
                continue
            while stack and temperatures[i]>temperatures[stack[-1]]:
                ind=stack.pop()
                res[ind]=i-ind
            else:
                stack.append(i)
            

        return res