class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        convert = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        check = [1000, 500, 100, 50, 10, 5, 1]
        countList = [0] * 7
        ans = ''
        count = 0
        
        for i, v in enumerate(check):
            while num >= v:
                count += 1
                num -= v
            countList[i] = count
            count = 0
        for i, v in enumerate(countList):
            for j in range(1,v+1):
                ans = convert[check[i]] + ans
        ans = ans[::-1]
        ans = ans.replace("DCCCC","CM").replace("CCCC", "CD").replace("LXXXX","XC").replace("XXXX","XL").replace("VIIII","IX").replace("IIII","IV")
        return ans
