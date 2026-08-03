class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sorted_str=defaultdict(list)

        for word in strs:
            count=[0]*26

            for letter in word:
                count[ord(letter)-ord('a')]+=1
            
            sorted_str[tuple(count)].append(word)

        return list(sorted_str.values())