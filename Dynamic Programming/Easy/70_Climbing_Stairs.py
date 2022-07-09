class Solution:
    def climbStairs(self, n: int) -> int:
        #[ Number of distinct ways to climb n - 1] + [Number of distinct ways to climb n - 2]
        
        # Basic recursion
        """
        if n == 1 or n == 2:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        
        # Using memoisation
        """
        if n == 1:
            return 1
        
        memo = [0] * n
        memo[0], memo[1] = 1, 2
        
        for i in range(2, n):
            memo[i] = memo[i-1] + memo[i-2]
            
        return memo[n-1]
        """
        # Without memoisation, like fibonnaci
        
        a = 1
        b = 1
        
        for _ in range(n):
            a , b = b, a + b
        
        return a
