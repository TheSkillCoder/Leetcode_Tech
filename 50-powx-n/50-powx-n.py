class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        if x==1 or x==0 or n==1:
            return x
        ans=1
        while(n>0):
            if n%2==0:
                x*=x
                n=n//2
            else:
                ans*=x
                n-=1
        return ans