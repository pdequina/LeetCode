# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prevNode, currentNode = None, head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        return prevNode
