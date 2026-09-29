class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen={}

        for string in strs:
            sorted_string = "".join(str(sorted(string)))
            if sorted_string in seen:
                seen[sorted_string].append(string)
            else:
                seen[sorted_string]=[string]

        
        out=[]
        for string in seen:
            out.append(seen[string])

        return out