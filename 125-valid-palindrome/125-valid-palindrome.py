class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    string+=i.lower()
                else:
                    string+=i
        return True if string==string[::-1] else False