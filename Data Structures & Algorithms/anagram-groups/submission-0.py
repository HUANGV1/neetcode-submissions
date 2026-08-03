class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sorted_str=defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))

            sorted_str[sorted_word].append(word)

        return list(sorted_str.values())