class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # x = str(x)
        # if x[::-1] == x:
        #     return True
        # else:
        #     return False
        r = 0
        num = x
        while (x>0):
            r = r*10 + x%10
            x = x//10
        return num == r