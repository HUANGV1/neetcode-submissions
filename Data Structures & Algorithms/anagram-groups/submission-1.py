class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sorted_str=defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word)) # because sorted() returns a list

            sorted_str[sorted_word].append(word) # allows to make dict without checking if key exists already, if it exists, it will append as a list

        return list(sorted_str.values())