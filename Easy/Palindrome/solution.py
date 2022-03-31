class Solution:
    def reverseNumber(self, x: int) -> int:
        reverse = 0
        while(x>0):
            rem = x%10
            reverse = reverse*10 + rem
            x = int(x/10)
        return reverse
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            reverse = self.reverseNumber(x)
            if reverse == x :
                return True
            else:
                return False
