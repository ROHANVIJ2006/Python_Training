'''class Solution:
    def climbStairs(self, n: int) -> int:
        d1=1
        d2=2
        if n<=2:
            return n
        for i in range(3,n+1):
            current=d1+d2
            d1=d2
            d2=current
        return d2'''

class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def helpFunction(n):
            if n<=2:
                return n
            if n in d:
                return d[n]
            temp = helpFunction(n-1) + helpFunction(n-2)
            d[n] = temp
            return temp
        return helpFunction(n)