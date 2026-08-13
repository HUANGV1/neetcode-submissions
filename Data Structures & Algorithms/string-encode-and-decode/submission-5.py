class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for string in strs:
            encoded_string+=(f"{len(string)}#{string}")

        return encoded_string;

    def decode(self, s: str) -> List[str]:

        decoded_strs=[]

        i=0

        while i < len(s):

            # set j to look from i to next '#'
            j=i

            while s[j]!="#":
                j+=1
            
            # j is a '#'
            length=int(s[i:j])

            # string start
            start=j+1

            decoded_strs.append(s[start:start+length])

            i=start+length
            
            
        return decoded_strs
        
