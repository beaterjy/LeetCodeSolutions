class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''回文数'''
        Xlist = list(str(x))
        
        return Xlist == list(reversed(Xlist))