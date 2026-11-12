class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        '''
        [38,36]
        [1]
        '''

        ret=[0]*len(temperatures)

        stack=[]

        for i in range(len(temperatures)):

            while stack and temperatures[i]>temperatures[stack[-1]]:
                index=stack.pop()
                ret[index]=i-index

            stack.append(i)


        
        return ret
            
            
            