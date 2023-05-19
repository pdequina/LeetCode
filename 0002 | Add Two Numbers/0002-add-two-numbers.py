# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Solution 1 | Linked List Traversal
        # Runtime: O(max(M,N)) | Memory: O(max(M,N))
        # Algorithm: create a dummp pointer then traverse each 
        # linked list updating value, carry, and current node
        current = head = ListNode(0)
        carry = 0
        while (l1 or l2 or carry):
            sumVal = carry
            if l1:
                sumVal += l1.val
                l1 = l1.next
            if l2:
                sumVal += l2.val
                l2 = l2.next
            carry = sumVal // 10
            current.next = ListNode(sumVal % 10)
            current = current.next
        return head.next
