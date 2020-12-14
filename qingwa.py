"""
青蛙跳台阶问题，一只青蛙要跳上n层高的台阶，一次能跳一级，也可以跳两级，
请问这只青蛙有多少种跳上这个n层高台阶的方法
设青蛙跳上n级台阶有f(n)种方法，把这n种方法分为两大类，第一种最后一次跳了一级台阶，这类方法共有f(n-1)种，
第二种最后一次跳了两级台阶，这种方法共有f(n-2)种，则得出递推公式f(n)=f(n-1)+f(n-2),显然，f(1)=1,f(2)=2
类似的题目还有矩形覆盖：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


class Solution:
    # 递归虽然简单，但效率低
    def climbStairs1(self, n:int):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs1(n-1) + self.climbStairs1(n-2)

    def climbStairs2(self, n:int):
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b


s = Solution()
n = 15
assert(s.climbStairs1(n)) == 987
assert(s.climbStairs2(n)) == 987
