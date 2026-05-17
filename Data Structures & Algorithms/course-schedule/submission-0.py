class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
        
        #Unvisited is 0, visiting is 1, visted is 2

        states = [0] * numCourses

        def dfs(node):

            if states[node] == 1:
                return False
            elif states[node] == 2:
                return True
            
            states[node]=1

            for nei in g[node]:
                if not dfs(nei):
                    return False
                    
            states[node]=2
            return True
            
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True