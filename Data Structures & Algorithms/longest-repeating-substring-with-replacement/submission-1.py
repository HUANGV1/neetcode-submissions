class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        k=1
        
        aaababbbbb
           l     r
        """

        l=0

        seen=collections.defaultdict(int)

        max_len=0


        for r in range(len(s)):
            seen[s[r]]+=1
            maxf=max(seen.values())

            replacements=(r-l+1)-maxf
            if replacements>k: # slide the window
                seen[s[l]]-=1
                l+=1
            
            max_len=max(max_len, r-l+1)

        return max_len



