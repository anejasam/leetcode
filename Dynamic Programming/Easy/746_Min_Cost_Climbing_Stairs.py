class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Sol 1 recursion
        """
        def helper(index):
            if index == 0 or index == 1:
                return cost[index]
            
            return cost[index] + min(helper(index - 1), helper(index - 2))
        
        n = len(cost)
        return min(helper(n-1), helper(n-2))
        """
        
        # Sol 2 memoization
        """
        n = len(cost)
        min_cost = [c for c in cost]
        
        for i in range(2,n):
            min_cost[i] = cost[i] + min(min_cost[i-1], min_cost[i-2])
        
        return min(min_cost[n-1], min_cost[n-2])
        """
        
        # Sol 3 O(1) space
        n = len(cost)
        a,b = cost[0], cost[1]
        
        for i in range(2, n):
            b, a = cost[i] + min(a,b), b
        
        return min(a,b)
            
