class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        '''
        compare adjacent words and find an edge between them and add to topological graph (dictionary)

        create topological graph: a-> c
        then:
        use indegrees and add to result
        add all 0 indegrees 

        '''

        topological={char: set() for word in words for char in word}

        # create the topological graph by comparing adjacent words and finding differences 
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]

            # compare to find the first letter which differs. also check the prefix rule

            if len(word1)>len(word2) and word1.startswith(word2): return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j]!=word2[j]:
                    topological[word1[j]].add(word2[j])
                    break

        result=[]
        indegrees={char: 0 for char in topological}
        '''
        indegree how many chars come before a specific char
        topological shows what elements come after a specific char
        '''

        for char in topological:
            for neighbour in topological[char]:
                indegrees[neighbour]+=1
        
        # now we have the indegrees 

        q=deque()

        # add initial 0 indegrees
        for char in indegrees:
            if indegrees[char]==0:
                q.append(char)

        # everything in q has indegree 0
        while q:
            char=q.popleft()
            result.append(char)

            # update other chars and reduct indegree 
            for neighbour in topological[char]:
                indegrees[neighbour]-=1

                if indegrees[neighbour]==0: q.append(neighbour)

        # if cycles:
        if len(result)!=len(indegrees): return ""

        return "".join(result)
            





            

        