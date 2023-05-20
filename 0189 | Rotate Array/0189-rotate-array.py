class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        """
        # Solution 1 | Array Iteration
        # Runtime: O(N) | Memory: O(N)
        # Algorithm: traverse array to the midpoint, swapping as loop
        shifted = list(nums)
        for i, j in enumerate(shifted):
            nums[(i+k) % len(shifted)] = j
        """
        
        # Solution 2 | Swap In-Place
        # Runtime: O(N) | Memory: O(1)
        # Algorithm: find shift value, rotate in-place with subarrays
        if not k:
            return nums
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
