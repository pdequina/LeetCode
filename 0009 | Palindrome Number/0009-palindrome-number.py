class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # python alternate
        # s = str(x)
        # return s[::-1] == s
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        i = 0
        while x > i:
            i = (i * 10) + (x % 10)
            x //= 10
        return x == i or x == i // 10
