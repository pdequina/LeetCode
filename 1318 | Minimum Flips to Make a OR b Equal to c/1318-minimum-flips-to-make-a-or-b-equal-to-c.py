class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans, maxBit = 0, 30
        for i in range(maxBit):
            if c >> i & 1:
                ans += (a >> i & 1) == 0 and (b >> i & 1) == 0
            else:
                ans += ((a >> i & 1) == 1) + ((b >> i & 1) == 1)
        return ans
