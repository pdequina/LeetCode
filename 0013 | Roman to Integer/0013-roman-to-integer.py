class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        Int = 0
        for i in range(len(s)):
            char1 = convert[s[i]]
            if i + 1 < len(s):
                char2 = convert[s[i+1]]
                if char1 >= char2:
                    Int += char1
                else:
                    Int -= char1
            else:
                Int += char1
        return Int
