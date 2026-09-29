class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        seen=defaultdict(list)

        for s in strs:
            sorted_s=''.join(sorted(s))

            if sorted_s in seen:
                seen[sorted_s].append(s)
            else:
                seen[sorted_s]=[s]

        return list(seen.values())