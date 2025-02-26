class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_s = str(x)
        rev = x_s[::-1]
        return x_s == rev
                
        