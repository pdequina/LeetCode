# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        """
        # Solution 1 | Two Pointers with Array
        # Runtime: O(N) | Memory: O(N)
        # Algorithm: traverse linked list, two pointers meeting inwards,
        # track and return max twin sum
        current = head
        convert = []
        while(current):
            convert.append(current.val)
            current = current.next
        for i in range(len(convert) // 2):
            convert[i] += convert[len(convert) - 1 - i]
        return max(convert)
        """

        
        # Solution 2 | Two Pointers with Linked List
        # Runtime: O(N) | Memory: O(1)
        # Algorithm: first pass: traverse linked list and reverse the first half,
        # second pass: traverse linked list, tracking maxTwinSum
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        maxTwinSum = 0
        while slow and prev:
            maxTwinSum = max(slow.val + prev.val, maxTwinSum)
            slow = slow.next
            prev = prev.next
        return maxTwinSum
