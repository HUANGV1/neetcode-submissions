class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_chars = {}

        for letter in s:
            s_chars[letter] = s_chars.get(letter, 0) + 1
        
        t_chars = {}

        for letter in t:
            t_chars[letter] = t_chars.get(letter, 0) + 1

        return s_chars == t_chars