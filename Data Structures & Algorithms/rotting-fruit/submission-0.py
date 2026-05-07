class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in dir:
                    i, j = r+dr, c+dc
                    if 0<=i<m and 0<=j<n and grid[i][j] == 1:
                        grid[i][j] = 2
                        q.append((i, j))
                        fresh-=1
            time+=1
        
        if fresh == 0:
            return time
        else:
            return -1
                                    


        