class FibonacciCalculator:
    def __init__(self):
        self.memo = {}
    
    def calculate(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.calculate(n-1) + self.calculate(n-2)
        return self.memo[n]


calc = FibonacciCalculator()
N = int(input())
print(calc.calculate(N))