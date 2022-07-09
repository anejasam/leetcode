class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # let x = m - 1, y = n - 1
        # Unique(x, y) = Unique(x, y-1) + Unique(x-1, y)
        
        # Sol 1 Recursion
        """
        def helper(x,y):
            if x < 0 or y < 0:
                return 0
            elif x == 0 or y == 0:
                return 1

            return helper(x, y-1) + helper(x-1, y)
        
        return helper(m-1, n-1)
        """
        
        # Sol 2 memoization O(m*n) time and space
        paths = [[-1 for i in range(n)] for j in range(m)]
        paths[0][0] = 1
        
        def helper(x,y):
            if x < 0 or y < 0:
                return 0
            elif paths[x][y] != -1:
                return paths[x][y]
            
            paths[x][y] = helper(x, y-1) + helper(x-1, y)
            return paths[x][y]
        
        return helper(m-1, n-1)
