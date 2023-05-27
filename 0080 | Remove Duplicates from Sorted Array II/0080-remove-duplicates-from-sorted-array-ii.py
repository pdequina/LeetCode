class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in nums:
            if i < 2 or j != nums[i-2]:
                nums[i] = j
                i += 1
        return i
