class Solution:
    def isValid(self, s: str) -> bool:
        """
        ([{}])
        )]}{[(

        ([{

        )]}
        
        """
        stack=[]
        for n in s:
            if n=='(':
                stack.append(')')
            elif n=='{':
                stack.append('}')
            elif n=='[':
                stack.append(']')
            elif not stack or stack.pop()!=n:
                return False
        
        return len(stack)==0