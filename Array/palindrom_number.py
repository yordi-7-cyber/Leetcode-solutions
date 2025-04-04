class Solution:
    def is_palindrome(self,s:str | int) ->bool:
        s=str(s).replace(" ","").lower()
        return s==s[::-1]
sol=solution()
print(sol.is_palindrome(121))