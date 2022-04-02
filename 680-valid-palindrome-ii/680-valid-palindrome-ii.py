class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        loan=0
        j=len(s)-1
        while(i<j):
            if s[i]==s[j]:
                i+=1
                j-=1
            elif loan==0:
                if s[i+1]==s[j]:
                    i+=1
                elif s[i]==s[j-1]:
                    j-=1
                loan=1
            else:
                break
        else:
            return True
        i=0
        loan=0
        j=len(s)-1
        while(i<j):
            if s[i]==s[j]:
                i+=1
                j-=1
            elif loan==0:
                if s[i]==s[j-1]:
                    j-=1
                elif s[i+1]==s[j]:
                    i+=1
                loan=1
            else:
                break
        else:
            return True
        return False