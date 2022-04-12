class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x in [0, 1] or n == 1:
            return x 
        else:
            pow = 1
            if n < 0:
                x = 1 / x
                n = -(n + 1)
                pow *= x

            while n > 0:
                if n % 2:
                    pow *= x
                    n -= 1
                else:
                    x *= x
                    n //= 2
            else:
                return pow
