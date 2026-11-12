class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        bfs + a lot of extra steps

        from beginWord, for each word that differs by 1 letter, search that level

        '''

        import string

        
        level=1

        q=deque()
        q.append(beginWord)
        seen=set()
        seen.add(beginWord)

        wordSet=set(wordList)

        if endWord not in wordList: return 0

        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord: return level

                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        newWord=word[:i]+char+word[i+1:]
                        if newWord in wordSet and newWord not in seen : 
                            seen.add(newWord)
                            q.append(newWord)
                
            
            level+=1

        return 0

            