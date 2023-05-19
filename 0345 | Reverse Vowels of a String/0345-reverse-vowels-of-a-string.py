class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two pointers meeting inwards, swap in place
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s) - 1
        chars = list(s)
        while left < right:
            if chars[left] not in vowels:
                left += 1
                continue
            if chars[right] not in vowels:
                right -= 1
                continue
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return ''.join(chars)
