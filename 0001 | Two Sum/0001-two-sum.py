class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        codex = {}
        for i, n in enumerate(nums):
            if target - n in codex:
                return [codex[target - n], i]
            codex[n] = i
        return codex
