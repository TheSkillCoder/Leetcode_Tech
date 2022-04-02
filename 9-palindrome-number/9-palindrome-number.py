class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x!=0 and x%10==0:
            return False
        y=0
        z=x
        while(x>0):
            y=(y*10)+(x%10)
            x//=10
        if z==y:
            return True
        return False