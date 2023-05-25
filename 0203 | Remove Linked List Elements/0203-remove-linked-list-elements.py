# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        current = dummy
        while head:
            if head.val != val:
                current.next = head
                current = current.next
            head = head.next
        current.next = None
        return dummy.next
