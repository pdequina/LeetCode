class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        """
        # Solution 1 | Naive Approach (Two Loops)
        # Runtime: O(N^2) | Memory: O(N)
        # Algorithm: traverse array of heights, two pointers meeting inwards,
        # track and return max area
        current, maxArea = 0, 0
        for i in range(0,len(height)):
            for j in range(i,len(height)):
                current = (j-i)*min(height[i], height[j])
                maxArea = max(current, maxArea)
        return maxArea
        """
        
        # Solution 2 | Two Pointers 
        # Runtime: O(N) | Memory: O(1)
        # Algorithm: Find maximal height, then traverse inwards with
        # two pointers comparing area and returning the max area
        maxArea, left, right = 0, 0, len(height) - 1
        maxHeight = max(height)
        while left < right:
            maxArea = max(maxArea, min(height[left],
                height[right]) * (right - left))
            if height[left] <= height [right]:
                left += 1
            else:
                right -= 1
            if maxHeight * (right - left) <= maxArea:
                break
        return maxArea
