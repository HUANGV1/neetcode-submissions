class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        '''

        [a,b] is a graph pointing from a to b meaning, must take b to take a
        the end of a graph makes the element True since no prerequisites

        prereq is a list of prereqs a specific course has.

        dfs through all courses and return true if all of them can be taken

        use a set to track seen items so theres no cycles

        '''

        prereqs={i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            prereqs[a].append(b)

        seen=set()

        def dfs(course):

            if course in seen: return False
            
            if prereqs[course]==[]:
                return True

            seen.add(course)

            for pre in prereqs[course]:
                if not dfs(pre): return False

            seen.remove(course)
            prereqs[course]=[]

            return True

        for course in range(numCourses):
            if not dfs(course): return False


        return True
            
                
