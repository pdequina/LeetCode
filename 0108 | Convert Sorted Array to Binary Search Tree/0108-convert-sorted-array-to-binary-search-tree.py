# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def treeMake(nums1):
            if not nums1:
                return None
            rootIndex = len(nums1) // 2
            return TreeNode(nums1[rootIndex],
            treeMake(nums1[:rootIndex]),
            treeMake(nums1[rootIndex + 1:]))
        return treeMake(nums)
