class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        mapStones = dict()
        result = 0
        for i in stones:
            if i in mapStones.keys():
                mapStones[i] += 1
            else:
                mapStones[i] = 1
        for i in jewels:
            if i in mapStones:
                result += mapStones[i]
        return result
