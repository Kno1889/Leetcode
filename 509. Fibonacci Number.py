class Solution:
    def fib(self, n: int) -> int:

        def fib_number(n):
            if n == 0:
                return 0
            
            elif n == 1:
                return 1
            
            return fib_number(n - 1) + fib_number(n - 2)
    
        return fib_number(n)