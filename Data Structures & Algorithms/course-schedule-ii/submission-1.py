class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        order = []
        for a, b in prerequisites:
            g[a].append(b)
        
        #unvisited is 0, visiting is 1, visited is 2

        states = [0] * numCourses

        def dfs(node):
            nonlocal order
            if states[node] == 1:
                return False
            elif states[node] == 2:
                return True
            

            states[node] = 1

            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            states[node] = 2
            order.append(node)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []

        return order 

        