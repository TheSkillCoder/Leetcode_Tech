class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -(1<<31) and divisor ==-1:
            return (1<<31)-1
        
        '''Marking if divison operatioin is negative.....Hoping so you will understand this'''
        flag=0
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            flag=1
        dividend, divisor = abs(dividend), abs(divisor)
        
        ans=count=0
        
        while(dividend>=divisor):
            count=0
            '''same operation as divisor = divisor * 2  (divisor=divisor<<1)'''      
            while(dividend>=divisor<<1<<count):
                count+=1
            ans+=1<<count
            dividend-=divisor<<count
        return ans if flag==0 else -ans
        