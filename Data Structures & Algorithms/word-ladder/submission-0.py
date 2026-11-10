class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''

        cat -> sag
        ["bat","bag","sag","dag","dot"]

        cat: bat
        bat: bag
        bag: sag, dag
        
        loop through options to see which are valid and then run same search on valid words 
        cannot use words that have already been used (cycle)
        keep count of current number of moves and each time, find valid way, get the min

        '''

        import string

        ways=1
        seen=set()
        wordSet=set(wordList)

        if endWord not in wordSet: return 0

        q=deque()

        q.append(beginWord)

        def list_differs(word, words):
            differs=set()

            for i in range(len(word)): # each position of word
                for char in string.ascii_lowercase:
                    new_word=word[:i]+char+word[i+1:]
                    if new_word in words: differs.add(new_word)

            return differs


        while q:
            
            for _ in range(len(q)):
            
                word=q.popleft()
                if word==endWord:
                    return ways
                options=list_differs(word, wordList)

                for option in options:
                    if option not in seen:
                        seen.add(option)
                        q.append(option)
            if len(q)==0: return 0
            ways+=1
        
            
        return ways


            


