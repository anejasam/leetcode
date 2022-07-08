class Solution:
    # Sol 1 memoization
    """
    def fib(self, n: int) -> int:
        if n == 0: return 0
        fib_nums = [0] * (n+1)
        fib_nums[1] = 1
        
        for i in range(2, n+1):
            fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]
        
        return fib_nums[n]
    """
    
    # Sol 2 iterative
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        fib0 = 0
        fib1 = 1

        for i in range(2, n+1):
            fib1, fib0 = fib1 + fib0, fib1

        return fib1

        
