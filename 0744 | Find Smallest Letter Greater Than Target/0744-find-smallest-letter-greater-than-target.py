class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        target_ord, last_ord = ord(target), ord(letters[-1])
        if target_ord >= last_ord:
            return letters[0]
        L, R = 0, len(letters)
        while L < R:
            mid = L + (R - L) // 2
            mid_ord = ord(letters[mid])
            if target_ord < mid_ord:
                R = mid
            else:
                L = mid + 1
        return letters[L]
