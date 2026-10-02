class Solution:

    def encode(self, strs: List[str]) -> str:

        ret=""

        for string in strs:
            ret+=f'{len(string)}#{string}'
            
        return ret

        # hello#world#


    def decode(self, s: str) -> List[str]:

        ret=[]

        l=0 
        
        # 5#hello5#world
        while l<len(s):
            r=l

            while s[r]!="#":
                r+=1
            
            if s[r]=="#":
                length=int(s[l:r])
            
            ret.append(s[r+1:r+1+length])
            l=r+1+length

        return ret
            
            

