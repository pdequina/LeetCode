# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        current1, current2 = headA, headB
        while current1 != current2:
            current1 = headB if not current1 else current1.next
            current2 = headA if not current2 else current2.next
        return current1
