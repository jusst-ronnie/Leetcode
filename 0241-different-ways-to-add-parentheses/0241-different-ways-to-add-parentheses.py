class Solution:
    def diffWaysToCompute(self, expression: str):
        
        memo = {}
        
        def solve(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                res.append(l + r)
                            elif expr[i] == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            
            # base case: number
            if not res:
                res.append(int(expr))
            
            memo[expr] = res
            return res
        
        return solve(expression)