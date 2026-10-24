class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        """
        [a,b],[b,c],[b,d], numCourses=4

        dfs through the starting point and if the node is not a root or if all its children are True, then the node is True
        reflect this change until the starting point

        a: b
        b: c, d
        """

        prereqs={i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            prereqs[a].append(b)

        seen=set() # seen is temp courses seen in current dfs. if False, the entire problem is over so we dont care about removing from seen. only if return True, we want to remove from seen and this happens during the backtracking. each time we go up a level, we remove the level's course from seen.

        def dfs(course):
            if course in seen:
                return False
            
            if prereqs[course]==[]:
                return True

            seen.add(course)

            for pre in prereqs[course]:
                if not dfs(pre): return False
            
            # other wise dfs works
            seen.remove(course)
            prereqs[course]=[]
            return True

        
        for course in range(numCourses):
            if not dfs(course): return False

        return True

        
        
        