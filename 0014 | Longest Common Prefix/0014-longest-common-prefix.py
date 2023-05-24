class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        compare = min(strs, key=len)
        for i, j in enumerate(compare):
            for words in strs:
                if words[i] != j:
                    return compare[:i]
        return compare
